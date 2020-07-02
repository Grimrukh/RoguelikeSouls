using SoulsFormatsMod;
using System;
using System.Collections.Generic;
using System.Linq;
using RoguelikeSouls.Extensions;
using SoulsFormatsMod.PARAMS;

namespace RoguelikeSouls.Installation
{
    class MapItemLotsGenerator
    {
        /* Note that I'm avoiding sampling from some giant treasure pool, so you
         * have a minor chance of learning what can appear in each map.
         *
         * Total of 300 corpse lots and 120 chest lots per map.
         * Start with 60 corpse lots and 30 chest lots unlocked.
         * Gain 40 corpse lots and 15 chest lots per unlock.
         
         * Chests are more likely to contain good stuff. Some chests in each unlock boost
         * also add keys in second slots (using 50000 lot flags).
         * 
         * Keep track of assigned (category, itemID) for equipment so it doesn't appear more than once
         * in a map.
         */

        SoulsMod Mod { get; }
        WeaponGenerator WeaponSetup { get; }
        ArmorGenerator ArmorSetup { get; }
        Random Rand { get; }
        ItemLot ItemLotTemplate { get => Mod.VanillaGPARAM.ItemLots[1000]; }

        List<(ItemLotCategory category, int itemID)> UsedItems;
        List<long> AvailableSpells;

        static List<(int keyID, int itemLotFlag)> KeyIDs { get; } = new List<(int, int)>()
        {
            ( 2001, 50050010 ),
            ( 2002, 50050020 ),
            ( 2003, 50050030 ),
            ( 2005, 50050050 ),
            ( 2006, 50050060 ),
            ( 2007, 50050070 ),
            ( 2100, 50050100 ),
        };

        public static Dictionary<GameFlag, (int rangeStart, int rangeEnd)> CorpseUnlockRanges { get; } = new Dictionary<GameFlag, (int rangeStart, int rangeEnd)>()
        {
            { GameFlag.None, (0, 60) },
            { GameFlag.LordvesselObtained, (60, 100) },
            { GameFlag.ArchivesBossDefeated, (100, 140) },
            { GameFlag.TombBossDefeated, (140, 180) },
            { GameFlag.NewLondoBossDefeated, (180, 220) },
            { GameFlag.IzalithBossDefeated, (220, 260) },
            { GameFlag.ChasmBossDefeated, (260, 300) },
        };

        public static Dictionary<GameFlag, (int rangeStart, int rangeEnd)> ChestUnlockRanges { get; } = new Dictionary<GameFlag, (int rangeStart, int rangeEnd)>()
        {
            { GameFlag.None, (0, 30) },
            { GameFlag.LordvesselObtained, (30, 45) },
            { GameFlag.ArchivesBossDefeated, (45, 60) },
            { GameFlag.TombBossDefeated, (60, 75) },
            { GameFlag.NewLondoBossDefeated, (75, 90) },
            { GameFlag.IzalithBossDefeated, (90, 105) },
            { GameFlag.ChasmBossDefeated, (105, 120) },
        };

        static Dictionary<string, List<(TreasureType type, int count)>> TreasureCorpseRanges { get; } = new Dictionary<string, List<(TreasureType, int)>>()
        {
            { "Base", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 20 ),
                ( TreasureType.CorpseRenewable, 20 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
            } },
            // All five Lordvessel/Lord Soul unlocks are identical distributions.
            { "Anor Londo", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
                ( TreasureType.LegendaryWeapon, 3 ),
                ( TreasureType.LegendaryArmor, 3 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Duke's Archives", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
                ( TreasureType.LegendaryWeapon, 3 ),
                ( TreasureType.LegendaryArmor, 3 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Tomb of the Giants", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
                ( TreasureType.LegendaryWeapon, 3 ),
                ( TreasureType.LegendaryArmor, 3 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
            { "New Londo Ruins", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
                ( TreasureType.LegendaryWeapon, 3 ),
                ( TreasureType.LegendaryArmor, 3 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Lost Izalith", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 10 ),
                ( TreasureType.BasicArmor, 10 ),
                ( TreasureType.LegendaryWeapon, 3 ),
                ( TreasureType.LegendaryArmor, 3 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Chasm of the Abyss", new List<(TreasureType, int)>()
            {
                ( TreasureType.CorpseRenewable, 10 ),
                ( TreasureType.BasicWeapon, 7 ),
                ( TreasureType.BasicArmor, 7 ),
                ( TreasureType.AbyssalWeapon, 6 ),
                ( TreasureType.AbyssalArmor, 6 ),
                ( TreasureType.Spell, 2 ),
                ( TreasureType.Ember, 1 ),
                ( TreasureType.Key, 1 ),
            } },
        };

        static Dictionary<string, List<(TreasureType, int)>> TreasureChestRanges { get; } = new Dictionary<string, List<(TreasureType, int)>>()
        {
            { "Base", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 24 ),
                ( TreasureType.Spell, 6 ),
            } },
            // All five Lordvessel/Lord Soul unlocks are identical distributions.
            { "Anor Londo", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 7 ),
                ( TreasureType.Spell, 4 ),
                ( TreasureType.Ember, 3 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Duke's Archives", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 7 ),
                ( TreasureType.Spell, 4 ),
                ( TreasureType.Ember, 3 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Tomb of the Giants", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 7 ),
                ( TreasureType.Spell, 4 ),
                ( TreasureType.Ember, 3 ),
                ( TreasureType.Key, 1 ),
            } },
            { "New Londo Ruins", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 7 ),
                ( TreasureType.Spell, 4 ),
                ( TreasureType.Ember, 3 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Lost Izalith", new List<(TreasureType, int)>()
            {
                ( TreasureType.ChestRenewable, 7 ),
                ( TreasureType.Spell, 4 ),
                ( TreasureType.Ember, 3 ),
                ( TreasureType.Key, 1 ),
            } },
            { "Chasm of the Abyss", new List<(TreasureType, int)>()
            {
                // Slightly better.
                ( TreasureType.ChestRenewable, 3 ),
                ( TreasureType.Spell, 5 ),
                ( TreasureType.Ember, 5 ),
                ( TreasureType.Key, 2 ),
            } },
        };

        public MapItemLotsGenerator(SoulsMod mod, WeaponGenerator weaponSetup, ArmorGenerator armorSetup, Random random)
        {
            Mod = mod;
            WeaponSetup = weaponSetup;
            ArmorSetup = armorSetup;
            Rand = random;
        }

        public void Install()
        {
            CreateFixedLots();
            CreateTreasureLots();
            CreateFixedEnemyLots();
        }

        void CreateFixedEnemyLots()
        {
            // Undead Dragon awards Dragonfire Ember.
            ItemLot undeadDragonLot = GetCleanItemLot(34200000);
            undeadDragonLot.SetSimpleItem(ItemLotCategory.Good, 1080, 1, -1);
            undeadDragonLot = GetCleanItemLot(34200200);
            undeadDragonLot.SetSimpleItem(ItemLotCategory.Good, 1080, 1, -1);

            // Moonlight Butterflies award Crystal Ember.
            ItemLot butterflyLot = GetCleanItemLot(32300000);  // Boss Butterfly in Darkroot Garden.
            butterflyLot.SetSimpleItem(ItemLotCategory.Good, 1000, 1, -1);
            butterflyLot = GetCleanItemLot(32300100);  // First Butterfly in Crystal Cave.
            butterflyLot.SetSimpleItem(ItemLotCategory.Good, 1000, 1, -1);
            butterflyLot = GetCleanItemLot(32300110);  // Second Butterfly in Crystal Cave.
            butterflyLot.SetSimpleItem(ItemLotCategory.Good, 1000, 1, -1);

            // Both Hydras award Piercing Eye, guaranteed (in EMEVD).
            ItemLot item = GetCleanItemLot(35300000);
            item.SetSimpleItem(ItemLotCategory.Good, 2007, 1, 50050070);
            item = GetCleanItemLot(35300100);
            item.SetSimpleItem(ItemLotCategory.Good, 2007, 1, 50050070);
            
            // Everlasting Dragon tail cut (Dragonfire Ember).
            item = GetCleanItemLot(34510000);
            item.SetSimpleItem(ItemLotCategory.Good, 1080, 1, 51320990);

            // Parasitic Wall Hugger in Blighttown.
            item = GetCleanItemLot(52400000);
            item.SetSimpleItem(ItemLotCategory.Weapon, 9000, 1, -1);  // Skull Lantern
        }

        void CreateFixedLots()
        {
            ItemLot firelinkWell;

            // Well corpse in Firelink Shrine. Get key items at first, then awards repeated Homeward Bones.
            firelinkWell = GetCleanItemLot(1020000, 5);
            firelinkWell.SetSimpleItem(ItemLotCategory.Good, 600, 1, 51020000);
            firelinkWell.Name = "Firelink Well Treasure";
            Mod.GPARAM.ItemLots[1020001].SetSimpleItem(ItemLotCategory.Good, 201, 5, 51020000);
            Mod.GPARAM.ItemLots[1020002].SetSimpleItem(ItemLotCategory.Good, 601, 1, 51020000);
            // Pick up some basic equipment on first run. These two item lot flags are never disabled.
            Mod.GPARAM.ItemLots[1020003].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Longsword"], 1, 51020001);
            Mod.GPARAM.ItemLots[1020004].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Wooden Shield"], 1, 51020001);
            // 2x Homeward Bone, available for each run.
            Mod.GPARAM.ItemLots[1020005].SetSimpleItem(ItemLotCategory.Good, 330, 2, 51020002);

            // Heart of St. Jude
            ItemLot heartLot = GetCleanItemLot(1020010);
            heartLot.SetSimpleItem(ItemLotCategory.Good, 602, 1, -1);
            heartLot.Name = "Heart of St. Jude";

            // Siegmeyer gift
            ItemLot siegmeyerGift = GetCleanItemLot(1020020, 4);
            siegmeyerGift.SetSimpleItem(ItemLotCategory.Good, 271, 3, -1);  // Purple Moss Clump
            Mod.GPARAM.ItemLots[1020021].SetSimpleItem(ItemLotCategory.Good, 272, 1, -1);  // Blooming Purple Moss Clump
            Mod.GPARAM.ItemLots[1020022].SetSimpleItem(ItemLotCategory.Good, 274, 1, -1);  // Purging Stone
            Mod.GPARAM.ItemLots[1020023].SetSimpleItem(ItemLotCategory.Good, 406, 1, -1);  // Soul of a Brave Warrior
            Mod.GPARAM.ItemLots[1020024].SetSimpleItem(ItemLotCategory.Good, 500, 1, -1);  // Humanity
            siegmeyerGift.Name = "Siegmeyer Gift";

            // Quelana gift
            ItemLot quelanaGift = GetCleanItemLot(1020030, 2);
            quelanaGift.SetSimpleItem(ItemLotCategory.Good, 4010, 1, -1);  // "Fire Orb"
            Mod.GPARAM.ItemLots[1020031].SetSimpleItem(ItemLotCategory.Good, 4100, 1, -1);  // "Combustion"
            Mod.GPARAM.ItemLots[1020032].SetSimpleItem(ItemLotCategory.Good, 4060, 1, -1);  // "Fire Whip"
            quelanaGift.Name = "Quelana Gift";

            // Mark of Death
            ItemLot markOfDeath = GetCleanItemLot(50200);
            markOfDeath.SetSimpleItem(ItemLotCategory.Good, 603, 1, -1);
            markOfDeath.Name = "Mark of Death";

            // Starting class lots (from Firelink bonfire)
            ItemLot warrior = GetCleanItemLot(1020100, 1);
            warrior.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Longsword"]);
            Mod.GPARAM.ItemLots[1020101].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Wooden Shield"]);

            ItemLot knight = GetCleanItemLot(1020110, 1);
            knight.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Broadsword"]);
            Mod.GPARAM.ItemLots[1020111].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Tower Kite Shield"]);

            ItemLot wanderer = GetCleanItemLot(1020120, 1);
            wanderer.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Scimitar"]);
            Mod.GPARAM.ItemLots[1020121].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Leather Shield"]);

            ItemLot thief = GetCleanItemLot(1020130, 2);
            thief.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Bandit's Knife"]);
            Mod.GPARAM.ItemLots[1020131].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Target Shield"]);
            Mod.GPARAM.ItemLots[1020132].SetSimpleItem(ItemLotCategory.Good, 2003, 1, 50050030);  // lot flag shared with 50030

            ItemLot barbarian = GetCleanItemLot(1020140, 2);
            barbarian.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Battle Axe"]);
            Mod.GPARAM.ItemLots[1020141].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Spider Shield"]);
            Mod.GPARAM.ItemLots[1020142].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Pyromancy Flame"]);

            ItemLot hunter = GetCleanItemLot(1020150, 3);
            hunter.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Shortsword"]);
            Mod.GPARAM.ItemLots[1020151].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Short Bow"]);
            Mod.GPARAM.ItemLots[1020152].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Large Leather Shield"]);
            Mod.GPARAM.ItemLots[1020153].SetSimpleItem(ItemLotCategory.Weapon, 2000000, 40);

            ItemLot sorcerer = GetCleanItemLot(1020160, 3);
            sorcerer.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Dagger"] + 500);  // Enchanted Dagger
            Mod.GPARAM.ItemLots[1020161].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Small Leather Shield"]);
            Mod.GPARAM.ItemLots[1020162].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Sorcerer's Catalyst"]);
            Mod.GPARAM.ItemLots[1020163].SetSimpleItem(ItemLotCategory.Good, 3000);  // "Soul Arrow"

            ItemLot cleric = GetCleanItemLot(1020170, 3);
            cleric.SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Mace"]);
            Mod.GPARAM.ItemLots[1020171].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["East-West Shield"]);
            Mod.GPARAM.ItemLots[1020172].SetSimpleItem(ItemLotCategory.Weapon, WeaponGenerator.FixedWeapons["Canvas Talisman"]);
            Mod.GPARAM.ItemLots[1020173].SetSimpleItem(ItemLotCategory.Good, 5000);  // "Heal"

            ItemLot oneLifeMode = GetCleanItemLot(1020200, 1);
            oneLifeMode.SetSimpleItem(ItemLotCategory.Good, 240, 4);  // 4x Divine Blessing
            Mod.GPARAM.ItemLots[1020201].SetSimpleItem(ItemLotCategory.Good, 603, 4);  // 4x Mark of Death
        }

        void CreateTreasureLots()
        {
            foreach (Map map in Maps.MapList)
            {
                UsedItems = new List<(ItemLotCategory category, int itemID)>();
                AvailableSpells = new List<long>(Mod.GPARAM.Magic.Keys.Where(id => 3000 <= id && id < 6000));
                
                int corpseLotID = map.BaseCorpseItemLotID;
                foreach (List<(TreasureType, int)> treasureList in TreasureCorpseRanges.Values)
                {
                    foreach ((var type, var count) in treasureList)
                    {
                        for (int i = 0; i < count; i++)
                        {
                            ItemLot corpseLot = CreateLot(type, corpseLotID, map.Rating, itemLotFlag: 50000000 + corpseLotID);
                            corpseLotID += 10;
                            corpseLot.Name = $"{map.Name} Corpse {i}";
                        }
                    }
                }

                int chestLotID = map.BaseChestItemLotID;
                int chestFlagID = 0;
                foreach (List<(TreasureType, int)> treasureList in TreasureChestRanges.Values)
                {
                    foreach ((var type, var count) in treasureList)
                    {
                        for (int i = 0; i < count; i++)
                        {
                            // Chests use standard map flags in the 4000 range (e.g. 11014003).
                            ItemLot chestLot = CreateLot(type, chestLotID, map.Rating, itemLotFlag: map.BaseFlag + 2000 + chestFlagID);
                            chestLotID += 10;
                            chestLot.Name = $"{map.Name} Chest {i}";
                            chestFlagID++;
                        }
                    }
                }
            }
        }

        ItemLot CreateLot(TreasureType type, int itemLotID, int mapRating, int itemLotFlag)
        {
            Treasure treasure;
            int itemID;
            int count;
            ItemLot lot = GetCleanItemLot(itemLotID);
            switch (type)
            {
                case TreasureType.CorpseRenewable:
                    treasure = Treasures.GetCorpseRenewable(mapRating, Rand);
                    count = Rand.Next(Math.Max(1, treasure.MaxCount - 3), treasure.MaxCount + 1);
                    lot.SetSimpleItem(treasure.Category, treasure.ItemID, count, itemLotFlag);
                    break;
                case TreasureType.ChestRenewable:
                    treasure = Treasures.GetChestRenewable(mapRating, Rand);
                    count = Rand.Next(Math.Max(1, treasure.MaxCount - 3), treasure.MaxCount + 1);
                    lot.SetSimpleItem(treasure.Category, treasure.ItemID, count, itemLotFlag);
                    break;
                case TreasureType.BasicWeapon:
                case TreasureType.LegendaryWeapon:
                case TreasureType.AbyssalWeapon:
                    do
                    {
                        itemID = GetRandomWeaponID(type, mapRating);
                    } while (UsedItems.Contains((ItemLotCategory.Weapon, itemID)));
                    lot.SetSimpleItem(ItemLotCategory.Weapon, itemID, 1, itemLotFlag);
                    UsedItems.Add((ItemLotCategory.Weapon, itemID));
                    break;
                case TreasureType.BasicArmor:
                case TreasureType.LegendaryArmor:
                case TreasureType.AbyssalArmor:
                    do
                    {
                        itemID = GetRandomArmorID(type, mapRating);
                    } while (!Mod.GPARAM.Armor.Keys.Contains(itemID) || UsedItems.Contains((ItemLotCategory.Armor, itemID)));
                    lot.SetSimpleItem(ItemLotCategory.Armor, itemID, 1, itemLotFlag);
                    UsedItems.Add((ItemLotCategory.Armor, itemID));
                    break;
                case TreasureType.Key:
                    // First lot is a corpse or chest renewable. Second lot is key, using shared flag with standard key lot.
                    CreateLot(Rand.NextDouble() < 0.3 ? TreasureType.ChestRenewable : TreasureType.CorpseRenewable, itemLotID, mapRating, itemLotFlag);
                    int keyLotFlag;
                    (itemID, keyLotFlag) = KeyIDs.GetRandomElement(Rand);
                    ItemLot extraLot = GetCleanItemLot(itemLotID + 1);
                    extraLot.SetSimpleItem(ItemLotCategory.Good, itemID, 1, keyLotFlag);
                    extraLot.Name = $"Bonus Key";
                    UsedItems.Add((ItemLotCategory.Good, itemID));
                    break;
                case TreasureType.Spell:
                    itemID = (int)AvailableSpells.GetRandomElement(Rand);
                    lot.SetSimpleItem(ItemLotCategory.Good, itemID, 1, itemLotFlag);
                    UsedItems.Add((ItemLotCategory.Good, itemID));
                    AvailableSpells.Remove(itemID);
                    break;
                default:  // Ember, etc.
                    treasure = Treasures.GetRandomReward(type, Rand);
                    count = Rand.Next(Math.Max(1, treasure.MaxCount - 3), treasure.MaxCount + 1);
                    lot.SetSimpleItem(treasure.Category, treasure.ItemID, count, itemLotFlag);
                    break;
            }
            return lot;
        }

        int GetRandomWeaponID(TreasureType weaponType, int mapRating)
        {
            double upgradeOdds;
            switch (Math.Abs(mapRating))
            {
                case 1:
                    upgradeOdds = 0.01;
                    break;
                case 2:
                    upgradeOdds = 0.05;
                    break;
                case 3:
                    upgradeOdds = 0.1;
                    break;
                case 4:
                    upgradeOdds = 0.2;
                    break;
                default:
                    upgradeOdds = 0.0;
                    break;
            }
            List<(Upgrade upgrade, double odds)> upgradeOptions = new List<(Upgrade, double)>()
            {
                ( Upgrade.Normal, upgradeOdds ),
                ( Upgrade.Crystal, upgradeOdds ),
                ( Upgrade.Lightning, upgradeOdds ),
                ( Upgrade.Refined, 0.0 ),
                ( Upgrade.Magic, upgradeOdds ),
                ( Upgrade.Enchanted, 0.0 ),
                ( Upgrade.Divine, upgradeOdds ),
                ( Upgrade.Dire, 0.0 ),
                ( Upgrade.Fire, upgradeOdds ),
                ( Upgrade.Draconic, 0.0 ),
            };
            return WeaponSetup.GetRandomWeaponID(
                generic: weaponType == TreasureType.BasicWeapon, 
                legendary: weaponType == TreasureType.LegendaryWeapon,
                abyssal: weaponType == TreasureType.AbyssalWeapon, 
                upgradeOptions.ToArray());
        }

        int GetRandomArmorID(TreasureType armorType, int mapRating)
        {
            (int upgrade, double odds)[] upgradeOptions = { (1, 0.1 * mapRating), (2, 0.05 * mapRating), (3, 0.03 * mapRating), (4, 0.01 * mapRating) };
            return ArmorSetup.GetRandomArmorID(generic: armorType == TreasureType.BasicArmor, basic: armorType == TreasureType.BasicArmor,
                legendary: armorType == TreasureType.LegendaryArmor, abyssal: armorType == TreasureType.AbyssalArmor, upgradeOptions);
        }

        ItemLot GetCleanItemLot(int itemLotID, int additionalSlots = 0)
        {
            // Return to template.
            Mod.GPARAM.ItemLots.DeleteRowRange(itemLotID, itemLotID + 10);
            for (int i = 0; i <= additionalSlots; i++)
            {
                Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, itemLotID + i);
            }
            return Mod.GPARAM.ItemLots[itemLotID];
        }
    }
}
