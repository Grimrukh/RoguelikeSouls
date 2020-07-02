using RoguelikeSouls.Extensions;
using System;
using System.Collections.Generic;
using System.Linq;
using ConnectionList = System.Collections.Generic.List<(int depth, bool isStart, bool isEnd, int[] extraStartFlags)>;

namespace RoguelikeSouls.Installation
{
    class Connection
    {
        public int LevelBaseFlag { get; set; }
        public int LevelBaseEntity { get; set; }
        public int LevelIndexInMap { get; set; }  // e.g. 1 for Undead Parish or Lost Izalith
        public int IndexInLevel { get; set; }  // in level, not map
        public int Depth { get; set; }  // -2 to +2
        public bool IsStart { get; set; }
        public bool IsEnd { get; set; }
        public int SpawnPointID { get => LevelBaseEntity + 230 + IndexInLevel; }  // SpawnPoint event in MSB.
        public int WarpPointID { get => LevelBaseEntity + 240 + IndexInLevel; }  // "Player" entity in MSB for warping.
        public int DisableEndFlag { get => LevelBaseFlag + 10 * IndexInLevel; }  // end cannot be triggered if this flag is enabled
        public int EndTriggerFlag { get => LevelBaseFlag + 10 * IndexInLevel + 1; }  // flag enabled in EMEVD when exit prompt activated
        public int WarpRequestFlag { get => LevelBaseFlag + 10 * IndexInLevel + 5; }  // will cause a warp to this connection warp point in common EMEVD when enabled
        public List<int> ExtraStartFlags { private get; set; }  // generally to disable overlapping end points and mark bosses as dead
        public List<int> AllStartFlags
        {
            // combines DisableEndFlag and any ExtraStartFlags specified
            get => new List<int>() { DisableEndFlag }.Concat(ExtraStartFlags).ToList();
        }
        
        public Connection() { }
    }

    class Map
    {
        public string Name { get; set; }
        public int[] MapID { get; set; }
        public int InMapFlag { get; set; }  // Enabled when character is currently in this map (or has travelled to the Painted World or Abyss challenge from it, pending return).
        public int BaseFlag { get; set; }  // Map state flags are stored at offsets relative to this base.
        public int BaseEntityID { get; set; }  // e.g. 1010000 for Undead Parish.
        public int BaseCorpseItemLotID { get; set; }  // e.g. 1216000 for Chasm of the Abyss
        public int BaseChestItemLotID { get; set; }  // e.g. 2216000 for Chasm of the Abyss
        public int IndexInMap { get; set; }  // Undead Parish, Oolacile Township, Ash Lake, Lost Izalith == 1, Chasm == 2
        public int BonfireCharacterID { get; set; }
        public int Rating { get; set; }  // Determines when map is most likely to appear (e.g. rating 2 prefers to appear after you've completed two maps).
        public int BasicEnemyCount { get; set; }
        public int RareEnemyCount { get; set; }
        public int ItemCorpseCount { get; set; }
        public int ChestCount { get; set; }
        public int BossCount { get; set; }
        public List<Connection> Connections { get; private set; }
        public HashSet<int> DefaultModels { get; set; } = new HashSet<int>();  // for constant enemies like the Hydra
        public HashSet<int> DefaultBattleScriptIDs { get; set; } = new HashSet<int>();  // ditto
        public HashSet<int> DefaultLogicScriptIDs { get; set; } = new HashSet<int>();  // ditto

        public ConnectionList ConnectionInfo
        {
            set
            {
                Connections = new List<Connection>();
                int connectionIndex = 0;
                foreach ((int depth, bool isStart, bool isEnd, int[] extraStartFlags) in value)
                {
                    Connections.Add(new Connection()
                    {
                        LevelBaseFlag = BaseFlag,
                        LevelBaseEntity = BaseEntityID,
                        LevelIndexInMap = IndexInMap,
                        IndexInLevel = connectionIndex,
                        Depth = depth,
                        IsStart = isStart,
                        IsEnd = isEnd,
                        ExtraStartFlags = extraStartFlags.ToList(),
                    });
                    connectionIndex++;
                }
            }
        }

        public string MsbName
        {
            get => $"m{MapID[0]:00}_{MapID[1]:00}_{MapID[2]:00}_{MapID[3]:00}";
        }

        public string EmevdName  // or script, sfx, etc.
        {
            get => $"m{MapID[0]:00}_{MapID[1]:00}_{MapID[2]:00}_00";
        }

        public int TalkIDBase
        {
            get => int.Parse($"{MapID[0]:00}{MapID[1]:0}000");
        }

        public int IsVisitedFlag
        {
            get => BaseFlag + 100;
        }

        public int HasLabelFlagBase
        {
            get => BaseFlag + 100;  // e.g. 11012100
        }

        public int DeadEnemyFlagBase
        {
            // Shared by levels in the same map (e.g. 11013000).
            get => 10000000 + 100000 * MapID[0] + 10000 * MapID[1] + 3000;
        }

        public int BaseItemCorpseLotID
        {
            get => BaseEntityID;
        }

        public int BonfireTalkID
        {
            get
            {
                if (MapID[0] == 10)  // m10 bonfire talks are numbered weirdly.
                    return int.Parse($"{MapID[0]:00}0{MapID[1]:0}00");  // no longer offsetting by index
                else
                    return int.Parse($"{MapID[0]:00}{MapID[1]:0}000");
            }
        }

        public int BonfireObjectID
        {
            get => BonfireCharacterID + 1000;
        }

        public int BaseNPCEntityID
        {
            get => 6200 + IndexInMap * 300;
        }

        public int BaseChestEntityID
        {
            get => int.Parse($"{MapID[0]:00}{MapID[1]:0}1650") + 10 * IndexInMap;
        }

        public int BaseChestObjActFlagID
        {
            get => 10000000 + MapID[0] * 100000 + MapID[1] * 10000 + 600 + 10 * IndexInMap;
        }

        public int InvaderTriggerRegionID
        {
            get => BaseEntityID + 200;
        }

        public int InvaderSpawnPointID
        {
            get => BaseEntityID + 201;
        }

        public int PortalWarpPointID
        {
            get => 100000 * MapID[0] + 10000 * MapID[1] + 999;
        }

        public int PortalFXID
        {
            get => 100000 * MapID[0] + 10000 * MapID[1] + 998;
        }

        public int PortalTriggerCharacterID
        {
            get => 100000 * MapID[0] + 10000 * MapID[1] + 997;
        }

        public Map() { }

        public int GetBossID(int index, bool isTwin = false)
        {
            // Boss 0 has relative ID 290, boss 1 has relative ID 280, etc.
            // Boss's twin is +1.
            if (index < 0 || index >= BossCount)
                throw new ArgumentException($"Boss index for map {MsbName} must be between 0 and {BossCount - 1}.");
            return BaseEntityID + 300 - 10 * (index + 1) + (isTwin ? 1 : 0);
        }

        public int GetBossTwinFlag(int bossIndex)
        {
            // Boss 0 has relative flag ID 291, boss 1 has relative ID 280, etc.
            return BaseFlag + 300 - 10 * (bossIndex + 1) + 1;
        }

        public int GetRareEnemyID(int index)
        {
            if (index < 0 || index > 99)
                throw new ArgumentException($"Rare enemy index must be between 0 and 99.");
            return BaseEntityID + 130 + index;
        }

        public int GetCommonUncommonEnemyID(int index, bool isRedPhantom)
        {
            if (index < 0 || index > 99)
                throw new ArgumentException($"Common/uncommon enemy index must be between 0 and 99.");
            return BaseEntityID + index + (isRedPhantom ? 100 : 0);
        }

        public Connection GetRandomStartPoint(Random random)
        {
            List<Connection> options = new List<Connection>(Connections.Where(connection => connection.IsStart));
            return options.GetRandomElement(random);
        }

        public Connection GetEndPointFromTriggerFlag(int triggerFlag)
        {
            IEnumerable<Connection> matches = Connections.Where(connection => connection.EndTriggerFlag == triggerFlag);
            if (!matches.Any())
                throw new ArgumentException($"Invalid endpoint trigger flag: {triggerFlag}");
            return matches.First();
        }
    }

    static class Maps
    {
        public static Dictionary<string, string[]> NoKeyCollisions = new Dictionary<string, string[]>()
        {
            // Actually not using this for now, since you can always get out of the Depths by beating the boss
            // and there's no longer a critical key in Anor Londo. (No houses are locked in Undead Burg anymore.)
            { "Depths", new string[] { "h0001B0", "h0003B0" } },  // locked bonfire chamber
            { "Anor Londo", new string[] { "h0030B1_0000", "h0031B1_0000", "h0032B1_0000" } }  // Gwyn's tomb (beyond statue)
        };

        // Maps boss entity IDs to their fixed coordinates. Optional twin boss IDs end in 1; twin ID's absence implies that twin battles are not possible there.
        public static Dictionary<int, (GamePoint point, int emevdIndex)> BossLocations = new Dictionary<int, (GamePoint point, int emevdIndex)>()
        {
            { 1000290, (new GamePoint(-170.0f, -100.0f, 30.0f, 0.0f, "h0074B0", "", ArenaSize.Giant), 0) },  // Gaping Dragon arena
            { 1000291, (new GamePoint(-170.0f, -100.0f, 20.0f, 0.0f, "h0074B0", "", ArenaSize.Giant), 0) },

            { 1010290, (new GamePoint(10.161f, 15.819f, -118.262f, -79.844f, "h1117B1", "", ArenaSize.Medium), 0) },  // Taurus Demon arena (maybe Small?)
            { 1010291, (new GamePoint(24.562f, 15.819f, -120.842f, -91.475f, "h1117B1", "", ArenaSize.Medium), 0) },
            { 1010280, (new GamePoint(57.526f, -38.254f, -117.677f, -133.605f, "h1121B1", "", ArenaSize.Small), 1) },  // Watchtower Basement arena
            // No twin for Watchtower Basement.

            { 1010590, (new GamePoint(2.062f, 48.430f, 107.960f, -20.288f, "h1034B1", "", ArenaSize.Large), 2) },  // Bell Gargoyle arena
            { 1010591, (new GamePoint(19.891f, 48.430f, 107.960f, 3.449f, "h1034B1", "", ArenaSize.Large), 2) },
            { 1010580, (new GamePoint(87.780f, -2.689f, 57.965f, -178.067f, "h1049B1", "", ArenaSize.Medium), 3) },  // Titanite Demon arena (requires Medium-level navigation)
            { 1010581, (new GamePoint(81.075f, -2.689f, 73.225f, -164.006f, "h1049B1", "", ArenaSize.Medium), 3) },

            { 1100290, (new GamePoint(-22.750f, 60.500f, 697.000f, 180.000f, "h0041B0", "", ArenaSize.Large), 0) },  // Priscilla arena
            { 1100291, (new GamePoint(-16.129f, 60.500f, 692.558f, 158.416f, "h0041B0", "", ArenaSize.Large), 0) },

            { 1200290, (new GamePoint(256.690f, -15.9f, -311.650f, -155.000f, "h0035B0", "", ArenaSize.Giant), 0) },  // Sif arena
            { 1200291, (new GamePoint(250.641f, -15.9f, -308.829f, -144.967f, "h0035B0", "", ArenaSize.Giant), 0) },
            // Moonlight Butterfly and Hydra are left alone where they are.

            { 1210290, (new GamePoint(962.797f, -320.980f, 508.997f, -150.000f, "h0036B1", "", ArenaSize.Giant), 0) },  // Sanctuary Guardian arena
            { 1210291, (new GamePoint(980.418f, -320.980f, 494.211f, -125.000f, "h0036B1", "", ArenaSize.Giant), 0) },
            // Kalameet arena disabled (Kalameet can appear elsewhere and I can't handle the cheese here).
            // Boss fight takes place in ravine before the original arena instead.
            { 1210280, (new GamePoint(892.929f, -344.418f, 767.920f, 46.424f, "h0011B1", "", ArenaSize.Large), 1) },  // Pre-Kalameet ravine arena
            { 1210281, (new GamePoint(900.139f, -344.285f, 767.027f, 59.232f, "h0011B1", "", ArenaSize.Large), 1) },

            { 1210590, (new GamePoint(1059.899f, -330.0f, 811.875f, 87.282f, "h0095B1", "", ArenaSize.Giant), 2) },  // Artorias arena
            { 1210591, (new GamePoint(1060.724f, -330.0f, 823.403f, 71.193f, "h0095B1", "", ArenaSize.Giant), 2) },
            { 1210580, (new GamePoint(909.924f, -400.500f, 937.150f, -56.975f, "h0106B1", "", ArenaSize.Giant), 3) },  // Pre-Chasm hall arena
            { 1210581, (new GamePoint(904.864f, -400.500f, 933.410f, -82.590f, "h0106B1", "", ArenaSize.Giant), 3) },
            
            { 1210890, (new GamePoint(848.320f, -576.840f, 847.957f, -157.052f, "h0113B1", "", ArenaSize.Giant), 4) },  // Manus arena
            { 1210891, (new GamePoint(836.642f, -576.840f, 855.776f, -146.194f, "h0113B1", "", ArenaSize.Giant), 4) },

            { 1300290, (new GamePoint(46.0f, -165.8f, 146.0f, -180.0f, "h0036B0", "", ArenaSize.Small), 0) },  // Pinwheel arena
            // No twin for Pinwheel arena.
            { 1300280, (new GamePoint(46.5f, -111.947f, 163.951f, 172.0f, "h0101B0", "", ArenaSize.Small), 1) },  // New upper Catacombs arena
            // No twin for upper Catacombs arena.

            { 1310290, (new GamePoint(-147.430f, -264.654f, -46.4f, -132.713f, "h0047B1", "", ArenaSize.Large), 0) },  // Nito arena
            { 1310291, (new GamePoint(-157.536f, -264.654f, -31.043f, -121.749f, "h0047B1", "", ArenaSize.Large), 0) },
            // Baby Skeleton spawner left intact.

            // No bosses in Ash Lake.

            { 1400290, (new GamePoint(59.577f, -240.744f, 124.629f, 83.169f, "h0053B0", "", ArenaSize.Giant), 0) },  // Quelaag arena
            { 1400291, (new GamePoint(47.443f, -240.744f, 130.666f, 61.322f, "h0053B0", "", ArenaSize.Giant), 0) },
            { 1400280, (new GamePoint(-90.194f, -138.436f, 18.227f, 114.614f, "h0062B0", "", ArenaSize.Small), 1) },  // Tunnel arena (new)
            // No twin for new tunnel arena.
            
            { 1410290, (new GamePoint(184.269f, -383.680f, 43.354f, 137.720f, "h0062B1", "", ArenaSize.Large), 0) },  // Centipede Demon arena
            // No twin.
            { 1410280, (new GamePoint(395.910f, -278.125f, 64.479f, 132.0f, "h0600B1", "", ArenaSize.Giant), 1) },  // Ceaseless Discharge arena
            { 1410281, (new GamePoint(393.634f, -278.125f, 84.951f, 65.0f, "h0600B1", "", ArenaSize.Giant), 1) },
            { 1410590, (new GamePoint(537.693f, -440.354f, 407.500f, 48.619f, "h0045B1", "", ArenaSize.Large), 2) },  // Bed of Chaos arena (Bed is always "twin").
            // No twin. EMEVD slot is also unused.

            { 1500290, (new GamePoint(113.743f, 83.0f, 255.0f, 90.0f, "h0024B0_0000", "", ArenaSize.Medium), 0) },  // Iron Golem arena
            // No twin for Iron Golem arena.
            { 1500280, (new GamePoint(89.819f, 45.241f, 181.481f, 150.0f, "h0100B0_0000", "", ArenaSize.Medium), 1) },  // New arena above gate
            // No twin for arena above gate.

            { 1510290, (new GamePoint(572.0f, 142.8f, 261.082f, 78.276f, "h0022B1_0000", "", ArenaSize.Large), 0) },  // O&S arena (not giant due to pillars)
            { 1510291, (new GamePoint(572.0f, 142.8f, 249.823f, 103.310f, "h0022B1_0000", "", ArenaSize.Large), 0) },  // O&S arena
            // { 1510280, (new GamePoint(203.632f, 179.400f, 191.642f, 180.0f, "h0002B1_0000", "", ArenaSize.Medium) },  // Pale Wing exit arena (unused)
            // { 1510270, (new GamePoint(203.720f, 179.400f, 318.890f, 0.0f, "h0040B1_0000", "", ArenaSize.Medium) },  // Archives exit arena (unused)
            
            // Abyss battle (via drop or one-off portal).
            { 1600290, (new GamePoint(92.399f, -311.0f, 34.585f, -4.0f, "h0040B0_0000", "", ArenaSize.Giant), 0) },  // Abyss arena
            { 1600291, (new GamePoint(62.993f, -311.0f, 26.506f, -30.0f, "h0040B0_0000", "", ArenaSize.Giant), 0) },

            { 1700290, (new GamePoint(295.500f, 389.0f, 538.0f, 48.0f, "h0032B0", "", ArenaSize.Large), 0) },  // Tower arena
            // No twin.
            { 1700280, (new GamePoint(107.320f, 134.050f, 852.270f, -55.0f, "h0082B0", "", ArenaSize.Large), 1) },  // Seath arena
            { 1700281, (new GamePoint(94.696f, 134.050f, 857.493f, -62.023f, "h0082B0", "", ArenaSize.Large), 1) },

            { 1800290, (new GamePoint(386.357f, -117.0f, 190.595f, -60.0f, "h0006B0", "", ArenaSize.Large), 0) },  // Gwyn arena
            // No twin.
        };

        public static List<Map> MapList = new List<Map>()
        {
            new Map()
            {
                Name = "Depths",
                IndexInMap = 0,
                Rating = -1,
                InMapFlag = 1800,
                BasicEnemyCount = 40,
                RareEnemyCount = 5,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 10, 0, 0, 0 },
                BaseFlag = 11002000,
                BaseEntityID = 1000000,
                BaseCorpseItemLotID = 1000000,
                BaseChestItemLotID = 100000,
                BonfireCharacterID = 1000960,
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { }),  // Parish door
                    (-1, false, true, new int[] { }),  // Boss arena drop
                    (-1, true, true, new int[] { }),  // Blighttown door
                },
            },
            new Map()
            {
                Name = "UndeadBurg",
                IndexInMap = 0,
                Rating = 0,
                InMapFlag = 1801,
                BasicEnemyCount = 40,
                RareEnemyCount = 8,
                ItemCorpseCount = 20,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 10, 1, 0, 0 },
                BaseFlag = 11012000,
                BaseEntityID = 1010000,
                BaseCorpseItemLotID = 1010000,
                BaseChestItemLotID = 101000,
                BonfireCharacterID = 1010960,
                DefaultModels = new HashSet<int>() { 3430 },
                DefaultBattleScriptIDs = new HashSet<int>() { 343000 },  // Hellkite Wyvern
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { 11012010 }),  // Parish bridge (portcullis)
                    (+1, true, true, new int[] { 11012000 }),  // Parish bridge (underneath)
                    ( 0, true, true, new int[] { }),  // (Polished Key) Firelink aqueduct (near end)
                    ( 0, true, true, new int[] { }),  // (Polished Key) Firelink aqueduct (far end)
                    (-1, true, true, new int[] { 11012280 }),  // (Rusted Key) Watchtower basement
                    (-2, true, true, new int[] { }),  // (Tarnished Key) Depths door
                },
            },
            new Map()
            {
                Name = "UndeadParish",
                IndexInMap = 1,
                Rating = +1,
                InMapFlag = 1802,
                BasicEnemyCount = 30,
                RareEnemyCount = 5,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 10, 1, 0, 0 },
                BaseFlag = 11012300,
                BaseEntityID = 1010300,
                BaseCorpseItemLotID = 1013000,
                BaseChestItemLotID = 101300,
                BonfireCharacterID = 1010960,
                ConnectionInfo = new ConnectionList()
                {
                    (+2, true, true, new int[] { }),  // (Bell Required) Sen's Fortress door
                    ( 0, true, true, new int[] { 11012580 }),  // Titanite Demon room
                    (-1, true, true, new int[] { }),  // (Holy Sigil) Parish elevator
                    (-1, true, true, new int[] { }),  // (Rusted Key) Rat room
                    (-1, true, false, new int[] { }),  // Sunlight portcullis
                },
            },
            new Map()
            {
                Name = "PaintedWorld",
                IndexInMap = 0,
                Rating = +4,  // for high loot quality
                InMapFlag = 1803,
                BasicEnemyCount = 40,
                RareEnemyCount = 8,
                ItemCorpseCount = 20,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 11, 0, 0, 0 },
                BaseFlag = 11102000,
                BaseEntityID = 1100000,
                BaseCorpseItemLotID = 1100000,
                BaseChestItemLotID = 110000,
                BonfireCharacterID = 1100960,
                DefaultModels = new HashSet<int>() { 3420, 3421, 3422 },  // Undead Dragon (top/bottom/wing)
                DefaultBattleScriptIDs = new HashSet<int>() { 342000 },  // Undead Dragon
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    ( 0, true, false, new int[] { }),  // Arrival on bridge
                    ( 0, false, true, new int[] { 11102290 }),  // Drop after boss
                },
            },
            new Map()
            {
                Name = "DarkrootGarden",
                IndexInMap = 0,
                Rating = 0,
                InMapFlag = 1804,
                BasicEnemyCount = 60,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 12, 0, 0, 1 },
                BaseFlag = 11202000,
                BaseEntityID = 1200000,
                BaseCorpseItemLotID = 1200000,
                BaseChestItemLotID = 120000,
                BonfireCharacterID = 1200960,
                DefaultModels = new HashSet<int>() { 3230, 3530, 3531 },
                DefaultBattleScriptIDs = new HashSet<int>() { 323000, 353001, 11000 },  // Moonlight Butterfly, Hydra (Darkroot version), Hydra head
                DefaultLogicScriptIDs = new HashSet<int>() { 10000, 11000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { }),  // (Rusted Key) Watchtower door
                    ( 0, true, true, new int[] { }),  // (Butterfly Defeated) Titanite Demon room
                    (-1, true, true, new int[] { }),  // (Holy Sigil) Valley elevator
                    (30, true, true, new int[] { 11202290, 61200501 }),  // Grave of Artorias (always goes to/comes from Royal Woods or Township)
                },
            },
            new Map()
            {
                Name = "RoyalWood",
                IndexInMap = 0,
                Rating = +1,
                InMapFlag = 1805,
                BasicEnemyCount = 60,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 12, 1, 0, 0 },
                BaseFlag = 11212000,
                BaseEntityID = 1210000,
                BaseCorpseItemLotID = 1210000,
                BaseChestItemLotID = 121000,
                BonfireCharacterID = 1210960,
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { 11212290 }),  // Sanctuary tunnel
                    (-1, true, true, new int[] { 11210121, 11212280 }),  // Kalameet entrance fog (elevator reversed)
                },
            },
            new Map()
            {
                Name = "OolacileTownship",
                IndexInMap = 1,
                Rating = -1,
                InMapFlag = 1806,
                BasicEnemyCount = 30,
                RareEnemyCount = 6,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 12, 1, 0, 0 },
                BaseFlag = 11212300,
                BaseEntityID = 1210300,
                BaseCorpseItemLotID = 1213000,
                BaseChestItemLotID = 121300,
                BonfireCharacterID = 1210960,
                ConnectionInfo = new ConnectionList()
                {
                    (+2, true, true, new int[] { 11212590 }),  // Artorias arena
                    (-2, true, true, new int[] { 11210101, 11212580 }),  // Chasm hall (Township shortcut elevator reversed)
                },
            },
            new Map()
            {
                Name = "ChasmOfTheAbyss",
                IndexInMap = 2,
                Rating = -3,
                InMapFlag = 1807,
                BasicEnemyCount = 20,
                RareEnemyCount = 8,
                ItemCorpseCount = 10,
                ChestCount = 3,
                BossCount = 1,
                MapID = new int[] { 12, 1, 0, 0 },
                BaseFlag = 11212600,
                BaseEntityID = 1210600,
                BaseCorpseItemLotID = 1216000,
                BaseChestItemLotID = 121600,
                BonfireCharacterID = 1210960,
                ConnectionInfo = new ConnectionList()
                {
                    ( 0, true, false, new int[] { }),  // Prison entrance
                    ( 0, false, true, new int[] { 11212890 }),  // Boss bonfire
                },
            },
            new Map()
            {
                Name = "Catacombs",
                IndexInMap = 0,
                Rating = -1,
                InMapFlag = 1808,
                BasicEnemyCount = 40,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 13, 0, 0, 0 },
                BaseFlag = 11302000,
                BaseEntityID = 1300000,
                BaseCorpseItemLotID = 1300000,
                BaseChestItemLotID = 130000,
                BonfireCharacterID = 1300960,
                ConnectionInfo = new ConnectionList()
                {
                    // Currently only starting at top (new boss arena needed).
                    (+1, true, false, new int[] { }),  // Upper Firelink exit
                    ( 0, false, true, new int[] { }),  // Coffin
                    (-2, false, true, new int[] { 11302290, 11300900 }),  // Pinwheel ladder (top door alredy opened)
                },
            },
            new Map()
            {
                Name = "TombOfTheGiants",
                IndexInMap = 0,
                Rating = -2,
                InMapFlag = 1809,
                BasicEnemyCount = 30,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 13, 1, 0, 0 },
                BaseFlag = 11312000,
                BaseEntityID = 1310000,
                BaseCorpseItemLotID = 1310000,
                BaseChestItemLotID = 131000,
                BonfireCharacterID = 1310960,
                DefaultModels = new HashSet<int>() { 2940 },
                DefaultBattleScriptIDs = new HashSet<int>() { 294000 },  // Baby Skeleton
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, false, new int[] { }),  // Arrival from Pinwheel ladder
                    (70, false, true, new int[] { 11312290 }),  // Boss bonfire
                },
            },
            new Map()
            {
                Name = "GreatHollow",
                IndexInMap = 0,
                Rating = 1,
                InMapFlag = 1810,
                BasicEnemyCount = 20,
                RareEnemyCount = 5,
                ItemCorpseCount = 10,
                ChestCount = 3,
                BossCount = 0,
                MapID = new int[] { 13, 2, 0, 0 },
                BaseFlag = 11322000,
                BaseEntityID = 1320000,
                BaseCorpseItemLotID = 1320000,
                BaseChestItemLotID = 132000,
                BonfireCharacterID = 1320960,
                ConnectionInfo = new ConnectionList()
                {
                    (+2, true, true, new int[] { }),  // Upper exit
                    (-2, true, true, new int[] { }),  // Lower exit
                },
            },
            new Map()
            {
                Name = "AshLake",
                IndexInMap = 1,
                Rating = 1,
                InMapFlag = 1811,
                BasicEnemyCount = 20,
                RareEnemyCount = 5,
                ItemCorpseCount = 10,
                ChestCount = 3,
                BossCount = 0,
                MapID = new int[] { 13, 2, 0, 0 },
                BaseFlag = 11322300,
                BaseEntityID = 1320300,
                BaseCorpseItemLotID = 1323000,
                BaseChestItemLotID = 132300,
                BonfireCharacterID = 1320960,
                DefaultModels = new HashSet<int>() { 2711, 3450, 3451, 3530, 3531 },
                DefaultBattleScriptIDs = new HashSet<int>() { 11000, 353000, 271100 },  // Everlasting Dragon, Hydra (Lake version), and Golden Crystal Golem
                DefaultLogicScriptIDs = new HashSet<int>() { 10000, 11000 },
                ConnectionInfo = new ConnectionList()
                {
                    (0, true, true, new int[] { }),  // Hollow exit
                    (0, true, true, new int[] { }),  // Stone Dragon prompt
                },
            },
            new Map()
            {
                Name = "Blighttown",
                IndexInMap = 0,
                Rating = 1,
                InMapFlag = 1812,
                BasicEnemyCount = 50,
                RareEnemyCount = 10,
                ItemCorpseCount = 20,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 14, 0, 0, 0 },
                BaseFlag = 11402000,
                BaseEntityID = 1400000,
                BaseCorpseItemLotID = 1400000,
                BaseChestItemLotID = 140000,
                BonfireCharacterID = 1400960,
                DefaultModels = new HashSet<int>() { 3090, 5240 },
                DefaultBattleScriptIDs = new HashSet<int>() { 309000, 524000 },  // Giant Mosquito, Parasitic Wall Hugger
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+2, true, true, new int[] { }),  // Depths exit
                    (+1, true, true, new int[] { 11402280 }),  // Valley exit
                    (-1, true, true, new int[] { }),  // Great Hollow exit
                    (-2, true, true, new int[] { 11402290 }),  // Quelaag exit
                },
            },
            new Map()
            {
                Name = "DemonRuins",
                IndexInMap = 0,
                Rating = 1,
                InMapFlag = 1813,
                BasicEnemyCount = 50,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 14, 1, 0, 0 },
                BaseFlag = 11412000,
                BaseEntityID = 1410000,
                BaseCorpseItemLotID = 1410000,
                BaseChestItemLotID = 141000,
                BonfireCharacterID = 1410960,
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { 11412280 }),  // Fair Lady tunnel exit
                    ( 0, true, true, new int[] { }),  // Shortcut elevator exit
                    (-2, true, true, new int[] { 11412290 }),  // Centipede Demon exit
                    (-1, true, true, new int[] { }),  // Covenant door exit
                },
            },
            new Map()
            {
                Name = "LostIzalith",
                IndexInMap = 1,
                Rating = -2,
                InMapFlag = 1814,
                BasicEnemyCount = 30,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 14, 1, 0, 0 },
                BaseFlag = 11412300,
                BaseEntityID = 1410300,
                BaseCorpseItemLotID = 1413000,
                BaseChestItemLotID = 141300,
                BonfireCharacterID = 1410960,
                DefaultModels = new HashSet<int>() { 5230, 5400, 5401 },
                DefaultBattleScriptIDs = new HashSet<int>() { 523000, 540000, 11000 },  // Bed of Chaos (all three parts)
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+1, true, true, new int[] { 11412310 }),  // Covenant door exit (disables dome exit)
                    ( 0, true, true, new int[] { 11412300 }),  // Lava dome exit (disables door exit)
                    (70, false, true, new int[] { 11412590 }),  // Bed of Chaos boss bonfire
                },
            },
            new Map()
            {
                Name = "SensFortress",
                IndexInMap = 0,
                Rating = 1,
                InMapFlag = 1815,
                BasicEnemyCount = 40,
                RareEnemyCount = 8,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 15, 0, 0, 0 },
                BaseFlag = 11502000,
                BaseEntityID = 1500000,
                BaseCorpseItemLotID = 1500000,
                BaseChestItemLotID = 150000,
                BonfireCharacterID = 1500960,
                DefaultModels = new HashSet<int>() { 2860 },
                DefaultBattleScriptIDs = new HashSet<int>() { 286000, 286001 },  // Bomb and Boulder Giants
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    // Currently only starting at bottom (new boss arena needed).
                    (-1, true, false, new int[] { }),  // (Tarnished Key) Parish bridge
                    (+2, false, true, new int[] { 11502290 }),  // Golem arena pickup
                },
            },
            new Map()
            {
                Name = "AnorLondo",
                IndexInMap = 0,
                Rating = 2,
                InMapFlag = 1816,
                BasicEnemyCount = 55,
                RareEnemyCount = 10,
                ItemCorpseCount = 20,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 15, 1, 0, 0 },
                BaseFlag = 11512000,
                BaseEntityID = 1510000,
                BaseCorpseItemLotID = 1510000,
                BaseChestItemLotID = 151000,
                BonfireCharacterID = 1510960,
                DefaultModels = new HashSet<int>() { 5310 },
                DefaultBattleScriptIDs = new HashSet<int>() { 11000 },  // Gwynevere
                DefaultLogicScriptIDs = new HashSet<int>() { 11000 },
                ConnectionInfo = new ConnectionList()
                {
                    (-1, true, true, new int[] { 11512010 }),  // Batwing Demon ledge (disables Archives)
                    (+2, true, true, new int[] { 11512000 }),  // Archives entrance (disables Batwing)
                    (70, false, true, new int[] { 11512290 }),  // Gwynevere's room
                },
            },
            new Map()
            {
                Name = "NewLondoRuins",
                IndexInMap = 0,
                Rating = -1,  // Note that this map can appear randomly, despite being an endpoint.
                InMapFlag = 1817,
                BasicEnemyCount = 30,  // NOTE: Can't go over 50.
                RareEnemyCount = 8,  // NOTE: Can't go over 15.
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 1,
                MapID = new int[] { 16, 0, 0, 0 },
                BaseFlag = 11602000,
                BaseEntityID = 1600000,
                BaseCorpseItemLotID = 1600000,
                BaseChestItemLotID = 160000,
                BonfireCharacterID = 1600960,
                DefaultModels = new HashSet<int>() { 3420 },  // Undead Dragon (no wing/tail)
                DefaultBattleScriptIDs = new HashSet<int>() { 342002 },  // Undead Dragon (New Londo version)
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (+2, true, true, new int[] { }),  // (Holy Sigil) Darkroot elevator
                    (+1, true, true, new int[] { }),  // (Holy Sigil) Firelink elevator
                    ( 0, false, true, new int[] { }),  // Blighttown tunnel (disabled as start point because Holy Sigil drop seems unreliable)
                    (60, false, true, new int[] { 11602290 }),  // Abyss (goes to completely random map except Painted World, with a 25% chance of Chasm)
                },
            },
            new Map()
            {
                Name = "DukesArchives",
                IndexInMap = 0,
                Rating = +2,
                InMapFlag = 1818,
                BasicEnemyCount = 55,
                RareEnemyCount = 10,
                ItemCorpseCount = 15,
                ChestCount = 5,
                BossCount = 2,
                MapID = new int[] { 17, 0, 0, 0 },
                BaseFlag = 11702000,
                BaseEntityID = 1700000,
                BaseCorpseItemLotID = 1700000,
                BaseChestItemLotID = 170000,
                BonfireCharacterID = 1700960,
                DefaultModels = new HashSet<int>() { 3230 },
                DefaultBattleScriptIDs = new HashSet<int>() { 323001 },  // Moonlight Butterfly
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (-1, true, false, new int[] { }),  // Archives entrance
                    (70, false, true, new int[] { 11702290 }),  // Crystal Cave boss bonfire
                },
            },
            new Map()
            {
                Name = "KilnOfTheFirstFlame",
                IndexInMap = 0,
                Rating = +3,
                InMapFlag = 1819,
                BasicEnemyCount = 10,
                RareEnemyCount = 5,
                ItemCorpseCount = 5,
                ChestCount = 3,
                BossCount = 1,
                MapID = new int[] { 18, 0, 0, 0 },
                BaseFlag = 11802000,
                BaseEntityID = 1800000,
                BaseCorpseItemLotID = 1800000,
                BaseChestItemLotID = 180000,
                BonfireCharacterID = 1800960,
                DefaultModels = new HashSet<int>() { 2790 },
                DefaultBattleScriptIDs = new HashSet<int>() { 11000 },  // Ghost Knight
                DefaultLogicScriptIDs = new HashSet<int>() { 10000 },
                ConnectionInfo = new ConnectionList()
                {
                    (-1, true, false, new int[] { }),  // Kiln entrance
                    (70, false, true, new int[] { 11802290 }),  // Kiln boss bonfire
                },
            },
        };

        public static Map GetMap(string mapName)
        {
            IEnumerable<Map> matches = MapList.Where(map => map.Name == mapName);
            if (!matches.Any())
                throw new ArgumentException($"Invalid map name: {mapName}");
            return matches.First();
        }
    }
}
