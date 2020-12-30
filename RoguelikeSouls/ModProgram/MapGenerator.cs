using SoulsFormats;
using SoulsFormatsMod;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using RoguelikeSouls.Installation;
using RoguelikeSouls.Extensions;

namespace RoguelikeSouls.ModProgram
{
    static class ModelTemplates
    {
        public static MSB1.Model ChestModel { get; } = new MSB1.Model() { Name = "o0110", Placeholder = @"N:\FRPG\data\Model\obj\o0110\sib\o0110.sib" };
        public static MSB1.Model AndreAnvilModel { get; } = new MSB1.Model() { Name = "o1252", Placeholder = @"N:\FRPG\data\Model\obj\o1252\sib\o1252.sib" };
        public static MSB1.Model VamosAnvilModel { get; } = new MSB1.Model() { Name = "o3870", Placeholder = @"N:\FRPG\data\Model\obj\o3870\sib\o3870.sib" };
        public static MSB1.Model BonfireModel { get; } = new MSB1.Model() { Name = "o0200", Placeholder = @"N:\FRPG\data\Model\obj\o0200\sib\o0200.sib" };
        public static MSB1.Model CorpseModel { get; } = new MSB1.Model() { Name = "o0500", Placeholder = @"N:\FRPG\data\Model\obj\o0500\sib\o0500.sib" };
        public static MSB1.Model PaintingModel { get; } = new MSB1.Model() { Name = "o5850", Placeholder = @"N:\FRPG\data\Model\obj\o5850\sib\o5850.sib" };
        public static MSB1.Model PlayerModel { get; } = new MSB1.Model() { Name = "c0000", Placeholder = @"N:\FRPG\data\Model\chr\c0000\sib\c0000.SIB" };
        public static MSB1.Model EmptyModel { get; } = new MSB1.Model() { Name = "c1000", Placeholder = @"N:\FRPG\data\Model\chr\c1000\sib\c1000.sib" };
    }
    
    class MapGenerator
    {
        // Class created each time an MSB is generated.
        SoulsMod Mod { get; }
        RunManager Run { get; }
        MapInfo Map { get; }
        MSB1 MSB { get; }
        MapPointManager Points { get; }
        EMEVD EMEVD { get; }
        Random Rand { get; }
        HashSet<int> LogicGoalIDs { get; }
        HashSet<int> BattleGoalIDs { get; }
        Vector3? PlayerStartPoint { get; }
        double RedPhantomOdds { get; }

        const int BasicEnemyOffset = 0;
        const int BasicPhantomOffset = 100;
        const int RareEnemyOffset = 130;
        const int VeryRareEnemyOffset = 170;
        const int MimicOffset = 180;
        const int VagrantOffset = 190;

        // Additional offsets for lower New Londo Ruins.
        const int NewLondoLowerBasicEnemyOffset = 50;
        const int NewLondoLowerBasicPhantomOffset = 15;
        const int NewLondoLowerRareEnemyOffset = 15;
        const int NewLondoVeryRareEnemyOffset = 5;
        // Mimics and Vagrants won't appear in lower New Londo.

        string ModMSBPath { get; } = @"Package\map\MapStudio\";
        string ModEMEVDPath { get; } = @"Package\event\";

        public MapGenerator(SoulsMod mod, RunManager run, MapInfo map, Random rand, double redPhantomOdds, Connection startPoint)
        {
            Mod = mod;
            Run = run;
            Map = map;
            MSB = MSB1.Read(ModMSBPath + $"{Map.MsbName}.msb");
            EMEVD = EMEVD.Read(ModEMEVDPath + $"{Map.EmevdName}.emevd.dcx");
            Points = new MapPointManager(map.Name, rand);
            Rand = rand;
            RedPhantomOdds = redPhantomOdds;
            LogicGoalIDs = new HashSet<int>();
            LogicGoalIDs.UnionWith(map.DefaultLogicScriptIDs);
            BattleGoalIDs = new HashSet<int>();
            BattleGoalIDs.UnionWith(map.DefaultBattleScriptIDs);
            PlayerStartPoint = startPoint?.GetTranslateVector(MSB);                
        }

        public void Generate()
        {
            // Generate and write MSB, LUABND, FFXBND, and slightly modified EMEVD for given Map.

#if DEBUG
            Console.WriteLine($"GENERATING MAP: {Map.Name}");
#endif
            for (int i = 0; i < Map.BossCount; i++)
                GenerateBossFight(bossIndex: i);
            if (Rand.Roll(Settings.InvaderOdds))
                GenerateInvader();
            double veryRareEnemyOdds = Run.GetFlag(GameFlag.MornsteinRingFlag) ? Settings.MornsteinVeryRareEnemyOdds : Settings.VeryRareEnemyOdds;
            if (Rand.Roll(veryRareEnemyOdds))
                GenerateVeryRareEnemy();
            bool requestAbyssPortal = Run.GetFlag(GameFlag.LoganRingFlag) || Rand.Roll(Settings.AbyssPortalOdds);
            if (requestAbyssPortal && !Map.Name.In("PaintedWorld", "ChasmOfTheAbyss", "NewLondoRuins"))
                GenerateAbyssPortal();
            if (!Run.MapsVisited.Contains(Maps.GetMap("PaintedWorld")) && Rand.Roll(Settings.PaintingOdds))
                GeneratePainting();
            GenerateMerchants();
            GenerateChests();
            GenerateItemCorpses();
            if (Rand.Roll(Settings.MimicOdds))
                GenerateMimic();
            GenerateRareEnemies();
            GenerateBasicEnemies();
            if (Rand.Roll(Settings.VagrantOdds))
                GenerateVagrant();

            FinishAndWrite();
            ClearOtherMapLUABNDs();
        }

        public void GenerateAbyssVisit()
        {
            // Generates nothing except a boss fight.
            GenerateBossFight(bossIndex: 0, isAbyss: true);
            FinishAndWrite();
        }

        public static int CreateBonfire(string gameDir, MapInfo map, float x, float y, float z, float angle, Random rand)
        {
            MapPointManager pointManager = new MapPointManager(map.Name, rand);
            GamePoint bonfirePoint = pointManager.GetClosestPoint(x, y, z, 3.0);
            if (bonfirePoint == null)
                return -1;
            GamePoint spawnPoint = pointManager.GetClosestPoint(bonfirePoint.Position, 3.0, excludeEqual: true);
            if (spawnPoint == null)
                return -1;

            MSB1 generatedMSB = MSB1.Read(gameDir + $@"map\MapStudio\{map.MsbName}.msb.rls");

            MSB1.Part.Collision bonfireCollision = generatedMSB.Parts.Collisions.Where(c => c.Name == bonfirePoint.CollisionName).First();
            MSB1.Part.Object bonfire = new MSB1.Part.Object()
            {
                ModelName = "o0200",
                EntityID = map.BonfireCharacterID + 1000,
                Name = "Bonfire Obj",
                Position = bonfirePoint.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),
                CollisionName = bonfirePoint.CollisionName,
                LightID = bonfireCollision.LightID,
                ScatterID = bonfireCollision.ScatterID,
                FogID = bonfireCollision.FogID,
                IsShadowDest = 1,
                DrawByReflectCam = 1,
            };
            generatedMSB.Parts.Objects.Add(bonfire);

            MSB1.Part.Enemy bonfireChr = new MSB1.Part.Enemy()
            {
                ModelName = "c1000",
                EntityID = map.BonfireCharacterID,
                Name = "Bonfire Chr",
                Position = bonfirePoint.Position + new Vector3(0.0f, 0.5f, 0.0f),
                Rotation = new Vector3(0.0f, angle, 0.0f),
                CollisionName = bonfirePoint.CollisionName,
                ThinkParamID = 1,
                TalkID = map.BonfireTalkID,
                NPCParamID = 100000,
                IsShadowSrc = 1,
                IsShadowDest = 1,
                DrawByReflectCam = 1,
            };
            generatedMSB.Parts.Enemies.Add(bonfireChr);

            MSB1.Region bonfireSpawnPoint = new MSB1.Region()
            {
                Name = "Bonfire Spawn Point",
                Shape = new MSB1.Shape.Point(),
                Position = spawnPoint.Position,
                EntityID = -1,
                Rotation = new Vector3(0.0f, angle, 0.0f),
            };
            generatedMSB.Regions.Regions.Add(bonfireSpawnPoint);

            MSB1.Event.SpawnPoint bonfireSpawn = new MSB1.Event.SpawnPoint()
            {
                Name = "Bonfire Spawn",
                EntityID = map.BonfireCharacterID + 2000,
                PartName = spawnPoint.CollisionName,
                SpawnPointName = "Bonfire Spawn Point",
            };
            generatedMSB.Events.SpawnPoints.Add(bonfireSpawn);

            generatedMSB.Write(gameDir + $@"map\MapStudio\{map.MsbName}.msb");
            // Keep the original '.rls' backup for potential bonfire re-creation with Solaire's Ring.
            return bonfireSpawn.EntityID;
        }

        void FinishAndWrite()
        {
            // Output MSB. Also output a '.rls' copy, so it can be reloaded and modified at bonfire creation.
            UpdateMSBModels();
#if DEBUG
            Console.WriteLine($"    Writing MSB...");
#endif
            MSB.Write(Mod.GameDir + $@"map\MapStudio\{Map.MsbName}.msb");
            MSB.Write(Mod.GameDir + $@"map\MapStudio\{Map.MsbName}.msb.rls");  // file to modify for bonfire creation
#if DEBUG
            Console.WriteLine($"    Writing EMEVD...");
#endif
            EMEVD.Write(Mod.GameDir + $@"event\{Map.EmevdName}.emevd.dcx");
            WriteMapLUABND();
            HashSet<int> enemyModels = new HashSet<int>(MSB.Models.Enemies.Select(model => int.Parse(model.Name.Substring(1))));
            WriteMapFFXBND(Map.MapID[0], enemyModels);
        }

        void GenerateBossFight(int bossIndex, bool isAbyss = false)
        {
            int bossEntityID = Map.GetBossID(bossIndex);
            if (!Maps.BossLocations.Keys.Contains(bossEntityID))
                throw new Exception($"Could not find information about location for (non-twin) boss ID {bossEntityID}.");
            (GamePoint bossPoint, int emevdIndex, int[] invalidCategories) = Maps.BossLocations[bossEntityID];
            List<int> invalidBossCategories;
            invalidBossCategories = Run.GetBossCategoriesUsed(abyss: isAbyss);
            invalidBossCategories.AddRange(invalidCategories);
            Boss boss = EnemyGenerator.GetRandomBoss(Rand, bossPoint.ArenaSize, invalidBossCategories);
#if DEBUG
            Console.WriteLine($"Excluded Boss Categories: {string.Join(", ", invalidBossCategories)}");
            Console.WriteLine($"Boss {bossIndex}: {boss.Name}");
#endif
            Enemy bossEnemy = EnemyGenerator.GetEnemy(boss.Name);
            bool isRedPhantom = Map.Name == "ChasmOfTheAbyss" || boss.AlwaysRedPhantom;  // Red phantom bosses are otherwise fought in Abyss battles only.

            var bossPart = bossEnemy.CreateMSBPart($"Boss {bossIndex}", bossEntityID, bossPoint, bossPoint.Angle, Run.MapLevel, isRedPhantom);
            MSB.Parts.Enemies.Add(bossPart);
            UpdateGoalIDs(bossPart);
            Run.EnableBossCategoryFlag(boss.Category, abyss: isAbyss);
#if DEBUG
            Console.WriteLine($"Boss Categories Used: {string.Join(", ", Run.GetBossCategoriesUsed(abyss: isAbyss))}");
#endif

            // TWIN BOSSES:
            // If arena is Large or Giant, there's a chance of a twin boss (capping their combined aggression).
            // Mornstein's ring makes it 100% chance whenever possible.
            Boss twinBoss = null;
            bool tryTwinBoss = Rand.Roll(Settings.TwinBossOdds) || Run.GetFlag(GameFlag.MornsteinRingFlag);
            if (tryTwinBoss && Maps.BossLocations.ContainsKey(bossEntityID + 1) && bossPoint.ArenaSize.In(ArenaSize.Large, ArenaSize.Giant) && boss.AggressionLevel < 5)
            {
                (GamePoint twinBossPoint, _, int[] twinInvalidCategories) = Maps.BossLocations[bossEntityID + 1];
                List<Boss> twinOptions = new List<Boss>(EnemyGenerator.BossList.Where(twin =>
                       twin.Category != boss.Category
                    && !twin.Category.In(twinInvalidCategories)
                    && twin.AggressionLevel + boss.AggressionLevel <= 5
                    && twin.RequiredArenaSize <= bossPoint.ArenaSize)
                );
                twinBoss = twinOptions.GetRandomElement(Rand);

                Enemy twinBossEnemy = EnemyGenerator.GetEnemy(twinBoss.Name);
                bool twinIsRedPhantom = Map.Name == "ChasmOfTheAbyss" || twinBoss.AlwaysRedPhantom;  // Red phantom bosses are otherwise fought in Abyss battles only.

                var twinPart = twinBossEnemy.CreateMSBPart(
                    $"Boss {bossIndex} Twin", bossEntityID + 1, twinBossPoint, twinBossPoint.Angle, Run.MapLevel, twinIsRedPhantom);
                MSB.Parts.Enemies.Add(twinPart);
                UpdateGoalIDs(twinPart);
                Run.EnableBossCategoryFlag(twinBoss.Category, abyss: isAbyss);
                Run.EnableFlag(Map.GetBossTwinFlag(bossIndex));
            }
            else
            {
                Run.DisableFlag(Map.GetBossTwinFlag(bossIndex));  // e.g. may have been set for New Londo Abyss boss previously
            }

            if (Map.Name != "LostIzalith")
            {
                // Inject name and item lot reward into EMEVD constructor.
                EMEVD.Event constructor = EMEVD.Events.Where(evt => evt.ID == 0).First();
                EMEVD.Instruction bossBattleCall = constructor.Instructions[emevdIndex];
                int itemLotID = isRedPhantom ? bossEnemy.RedPhantomItemLotParamID : bossEnemy.ItemLotParamID;  // twin item lot ignored
                WriteEventInstructionInt(bossBattleCall, 32, itemLotID);
                WriteEventInstructionShort(bossBattleCall, 52, boss.NameTextID);
                if (twinBoss != null)
                    WriteEventInstructionShort(bossBattleCall, 54, twinBoss.NameTextID);
            }
        }

        void GenerateInvader()
        {
            string regionLabel = GetRegionLabel();

            int invaderIndex = Run.CheckOutInvader();
            int invaderParamID = 7000 + 10 * invaderIndex;  // also invasion event text base ID
            int invaderEntityID = Map.BaseNPCEntityID + 50;

            GamePoint spawnPoint = Points.CheckOutRandomPoint("Invader", (int)ChrSize.Normal);
            GamePoint triggerPoint = Points.CheckOutRandomPointWithinDistance(
                "Invader Trigger",
                spawnPoint,
                Math.Pow(Settings.MinInvaderDistanceFromTrigger, 2),
                Math.Pow(Settings.MaxInvaderDistanceFromTrigger, 2)
            );
            float angle = MapPointManager.GetFacingPoint(spawnPoint, triggerPoint);
            MSB1.Part.Enemy invader = GetInvaderPart(invaderEntityID, spawnPoint.Position, angle, spawnPoint.CollisionName, invaderParamID, Run.MapLevel);
            MSB.Parts.Enemies.Add(invader);
            
            MSB1.Region triggerRegion = new MSB1.Region()
            {
                Name = "Invader Trigger",
                Position = triggerPoint.Position - new Vector3(0.0f, 1.0f, 0.0f),  // 1.0 units below point
                Shape = new MSB1.Shape.Box() { Width = 20.0f, Depth = 20.0f, Height = 10.0f },
                EntityID = Map.InvaderTriggerRegionID,
            };
            MSB.Regions.Regions.Add(triggerRegion);

            // All invader AI scripts are already present in the `aiCommon.luabnd.dcx` file in the Roguelike `Package` folder.

            // Inject invasion message IDs into EMEVD preconstructor (always first instruction, plus area offset).
            EMEVD.Event preconstructor = EMEVD.Events.Where(evt => evt.ID == 50).First();
            EMEVD.Instruction invaderTriggerCall = preconstructor.Instructions[Map.IndexInMap];
            int invaderTriggerMessage = invaderParamID;
            int invaderDeathMessage = invaderParamID + 1;
            WriteEventInstructionInt(invaderTriggerCall, 8, invaderTriggerMessage);
            WriteEventInstructionInt(invaderTriggerCall, 12, invaderDeathMessage);
        }

        void GenerateVeryRareEnemy()
        {
            string regionLabel = GetRegionLabel();
            int entityID = Map.BaseEntityID + VeryRareEnemyOffset;
            Enemy enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, EnemyRarity.VeryRare, Run.MapLabels[Map]);
            GamePoint point = Points.CheckOutRandomPoint(
                "VeryRare Enemy",
                (int)enemy.Size,
                regionLabel,
                avoidPoint: PlayerStartPoint,
                avoidRadiusSq: Math.Pow(Settings.MinEnemyDistanceFromSpawnPoint, 2)
            );
            if (Map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                entityID += NewLondoVeryRareEnemyOffset;
            var enemyPart = enemy.CreateMSBPart("VeryRare Enemy 1", entityID, point, Rand.NextAngle(), Run.MapLevel, isRedPhantom: Rand.Roll(RedPhantomOdds));
            
            // Enemy is likely to be huge, and so is always drawn.
            enemyPart.DrawGroups = new uint[4] { 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF };
            enemyPart.CollisionName = null;
            
            MSB.Parts.Enemies.Add(enemyPart);
            UpdateGoalIDs(enemyPart);
        }

        void GenerateAbyssPortal()
        {
            GamePoint point = Points.CheckOutRandomPoint(
                "Abyss Portal",
                0,
                avoidPoint: PlayerStartPoint,
                avoidRadiusSq: Math.Pow(Settings.MinEnemyDistanceFromSpawnPoint, 2)
            );
            MSB1.Part.Player portalWarpBack = new MSB1.Part.Player()
            {
                Name = "Portal Return",
                Position = point.Position,
                Rotation = new Vector3(0.0f, Rand.NextAngle(), 0.0f),
                EntityID = Map.PortalWarpPointID,
                IsShadowSrc = 1,
                IsShadowDest = 1,
                ModelName = "c0000",
            };
            MSB.Parts.Players.Add(portalWarpBack);
            MSB1.Region portalPoint = new MSB1.Region()
            {
                Name = "Portal VFX Point",
                Position = point.Position + new Vector3(0.0f, 2.0f, 0.0f),
                Shape = new MSB1.Shape.Point(),
                EntityID = -1,
            };
            MSB.Regions.Regions.Add(portalPoint);
            MSB1.Event.SFX portalVFX = new MSB1.Event.SFX()
            {
                Name = "Portal VFX",
                FFXID = 120027,
                RegionName = "Portal VFX Point",
                PartName = point.CollisionName,
                EntityID = Map.PortalFXID,
            };
            MSB.Events.SFXs.Add(portalVFX);
            MSB1.Part.Enemy portalTrigger = new MSB1.Part.Enemy()
            {
                ModelName = "c1000",
                Name = "Portal Trigger",
                Position = point.Position + new Vector3(0.0f, 0.5f, 0.0f),
                EntityID = Map.PortalTriggerCharacterID,
                NPCParamID = 100000,
                TalkID = 0,
                CollisionName = point.CollisionName,
                ThinkParamID = 1,
            };
            MSB.Parts.Enemies.Add(portalTrigger);
        }

        void GeneratePainting()
        {
            // Painting appears, in a random choice of its possible positions (pre-existing in base MSB).
            // TODO: 3-4 positions per Map. Wherever it fits. Proper collision assignment, etc. Also prompt regions for simplicity.
        }

        void GenerateMerchants()
        {
            foreach (Merchant merchant in CharacterGenerator.MerchantList)
            {
                if (Run.GetFlag(merchant.DeadFlag))
                    continue;  // Merchant is dead and cannot appear again.

                string regionLabel;
                if (Map.Name == "Blighttown")
                    regionLabel = Rand.Roll(Settings.BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                double merchantOdds = merchant.Name == "Marvelous Chester" ? Settings.ChesterOdds : Settings.MerchantOdds;
                if (Rand.Roll(merchantOdds))
                {
                    if (Map.Name == "NewLondoRuins")
                        regionLabel = "Upper";  // no merchants in lower
                    GamePoint point = Points.CheckOutRandomPointCustomNearbyRadius("Merchant", 2.0, 5, regionLabel);
                    var merchantPart = merchant.GetPart(point, Points.GetAngleFacingNearestPoint(point), Map.TalkIDBase);
                    MSB.Parts.Enemies.Add(merchantPart);
                    LogicGoalIDs.Add(Mod.GPARAM.AI[merchantPart.ThinkParamID].LogicID);
                    BattleGoalIDs.Add(Mod.GPARAM.AI[merchantPart.ThinkParamID].BattleID);

                    if (merchant.Name == "Andre of Astora")
                    {
                        if (!MSB.Models.Objects.Select(model => model.Name).Contains("o1252"))
                            MSB.Models.Objects.Add(ModelTemplates.AndreAnvilModel);

                        var anvilPart = GetGroupedObject(
                            merchantPart, xzDistance: 0.6594619018563561f, yOffset: 0.043f, relativeDirection: -7.0892628848495605f, relativeOrientation: -0.5f,
                            modelName: "o1252", objectName: "o1252_AndreAnvil"
                        );
                        MSB.Parts.Objects.Add(anvilPart);
                    }

                    if (merchant.Name == "Vamos")
                    {
                        if (!MSB.Models.Objects.Select(model => model.Name).Contains("o3870"))
                            MSB.Models.Objects.Add(ModelTemplates.VamosAnvilModel);
                        var anvilPart = GetGroupedObject(
                            merchantPart, xzDistance: 0.25831182706178923f, yOffset: 0.0f, relativeDirection: -168.55588615611774f, relativeOrientation: 0.5f,
                            modelName: "o3870", objectName: "o3870_VamosAnvil"
                        );
                        MSB.Parts.Objects.Add(anvilPart);
                    }
                }
            }
        }

        void GenerateChests()
        {
            int chestCount = Math.Max(0, Rand.Next(Map.ChestCount - 2, Map.ChestCount));
            List<int> usedChestTreasure = new List<int>();
            for (int i = 0; i < chestCount; i++)
            {
                string regionLabel;
                if (Map.Name == "Blighttown")
                    regionLabel = Rand.Roll(Settings.BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                int chestID = Map.BaseChestEntityID + i;
                GamePoint point = Points.CheckOutRandomPointCustomNearbyRadius("Chest", 2.0, 5, regionLabel);
                float angle = Points.GetAngleFacingNearestPoint(point);
                MSB1.Part.Object chestPart = GetTreasureObjectPart(i, chestID, angle, point, isChest: true);
                MSB.Parts.Objects.Add(chestPart);

                var objAct = new MSB1.Event.ObjAct()
                {
                    Name = $"Chest ObjAct {i}",
                    ObjActEntityID = Map.BaseChestObjActFlagID + i,
                    ObjActPartName = $"Chest {i}",
                    EventFlagID = 0,
                };
                MSB.Events.ObjActs.Add(objAct);

                var treasure = new MSB1.Event.Treasure()
                {
                    Name = $"Chest Treasure {i}",
                    TreasurePartName = $"Chest {i}",
                    PartName = point.CollisionName,
                    InChest = true,
                    StartDisabled = true,  // can't get the treasure to disable itself based on 'InChest' alone...
                };
                // Choose random treasure in unlocked range.
                treasure.ItemLots[0] = GetChestTreasureID(Map.BaseChestItemLotID, usedChestTreasure);
                usedChestTreasure.Add(treasure.ItemLots[0]);
                MSB.Events.Treasures.Add(treasure);
            }
        }

        void GenerateItemCorpses()
        {
            int itemCount = Math.Max(0, Rand.Next(Map.ItemCorpseCount - 5, Map.ItemCorpseCount));
            List<int> usedCorpseTreasure = new List<int>();
            for (int i = 0; i < itemCount; i++)
            {
                string regionLabel = GetRegionLabel();
                GamePoint point = Points.CheckOutRandomPointWeightedInverseNearby($"Item Corpse {i}", 0, regionLabel);
                short pose = Objects.CorpsePoses.GetRandomElement(Rand);
                float poseOffset = Objects.CorpsePoseYOffsets[pose];
                
                MSB1.Part.Object corpsePart = GetTreasureObjectPart(i, -1, Rand.NextAngle(), point, isChest: false);
                corpsePart.ObjectPose = pose;
                corpsePart.Position += new Vector3(0.0f, poseOffset, 0.0f);
                MSB.Parts.Objects.Add(corpsePart);

                MSB1.Event.Treasure treasure = new MSB1.Event.Treasure()
                {
                    Name = $"Item Corpse Treasure {i}",
                    TreasurePartName = $"Item Corpse {i}",
                    PartName = point.CollisionName,
                    InChest = false,
                };
                // Assign random corpse treasure from unlocked ranges.
                treasure.ItemLots[0] = GetCorpseTreasureID(Map.BaseCorpseItemLotID, usedCorpseTreasure);
                usedCorpseTreasure.Add(treasure.ItemLots[0]);
                MSB.Events.Treasures.Add(treasure);
            }
        }

        void GenerateMimic()
        {
            string regionLabel = GetRegionLabel(forceUpperNewLondo: true);  // No Mimics in lower NLR
            int mimicEntityID = Map.BaseEntityID + MimicOffset;
            Enemy mimic = EnemyGenerator.GetEnemy("Mimic");
            GamePoint point = Points.CheckOutRandomPoint("Mimic", (int)mimic.Size, regionLabel);
            float angle = Points.GetAngleFacingNearestPoint(point);
            var part = mimic.CreateMSBPart("Mimic", mimicEntityID, point, angle, Run.MapLevel, isRedPhantom: Rand.Roll(RedPhantomOdds));
            MSB.Parts.Enemies.Add(part);
            UpdateGoalIDs(part);

            MSB1.Region mimicNest = new MSB1.Region()
            {
                Name = "Mimic Nest",
                Position = new Vector3(point.Position.X, point.Position.Y - 0.1f, point.Position.Z),
                Rotation = new Vector3(0.0f, angle, 0.0f),
                Shape = new MSB1.Shape.Box() { Width = 5.0f, Depth = 5.0f, Height = 2.0f },
                EntityID = mimicEntityID + 5,
            };
            MSB.Regions.Regions.Add(mimicNest);
        }

        void GenerateRareEnemies()
        {
            int rareCount = Math.Max(0, Rand.Next(Map.RareEnemyCount - 3, Map.RareEnemyCount));
            if (Run.GetFlag(GameFlag.LobosJrRingFlag))
                rareCount += 5;
            List<Enemy> usedRareEnemies = new List<Enemy>();
            int rarePhantomCount = 0;
            for (int i = 0; i < rareCount; i++)
            {
                // First rare enemy is always in Upper New Londo Ruins (for Holy Sigil drop).
                string regionLabel = GetRegionLabel(forceUpperNewLondo: i == 0);

                Enemy enemy;
                if (usedRareEnemies.Count > Settings.MaxRareEnemyTypeCount)
                    enemy = usedRareEnemies.GetRandomElement(Rand);
                else
                {
                    enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, EnemyRarity.Rare, Run.MapLabels[Map]);
                    if (!usedRareEnemies.Contains(enemy))
                        usedRareEnemies.Add(enemy);
                }

                bool isRedPhantom = rarePhantomCount < 15 && Rand.Roll(RedPhantomOdds);
                if (isRedPhantom)
                    rarePhantomCount++;

                GamePoint point = Points.CheckOutRandomPoint(
                    "Rare Enemy",
                    (int)enemy.Size,
                    regionLabel,
                    avoidPoint: PlayerStartPoint,
                    avoidRadiusSq: Math.Pow(Settings.MinEnemyDistanceFromSpawnPoint, 2)
                );
                int entityID = Map.BaseEntityID + RareEnemyOffset + i;
                if (Map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                    entityID += NewLondoLowerRareEnemyOffset;
                MSB1.Part.Enemy enemyPart = enemy.CreateMSBPart($"Rare Enemy {i}", entityID, point, Rand.NextAngle(), Run.MapLevel, isRedPhantom);
                MSB.Parts.Enemies.Add(enemyPart);
                UpdateGoalIDs(enemyPart);                
            }
        }

        void GenerateBasicEnemies()
        {
            // Includes both Common and Uncommon enemies.
            int basicEnemyCount = Math.Max(0, Rand.Next(Map.BasicEnemyCount - 5, Map.BasicEnemyCount));
            if (Run.GetFlag(GameFlag.LobosJrRingFlag))
                basicEnemyCount -= 5;  // replaced by rare enemies
            int basicPhantomCount = 0;
            int basicNonPhantomCount = 0;
            List<Enemy> usedCommonEnemyTypes = new List<Enemy>();
            List<Enemy> usedUncommonEnemyTypes = new List<Enemy>();
            for (int i = 0; i < basicEnemyCount; i++)
            {
                string regionLabel = GetRegionLabel();

                Enemy enemy;
                double uncommonEnemyOdds = Run.GetFlag(GameFlag.LobosJrRingFlag) ? Settings.UncommonEnemyOdds : Settings.LobosJrUncommonEnemyOdds;
                EnemyRarity rarity = Rand.Roll(uncommonEnemyOdds) ? EnemyRarity.Uncommon : EnemyRarity.Common;
                if (rarity == EnemyRarity.Common)
                {
                    if (usedCommonEnemyTypes.Count > Settings.MaxCommonEnemyTypeCount)
                        enemy = usedCommonEnemyTypes.GetRandomElement(Rand);
                    else
                    {
                        enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, rarity, Run.MapLabels[Map]);
                        usedCommonEnemyTypes.Add(enemy);
                    }
                }
                else
                {
                    if (usedUncommonEnemyTypes.Count > Settings.MaxUncommonEnemyTypeCount)
                        enemy = usedUncommonEnemyTypes.GetRandomElement(Rand);
                    else
                    {
                        enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, rarity, Run.MapLabels[Map]);
                        usedUncommonEnemyTypes.Add(enemy);
                    }
                }

                bool isRedPhantom = basicPhantomCount < 15 && Rand.Roll(RedPhantomOdds);
                if (isRedPhantom)
                    basicPhantomCount++;
                else
                    basicNonPhantomCount++;

                int entityID = Map.BaseEntityID + (isRedPhantom ? BasicPhantomOffset + basicPhantomCount : BasicEnemyOffset + basicNonPhantomCount);
                GamePoint point = Points.CheckOutRandomPoint(
                    "Basic Enemy",
                    (int)enemy.Size,
                    regionLabel,
                    avoidPoint: PlayerStartPoint,
                    avoidRadiusSq: Math.Pow(Settings.MinEnemyDistanceFromSpawnPoint, 2)
                );
                if (Map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                    entityID += isRedPhantom ? NewLondoLowerBasicPhantomOffset : NewLondoLowerBasicEnemyOffset;
                MSB1.Part.Enemy enemyPart = enemy.CreateMSBPart($"Basic Enemy {i}", entityID, point, Rand.NextAngle(), Run.MapLevel, isRedPhantom);
                MSB.Parts.Enemies.Add(enemyPart);
                UpdateGoalIDs(enemyPart);

                if (Rand.Roll(Settings.EnemyPatrolOdds))
                {
                    int patrolPointCount = Rand.Next(Settings.MinEnemyPatrolPointCount, Settings.MaxEnemyPatrolPointCount + 1);
                    GamePoint lastPoint = point;
                    List<string> patrolPointNames = new List<string>();
                    for (int j = 0; j < patrolPointCount; j++)
                    {
                        string patrolPointName = $"Basic Enemy {i} Patrol {j}";
                        GamePoint patrolPoint;
                        try
                        {
                            patrolPoint = Points.CheckOutRandomPointWithinDistance(
                                patrolPointName, lastPoint, Math.Pow(Settings.MinPatrolPointGap, 2), Math.Pow(Settings.MaxPatrolPointGap, 2)
                            );
                        }
                        catch (ArgumentException)
                        {
                            // Can't find next patrol point. No more patrol points.
                            break;
                        }
                        
                        MSB1.Region patrolRegion = new MSB1.Region()
                        {
                            Name = patrolPointName,
                            Shape = new MSB1.Shape.Point(),
                            Position = patrolPoint.Position,
                            EntityID = -1,
                            Rotation = new Vector3(0.0f, Rand.NextAngle(), 0.0f),
                        };
                        MSB.Regions.Regions.Add(patrolRegion);
                        patrolPointNames.Add(patrolPointName);
                        lastPoint = patrolPoint;
                    }
                    while (patrolPointNames.Count < 8)
                        patrolPointNames.Add(null);
                    enemyPart.MovePointNames = patrolPointNames.ToArray();
                }
            }
        }

        void GenerateVagrant()
        {
            string regionLabel = GetRegionLabel(forceUpperNewLondo: true);  // No Vagrants in lower New Londo Ruins
            double redPhantomOdds;
            if (Run.GetFlag(GameFlag.MornsteinRingFlag))
                redPhantomOdds = Settings.MornsteinVagrantRedPhantomOdds;
            else
                redPhantomOdds = Settings.VagrantRedPhantomOdds;
            bool isRedPhantom = Rand.Roll(redPhantomOdds);
            int entityID = Map.BaseEntityID + VagrantOffset;
            Enemy vagrant = EnemyGenerator.GetEnemy(Rand.Roll(Settings.EvilVagrantOdds) ? "Evil Vagrant" : "Good Vagrant");
            GamePoint point = Points.CheckOutRandomPoint(
                "Vagrant",
                (int)vagrant.Size,
                regionLabel,
                avoidPoint: PlayerStartPoint,
                avoidRadiusSq: Math.Pow(Settings.MinEnemyDistanceFromSpawnPoint, 2)
            );
            MSB1.Part.Enemy vagrantPart = vagrant.CreateMSBPart($"Vagrant", entityID, point, Rand.NextAngle(), Run.MapLevel, isRedPhantom);
            MSB.Parts.Enemies.Add(vagrantPart);
            UpdateGoalIDs(vagrantPart);
        }

        string GetRegionLabel(bool forceUpperNewLondo = false)
        {
            if (Map.Name == "Blighttown")
                return Rand.Roll(Settings.BlighttownSwampOdds) ? "Swamp" : "Shanty";
            else if (Map.Name == "NewLondoRuins" && forceUpperNewLondo)
                return "Upper";
            else
                return "";
        }

        void UpdateGoalIDs(MSB1.Part.Enemy enemyPart)
        {
            LogicGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].LogicID);
            BattleGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].BattleID);
        }

        void UpdateMSBModels()
        {
#if DEBUG
            Console.WriteLine($"    Updating models...");
#endif
            // Basic object models should always be present (including Painting).
            if (!MSB.Models.Objects.Select(model => model.Name).Contains("o0110"))
                MSB.Models.Objects.Add(ModelTemplates.ChestModel);
            if (!MSB.Models.Objects.Select(model => model.Name).Contains("o0200"))
                MSB.Models.Objects.Add(ModelTemplates.BonfireModel);
            if (!MSB.Models.Objects.Select(model => model.Name).Contains("o0500"))
                MSB.Models.Objects.Add(ModelTemplates.CorpseModel);
            if (!MSB.Models.Objects.Select(model => model.Name).Contains("o5850"))
                MSB.Models.Objects.Add(ModelTemplates.PaintingModel);
            // Clear enemy and Player models, then repopulate enemy models from all present enemies.
            MSB.Models.Enemies.Clear();
            MSB.Models.Players.Clear();  // c0000 added to Enemy models instead
            MSB.Models.Enemies.Add(ModelTemplates.PlayerModel);  // c0000
            MSB.Models.Enemies.Add(ModelTemplates.EmptyModel);  // c1000
            foreach (MSB1.Part.Enemy enemy in MSB.Parts.Enemies)
            {
                if (!MSB.Models.Enemies.Select(model => model.Name).Contains(enemy.ModelName))
                    MSB.Models.Enemies.Add(GetEnemyModel(enemy.ModelName));
            }
            foreach (MSB1.Part.DummyEnemy enemy in MSB.Parts.DummyEnemies)
            {
                if (!MSB.Models.Enemies.Select(model => model.Name).Contains(enemy.ModelName))
                    MSB.Models.Enemies.Add(GetEnemyModel(enemy.ModelName));
            }
        }      

        MSB1.Part.Object GetTreasureObjectPart(int index, int entityID, float angle, GamePoint point, bool isChest)
        {
            MSB1.Part.Collision objCollision = MSB.Parts.Collisions.Where(c => c.Name == point.CollisionName).First();
            MSB1.Part.Object objPart = new MSB1.Part.Object()
            {
                Name = isChest ? $"Chest {index}" : $"Item Corpse {index}",
                Position = point.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),
                CollisionName = point.CollisionName,
                EntityID = entityID,
                ModelName = isChest ? "o0110" : "o0500",
                IsShadowSrc = 1,
                IsShadowDest = 1,
                DrawByReflectCam = 1,  // Enabled in vanilla Archives; likely can't hurt.
                LightID = objCollision.LightID,
                ScatterID = objCollision.ScatterID,
                FogID = objCollision.FogID,
            };
            objPart.ClearDrawGroups();
            objPart.ClearDispGroups();
            return objPart;
        }

        int GetCorpseTreasureID(int baseItemLotID, List<int> usedTreasureIDs)
        {
            List<int> available = new List<int>();
            foreach (var keyValue in MapItemLotsGenerator.CorpseUnlockRanges)
            {
                if (keyValue.Key == GameFlag.None || Run.GetFlag(keyValue.Key))
                {
                    (int baseMin, int baseMax) = keyValue.Value;
                    for (int i = baseMin; i < baseMax; i++)
                    {
                        int treasureID = baseItemLotID + 10 * i;
                        if (!usedTreasureIDs.Contains(treasureID))
                            available.Add(treasureID);
                    }
                }
            }
            return available.GetRandomElement(Rand);
        }

        int GetChestTreasureID(int baseItemLotID, List<int> usedTreasureIDs)
        {
            List<int> available = new List<int>();
            foreach (var keyValue in MapItemLotsGenerator.ChestUnlockRanges)
            {
                if (keyValue.Key == GameFlag.None || Run.GetFlag(keyValue.Key))
                {
                    (int baseMin, int baseMax) = keyValue.Value;
                    for (int i = baseMin; i < baseMax; i++)
                    {
                        int treasureID = baseItemLotID + 10 * i;
                        if (!usedTreasureIDs.Contains(treasureID))
                            available.Add(treasureID);
                    }
                }
            }
            return available.GetRandomElement(Rand);
        }

        void WriteMapFFXBND(int mapBlockID, HashSet<int> enemyModels)
        {
#if DEBUG
            Console.WriteLine($"    Writing FFXBND...");
#endif
            HashSet<int> addedIDs = new HashSet<int>();
            string ffxBNDName = $"FRPG_SfxBnd_m{mapBlockID:00}";
            BND3 ffxBND = BND3.Read(GetGameDataResource(ffxBNDName + "_ffxbnd"));
            int bndIndex = ffxBND.Files.Where(file => file.ID < 100000).Max(file => file.ID) + 1;
            Dictionary<string, BND3> openBNDs = new Dictionary<string, BND3>();
            foreach (int enemyModel in enemyModels)
            {
                if (!EnemyGenerator.EnemyFFXSources.ContainsKey(enemyModel))
                {
                    Console.WriteLine($"ERROR: No FFX dictionary listed for enemy model {enemyModel:0000}. VFX will be missing; please report to Grim!");
                    continue;
                }
                foreach (var indexPath in EnemyGenerator.EnemyFFXSources[enemyModel])
                {
                    if (addedIDs.Contains(indexPath.Key))
                        continue;  // already added by another enemy
                    if (!indexPath.Value.Contains($"m{mapBlockID:00}"))  // if enemy FFX is not already present in current block (or sub) FFXBND file...
                    {
                        string ffxFileName = $"f{indexPath.Key:0000000}.ffx";
                        //Console.WriteLine($"{enemyModel} enemy model adding: {ffxFileName}");
                        if (!openBNDs.ContainsKey(indexPath.Value))
                            openBNDs[indexPath.Value] = BND3.Read(GetGameDataResource(indexPath.Value + "_ffxbnd"));
                        // Lookup should never fail, by construction of FFXInfo. (But just in case it does, I'd rather print an error and have missing VFX.)
                        var matches = openBNDs[indexPath.Value].Files.Where(f => f.Name.EndsWith(ffxFileName));
                        if (!matches.Any())
                        {
                            Console.WriteLine($"ERROR: Could not find FFX {ffxFileName} in FFXBND {indexPath.Value}. VFX will be missing; please report to Grim!");
                            continue;
                        }
                        BinderFile ffxFile = matches.First();
                        ffxFile.ID = bndIndex;
                        bndIndex++;
                        ffxBND.Files.Add(ffxFile);
                        addedIDs.Add(indexPath.Key);
                    }
                }
            }
            ffxBND.Write(Mod.GameDir + $@"sfx\{ffxBNDName}.ffxbnd.dcx");
        }

        void WriteMapLUABND()
        {
#if DEBUG
            Console.WriteLine($"    Writing LUABND...");
#endif
            // Reads from a folder full of unpacked binary AI Lua scripts and generates a LUABND for the given map ID name.
            // Note that in DSR, LUAINFO files are not needed (and LUAGNL was never needed).
            if (!BattleGoalIDs.Any())
                throw new Exception("Empty list of battle goal IDs passed to Lua packer, which is not ever expected.");

            BND3 mapLuaBND = new BND3 { Timestamp = "07D7R6" };
            mapLuaBND.Compression = DCX.Type.DarkSouls1;

            int bndID = 1055;  // first "safe" ID for loading order, according to vanilla use
            
            // Ignore logic goals already in aiCommon.
            int[] commonLogicGoals = { 10000, 10001, 11000 };
            
            foreach (int goalID in LogicGoalIDs)
            {
                if (commonLogicGoals.Contains(goalID)) continue;
                string scriptPath = $"_{goalID:000000}_logic";
                string bndPath = $@"N:\FRPG\data\INTERROOT_x64\script\ai\out\bin\{goalID:000000}_logic.lua";
                BinderFile bndEntry = new BinderFile(Binder.FileFlags.x40, bndID, bndPath, GetGameDataResource(scriptPath));
                mapLuaBND.Files.Add(bndEntry);
                bndID++;
            }
            foreach (int goalID in BattleGoalIDs)
            {
                string scriptPath = $"_{goalID:000000}_battle";
                string bndPath = $@"N:\FRPG\data\INTERROOT_x64\script\ai\out\bin\{goalID:000000}_battle.lua";
                BinderFile bndEntry = new BinderFile(Binder.FileFlags.x40, bndID, bndPath, GetGameDataResource(scriptPath));
                mapLuaBND.Files.Add(bndEntry);
                bndID++;
            }
            // LUABND name is same as EMEVD name.
            mapLuaBND.Write(Mod.GameDir + $@"script\{Map.EmevdName}.luabnd.dcx");
        }

        void ClearOtherMapLUABNDs()
        {
            // Puts an empty LUABND into other used game maps (not Firelink Shrine or Undead Asylum).
            foreach (MapInfo map in Maps.MapList)
            {
                string emevdName = map.EmevdName;
                if (emevdName == Map.EmevdName) continue;  // skip active map
                BND3 mapLuaBND = new BND3 { Timestamp = "07D7R6"};
                mapLuaBND.Compression = DCX.Type.DarkSouls1;
                mapLuaBND.Write(Mod.GameDir + $@"script\{map.EmevdName}.luabnd.dcx");
            }
        }

        MSB1.Part.Enemy GetInvaderPart(int entityID, Vector3 position, float angle, string collisionName, int paramID, int level)
        {
            return new MSB1.Part.Enemy()
            {
                Name = $"Invader {paramID}",
                ThinkParamID = paramID,
                NPCParamID = paramID + (level - 1),
                TalkID = -1,
                CharaInitID = paramID,
                CollisionName = collisionName,
                EntityID = entityID,
                Position = position,
                Rotation = new Vector3(0.0f, angle, 0.0f),  // in degrees
                ModelName = "c0000",
                DispGroups = new uint[4] { 0, 0, 0, 0 },
                // Leave all draw groups active (in addition to collision name).
            };
        }

        MSB1.Model GetEnemyModel(string modelName)
        {
            return new MSB1.Model() { Name = modelName, Placeholder = $@"N:\FRPG\data\Model\chr\{modelName}\sib\{modelName}.sib" };
        }

        byte[] GetGameDataResource(string resourceName)
        {
            return (byte[])Resources.GameData.ResourceManager.GetObject(resourceName);
        }

        void WriteEventInstructionInt(EMEVD.Instruction instruction, int offset, int value)
        {
            List<byte> argData = instruction.ArgData.ToList();
            argData[offset + 0] = (byte)(value >> 0x00);
            argData[offset + 1] = (byte)(value >> 0x08);
            argData[offset + 2] = (byte)(value >> 0x10);
            argData[offset + 3] = (byte)(value >> 0x18);
            instruction.ArgData = argData.ToArray();
        }
        void WriteEventInstructionShort(EMEVD.Instruction instruction, int offset, short value)
        {
            List<byte> argData = instruction.ArgData.ToList();
            argData[offset + 0] = (byte)(value >> 0x00);
            argData[offset + 1] = (byte)(value >> 0x08);
            instruction.ArgData = argData.ToArray();
        }

        MSB1.Part.Object GetGroupedObject(
            MSB1.Part.Enemy baseChr, float xzDistance, float yOffset, float relativeDirection, float relativeOrientation,
            string modelName, string objectName
        )
        {
            float objectDirection = baseChr.Rotation.Y + relativeDirection;
            float objectX = baseChr.Position.X + xzDistance * (float)-Math.Sin(Math.PI / 180.0f * objectDirection);
            float objectY = baseChr.Position.Y + yOffset;
            float objectZ = baseChr.Position.Z + xzDistance * (float)-Math.Cos(Math.PI / 180.0f * objectDirection);
            float objectAngle = baseChr.Rotation.Y - 5.0f;

            return new MSB1.Part.Object()
            {
                Name = objectName,
                ModelName = modelName,
                CollisionName = baseChr.CollisionName,
                LightID = baseChr.LightID,
                FogID = baseChr.FogID,
                ScatterID = baseChr.ScatterID,
                DrawGroups = new uint[4] { 0, 0, 0, 0 },
                Position = new Vector3(objectX, objectY, objectZ),
                Rotation = new Vector3(0.0f, objectAngle, 0.0f),
            };
        }
    }
}
