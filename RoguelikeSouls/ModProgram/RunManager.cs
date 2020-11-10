using GameHook;
using RoguelikeSouls.Installation;
using RoguelikeSouls.Extensions;
using SoulsFormatsMod;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Microsoft.Win32.SafeHandles;

namespace RoguelikeSouls.ModProgram
{
    class RunManager
    {
        SoulsMod Mod { get; }
        Random Rand { get; }
        DSRHook Hook { get; }
        bool InitialRestartDone { get; set; } = false;

        public static string DEBUG_MAP { get; } = "";        

        // Current map instance. This is NOT updated when you go to the Painted World or an Abyss battle.
        MapInfo CurrentMap { get; set; }

        // Maps are sampled and removed from this list as they are used in the run.
        // Excludes Painted World, Kiln, and Abyss, which are special cases for access.
        public List<MapInfo> MapsAvailable { get; } = new List<MapInfo>();

        // Maps visited, which is particularly useful for recording when Painted World has been visited.
        public List<MapInfo> MapsVisited { get; } = new List<MapInfo>();

        // List of boss categories used in the current run, which will prevent the same
        // category appearing again.
        public List<int> BossCategoriesUsed { get; } = new List<int>();
        
        // Same, but for Abyss battles.
        public List<int> AbyssBossCategoriesUsed { get; } = new List<int>();

        // List of invaders that are still available for appearance.
        public List<int> InvadersAvailable { get; } = new List<int>(Enumerable.Range(0, 30));

        // List of invaders that have been used.
        public List<int> InvadersUsed { get; } = new List<int>();

        // Current map difficulty level in current run. Ranges from 1 to 10.
        public int MapLevel
        {
            get
            {
                int maxLevel = 0;
                for (int level = 1; level <= 10; level++)
                {
                    if (GetFlag(GameFlag.MapLevelBaseFlag + level))
                        maxLevel = level;
                }
                return maxLevel;
            }
            set
            {
                if (value < 1 || value > 10)
                    throw new Exception($"Cannot set map level to {value}. Must range from 1 to 10.");
                for (int level = 1; level <= 10; level++)
                    DisableFlag(GameFlag.MapLevelBaseFlag + level);
                EnableFlag(GameFlag.MapLevelBaseFlag + value);
            }
        }

        // Dictionary of all map labels for current run (generated when run starts).
        public Dictionary<MapInfo, List<Label>> MapLabels { get; } = new Dictionary<MapInfo, List<Label>>();

        public RunManager(SoulsMod mod, DSRHook hook, string inputSeed = "")
        {
#if !DEBUG
            if (DEBUG_MAP != "")
                throw new ApplicationException("Debug map must be empty for release version!");
#endif
            Mod = mod;
            Rand = inputSeed == "" ? new Random() : new Random(inputSeed.GetHashCode());
            Hook = hook;
            
            if (GetFlag(GameFlag.RunStartedFlag))
            {
                Console.WriteLine("Loading existing journey...");
                LoadExistingRun();
                Console.WriteLine("Journey loaded.");
            }
        }

        public void RunMainLoop(bool immediateRestart = false)
        {
            Console.WriteLine("~~~ MAIN LOOP START ~~~");
            while (true)
            {
                // EMEVD keeps enabling this and gives mod program a few seconds to disable it before complaining.
                if (GetFlag(GameFlag.HookCheckFlag))
                    DisableFlag(GameFlag.HookCheckFlag);

                if (immediateRestart && !InitialRestartDone)
                {
                    // Trigger EMEVD run abort (even if not in a run).
                    EnableFlag(GameFlag.DoRunCleanupFlag);
                    InitialRestartDone = true;
                }

                if (GetFlag(GameFlag.StatResetRequest))
                {
#if DEBUG
                    Console.WriteLine($"Stat reset requested.");
#endif
                    DisableFlag(GameFlag.StatResetRequest);
                    ResetPlayerLevel();
                }

                if (GetFlag(GameFlag.AttunementClearRequest))
                {
#if DEBUG
                    Console.WriteLine($"Attunement clear requested.");
#endif
                    DisableFlag(GameFlag.AttunementClearRequest);
                    ClearAttunementSlots();
                }

                if (GetFlag(GameFlag.RunStartedFlag))
                {
                    if (CurrentMap == null)
                    {
                        Console.WriteLine("ERROR: Journey has begun, but your whereabouts in Lordran are unknown!");
                        Thread.Sleep(1000);
                        continue;
                    }
                    // Wait for a map endpoint to be triggered.
                    foreach (Connection connection in CurrentMap.Connections)
                    {
                        if (GetFlag(connection.EndTriggerFlag))
                        {
#if DEBUG
                            Console.WriteLine($"Activating map based on end trigger flag {connection.EndTriggerFlag}");
#endif
                            MapInfo newMap = ActivateMap(connection.EndTriggerFlag);
                            Console.WriteLine($"Travelling to new region: {newMap.Name} (level {MapLevel})");
                        }
                    }

                    if (GetFlag(GameFlag.InvisibleEffect))
                    {
                        // TODO. Doesn't work.
                    }

                    if (GetFlag(GameFlag.StatBoostRequest))
                    {
#if DEBUG
                        Console.WriteLine($"Stat boost requested.");
#endif
                        DisableFlag(GameFlag.StatBoostRequest);
                        CheckStatBoost();
                    }

                    if (GetFlag(GameFlag.SpellRechargeRequest))
                    {
#if DEBUG
                        Console.WriteLine($"Spell recharge requested.");
#endif
                        DisableFlag(GameFlag.SpellRechargeRequest);
                        RechargeSpells();
                    }

                    if (GetFlag(GameFlag.AbyssBattleRequest))
                    {
#if DEBUG
                        Console.WriteLine($"Abyssal visit requested...");
#endif
                        DisableFlag(GameFlag.AbyssBattleRequest);
                        RequestAbyssFight();
                    }

                    if (GetFlag(GameFlag.BonfireCreationRequest))
                    {
#if DEBUG
                        Console.WriteLine($"Bonfire creation requested.");
#endif
                        DisableFlag(GameFlag.BonfireCreationRequest);
                        RequestBonfireCreation();
                    }
                }
                else
                {
                    // Wait for run to be started by request flag from common EMEVD (when Firelink bonfire activated).
                    if (GetFlag(GameFlag.DoRunSetupFlag))
                    {
                        Console.WriteLine($"Preparing new journey...");
                        PrepareNewRun();
                        ActivateFirstMap();  // Generates MSB and requests warp in common EMEVD.
                        DisableFlag(GameFlag.DoRunSetupFlag);
                        EnableFlag(GameFlag.RunStartedFlag);
                        EnableFlag(GameFlag.RunSetupCompleteFlag);
                    }
                }
                
                Thread.Sleep(10);  // less than one frame (at 60 Hz)
            }
        }

        void LoadExistingRun()
        {
            // Load data from game flags about a run that is already underway.
            ResetRunData();
            List<Label> allLabels = new List<Label>(Enum.GetValues(typeof(Label)).Cast<Label>());
            {
                foreach (MapInfo map in Maps.MapList)
                {
                    if (GetFlag(map.IsVisitedFlag))
                    {
                        MapsAvailable.Remove(map);
                        MapsVisited.Add(map);
                    }
                    MapLabels[map] = new List<Label>(allLabels.Where(label => GetFlag(map.HasLabelFlagBase + (int)label)));
                    if (GetFlag(map.InMapFlag))
                        CurrentMap = map;
                }
                int maxBossCategory = EnemyGenerator.LastBossCategory;
                for (int category = 0; category <= maxBossCategory; category++)
                {
                    if (GetFlag(GameFlag.BossCategoryUsedBaseFlag + category))
                        BossCategoriesUsed.Add(category);
                    if (GetFlag(GameFlag.AbyssBossCategoryUsedBaseFlag + category))
                        AbyssBossCategoriesUsed.Add(category);
                }
            }

            foreach (int invader in InvadersAvailable.ToArray())
            {
                if (GetFlag(GameFlag.InvaderUsedBaseFlag + invader))
                {
                    InvadersAvailable.Remove(invader);
                    InvadersUsed.Add(invader);
                }
            }
        }

        void PrepareNewRun()
        {
            ResetRunData();
            ChooseMapLabels();
            DisableRandomShopFlags();
            ResetPlayerLevel();  // Just in case it wasn't done on last cleanup. (Spells are not un-attuned again, though.)
        }

        void ResetRunData()
        {
            InvadersAvailable.Clear();
            InvadersAvailable.AddRange(Enumerable.Range(0, 30));
            InvadersUsed.Clear();
            BossCategoriesUsed.Clear();
            AbyssBossCategoriesUsed.Clear();
            MapsAvailable.Clear();
            MapsAvailable.AddRange(Maps.MapList.Where(map => -2 <= map.Rating && map.Rating <= 2));
            MapsVisited.Clear();
            MapLabels.Clear();
        }

        void ChooseMapLabels()
        {
            // Labels chosen for each map independently.
            Dictionary<Label, int> weightedLabels = GetWeightedLabels();
            foreach (MapInfo map in Maps.MapList)
            {
                List<Label> mapLabels = new List<Label>();
                if (GetFlag(GameFlag.LobosJrRingFlag))
                {
                    // Choose a (large) number of random labels for high enemy variety.
                    while (mapLabels.Count < Settings.LobosJrLabelCount)
                    {
                        Dictionary<Label, int> weightedOptions = weightedLabels.Where(
                            kv => !mapLabels.Contains(kv.Key)).ToDictionary(item => item.Key, item => item.Value);
                        Label chosenLabel = weightedOptions.GetWeightedRandomElement(Rand);
                        mapLabels.Add(chosenLabel);
                    }
                }
                else
                {
                    // Labels will keep being added until the size of the common/uncommon enemy pool
                    // is above a minimum enemy count drawn from a certain range. If only one
                    // label ends up being chosen, there's a 50% chance of adding a second.
                    int basicEnemyTypeCount = 0;
                    int desiredBasicEnemyTypeCount = Rand.Next(Settings.MinBasicEnemyTypeCount, Settings.MaxBasicEnemyTypeCount + 1);
                    while (basicEnemyTypeCount < desiredBasicEnemyTypeCount)
                    {
                        Dictionary<Label, int> weightedOptions = weightedLabels.Where(
                            kv => !mapLabels.Contains(kv.Key)).ToDictionary(item => item.Key, item => item.Value);
                        Label chosenLabel = weightedOptions.GetWeightedRandomElement(Rand);
                        mapLabels.Add(chosenLabel);
                        basicEnemyTypeCount += EnemyGenerator.EnemyList.Where(enemy =>
                            enemy.Labels.Contains(chosenLabel)
                            && enemy.Rarity.In(EnemyRarity.Common, EnemyRarity.Uncommon)
                        ).Count();
                    }
                    if (mapLabels.Count == 1 && Rand.Roll(0.5))
                    {
                        Dictionary<Label, int> weightedOptions = weightedLabels.Where(
                            kv => !mapLabels.Contains(kv.Key)).ToDictionary(item => item.Key, item => item.Value);
                        Label chosenLabel = weightedOptions.GetWeightedRandomElement(Rand);
                        mapLabels.Add(chosenLabel);
                    }
                }
                
                MapLabels[map] = mapLabels;
#if DEBUG
                Console.WriteLine($"{map.Name} labels:\n  {string.Join(", ", mapLabels)}");
#endif

                // EMEVD cleanup function disables all these record-keeping flag ranges.
                foreach (Label label in MapLabels[map])
                    EnableFlag(map.HasLabelFlagBase + (int)label);
            }
        }

        void DisableRandomShopFlags()
        {
            // Andre
            List<int> andreArmor = new List<int>() { 0, 1, 2, 3, 4 };
            andreArmor.PopRandomElement(Rand);
            andreArmor.PopRandomElement(Rand);
            foreach (int offset in andreArmor)
            {
                EnableFlag(11817000 + 40 * offset +  0);
                EnableFlag(11817000 + 40 * offset + 10);
                EnableFlag(11817000 + 40 * offset + 20);
                EnableFlag(11817000 + 40 * offset + 30);
            }
            
            List<int> andreEmbers = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            andreEmbers.PopRandomElement(Rand);
            andreEmbers.PopRandomElement(Rand); ;
            foreach (int offset in andreEmbers)
                EnableFlag(11817200 + 10 * offset);

            List<int> vamosWeapons = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            vamosWeapons.PopRandomElement(Rand);
            vamosWeapons.PopRandomElement(Rand);
            vamosWeapons.PopRandomElement(Rand);
            foreach (int offset in vamosWeapons)
                EnableFlag(11817400 + 10 * offset);

            List<int> vamosEmbers = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            vamosEmbers.PopRandomElement(Rand);
            vamosEmbers.PopRandomElement(Rand);
            foreach (int offset in vamosEmbers)
                EnableFlag(11817500 + 10 * offset);

            List<int> undeadMerchantWeapons = new List<int>() { 0, 1, 2, 3, 4 };
            undeadMerchantWeapons.PopRandomElement(Rand);
            foreach (int offset in undeadMerchantWeapons)
                EnableFlag(11817600 + 10 * offset);
            // Always sells keys, too lazy. But 50% chance of selling Piercing Eye.
            if (Rand.Roll(0.5))
                EnableFlag(11817680);

            List<int> chesterWeapons = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            chesterWeapons.PopRandomElement(Rand);
            chesterWeapons.PopRandomElement(Rand);
            chesterWeapons.PopRandomElement(Rand);
            foreach (int offset in chesterWeapons)
                EnableFlag(11817700 + 10 * offset);

            List<int> chesterArmor = new List<int>() { 0, 1, 2, 3, 4 };
            chesterArmor.PopRandomElement(Rand);
            chesterArmor.PopRandomElement(Rand);
            foreach (int offset in chesterArmor)
                EnableFlag(11817800 + 10 * offset);
        }

        void ResetPlayerLevel()
        {
#if DEBUG
            Hook.Vitality = 99;
            Hook.Attunement = 99;
            Hook.Endurance = 99;
            Hook.Strength = 99;
            Hook.Dexterity = 99;
            Hook.Resistance = 99;
            Hook.Intelligence = 99;
            Hook.Faith = 99;
            Hook.SoulLevel = 99;
            Hook.MaxHealth = 999;
            Hook.MaxStamina = 150;
#else
            Hook.Vitality = 14;
            Hook.Attunement = 11;
            Hook.Endurance = 25;  // Starts nice and high for equip load.
            Hook.Strength = 12;
            Hook.Dexterity = 12;
            Hook.Resistance = 10;
            Hook.Intelligence = 10;
            Hook.Faith = 10;
            Hook.SoulLevel = 20;
            Hook.MaxHealth = 659;  // Appropriate for vitality 14.
            Hook.MaxStamina = 95;  // Actually for 12 endurance, not 20.
#endif
        }

        void ClearAttunementSlots()
        { 
            // Un-attune all spells.
            Hook.Spell1ID = -1;
            Hook.Spell2ID = -1;
            Hook.Spell3ID = -1;
            Hook.Spell4ID = -1;
            Hook.Spell5ID = -1;
            Hook.Spell6ID = -1;
            Hook.Spell7ID = -1;
            Hook.Spell8ID = -1;
            Hook.Spell9ID = -1;
            Hook.Spell10ID = -1;
            Hook.Spell11ID = -1;
            Hook.Spell12ID = -1;
            Hook.Spell1Casts = 0;
            Hook.Spell2Casts = 0;
            Hook.Spell3Casts = 0;
            Hook.Spell4Casts = 0;
            Hook.Spell5Casts = 0;
            Hook.Spell6Casts = 0;
            Hook.Spell7Casts = 0;
            Hook.Spell8Casts = 0;
            Hook.Spell9Casts = 0;
            Hook.Spell10Casts = 0;
            Hook.Spell11Casts = 0;
            Hook.Spell12Casts = 0;
        }

        Dictionary<Label, int> GetWeightedLabels()
        {
            // Some labels can't be chosen, and some are more likely than others (e.g. Sapient, Hollow).
            List<Label> allLabels = new List<Label>(Enum.GetValues(typeof(Label)).Cast<Label>());
            Dictionary<Label, int> weightedLabels = new Dictionary<Label, int>();
            foreach (Label label in allLabels)
                weightedLabels[label] = 1;
            weightedLabels[Label.Mimic] = 0;
            weightedLabels[Label.Vagrant] = 0;
            weightedLabels[Label.Ghost] = 0;
            weightedLabels[Label.Part] = 0;
            return weightedLabels;
        }

        public MapInfo ActivateMap(int triggerFlag)
        {
            // Enemies get harder (unless at max).
            if (MapLevel < 10)
                MapLevel += 1;

#if DEBUG
            Console.WriteLine($"Requesting map with level: {MapLevel}");
#endif

            MapInfo newMap = GetNextMap();
            Connection startPoint = GetStartPoint(newMap, 0, ignoreDepth: true);

            // Not using depth for now; going full random.
            //Connection endPoint = CurrentMap.GetEndPointFromTriggerFlag(triggerFlag);
            //Connection startPoint = GetStartPoint(newMap, endPoint.Depth);
#if DEBUG
            Console.WriteLine($"Activating map: {newMap.Name}");
            Console.WriteLine($"    Labels: {string.Join(", ", MapLabels[newMap])}");
            Console.WriteLine($"    Start point index: {startPoint.IndexInLevel}");
#endif
            // Disable map's "dead enemies" flags.
            for (int i = 0; i < 100; i++)
                DisableFlag(newMap.DeadEnemyFlagBase + i);

            // Reset shop stocks of Motes/Tomes.
            for (int i = 0; i < 100; i++)
                DisableFlag(11027000 + i);  // Includes "bonfire shop" (11027090).

            // Generate MSB, LUABND, and tweaked EMEVD for new map.
            double redPhantomOdds = GetFlag(GameFlag.MornsteinRingFlag) ? 0.2 : 0.1;
            MapGenerator mapGen = new MapGenerator(Mod, this, newMap, Rand, redPhantomOdds);
            mapGen.Generate();

            foreach (int startFlag in startPoint.AllStartFlags)
            {
#if DEBUG
                Console.WriteLine($"    Enabling start flag: {startFlag}");
#endif
                EnableFlag(startFlag);  // "disable end" flag and other miscellaneous flags to enable (e.g. boss dead).
            }
            DisableFlag(GameFlag.DisableAbyssPortal);  // Reset Abyss portal for new map.
            DisableFlag(GameFlag.AbyssBattleActive);
            if (newMap.Name != "Painted World")  // Current map is not updated when you're in the Painted World, which is only temporary.
            {
                CurrentMap = newMap;
                foreach (var map in Maps.MapList)
                    DisableFlag(map.InMapFlag);
                EnableFlag(CurrentMap.InMapFlag);
            }
            MapsAvailable.Remove(newMap);
            MapsVisited.Add(newMap);
            EnableFlag(newMap.IsVisitedFlag);  // Painted World also marked as visited here.

            DisableFlag(GameFlag.OneBonfireCreated);
            DisableFlag(GameFlag.TwoBonfiresCreated);

            Hook.LastBonfire = startPoint.SpawnPointID;

            EnableFlag(GameFlag.RequestLevelMessageBase + MapLevel - 1);
            EnableFlag(startPoint.WarpRequestFlag);
            return newMap;
        }

        MapInfo GetNextMap()
        {
            // First maps are completely random (sans endpoint maps), with random start points.
            // Last map is an endpoint: Anor Londo, Duke's Archives, New Londo Ruins, Lost Izalith, or Tomb of the Giants.
            // It's Anor Londo if you don't have the Lordvessel (and the others will never appear).
            // Otherwise, it's a random map from among the endpoints you haven't beaten.
            // If you've beaten them all, it's any endpoint.
            if (DEBUG_MAP != "")
                return Maps.GetMap(DEBUG_MAP);

            int mapLevel = MapLevel;  // Note that map level is incremented just before this is called, so it's the level of THIS upcoming map.
            int endMapLevel = GetFlag(GameFlag.LobosJrRingFlag) ? 9 : 6;
            if (mapLevel < endMapLevel)
            {
                List<MapInfo> options = new List<MapInfo>(Maps.MapList.Where(map => -1 <= map.Rating && map.Rating <= 1 && MapsAvailable.Contains(map)));
                // 80% chance to remove Great Hollow and Ash Lake from options.
                if (options.Count > 2 && Rand.Roll(0.8))
                {
                    if (options.Contains(Maps.GetMap("AshLake")))
                        options.Remove(Maps.GetMap("AshLake"));
                    if (options.Contains(Maps.GetMap("GreatHollow")))
                        options.Remove(Maps.GetMap("GreatHollow"));
                }
                return options.GetRandomElement(Rand);
            }
            else if (mapLevel == endMapLevel)
            {
                if (!GetFlag(GameFlag.LordvesselObtained))
                {
                    // If you don't have the Lordvessel, the final level is always Anor Londo,
                    // with the only possible exit being Gwynevere's bonfire.
                    EnableFlag(11512000);  // Disable Batwing exit.
                    EnableFlag(11512010);  // Disable Archives exit.
                    return Maps.GetMap("AnorLondo");
                }
                else
                {
                    // If you have the Lordvessel, the final level is one of the four Lord Soul areas
                    // whose boss you have not yet defeated.
                    List<MapInfo> options = new List<MapInfo>(Maps.MapList.Where(
                        map => (Math.Abs(map.Rating) == 2 || map.Name == "NewLondoRuins") && map.Name != "AnorLondo" && MapsAvailable.Contains(map)));
                    if (GetFlag(GameFlag.ArchivesBossDefeated))
                        options.Remove(Maps.GetMap("DukesArchives"));
                    if (GetFlag(GameFlag.TombBossDefeated))
                        options.Remove(Maps.GetMap("TombOfTheGiants"));
                    if (GetFlag(GameFlag.IzalithBossDefeated))
                        options.Remove(Maps.GetMap("LostIzalith"));
                    if (GetFlag(GameFlag.NewLondoBossDefeated))
                        options.Remove(Maps.GetMap("NewLondoRuins"));
                    if (!options.Any())
                        // All Lord Souls have been obtained. Go to any rating 2 map instead.
                        options = new List<MapInfo>(Maps.MapList.Where(map => Math.Abs(map.Rating) == 2 && MapsAvailable.Contains(map)));
                    MapInfo chosen = options.GetRandomElement(Rand);
                    if (chosen.Name == "NewLondoRuins")
                    {
                        // No way out of New Londo except into the Abyss at this point.
                        EnableFlag(chosen.Connections[0].DisableEndFlag);
                        EnableFlag(chosen.Connections[1].DisableEndFlag);
                        EnableFlag(chosen.Connections[2].DisableEndFlag);
                        // Seal gate is automatically opened if it's an endpoint.
                        EnableFlag(61600110);
                        EnableFlag(11600110);
                    }
                    return chosen;
                }
            }
            else  // Only requested from EMEVD if the game KNOWS you're allowed to one of these true-ending maps.
            {
                if (GetFlag(GameFlag.AbyssBattleVictoryCountBase + 3))
                    return Maps.GetMap("ChasmOfTheAbyss");
                else
                    return Maps.GetMap("KilnOfTheFirstFlame");
            }
        }

        public void ActivateFirstMap()
        {
#if DEBUG
            Console.WriteLine($"Requesting first map with level: {MapLevel}");
#endif
            Console.WriteLine("Travelling to Lordran...");

            MapLevel = 1;  // should already be done in EMEVD cleanup

            MapInfo firstMap = GetNextMap();  // Any map rated from -1 to 1.

            // Get random start point.
            Connection startPoint = GetStartPoint(firstMap, 0, ignoreDepth: true);
#if DEBUG
            Console.WriteLine($"Activating first map: {firstMap.Name}");
            Console.WriteLine($"    Labels: {string.Join(", ", MapLabels[firstMap])}");
            Console.WriteLine($"    Start point index: {startPoint.IndexInLevel}");
#endif
            foreach (int startFlag in startPoint.AllStartFlags)
            {
#if DEBUG
                Console.WriteLine($"    Enabling start flag: {startFlag}");
#endif
                EnableFlag(startFlag);  // "disable end" flag and other miscellaneous flags to enable (e.g. boss dead).
            }

            DisableFlag(GameFlag.DisableAbyssPortal);  // Reset Abyss portal for new map.

            // Disable map's "dead enemies" flags.
            for (int i = 0; i < 100; i++)
                DisableFlag(firstMap.DeadEnemyFlagBase + i);

            // Reset shop stocks of Motes/Tomes.
            for (int i = 0; i < 100; i++)
                DisableFlag(11027000 + i);  // Includes "bonfire shop" (11027090).

            // Generate MSB, LUABND, EMEVD, FFXBND.
            double redPhantomOdds = GetFlag(GameFlag.MornsteinRingFlag) ? 0.2 : 0.1;
            MapGenerator mapGen = new MapGenerator(Mod, this, firstMap, Rand, redPhantomOdds);
            mapGen.Generate();

            CurrentMap = firstMap;
            foreach (var map in Maps.MapList)
                DisableFlag(map.InMapFlag);
            EnableFlag(CurrentMap.InMapFlag);

            MapsAvailable.Remove(firstMap);
            MapsVisited.Add(firstMap);
            EnableFlag(firstMap.IsVisitedFlag);

            DisableFlag(GameFlag.OneBonfireCreated);
            DisableFlag(GameFlag.TwoBonfiresCreated);

            EnableFlag(GameFlag.RunSetupCompleteFlag);
            EnableFlag(GameFlag.RequestLevelMessageBase + MapLevel - 1);
            EnableFlag(startPoint.WarpRequestFlag);
        }

        Connection GetStartPoint(MapInfo newMap, int fromDepth, bool ignoreDepth = false)
        {
            if (ignoreDepth)  // e.g. for first map
            {
                var options = new List<Connection>(newMap.Connections.Where(c => c.IsStart));
                return options.GetRandomElement(Rand);
            }

            // Opposite depth is weighted higher.
            // So if fromDepth == +2, connections with depth -2 are most likely, depth -1 is somewhat likely,
            // depth 0 is unlikely, etc.
            Dictionary<Connection, int> weights = new Dictionary<Connection, int>();
            foreach (Connection connection in newMap.Connections)
            {
                int invertedDepthDeviation = Math.Abs(connection.Depth + fromDepth);
                switch (invertedDepthDeviation)
                {
                    case 0:
                        weights[connection] = 20;
                        break;
                    case 1:
                        weights[connection] = 10;
                        break;
                    case 2:
                        weights[connection] = 5;
                        break;
                    default:
                        weights[connection] = 1;
                        break;
                }
            }
            return weights.GetWeightedRandomElement(Rand);
        }

        void RequestBonfireCreation()
        {
            Hook.GetStablePosition(out float x, out float y, out float z, out float angle);
            int bonfireSpawnID = MapGenerator.CreateBonfire(Mod.GameDir, CurrentMap, x, y, z, angle, Rand);
            if (bonfireSpawnID == -1)
            {
                EnableFlag(GameFlag.BonfireRequestUnsuccessful);  // could not create bonfire
                return;
            }
            else
            {
                Hook.LastBonfire = bonfireSpawnID;
                EnableFlag(GameFlag.BonfireRequestSuccessful);
                Thread.Sleep(2000);
                Hook.BonfireWarp();
            }
        }

        void RequestAbyssFight()
        {
            Console.WriteLine("Delving into the Abyss...");
            MapGenerator abyssGen = new MapGenerator(Mod, this, Maps.GetMap("NewLondoRuins"), Rand, redPhantomOdds: 1.0);
            abyssGen.GenerateAbyssVisit();
            EnableFlag(GameFlag.AbyssBattleRequestComplete);
        }

        void CheckStatBoost()
        {
            // Look for an enabled stat boost flag and apply stat boost (and max health/stamina upgrades) to player.
            for (int i = 0; i < 10; i++)
            {
                if (GetFlag(GameFlag.BoostVitalityBase + i))
                {
                    int oldVitality = Hook.Vitality;
                    Hook.Vitality += i + 1;
                    if (Hook.Vitality > 99) Hook.Vitality = 99;
                    Hook.MaxHealth += (Hook.Vitality - oldVitality) * 25;  // 25 HP per level
                    DisableFlag(GameFlag.BoostVitalityBase + i);
                }
                if (GetFlag(GameFlag.BoostAttunementBase + i))
                {
                    Hook.Attunement += i + 1;
                    if (Hook.Attunement > 99) Hook.Attunement = 99;
                    DisableFlag(GameFlag.BoostAttunementBase + i);
                }
                if (GetFlag(GameFlag.BoostEnduranceBase + i))
                {
                    int oldEndurance = Hook.Endurance;
                    Hook.Endurance += i + 1;
                    if (Hook.Endurance > 99) Hook.Endurance = 99;
                    Hook.MaxStamina += (Hook.Endurance - oldEndurance) * 2;  // 2 stamina points per level
                    DisableFlag(GameFlag.BoostEnduranceBase + i);
                }
                if (GetFlag(GameFlag.BoostStrengthBase + i))
                {
                    Hook.Strength += i + 1;
                    if (Hook.Strength > 99) Hook.Strength = 99;
                    DisableFlag(GameFlag.BoostStrengthBase + i);
                }
                if (GetFlag(GameFlag.BoostDexterityBase + i))
                {
                    Hook.Dexterity += i + 1;
                    if (Hook.Dexterity > 99) Hook.Dexterity = 99;
                    DisableFlag(GameFlag.BoostDexterityBase + i);
                }
                if (GetFlag(GameFlag.BoostResistanceBase + i))
                {
                    Hook.Resistance += i + 1;
                    if (Hook.Resistance > 99) Hook.Resistance = 99;
                    DisableFlag(GameFlag.BoostResistanceBase + i);
                }
                if (GetFlag(GameFlag.BoostIntelligenceBase + i))
                {
                    Hook.Intelligence += i + 1;
                    if (Hook.Intelligence > 99) Hook.Intelligence = 99;
                    DisableFlag(GameFlag.BoostIntelligenceBase + i);
                }
                if (GetFlag(GameFlag.BoostFaithBase + i))
                {
                    Hook.Faith += i + 1;
                    if (Hook.Faith > 99) Hook.Faith = 99;
                    DisableFlag(GameFlag.BoostFaithBase + i);
                }
            }
        }

        void RechargeSpells()
        {
            // Recover 10% of usages of EVERY spell slot, up to max (or +1 for spells with <10 casts).
            // Only works every five seconds in EMEVD.
            for (int slot = 1; slot <= 12; slot++)
            {
                int spellID = Hook.GetSpellID(slot);
                if (spellID != -1)
                {
                    int currentCastCount = Hook.GetSpellCasts(slot);
                    int maxCastCount = Mod.GPARAM.Magic[spellID].BaseCastCount;
                    int newCastCount;
                    if (maxCastCount < 10 && currentCastCount < maxCastCount)
                        newCastCount = currentCastCount + 1;
                    else
                        newCastCount = Math.Min(maxCastCount, (int)(currentCastCount * 1.1));
                    Hook.SetSpellCasts(slot, newCastCount);
                }
            }
        }

        public void EnableFlag(int flag)
        {
            Hook.EnableEventFlag(flag);
        }
        public void EnableFlag(GameFlag flag)
        {
            Hook.EnableEventFlag((int)flag);
        }

        public void DisableFlag(int flag)
        {
            Hook.DisableEventFlag(flag);
        }
        public void DisableFlag(GameFlag flag)
        {
            Hook.DisableEventFlag((int)flag);
        }

        public bool GetFlag(int flag)
        {
            return Hook.ReadEventFlag(flag);
        }

        public bool GetFlag(GameFlag flag)
        {
            return Hook.ReadEventFlag((int)flag);
        }
    }
}
