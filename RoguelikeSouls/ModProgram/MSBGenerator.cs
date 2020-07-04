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
        public static MSB1.Model PaintingModel { get; } = new MSB1.Model() { Name = "o5850", Placeholder = @"N:\FRPG\data\Model\obj\o5850\sib\o5850.sib" };
        public static MSB1.Model CorpseModel { get; } = new MSB1.Model() { Name = "o0500", Placeholder = @"N:\FRPG\data\Model\obj\o0500\sib\o0500.sib" };
        public static MSB1.Model ChestModel { get; } = new MSB1.Model() { Name = "o0110", Placeholder = @"N:\FRPG\data\Model\obj\o0110\sib\o0110.sib" };
        public static MSB1.Model PlayerModel { get; } = new MSB1.Model() { Name = "c0000", Placeholder = @"N:\FRPG\data\Model\chr\c0000\sib\c0000.SIB" };
        public static MSB1.Model EmptyModel { get; } = new MSB1.Model() { Name = "c1000", Placeholder = @"N:\FRPG\data\Model\chr\c1000\sib\c1000.sib" };
    }

    class MSBGenerator
    {
        SoulsMod Mod { get; }
        RunManager Run { get; }
        Random Rand { get; }

        const int BasicEnemyOffset = 0;
        const int BasicPhantomOffset = 100;
        const int RareEnemyOffset = 130;
        const int VeryRareEnemyOffset = 170;
        const int MimicOffset = 180;
        const int VagrantOffset = 190;

        const int NewLondoLowerBasicEnemyOffset = 50;
        const int NewLondoLowerBasicPhantomOffset = 15;
        const int NewLondoLowerRareEnemyOffset = 15;
        const int NewLondoVeryRareEnemyOffset = 5;
        // Mimics and Vagrants won't appear in lower New Londo.
        
        const int MaxCommonEnemyTypeCount = 15;
        const int MaxUncommonEnemyTypeCount = 10;
        const int MaxRareEnemyTypeCount = 10;

        const double PaintingOdds = 0.15;
        const double VeryRareEnemyOdds = 0.3;
        const double MimicOdds = 0.4;
        const double MerchantOdds = 0.25;
        const double ChesterOdds = 0.1;
        const double InvaderOdds = 0.0;  // TODO: if I get it working, probably 0.5
        const double AbyssPortalOdds = 0.33;
        const double UncommonEnemyOdds = 0.25;
        const double TwinBossOdds = 0.5;  // odds only apply if twin boss is possible
        
        // Map-specific odds.
        const double BlighttownSwampOdds = 0.25;

        string ModMSBPath { get; } = @"Package\map\MapStudio\";
        string ModEMEVDPath { get; } = @"Package\event\";
        
        public MSBGenerator(RunManager runManager, SoulsMod mod, Random random)
        {
            Run = runManager;
            Mod = mod;
            Rand = random;
        }

        public void GenerateMapData(Map map, double redPhantomOdds)
        {
            // Generate and write MSB, LUABND, and tweaked EMEVD for given map.

#if DEBUG
            Console.WriteLine($"GENERATING MAP: {map.Name}");
#endif

            MSB1 msb = MSB1.Read(ModMSBPath + $"{map.MsbName}.msb");
            EMEVD emevd = EMEVD.Read(ModEMEVDPath + $"{map.EmevdName}.emevd.dcx");

            EMEVD.Event constructor = emevd.Events.Where(evt => evt.ID == 0).First();

            HashSet<int> enemyModels = new HashSet<int>();
            HashSet<int> logicGoalIDs = new HashSet<int>(map.DefaultLogicScriptIDs);
            HashSet<int> battleGoalIDs = new HashSet<int>(map.DefaultBattleScriptIDs);

            MapPointManager pointManager = new MapPointManager(map.Name, Rand);
            int rarePhantomCount = 0;
            int basicPhantomCount = 0;

            string regionLabel;
            
            for (int i = 0; i < map.BossCount; i++)
            {
                // BOSSES

                int bossEntityID = map.GetBossID(i);
                if (!Maps.BossLocations.Keys.Contains(bossEntityID))
                    throw new Exception($"Could not find information about location for (non-twin) boss ID {bossEntityID}.");
                (GamePoint bossPoint, int emevdIndex, int[] invalidCategories) = Maps.BossLocations[bossEntityID];
                List<int> invalidBossCategories = new List<int>(Run.BossCategoriesUsed);
                invalidBossCategories.AddRange(invalidCategories);
                Boss boss = EnemyGenerator.GetRandomBoss(Rand, bossPoint.ArenaSize, invalidBossCategories);
#if DEBUG
                Console.WriteLine($"Boss {i}: {boss.Name}");
#endif
                Enemy bossEnemy = EnemyGenerator.GetEnemy(boss.Name);
                bool isRedPhantom = map.Name == "ChasmOfTheAbyss" || boss.AlwaysRedPhantom;  // Red phantom bosses are otherwise fought in Abyss battles only.

                var part = bossEnemy.GetMSBPart($"Boss {i}", bossEntityID, bossPoint, bossPoint.Angle, Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(part);
                logicGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].BattleID);
                Run.BossCategoriesUsed.Add(boss.Category);
                enemyModels.Add(bossEnemy.ModelID);

                // TWIN BOSSES:
                // If arena is Large or Giant, there's a chance of a twin boss (capping their combined aggression).
                // Mornstein's ring makes it 100% chance whenever possible.
                Boss twinBoss = null;
                if ((Roll(TwinBossOdds) || Run.GetFlag(GameFlag.MornsteinRingFlag)) && Maps.BossLocations.ContainsKey(bossEntityID + 1) && bossPoint.ArenaSize.In(ArenaSize.Large, ArenaSize.Giant) && boss.AggressionLevel < 5)
                {                    
                    (GamePoint twinBossPoint, _, int[] twinInvalidCategories) = Maps.BossLocations[bossEntityID + 1];
                    List<Boss> twinOptions = new List<Boss>(EnemyGenerator.BossList.Where(
                        twin => twin.Category != boss.Category && !twin.Category.In(twinInvalidCategories) && twin.AggressionLevel + boss.AggressionLevel <= 5 && twin.RequiredArenaSize <= bossPoint.ArenaSize));
                    twinBoss = twinOptions.GetRandomElement(Rand);

                    Enemy twinBossEnemy = EnemyGenerator.GetEnemy(twinBoss.Name);
                    bool twinIsRedPhantom = map.Name == "ChasmOfTheAbyss" || twinBoss.AlwaysRedPhantom;  // Red phantom bosses are otherwise fought in Abyss battles only.

                    var twinPart = twinBossEnemy.GetMSBPart($"Boss {i} Twin", bossEntityID + 1, twinBossPoint, twinBossPoint.Angle, Run.MapLevel, twinIsRedPhantom);
                    msb.Parts.Enemies.Add(twinPart);
                    logicGoalIDs.Add(Mod.GPARAM.AI[twinPart.ThinkParamID].LogicID);
                    battleGoalIDs.Add(Mod.GPARAM.AI[twinPart.ThinkParamID].BattleID);
                    Run.BossCategoriesUsed.Add(twinBoss.Category);
                    enemyModels.Add(twinBossEnemy.ModelID);

                    Run.EnableFlag(map.GetBossTwinFlag(i));
                }
                else
                {
                    Run.DisableFlag(map.GetBossTwinFlag(i));  // e.g. may have been set for New Londo Abyss boss previously
                }

                if (map.Name != "Lost Izalith")
                {
                    // Inject name and item lot reward into EMEVD constructor.
                    EMEVD.Instruction bossBattleCall = constructor.Instructions[emevdIndex];
                    List<byte> argData = bossBattleCall.ArgData.ToList();
                    int itemLotID = isRedPhantom ? bossEnemy.RedPhantomItemLotParamID : bossEnemy.ItemLotParamID;  // twin item lot ignored
                    argData[32] = (byte)itemLotID;
                    argData[33] = (byte)(itemLotID >> 0x08);
                    argData[34] = (byte)(itemLotID >> 0x10);
                    argData[35] = (byte)(itemLotID >> 0x18);
                    argData[52] = (byte)boss.NameTextID;
                    argData[53] = (byte)(boss.NameTextID >> 0x08);
                    if (twinBoss != null)
                    { 
                        argData[54] = (byte)twinBoss.NameTextID;
                        argData[55] = (byte)(twinBoss.NameTextID >> 0x08);
                    }                    
                    bossBattleCall.ArgData = argData.ToArray();
                }
            }

            if (Roll(InvaderOdds))
            {
                // INVADER
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                int invaderIndex = Run.InvadersAvailable.GetRandomElement(Rand);
                int invaderParamID = 7000 + 10 * invaderIndex;
                int invaderEntityID = map.BaseNPCEntityID + 50;
                GamePoint spawnPoint = pointManager.CheckOutRandomPoint("Invader", (int)ChrSize.Normal);
                GamePoint triggerPoint = pointManager.CheckOutRandomPointWithinDistance("Invader Trigger", spawnPoint, 20.0, 40.0);
                float angle = MapPointManager.GetFacingPoint(spawnPoint, triggerPoint);
                MSB1.Part.Enemy invader = GetInvaderPart(invaderEntityID, spawnPoint, angle, invaderParamID, Run.MapLevel);
                msb.Parts.Enemies.Add(invader);
                Run.InvadersAvailable.Remove(invaderIndex);
                Run.InvadersUsed.Add(invaderIndex);
                Run.EnableFlag(GameFlag.InvaderUsedBaseFlag + invaderIndex);

                MSB1.Region triggerRegion = new MSB1.Region()
                {
                    Name = "Invader Trigger",
                    Position = triggerPoint.Position - new Vector3(0.0f, 1.0f, 0.0f),  // 1.0 units below point
                    Shape = new MSB1.Shape.Box() { Width = 20.0f, Depth = 20.0f, Height = 10.0f },
                    EntityID = map.InvaderTriggerRegionID,
                };
                msb.Regions.Regions.Add(triggerRegion);

                MSB1.Region spawnRegion = new MSB1.Region()
                {
                    Name = "Invader Spawn",
                    Position = spawnPoint.Position,
                    Shape = new MSB1.Shape.Point(),
                    EntityID = map.InvaderSpawnPointID,
                };
                msb.Regions.Regions.Add(spawnRegion);
            }

            if (Roll(VeryRareEnemyOdds * (Run.GetFlag(GameFlag.MornsteinRingFlag) ? 2 : 1)))
            {
                // VERY RARE ENEMY
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                bool isRedPhantom = Roll(redPhantomOdds);
                int entityID = map.BaseEntityID + VeryRareEnemyOffset;
                Enemy enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, EnemyRarity.VeryRare, Run.MapLabels[map]);
                GamePoint point = pointManager.CheckOutRandomPoint("VeryRare Enemy", (int)enemy.Size);  // don't care about region label
                if (map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                    entityID += NewLondoVeryRareEnemyOffset;
                var part = enemy.GetMSBPart("VeryRare Enemy 1", entityID, point, GetRandomAngle(), Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(part);
                logicGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].BattleID);
                enemyModels.Add(enemy.ModelID);
            }

            if (!map.Name.In("PaintedWorld", "ChasmOfTheAbyss", "NewLondoRuins") && (Run.GetFlag(GameFlag.LoganRingFlag) || Roll(AbyssPortalOdds)))
            {
                // ABYSS PORTAL

                GamePoint point = pointManager.CheckOutRandomPoint("Abyss Portal", 0);
                MSB1.Part.Player portalWarpBack = new MSB1.Part.Player()
                {
                    Name = "Portal Return",
                    Position = point.Position,
                    Rotation = new Vector3(0.0f, GetRandomAngle(), 0.0f),
                    EntityID = map.PortalWarpPointID,
                    IsShadowSrc = 1,
                    IsShadowDest = 1,
                    ModelName = "c0000",
                };
                msb.Parts.Players.Add(portalWarpBack);
                MSB1.Region portalPoint = new MSB1.Region()
                {
                    Name = "Portal VFX Point",
                    Position = point.Position + new Vector3(0.0f, 2.0f, 0.0f),
                    Shape = new MSB1.Shape.Point(),
                    EntityID = -1,
                };
                msb.Regions.Regions.Add(portalPoint);
                MSB1.Event.SFX portalVFX = new MSB1.Event.SFX()
                {
                    Name = "Portal VFX",
                    FFXID = 120027,
                    RegionName = "Portal VFX Point",
                    PartName = point.CollisionName,
                    EntityID = map.PortalFXID,
                };
                msb.Events.SFXs.Add(portalVFX);
                MSB1.Part.Enemy portalTrigger = new MSB1.Part.Enemy()
                {
                    ModelName = "c1000",
                    Name = "Portal Trigger",
                    Position = point.Position + new Vector3(0.0f, 0.5f, 0.0f),
                    EntityID = map.PortalTriggerCharacterID,
                    NPCParamID = 100000,
                    TalkID = 0,
                    CollisionName = point.CollisionName,
                    ThinkParamID = 1,
                };
                msb.Parts.Enemies.Add(portalTrigger);
            }

            if (!Run.MapsVisited.Contains(Maps.GetMap("PaintedWorld")) && Roll(PaintingOdds))
            {
                // Painting appears, in a random choice of its possible positions (pre-existing in base MSB).
                // TODO: 3-4 positions per map. Wherever it fits. Proper collision assignment, etc. Also prompt regions for simplicity.
            }

            foreach (Merchant merchant in CharacterGenerator.MerchantList)
            {
                // MERCHANTS
                if (Run.GetFlag(merchant.DeadFlag))
                    continue;  // Merchant is dead and cannot appear again.
                
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                double merchantOdds = merchant.Name == "Marvelous Chester" ? ChesterOdds : MerchantOdds;
                if (Roll(merchantOdds))
                {
                    if (map.Name == "NewLondoRuins")
                        regionLabel = "Upper";  // no merchants in lower
                    GamePoint point = pointManager.CheckOutRandomPointCustomNearbyRadius("Merchant", 2.0, 5, regionLabel);
                    var part = merchant.GetPart(point, pointManager.GetAngleFacingNearestPoint(point), map.TalkIDBase);
                    msb.Parts.Enemies.Add(part);
                    logicGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].LogicID);
                    battleGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].BattleID);
                }
            }

            int chestCount = Math.Max(0, Rand.Next(map.ChestCount - 2, map.ChestCount));
            List<int> usedChestTreasure = new List<int>();
            for (int i = 0; i < chestCount; i++)
            {
                // CHESTS
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                int chestID = map.BaseChestEntityID + i;
                GamePoint point = pointManager.CheckOutRandomPointCustomNearbyRadius("Chest", 2.0, 5, regionLabel);
                float angle = pointManager.GetAngleFacingNearestPoint(point);
                var part = GetChestPart(i, chestID, angle, point);
                msb.Parts.Objects.Add(part);

                var objAct = new MSB1.Event.ObjAct()
                {
                    Name = $"Chest ObjAct {i}",
                    ObjActEntityID = map.BaseChestObjActFlagID + i,
                    ObjActPartName = $"Chest {i}",
                    EventFlagID = 0,
                };
                msb.Events.ObjActs.Add(objAct);

                var treasure = new MSB1.Event.Treasure()
                {
                    Name = $"Chest Treasure {i}",
                    TreasurePartName = $"Chest {i}",
                    PartName = point.CollisionName,
                    InChest = true,
                    StartDisabled = true,  // can't get the treasure to disable itself based on 'InChest' alone...
                };
                // Choose random treasure in unlocked range.
                treasure.ItemLots[0] = GetChestTreasureID(map.BaseChestItemLotID, usedChestTreasure);
                usedChestTreasure.Add(treasure.ItemLots[0]);
                msb.Events.Treasures.Add(treasure);
            }

            if (Roll(MimicOdds))
            {
                // MIMIC
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                bool isRedPhantom = Roll(redPhantomOdds);
                int mimicEntityID = map.BaseEntityID + MimicOffset;
                if (map.Name == "NewLondoRuins")
                    regionLabel = "Upper";  // no Mimics in lower
                Enemy mimic = EnemyGenerator.GetEnemy("Mimic");
                GamePoint point = pointManager.CheckOutRandomPoint("Mimic", (int)mimic.Size, regionLabel);
                float angle = pointManager.GetAngleFacingNearestPoint(point);
                var part = mimic.GetMSBPart("Mimic", mimicEntityID, point, angle, Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(part);
                logicGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].BattleID);
                enemyModels.Add(mimic.ModelID);

                MSB1.Region mimicNest = new MSB1.Region()
                {
                    Name = "Mimic Nest",
                    Position = new Vector3(point.Position.X, point.Position.Y - 0.1f, point.Position.Z),
                    Rotation = new Vector3(0.0f, angle, 0.0f),
                    Shape = new MSB1.Shape.Box() { Width = 5.0f, Depth = 5.0f, Height = 2.0f },
                    EntityID = mimicEntityID + 5,
                };
                msb.Regions.Regions.Add(mimicNest);
            }

            int itemCount = Math.Max(0, Rand.Next(map.ItemCorpseCount - 5, map.ItemCorpseCount));
            List<int> usedCorpseTreasure = new List<int>();
            for (int i = 0; i < itemCount; i++)
            {
                // ITEM CORPSES
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                GamePoint point = pointManager.CheckOutRandomPointWeightedInverseNearby($"Item Corpse {i}", 0, regionLabel);
                int pose = Objects.CorpsePoses.GetRandomElement(Rand);
                float poseOffset = Objects.CorpsePoseYOffsets[pose];

                MSB1.Part.Object corpse = new MSB1.Part.Object()
                {
                    ModelName = "o0500",  // Not using o0502 or o0504, as they have different pose enums.
                    Name = $"Item Corpse {i}",
                    CollisionName = point.CollisionName,
                    Position = new Vector3(point.Position.X, point.Position.Y + poseOffset, point.Position.Z),
                    Rotation = new Vector3(0.0f, GetRandomAngle(), 0.0f),
                    EntityID = -1,  // not needed
                    ObjectPose = (short)pose,
                };
                corpse.ClearDrawGroups();
                corpse.ClearDispGroups();
                msb.Parts.Objects.Add(corpse);

                MSB1.Event.Treasure treasure = new MSB1.Event.Treasure()
                {
                    Name = $"Item Corpse Treasure {i}",
                    TreasurePartName = $"Item Corpse {i}",
                    PartName = point.CollisionName,
                    InChest = false,
                };
                // Assign random corpse treasure from unlocked ranges.
                treasure.ItemLots[0] = GetCorpseTreasureID(map.BaseCorpseItemLotID, usedCorpseTreasure);
                usedCorpseTreasure.Add(treasure.ItemLots[0]);
                msb.Events.Treasures.Add(treasure);
            }

            int rareCount = Math.Max(0, Rand.Next(map.RareEnemyCount - 3, map.RareEnemyCount));
            List<Enemy> usedRareEnemies = new List<Enemy>();
            for (int i = 0; i < rareCount; i++)
            {
                // RARE ENEMIES
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else if (map.Name == "NewLondoRuins" && i == 0)
                    regionLabel = "Upper";  // first rare enemy is always in Upper New Londo Ruins (for Holy Sigil drop)
                else
                    regionLabel = "";

                Enemy enemy;
                if (usedRareEnemies.Count > MaxRareEnemyTypeCount)
                    enemy = usedRareEnemies.GetRandomElement(Rand);
                else
                {
                    enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, EnemyRarity.Rare, Run.MapLabels[map]);
                    usedRareEnemies.Add(enemy);
                }

                bool isRedPhantom = rarePhantomCount < 15 && Roll(redPhantomOdds);

                GamePoint point = pointManager.CheckOutRandomPoint("Rare Enemy", (int)enemy.Size, regionLabel);

                int entityID = map.BaseEntityID + RareEnemyOffset + i;
                if (map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                    entityID += NewLondoLowerRareEnemyOffset;
                
                MSB1.Part.Enemy enemyPart = enemy.GetMSBPart($"Rare Enemy {i}", entityID, point, GetRandomAngle(), Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(enemyPart);
                logicGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].BattleID);
                enemyModels.Add(enemy.ModelID);

                if (isRedPhantom)
                    rarePhantomCount++;
            }

            int basicEnemyCount = Math.Max(0, Rand.Next(map.BasicEnemyCount - 5, map.BasicEnemyCount));
            int basicNonPhantomCount = 0;
            List<Enemy> usedCommonEnemyTypes = new List<Enemy>();
            List<Enemy> usedUncommonEnemyTypes = new List<Enemy>();
            for (int i = 0; i < basicEnemyCount; i++)
            {
                // BASIC (COMMON/UNCOMMON) ENEMIES
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                Enemy enemy;
                EnemyRarity rarity = Roll(UncommonEnemyOdds) ? EnemyRarity.Uncommon : EnemyRarity.Common;
                if (rarity == EnemyRarity.Common)
                {
                    if (usedCommonEnemyTypes.Count > MaxCommonEnemyTypeCount)
                        enemy = usedCommonEnemyTypes.GetRandomElement(Rand);
                    else
                    {
                        enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, rarity, Run.MapLabels[map]);
                        usedCommonEnemyTypes.Add(enemy);
                    }
                }
                else
                {
                    if (usedUncommonEnemyTypes.Count > MaxUncommonEnemyTypeCount)
                        enemy = usedUncommonEnemyTypes.GetRandomElement(Rand);
                    else
                    {
                        enemy = EnemyGenerator.GetRandomEnemyWithRarity(Rand, rarity, Run.MapLabels[map]);
                        usedUncommonEnemyTypes.Add(enemy);
                    }
                }

                bool isRedPhantom = basicPhantomCount < 15 && Roll(redPhantomOdds);
                
                int entityID = map.BaseEntityID + (isRedPhantom ? BasicPhantomOffset + basicPhantomCount : BasicEnemyOffset + basicNonPhantomCount);
                GamePoint point = pointManager.CheckOutRandomPoint("Basic Enemy", (int)enemy.Size, regionLabel);
                if (map.Name == "NewLondoRuins" && point.RegionLabel == "Lower")
                    entityID += isRedPhantom ? NewLondoLowerBasicPhantomOffset : NewLondoLowerBasicEnemyOffset;
                MSB1.Part.Enemy enemyPart = enemy.GetMSBPart($"Basic Enemy {i}", entityID, point, GetRandomAngle(), Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(enemyPart);
                logicGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[enemyPart.ThinkParamID].BattleID);
                enemyModels.Add(enemy.ModelID);

                if (isRedPhantom)
                    basicPhantomCount++;
                else
                    basicNonPhantomCount++;
            }

            int vagrantCount = Rand.Next(3);
            for (int i = 0; i < vagrantCount; i++)
            {
                // VAGRANTS (max of 2)
                if (map.Name == "Blighttown")
                    regionLabel = Roll(BlighttownSwampOdds) ? "Swamp" : "Shanty";
                else
                    regionLabel = "";

                if (map.Name == "NewLondoRuins")
                    regionLabel = "Upper";  // No Vagrants in Lower New Londo
                bool isRedPhantom = Run.GetFlag(GameFlag.MornsteinRingFlag) ? Roll(0.2) : Roll(0.1);
                int entityID = map.BaseEntityID + VagrantOffset + i;
                Enemy enemy = EnemyGenerator.GetEnemy(Roll(0.5) ? "Good Vagrant" : "Evil Vagrant");
                GamePoint point = pointManager.CheckOutRandomPoint("Vagrant", (int)enemy.Size, regionLabel);
                var part = enemy.GetMSBPart($"Vagrant {i}", entityID, point, GetRandomAngle(), Run.MapLevel, isRedPhantom);
                msb.Parts.Enemies.Add(part);
                logicGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[part.ThinkParamID].BattleID);
                enemyModels.Add(enemy.ModelID);
            }

#if DEBUG
            Console.WriteLine($"    Updating models...");
#endif
            UpdateMSBModels(msb);

            // Output MSB. Also output a '.rls' copy, so it can be reloaded and modified at bonfire creation.
#if DEBUG
            Console.WriteLine($"    Writing MSB...");
#endif
            msb.Write(Mod.GameDir + $@"map\MapStudio\{map.MsbName}.msb");
            msb.Write(Mod.GameDir + $@"map\MapStudio\{map.MsbName}.msb.rls");  // file to modify for bonfire creation
#if DEBUG
            Console.WriteLine($"    Writing EMEVD...");
#endif
            emevd.Write(Mod.GameDir + $@"event\{map.EmevdName}.emevd.dcx");

#if DEBUG
            Console.WriteLine($"    Writing LUABND...");
#endif
            WriteMapLUABND(map.EmevdName, battleGoalIDs, logicGoalIDs);

#if DEBUG
            Console.WriteLine($"    Writing FFXBND...");
#endif
            WriteMapFFXBND(map.MapID[0], enemyModels);
        }

        void UpdateMSBModels(MSB1 msb)
        {
            // Add Painting object model to map, if necessary.
            if (!msb.Models.Objects.Select(model => model.Name).Contains("o5850"))
                msb.Models.Objects.Add(ModelTemplates.PaintingModel);
            if (!msb.Models.Objects.Select(model => model.Name).Contains("o0500"))
                msb.Models.Objects.Add(ModelTemplates.CorpseModel);
            if (!msb.Models.Objects.Select(model => model.Name).Contains("o0110"))
                msb.Models.Objects.Add(ModelTemplates.ChestModel);
            // Clear enemy and Player models, then repopulate enemy models from all present enemies.
            msb.Models.Enemies.Clear();
            msb.Models.Players.Clear();  // c0000 added to Enemy models instead
            msb.Models.Enemies.Add(ModelTemplates.PlayerModel);  // c0000
            msb.Models.Enemies.Add(ModelTemplates.EmptyModel);  // c1000
            foreach (MSB1.Part.Enemy enemy in msb.Parts.Enemies)
            {
                if (!msb.Models.Enemies.Select(model => model.Name).Contains(enemy.ModelName))
                    msb.Models.Enemies.Add(GetEnemyModel(enemy.ModelName));
            }
            foreach (MSB1.Part.DummyEnemy enemy in msb.Parts.DummyEnemies)
            {
                if (!msb.Models.Enemies.Select(model => model.Name).Contains(enemy.ModelName))
                    msb.Models.Enemies.Add(GetEnemyModel(enemy.ModelName));
            }
        }

        public void GenerateAbyssBattleMSB(int mapLevel, List<int> bossCategoriesUsed)
        {
            // Basically, create thin New Londo MSB containing boss, then enable "done" flag.
            // EMEVD handles the rest.

            Map newLondo = Maps.GetMap("NewLondoRuins");
            MSB1 msb = MSB1.Read(ModMSBPath + $"{newLondo.MsbName}.msb");
            EMEVD emevd = EMEVD.Read(ModEMEVDPath + $"{newLondo.EmevdName}.emevd.dcx");
            EMEVD.Event constructor = emevd.Events.Where(evt => evt.ID == 0).First();
            HashSet<int> enemyModels = new HashSet<int>();
            HashSet<int> logicGoalIDs = new HashSet<int>();
            HashSet<int> battleGoalIDs = new HashSet<int>();
            MapPointManager pointManager = new MapPointManager(newLondo.Name, Rand);

            // ABYSS BOSS
            int bossEntityID = newLondo.GetBossID(0);
            if (!Maps.BossLocations.Keys.Contains(bossEntityID))
                throw new Exception($"Could not find information about location for (non-twin) boss ID {bossEntityID}.");
            (GamePoint bossPoint, int emevdIndex, int[] invalidCategories) = Maps.BossLocations[bossEntityID];
            bossCategoriesUsed.AddRange(invalidCategories);
            Boss boss = EnemyGenerator.GetRandomBoss(Rand, bossPoint.ArenaSize, bossCategoriesUsed);
            Enemy bossEnemy = EnemyGenerator.GetEnemy(boss.Name);
            MSB1.Part.Enemy bossPart = bossEnemy.GetMSBPart("Abyss Boss", bossEntityID, bossPoint, bossPoint.Angle, mapLevel, isRedPhantom: true);
            msb.Parts.Enemies.Add(bossPart);
            enemyModels.Add(bossEnemy.ModelID);
            logicGoalIDs.Add(Mod.GPARAM.AI[bossPart.ThinkParamID].LogicID);
            battleGoalIDs.Add(Mod.GPARAM.AI[bossPart.ThinkParamID].BattleID);

            // TWIN BOSSES:
            // If arena is Large or Giant, there's a chance of a twin boss (capping their combined aggression).
            // Mornstein ring makes it 100% chance.
            Boss twinBoss = null;
            if ((Roll(TwinBossOdds) || Run.GetFlag(GameFlag.MornsteinRingFlag)) && Maps.BossLocations.ContainsKey(bossEntityID + 1) && bossPoint.ArenaSize.In(ArenaSize.Large, ArenaSize.Giant) && boss.AggressionLevel < 5)
            {
                (GamePoint twinBossPoint, _, int[] twinInvalidCategories) = Maps.BossLocations[bossEntityID + 1];
                List<Boss> twinOptions = new List<Boss>(EnemyGenerator.BossList.Where(
                    twin => twin.Category != boss.Category && !twin.Category.In(twinInvalidCategories) && twin.AggressionLevel + boss.AggressionLevel <= 5 && twin.RequiredArenaSize <= bossPoint.ArenaSize));
                twinBoss = twinOptions.GetRandomElement(Rand);

                Enemy twinBossEnemy = EnemyGenerator.GetEnemy(twinBoss.Name);

                var twinPart = twinBossEnemy.GetMSBPart($"Abyss Boss Twin", bossEntityID + 1, twinBossPoint, twinBossPoint.Angle, mapLevel, isRedPhantom: true);
                msb.Parts.Enemies.Add(twinPart);
                logicGoalIDs.Add(Mod.GPARAM.AI[twinPart.ThinkParamID].LogicID);
                battleGoalIDs.Add(Mod.GPARAM.AI[twinPart.ThinkParamID].BattleID);
                Run.BossCategoriesUsed.Add(twinBoss.Category);
                enemyModels.Add(twinBossEnemy.ModelID);

                Run.EnableFlag(newLondo.GetBossTwinFlag(0));
            }
            else
            {
                Run.DisableFlag(newLondo.GetBossTwinFlag(0));
            }

            // Inject name and item lot reward into EMEVD constructor.
            EMEVD.Instruction bossBattleCall = constructor.Instructions[emevdIndex];
            List<byte> argData = bossBattleCall.ArgData.ToList();
            int itemLotID = bossEnemy.RedPhantomItemLotParamID;
            argData[32] = (byte)itemLotID;
            argData[33] = (byte)(itemLotID >> 0x08);
            argData[34] = (byte)(itemLotID >> 0x10);
            argData[35] = (byte)(itemLotID >> 0x18);
            argData[52] = (byte)boss.NameTextID;
            argData[53] = (byte)(boss.NameTextID >> 0x08);
            if (twinBoss != null)
            {
                argData[54] = (byte)twinBoss.NameTextID;
                argData[55] = (byte)(twinBoss.NameTextID >> 0x08);
            }
            bossBattleCall.ArgData = argData.ToArray();

#if DEBUG
            Console.WriteLine($"    Updating models...");
#endif
            UpdateMSBModels(msb);

#if DEBUG
            Console.WriteLine($"    Writing MSB...");
#endif
            msb.Write(Mod.GameDir + $@"map\MapStudio\{newLondo.MsbName}.msb");  // No '.rls' copy needed.
#if DEBUG
            Console.WriteLine($"    Writing EMEVD...");
#endif
            emevd.Write(Mod.GameDir + $@"event\{newLondo.EmevdName}.emevd.dcx");

#if DEBUG
            Console.WriteLine($"    Writing LUABND...");
#endif
            WriteMapLUABND(newLondo.EmevdName, battleGoalIDs, logicGoalIDs);

#if DEBUG
            Console.WriteLine($"    Writing FFXBND...");
#endif
            WriteMapFFXBND(newLondo.MapID[0], enemyModels);
        }

        public int CreateBonfire(Map map, float x, float y, float z, float angle)
        {
            MapPointManager pointManager = new MapPointManager(map.Name, Rand);
            GamePoint bonfirePoint = pointManager.GetClosestPoint(x, y, z, 3.0);
            if (bonfirePoint == null)
                return -1;
            GamePoint spawnPoint = pointManager.GetClosestPoint(bonfirePoint.Position, 3.0, excludeEqual: true);
            if (spawnPoint == null)
                return -1;

            MSB1 msb = MSB1.Read(Mod.GameDir + $@"map\MapStudio\{map.MsbName}.msb.rls");

            MSB1.Part.Object bonfire = new MSB1.Part.Object()
            {
                ModelName = "o0200",
                EntityID = map.BonfireCharacterID + 1000,
                Name = "Bonfire Obj",
                Position = bonfirePoint.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),
                CollisionName = bonfirePoint.CollisionName,
                IsShadowDest = 1,
                DrawByReflectCam = 1,
            };
            msb.Parts.Objects.Add(bonfire);

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
            msb.Parts.Enemies.Add(bonfireChr);

            MSB1.Region bonfireSpawnPoint = new MSB1.Region()
            {
                Name = "Bonfire Spawn Point",
                Shape = new MSB1.Shape.Point(),
                Position = spawnPoint.Position,
                EntityID = -1,
                Rotation = new Vector3(0.0f, angle, 0.0f),
            };
            msb.Regions.Regions.Add(bonfireSpawnPoint);

            MSB1.Event.SpawnPoint bonfireSpawn = new MSB1.Event.SpawnPoint()
            {
                Name = "Bonfire Spawn",
                EntityID = map.BonfireCharacterID + 2000,
                PartName = spawnPoint.CollisionName,
                SpawnPointName = "Bonfire Spawn Point",
            };
            msb.Events.SpawnPoints.Add(bonfireSpawn);

            UpdateMSBModels(msb);

            msb.Write(Mod.GameDir + $@"map\MapStudio\{map.MsbName}.msb");
            // Keep the original '.rls' backup for second bonfire creation with Solaire's Ring.
            return bonfireSpawn.EntityID;
        }

        MSB1.Part.Object GetChestPart(int index, int entityID, float angle, GamePoint point)
        {
            var part = new MSB1.Part.Object()
            {
                Name = $"Chest {index}",
                Position = point.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),
                CollisionName = point.CollisionName,
                EntityID = entityID,
                ModelName = "o0110",
                IsShadowSrc = 1,
                IsShadowDest = 1,
                DrawByReflectCam = 1,  // Enabled in vanilla Archives; likely can't hurt.
                // TODO: Default draw params?
            };
            part.ClearDrawGroups();
            part.ClearDispGroups();
            return part;
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
            HashSet<int> addedIDs = new HashSet<int>();
            string ffxBNDName = $"FRPG_SfxBnd_m{mapBlockID:00}";
            BND3 ffxBND = BND3.Read(GetGameDataResource(ffxBNDName + "_ffxbnd"));
            int bndIndex = ffxBND.Files.Where(file => file.ID < 100000).Max(file => file.ID) + 1;
            Dictionary<string, BND3> openBNDs = new Dictionary<string, BND3>();
            foreach (int enemyModel in enemyModels)
            {
                foreach (var indexPath in EnemyGenerator.EnemyFFXSources[enemyModel])
                {
                    if (addedIDs.Contains(indexPath.Key))
                        continue;  // already added by another enemy
                    if (!indexPath.Value.Contains($"m{mapBlockID:00}"))  // if enemy FFX is not already present in current block (or sub) FFXBND file...
                    {
                        string ffxFileName = $"f{indexPath.Key:0000000}.ffx";
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

        void WriteMapLUABND(string luabndName, HashSet<int> battleGoalIDs, HashSet<int> logicGoalIDs = null)
        {
            // Reads from a folder full of unpacked binary AI Lua scripts and generates a LUABND for the given map ID name.
            // Note that in DSR, LUAINFO files are not needed (and LUAGNL was never needed).
            if (!battleGoalIDs.Any())
                throw new Exception("Empty list of battle goal IDs passed to Lua packer, which is not ever expected.");

            BND3 mapLuaBND = new BND3
            {
                Timestamp = "07D7R6"
            };
            mapLuaBND.Compression = DCX.Type.DarkSouls1;

            int bndID = 1055;  // first "safe" ID for loading order, according to vanilla use
            if (logicGoalIDs != null)
                foreach (int goalID in logicGoalIDs)
                {
                    string scriptPath = $"_{goalID:000000}_logic";
                    string bndPath = $@"N:\FRPG\data\INTERROOT_x64\script\ai\out\bin\{goalID:000000}_logic.lua";
                    BinderFile bndEntry = new BinderFile(Binder.FileFlags.x40, bndID, bndPath, GetGameDataResource(scriptPath));
                    mapLuaBND.Files.Add(bndEntry);
                    bndID++;
                }
            foreach (int goalID in battleGoalIDs)
            {
                string scriptPath = $"_{goalID:000000}_battle";
                string bndPath = $@"N:\FRPG\data\INTERROOT_x64\script\ai\out\bin\{goalID:000000}_battle.lua";
                BinderFile bndEntry = new BinderFile(Binder.FileFlags.x40, bndID, bndPath, GetGameDataResource(scriptPath));
                mapLuaBND.Files.Add(bndEntry);
                bndID++;
            }
            mapLuaBND.Write(Mod.GameDir + $@"script\{luabndName}.luabnd.dcx");
        }

        MSB1.Part.Enemy GetInvaderPart(int entityID, GamePoint point, float angle, int paramID, int level)
        {
            return new MSB1.Part.Enemy()
            {
                Name = $"Invader {paramID}",
                ThinkParamID = paramID,
                NPCParamID = paramID + (level - 1),
                TalkID = -1,
                CharaInitID = paramID,
                CollisionName = point.CollisionName,
                EntityID = entityID,
                Position = point.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),  // in degrees
                ModelName = "c0000",
            };
        }

        MSB1.Model GetEnemyModel(string modelName)
        {
            return new MSB1.Model() { Name = modelName, Placeholder = $@"N:\FRPG\data\Model\chr\{modelName}\sib\{modelName}.sib" };
        }

        float GetRandomAngle()
        {
            return (float)Rand.NextDouble() * 360.0f - 180.0f;
        }

        bool Roll(double odds)
        {
            return Rand.NextDouble() < odds;
        }

        byte[] GetGameDataResource(string resourceName)
        {
            return (byte[])Resources.GameData.ResourceManager.GetObject(resourceName);
        }
    }
}
