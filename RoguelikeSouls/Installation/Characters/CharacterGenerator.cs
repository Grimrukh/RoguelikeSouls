using System.Collections.Generic;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using System;
using System.Linq;
using RoguelikeSouls.Extensions;
using ItemList = System.Collections.Generic.List<(RoguelikeSouls.Installation.ItemType Category, int ItemID, int SoulCost, int ItemFlag, int Quantity)>;

namespace RoguelikeSouls.Installation
{
    class CharacterGenerator
    {
        // TODO: SpEffects are used in EMEVD to buff allies according to the level you're in.
        public static List<Ally> AllyList = new List<Ally>()
        {
            new Ally(0)  { Name = "Alvina", OldParamID = 536100 },
            new Ally(10) { Name = "Knight Solaire", OldParamID = 6000, Equipment =
                new EquipmentSet() {
                    RightHand1 = 50000, RightHand2 = 51000,
                    LeftHand1 = 52000, LeftHand2 = -1,
                    HeadArmor = 20000, BodyArmor = 21000,
                    ArmsArmor = 22000, LegsArmor = 23000,
                    } },
            new Ally(20) { Name = "Siegmeyer of Catarina", OldParamID = 6280, Equipment =
                new EquipmentSet() {
                    RightHand1 = 53000, RightHand2 = -1,
                    LeftHand1 = 54000, LeftHand2 = -1,
                    HeadArmor = 30000, BodyArmor = 31000,
                    ArmsArmor = 32000, LegsArmor = 33000,
                    } },
            new Ally(30) { Name = "Big Hat Logan", OldParamID = 6030, Equipment =
                new EquipmentSet() {
                    RightHand1 = 55000, RightHand2 = 56000,
                    LeftHand1 = 57000, LeftHand2 = -1,
                    HeadArmor = 40000, BodyArmor = 41000,
                    ArmsArmor = 42000, LegsArmor = 43000,
                    } },
            new Ally(40) { Name = "Quelana of Izalith", OldParamID = 6170, Equipment =
                new EquipmentSet() {
                    RightHand1 = 58000, RightHand2 = -1,
                    LeftHand1 = -1, LeftHand2 = -1,
                    HeadArmor = 50000, BodyArmor = 51000,
                    ArmsArmor = 52000, LegsArmor = 53000,
                    } },
            new Ally(50) { Name = "Havel the Rock", OldParamID = 6580, Equipment =
                new EquipmentSet() {
                    RightHand1 = 59000, RightHand2 = -1,
                    LeftHand1 = 60000, LeftHand2 = -1,
                    HeadArmor = 60000, BodyArmor = 61000,
                    ArmsArmor = 62000, LegsArmor = 63000,
                    } },
            new Ally(60) { Name = "King Mornstein", OldParamID = 527000 },
            new Ally(70) { Name = "Lobos Jr", OldParamID = 452000 },
        };

        public static List<Merchant> MerchantList { get; } = new List<Merchant>()
        {
            new Merchant()
            {
                Name = "Andre of Astora",
                ModelID = 2640,
                EntityID = 6100,
                ParamID = 6100,
                OldParamID = 264000,
                EzStateOffset = 700,
                ShopLineupID = 1000,
                DefaultAnimation = 9000,
                HostileFlag = 1600,
                DeadFlag = 1601,
                DropLotItem = (ItemLotCategory.Good, 1110),  // drops Large Titanite Piece
                ShopItemList = new ItemList()
                {
                    (ItemType.Weapon, 2006000, 6, -1, -1),  // Wooden Arrow
                    (ItemType.Weapon, 2000000, 20, -1, -1),  // Standard Arrow
                    (ItemType.Weapon, 2001000, 100, -1, -1),  // Large Arrow
                    (ItemType.Weapon, 2007000, 500, -1, -1),  // Dragonslayer Arrow
                    (ItemType.Weapon, 2103000, 20, -1, -1),  // Wood Bolt
                    (ItemType.Weapon, 2100000, 60, -1, -1),  // Standard Bolt
                    (ItemType.Weapon, 2101000, 200, -1, -1),  // Heavy Bolt

                    // Three of these five sets are disabled.
                    (ItemType.Armor, 110000, 2000, 11817000, 1),
                    (ItemType.Armor, 111000, 3500, 11817010, 1),
                    (ItemType.Armor, 112000, 2000, 11817020, 1),
                    (ItemType.Armor, 113000, 2000, 11817030, 1),
                    (ItemType.Armor, 110000, 2000, 11817000, 1),
                    (ItemType.Armor, 111000, 3500, 11817010, 1),
                    (ItemType.Armor, 112000, 2000, 11817020, 1),
                    (ItemType.Armor, 113000, 2000, 11817030, 1),
                    (ItemType.Armor, 120000, 2000, 11817040, 1),
                    (ItemType.Armor, 121000, 3500, 11817050, 1),
                    (ItemType.Armor, 122000, 2000, 11817060, 1),
                    (ItemType.Armor, 123000, 2000, 11817070, 1),
                    (ItemType.Armor, 130000, 2000, 11817080, 1),
                    (ItemType.Armor, 131000, 3500, 11817090, 1),
                    (ItemType.Armor, 132000, 2000, 11817100, 1),
                    (ItemType.Armor, 133000, 2000, 11817110, 1),
                    (ItemType.Armor, 140000, 2000, 11817120, 1),
                    (ItemType.Armor, 141000, 3500, 11817130, 1),
                    (ItemType.Armor, 142000, 2000, 11817140, 1),
                    (ItemType.Armor, 143000, 2000, 11817150, 1),
                    (ItemType.Armor, 150000, 2000, 11817160, 1),
                    (ItemType.Armor, 151000, 3500, 11817170, 1),
                    (ItemType.Armor, 152000, 2000, 11817180, 1),
                    (ItemType.Armor, 153000, 2000, 11817190, 1),

                    // Embers (two random)
                    (ItemType.Good, 1000, 10000, 11817200, 1),
                    (ItemType.Good, 1010, 10000, 11817210, 1),
                    (ItemType.Good, 1020, 10000, 11817220, 1),
                    (ItemType.Good, 1030, 10000, 11817230, 1),
                    (ItemType.Good, 1040, 10000, 11817240, 1),
                    (ItemType.Good, 1050, 10000, 11817250, 1),
                    (ItemType.Good, 1060, 10000, 11817260, 1),
                    (ItemType.Good, 1070, 10000, 11817270, 1),
                    (ItemType.Good, 1080, 10000, 11817280, 1),
                    
                    // Sells up to five Motes (shared stock).
                    (ItemType.Good, 650, 2000, 11027000, 5),
                    (ItemType.Good, 651, 2000, 11027000, 5),
                    (ItemType.Good, 652, 2000, 11027000, 5),
                    (ItemType.Good, 653, 2000, 11027000, 5),
                    (ItemType.Good, 654, 2000, 11027000, 5),
                    (ItemType.Good, 655, 2000, 11027000, 5),
                    (ItemType.Good, 656, 2000, 11027000, 5),
                    (ItemType.Good, 657, 2000, 11027000, 5),

                    // Also sells small and medium titanite pieces, and repair powder.
                    (ItemType.Good, 280, 2000, -1, -1),  // Repair Powder
                    (ItemType.Good, 1100, 4000, -1, -1),  // Small Titanite Piece
                    (ItemType.Good, 1110, 8000, -1, -1),  // Large Titanite Piece
                }
            },
            new Merchant()
            {
                Name = "Vamos",
                ModelID = 2920,
                EntityID = 6110,
                ParamID = 6110,
                OldParamID = 292000,
                EzStateOffset = 701,
                ShopLineupID = 2000,
                DefaultAnimation = 9003,
                HostileFlag = 1610,
                DeadFlag = 1611,
                DropLotItem = (ItemLotCategory.Weapon, 100000),  // drops his first weapon slot
                ShopItemList = new ItemList()
                {
                    (ItemType.Weapon, 2006000, 6, -1, -1),  // Wooden Arrow
                    (ItemType.Weapon, 2000000, 20, -1, -1),  // Standard Arrow
                    (ItemType.Weapon, 2001000, 100, -1, -1),  // Large Arrow
                    (ItemType.Weapon, 2103000, 20, -1, -1),  // Wood Bolt
                    (ItemType.Weapon, 2100000, 60, -1, -1),  // Standard Bolt
                    (ItemType.Weapon, 2101000, 200, -1, -1),  // Heavy Bolt

                    // Sells three of these melee weapons (cost varies from 4000 to 8000).
                    (ItemType.Weapon, 100000, 4000, 11817400, 1),
                    (ItemType.Weapon, 101000, 4000, 11817410, 1),
                    (ItemType.Weapon, 102000, 5000, 11817420, 1),
                    (ItemType.Weapon, 103000, 5000, 11817430, 1),
                    (ItemType.Weapon, 104000, 6000, 11817440, 1),
                    (ItemType.Weapon, 105000, 6000, 11817450, 1),
                    (ItemType.Weapon, 106000, 7000, 11817460, 1),
                    (ItemType.Weapon, 107000, 7000, 11817470, 1),
                    (ItemType.Weapon, 108000, 8000, 11817480, 1),
                    (ItemType.Weapon, 109000, 8000, 11817490, 1),

                    // Sells up to five Motes (shared stock).
                    (ItemType.Good, 650, 2000, 11027010, 5),
                    (ItemType.Good, 651, 2000, 11027010, 5),
                    (ItemType.Good, 652, 2000, 11027010, 5),
                    (ItemType.Good, 653, 2000, 11027010, 5),
                    (ItemType.Good, 654, 2000, 11027010, 5),
                    (ItemType.Good, 655, 2000, 11027010, 5),
                    (ItemType.Good, 656, 2000, 11027010, 5),
                    (ItemType.Good, 657, 2000, 11027010, 5),

                    (ItemType.Good, 310, 3000, -1, -1),  // Charcoal Pine Resin

                    // Sells two of these Embers.
                    (ItemType.Good, 1000, 10000, 11817500, 1),
                    (ItemType.Good, 1010, 10000, 11817510, 1),
                    (ItemType.Good, 1020, 10000, 11817520, 1),
                    (ItemType.Good, 1030, 10000, 11817530, 1),
                    (ItemType.Good, 1040, 10000, 11817540, 1),
                    (ItemType.Good, 1050, 10000, 11817550, 1),
                    (ItemType.Good, 1060, 10000, 11817560, 1),
                    (ItemType.Good, 1070, 10000, 11817570, 1),
                    (ItemType.Good, 1080, 10000, 11817580, 1),
                }
            },
            new Merchant()
            {
                Name = "Undead Merchant",
                ModelID = 2510,
                EntityID = 6120,
                ParamID = 6120,
                OldParamID = 251001,
                EzStateOffset = 702,
                ShopLineupID = 3000,
                DefaultAnimation = 9000,
                HostileFlag = 1620,
                DeadFlag = 1621,
                DropLotItem = (ItemLotCategory.Weapon, 200000),  // drops first weapon
                ShopItemList = new ItemList()
                {
                    (ItemType.Weapon, 2006000, 6, -1, -1),  // Wooden Arrow
                    (ItemType.Weapon, 2000000, 20, -1, -1),  // Standard Arrow
                    (ItemType.Weapon, 2001000, 100, -1, -1),  // Large Arrow
                    (ItemType.Weapon, 2103000, 20, -1, -1),  // Wood Bolt
                    (ItemType.Weapon, 2100000, 60, -1, -1),  // Standard Bolt
                    (ItemType.Weapon, 2101000, 200, -1, -1),  // Heavy Bolt

                    // Sells ONE random weapon.
                    (ItemType.Weapon, 150000, 5000, 11817600, 1),  // Melee
                    (ItemType.Weapon, 160000, 5000, 11817610, 1),  // Melee
                    (ItemType.Weapon, 200000, 5000, 11817620, 1),  // Catalyst
                    (ItemType.Weapon, 217000, 5000, 11817630, 1),  // Bow
                    (ItemType.Weapon, 235000, 5000, 11817640, 1),  // Shield

                    // Sells up to three Motes (shared stock).
                    (ItemType.Good, 650, 1500, 11027020, 3),
                    (ItemType.Good, 651, 1500, 11027020, 3),
                    (ItemType.Good, 652, 1500, 11027020, 3),
                    (ItemType.Good, 653, 1500, 11027020, 3),
                    (ItemType.Good, 654, 1500, 11027020, 3),
                    (ItemType.Good, 655, 1500, 11027020, 3),
                    (ItemType.Good, 656, 1500, 11027020, 3),
                    (ItemType.Good, 657, 1500, 11027020, 3),

                    // Sells some basic curative and offensive items.
                    (ItemType.Good, 270, 600, -1, -1),  // Bloodred Moss Clump
                    (ItemType.Good, 271, 800, -1, -1),  // Purple Moss Clump
                    (ItemType.Good, 272, 1500, -1, -1),  // Blooming Purple Moss Clump
                    (ItemType.Good, 292, 300, -1, -1),  // Firebomb
                    (ItemType.Good, 296, 800, -1, -1),  // Alluring Skull
                    (ItemType.Good, 330, 1000, -1, -1),  // Homeward Bone
                    (ItemType.Good, 313, 2000, -1, -1),  // Rotten Pine Resin

                    // Sells the three basic keys after certain conditions met.
                    (ItemType.Good, 2001, 5000,  11817650, 1),  // Rusted Key
                    (ItemType.Good, 2002, 8000,  11817660, 1),  // Tarnished Key
                    (ItemType.Good, 2003, 12000, 11817670, 1),  // Polished Key
                    (ItemType.Good, 2007, 5000,  11817680, 1),  // Piercing Eye
                }
            },
            //new Merchant("Crestfallen Merchant",       0, 6130, 6130,   6250, 150625, 5300,   -1),  // don't use his leaning animation
            new Merchant()
            {
                Name = "Marvelous Chester",
                ModelID = 4090,
                EntityID = 6140,
                ParamID = 6140,
                OldParamID = 409000,
                EzStateOffset = 704,
                ShopLineupID = 4000,
                DefaultAnimation = -1,  // no leaning animation
                HostileFlag = 1640,
                DeadFlag = 1641,
                DropLotItem = (ItemLotCategory.Weapon, 300000),  // drops first Abyssal weapon
                ShopItemList = new ItemList()
                {
                    // Ammo costs twice as much from Chester.
                    (ItemType.Weapon, 2006000, 12, -1, -1),  // Wooden Arrow
                    (ItemType.Weapon, 2000000, 40, -1, -1),  // Standard Arrow
                    (ItemType.Weapon, 2001000, 200, -1, -1),  // Large Arrow
                    (ItemType.Weapon, 2008000, 1000, -1, -1),  // Gough's Greatarrow
                    (ItemType.Weapon, 2103000, 40, -1, -1),  // Wood Bolt
                    (ItemType.Weapon, 2100000, 120, -1, -1),  // Standard Bolt
                    (ItemType.Weapon, 2101000, 400, -1, -1),  // Heavy Bolt

                    // Sells three random Abyssal weapons. (They start at 300000.)
                    (ItemType.Weapon, 300000, 8000, 11817700, 1),  // Melee weapon
                    (ItemType.Weapon, 301000, 8000, 11817710, 1),  // Melee Weapon
                    (ItemType.Weapon, 302000, 8000, 11817720, 1),  // Melee Weapon
                    (ItemType.Weapon, 303000, 2000, 11817730, 1),  // Melee Weapon
                    (ItemType.Weapon, 310000, 3000, 11817750, 1),  // Catalyst
                    (ItemType.Weapon, 312000, 3000, 11817760, 1),  // Talisman
                    (ItemType.Weapon, 314000, 3000, 11817770, 1),  // Bow
                    (ItemType.Weapon, 316000, 4000, 11817780, 1),  // Crossbow
                    (ItemType.Weapon, 320000, 4000, 11817790, 1),  // Shield
                    (ItemType.Weapon, 321000, 4000, 11817790, 1),  // Shield

                    // Sells two random Abyssal armor pieces. (They start at 700000.)
                    (ItemType.Armor, 700000, 5000, 11817800, 1),
                    (ItemType.Armor, 711000, 5000, 11817810, 1),
                    (ItemType.Armor, 722000, 5000, 11817820, 1),
                    (ItemType.Armor, 733000, 2000, 11817830, 1),
                    (ItemType.Armor, 740000, 3000, 11817840, 1),

                    // Sells up to three Tomes (shared stock).
                    (ItemType.Good, 660, 10000, 11027040, 3),
                    (ItemType.Good, 661, 10000, 11027040, 3),
                    (ItemType.Good, 662, 10000, 11027040, 3),
                    (ItemType.Good, 663, 10000, 11027040, 3),
                    (ItemType.Good, 664, 10000, 11027040, 3),
                    (ItemType.Good, 665, 10000, 11027040, 3),
                    (ItemType.Good, 666, 10000, 11027040, 3),
                    (ItemType.Good, 667, 10000, 11027040, 3),

                    (ItemType.Good, 2100, 12000, 11817850, 1),  // Skeleton Key (always)
                }
            },
        };

        public static List<Invader> InvaderList { get; } = new List<Invader>()
        {
            new Invader()  // Solaire template
            {
                TemplateParamID = 6000,
                RightHand1 = "StraightSword",
                RightHand2 = "Talisman",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                SpellType = "Miracle",
                SpellCount = 2,
                TitleNames = new string[] { "Knight", "Warrior", "Soldier", "Champion", "Paladin" }
            },
            new Invader()  // Oscar template
            {
                TemplateParamID = 6020,
                RightHand1 = "StraightSword",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                TitleNames = new string[] { "Knight", "Warrior", "Soldier", "Champion", "Veteran" }
            },
            new Invader()  // Logan template
            {
                TemplateParamID = 6030,
                RightHand1 = "Catalyst",
                RightHand2 = "CurvedSword",
                ArmorWeight = "Light",
                SpellType = "Sorcery",
                SpellCount = 4,
                TitleNames = new string[] { "Wizard", "Sorcerer", "Magus", "Warlock", "Witch" }
            },
            new Invader()  // Petrus template
            {
                TemplateParamID = 6080,
                RightHand1 = "Hammer",
                RightHand2 = "Talisman",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                SpellType = "Miracle",
                SpellCount = 2,
                TitleNames = new string[] { "Cleric", "Battlemage", "Magus", "Witch" }
            },
            new Invader()  // Laurentius template
            {
                TemplateParamID = 6130,
                RightHand1 = "Flame",
                RightHand2 = "Axe",
                ArmorWeight = "Light",
                SpellType = "Pyromancy",
                SpellCount = 3,
                TitleNames = new string[] { "Pyromancer", "Warlock" }
            },
            new Invader()  // Crestfallen Merchant template
            {
                TemplateParamID = 6250,
                RightHand1 = "Greatsword",
                LeftHand1 = "Greatshield",
                ArmorWeight = "Heavy",
                TitleNames = new string[] { "Warrior", "Soldier", "Knight", "Cavalier", "Great Knight" }
            },
            new Invader()  // Siegmeyer template
            {
                TemplateParamID = 6280,
                RightHand1 = "UltraGreatsword",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                TitleNames = new string[] { "Knight", "Warrior", "Champion" }
            },
            new Invader()  // Lautrec template 
            {
                TemplateParamID = 6300,
                RightHand1 = "CurvedSword",
                LeftHand1 = "CurvedSword",
                ArmorWeight = "Heavy",
                TitleNames = new string[] { "Knight", "Butcher", "Sellsword", "Mercenary" }
            },
            new Invader()  // Patches template
            {
                TemplateParamID = 6320,
                RightHand1 = "Spear",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                TitleNames = new string[] { "Lancer", "Piker", "Bodyguard" }
            },
            new Invader()  // Patches halberd variant
            {
                TemplateParamID = 6320,
                RightHand1 = "Halberd",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                TitleNames = new string[] { "Halberdier", "Lancer", "Knight", "Footsoldier" }
            },
            new Invader()  // Havel template
            {
                TemplateParamID = 6580,
                RightHand1 = "GreatHammer",
                LeftHand1 = "Greatshield",
                ArmorWeight = "Heavy",
                TitleNames = new string[] { "Knight", "Bishop", "Vanquisher", "Conqueror" } 
            },
            new Invader()  // Ricard template
            {
                TemplateParamID = 6600,
                RightHand1 = "StraightSword",
                RightHand2 = "Bow",
                LeftHand1 = "Shield",
                ArmorWeight = "Medium",
                TitleNames = new string[] { "Knight", "Hunter", "Archer", "Ranger" } 
            },
            new Invader()  // Witch template
            {
                TemplateParamID = 6620,
                RightHand1 = "Flame",
                ArmorWeight = "Light",
                SpellType = "Pyromancy",
                SpellCount = 4,
                TitleNames = new string[] { "Witch", "Warlock", "Pyromancer", "Pyromaniac", "Firemagus" } 
            },
            new Invader()  // Ciaran template
            {
                TemplateParamID = 6740,
                RightHand2 = "Dagger",  // Note her weapons are in slot 2, as Ciaran is unarmed by default.
                LeftHand2 = "CurvedSword",
                ArmorWeight = "Light",
                TitleNames = new string[] { "Twinblade", "Stalker", "Assassin", "Mercenary" },
                UsesOffensiveGood = true,
            },
        };

        SoulsMod Mod { get; }
        Random Rand { get; }
        NPCNameGenerator NameGenerator { get; }

        const int InvaderCount = 30;
        const double NoHelmOdds = 0.2;
        const int InvaderParamOffset = 7000;
        const int InvaderNameTextOffset = 700;
        const int InvaderEventTextOffset = 7000;

        static ItemList BonfireShop { get; } = new ItemList()
        {
            // Sells up to five Motes (shared stock).
            (ItemType.Good, 650, 3000, 11027090, 5),
            (ItemType.Good, 651, 3000, 11027090, 5),
            (ItemType.Good, 652, 3000, 11027090, 5),
            (ItemType.Good, 653, 3000, 11027090, 5),
            (ItemType.Good, 654, 3000, 11027090, 5),
            (ItemType.Good, 655, 3000, 11027090, 5),
            (ItemType.Good, 656, 3000, 11027090, 5),
            (ItemType.Good, 657, 3000, 11027090, 5),
        };

        string[] CharacterStatFields { get; } = new string[] { "baseVit", "baseWil", "baseEnd", "baseStr", "baseDex", "baseMag", "baseFai", "baseLuc" };
        int[] OffensiveGoods { get; } = new int[] { 290, 291, 292, 293, 297 };

        public CharacterGenerator(SoulsMod mod, Random random)
        {
            Mod = mod;
            Rand = random;
            NameGenerator = new NPCNameGenerator(random);
        }

        public void Install()
        {
            CreateAllies();
            ModifyDebugPlayer();
            CreateMerchants();
            CreateInvaders();
            CreateBonfireShop();
        }

        void CreateAllies()
        {
            // Not actually randomized.
            foreach (Ally ally in AllyList)
                ally.CreateParams(Mod.GPARAM, Mod.VanillaGPARAM, Mod.Text);

            // Add extra Conversation entries for Alvina.
            Talk newLine = Mod.GPARAM.Talks.CopyRow(Mod.GPARAM.Talks[23010020], 23010023);
            newLine.MsgId = 23010023;
            newLine.VoiceId = 23010023;
            newLine = Mod.GPARAM.Talks.CopyRow(Mod.GPARAM.Talks[23010020], 23010024);
            newLine.MsgId = 23010024;
            newLine.VoiceId = 23010024;
        }

        void ModifyDebugPlayer()
        {
            ChrInit debugPlayer = Mod.GPARAM.ChrInits[9000];
            debugPlayer.RightHandWeapon1 = 50000;  // Sunlight Straight Sword
            debugPlayer.RightHandWeapon2 = 51000;  // Sunlight Talisman
            debugPlayer.LeftHandWeapon1 = 52000;  // Sunlight Shield
            debugPlayer.LeftHandWeapon2 = -1;
            debugPlayer.HeadArmor = 50000;  // Gold-Hemmed set
            debugPlayer.BodyArmor = 51000;  // Gold-Hemmed set
            debugPlayer.ArmsArmor = 52000;  // Gold-Hemmed set
            debugPlayer.LegsArmor = 53000;  // Gold-Hemmed set
            debugPlayer.RingSlot1 = -1;  // No rings.
            debugPlayer.RingSlot2 = -1;
            debugPlayer.SpellSlot1 = -1;
            debugPlayer.SpellSlot2 = -1;
            debugPlayer.SpellSlot3 = -1;
            debugPlayer.SpellSlot4 = -1;
            debugPlayer.SpellSlot5 = -1;
            debugPlayer.SpellSlot6 = -1;
            debugPlayer.SpellSlot7 = -1;
            debugPlayer.GoodSlot1 = 240;  // Divine Blessing
            debugPlayer.GoodSlot1Count = 50;
            debugPlayer.GoodSlot2 = -1;
            debugPlayer.GoodSlot2Count = 0;
            debugPlayer.GoodSlot3 = -1;
            debugPlayer.GoodSlot3Count = 0;
            debugPlayer.GoodSlot4 = -1;
            debugPlayer.GoodSlot4Count = 0;
            debugPlayer.GoodSlot5 = -1;
            debugPlayer.GoodSlot5Count = 0;
            debugPlayer.GoodSlot6 = -1;
            debugPlayer.GoodSlot7 = -1;
            debugPlayer.GoodSlot8 = -1;
            debugPlayer.GoodSlot9 = -1;
            debugPlayer.GoodSlot10 = -1;
            debugPlayer.ArrowSlot1 = -1;
            debugPlayer.ArrowSlot1Count = 0;
            debugPlayer.BoltSlot1 = -1;
            debugPlayer.BoltSlot1Count = 0;
            debugPlayer.Sex = 0;  // Female
        }

        void CreateMerchants()
        {
            // Characters who will randomly appear and provide services.
            // Four currently available: Andre, Vamos, Undead Merchant, Chester.
            // Randomly set flags determine which subset of their full
            // stock is available that run.

            // Nothing here is actually randomized.
            foreach (Merchant merchant in MerchantList)
                merchant.CreateParams(Mod.GPARAM, Mod.VanillaGPARAM);
        }

        void CreateBonfireShop()
        {
            Mod.GPARAM.ShopLineups.DeleteRowRange(9000, 10000);
            int shopID = 9000;
            foreach ((ItemType itemType, int itemID, int soulCost, int itemFlag, int quantity) in BonfireShop)
            {
                ShopLineup shopEntry = Mod.GPARAM.ShopLineups.AddRow(shopID);
                shopEntry.Name = $"Bonfire: {itemID}";
                shopEntry.EquipType = (byte)itemType;
                shopEntry.EventFlag = itemFlag;
                shopEntry.Value = soulCost;
                shopEntry.SellQuantity = (short)quantity;
                shopEntry.EquipId = itemID;
                shopID++;
            }
        }

        void CreateInvaders()
        {
            // Fresh set of random invaders each install, based on some templates with compatible AI.
            Mod.GPARAM.NPCs.DeleteRowRange(InvaderParamOffset, InvaderParamOffset + 10 * InvaderCount);
            Mod.GPARAM.AI.DeleteRowRange(InvaderParamOffset, InvaderParamOffset + 10 * InvaderCount);
            Mod.GPARAM.ChrInits.DeleteRowRange(InvaderParamOffset, InvaderParamOffset + 10 * InvaderCount);
            Mod.GPARAM.ItemLots.DeleteRowRange(InvaderParamOffset, InvaderParamOffset + 10 * InvaderCount);
            for (int invaderIndex = 0; invaderIndex < InvaderCount; invaderIndex++)
                CreateRandomInvader(invaderIndex);
        }

        void CreateRandomInvader(int invaderIndex)
        {
            // Weapons and armor should have already been randomized before calling this.
            Invader invader = InvaderList.GetRandomElement(Rand);

            string title = invader.TitleNames[Rand.Next(invader.TitleNames.Length)];
            string invaderName = NameGenerator.GetRandomName(title, exact: false);
            bool noHelm = Rand.NextDouble() < NoHelmOdds;
            int invaderID = InvaderParamOffset + (10 * invaderIndex);
            int invaderNameID = InvaderNameTextOffset + invaderIndex;

            Mod.GPARAM.NPCs.DeleteRow(invaderID);
            Mod.GPARAM.AI.DeleteRow(invaderID);
            Mod.GPARAM.ChrInits.DeleteRow(invaderID);
            Mod.GPARAM.ItemLots.DeleteRowRange(invaderID, invaderID + 10);

            // Add invader name and invasion messages.
            Mod.Text.NPCNames[InvaderNameTextOffset + invaderIndex] = invaderName;
            Mod.Text.EventText[InvaderEventTextOffset + 10 * invaderIndex + 0] = $"Dark spirit {invaderName} has invaded!";
            Mod.Text.EventText[InvaderEventTextOffset + 10 * invaderIndex + 1] = $"Dark spirit {invaderName} was vanquished";
            Mod.Text.EventText[InvaderEventTextOffset + 10 * invaderIndex + 2] = $"Invading the world of {invaderName}";
            Mod.Text.EventText[InvaderEventTextOffset + 10 * invaderIndex + 3] = $"Vengeance claimed upon {invaderName}";

            NPC invaderNPC = Mod.GPARAM.NPCs.CopyRow(Mod.VanillaGPARAM.NPCs[invader.TemplateParamID], invaderID);
            invaderNPC.Name = invaderName;
            invaderNPC.NameID = invaderNameID;
            invaderNPC.DrawType = 2;  // Red phantom
            invaderNPC.NPCType = 0;  // Normal
            invaderNPC.TeamType = 0;  // Enemy
            invaderNPC.ItemLotID1 = invaderID;  // not sure if invaders give Humanity automatically when killed
            invaderNPC.SpecialEffectID4 = 7001;
            invaderNPC.NewGamePlusSpecialEffect = 7401;
            for (int lot = 2; lot < 7; lot++)  // Clear remaining item lots.
                invaderNPC.Row[$"itemLotId_{lot}"].Value = -1;
            
            // Create level variants. They all have the same drop table.
            for (int level = 1; level < 10; level++)
            {
                NPC levelParam = Mod.GPARAM.NPCs.CopyRow(invaderNPC, invaderID + level);
                levelParam.Name = invaderNPC.Name + $" ({level + 1})";
                levelParam.SpecialEffectID4 = 7000 + level + 1;
                levelParam.NewGamePlusSpecialEffect = 7400 + level + 1;
            }

            NPCThought invaderAI = Mod.GPARAM.AI.CopyRow(Mod.VanillaGPARAM.AI[invader.TemplateParamID], invaderID);
            invaderAI.Name = invaderName;
            invaderAI.SightDistance = 40;
            invaderAI.HearingDistance = 0;
            invaderAI.SmellDistance = 9999;
            invaderAI.MaxRetreatDistance = 9999;
            invaderAI.BattleRetreatDistance = 9999;
            invaderAI.RetreatBattleStartDistance = 9999;
            invaderAI.BattleStartDistance = 9999;
            invaderAI.SearchGoalAction = 3;

            ChrInit invaderChr = Mod.GPARAM.ChrInits.CopyRow(Mod.VanillaGPARAM.ChrInits[invader.TemplateParamID], invaderID);
            invaderChr.Name = invaderName;
            invaderChr.NPCType = 0;  // Normal
            if (invader.UsesOffensiveGood)
            {
                int offensiveGood = OffensiveGoods.GetRandomElement(Rand);
                invaderChr.GoodSlot1 = offensiveGood;
            }  // Otherwise, leave goods as they are.
            RandomizeChrInit(invaderChr, Rand);

            List<int> itemIDs = new List<int>();
            List<ItemLotCategory> itemCategories = new List<ItemLotCategory>();

            // Assign random weapons of given types.
            if (invader.RightHand1 != "")
            {
                Weapon rightHandWeapon1 = GetRandomWeaponFromSubclass(invader.RightHand1);
                invaderChr.RightHandWeapon1 = rightHandWeapon1;
                itemIDs.Add(invaderChr.RightHandWeapon1);
                itemCategories.Add(ItemLotCategory.Weapon);
                EnsureRequiredWeaponStats(invaderChr, rightHandWeapon1);
            }
            else
            {
                invaderChr.RightHandWeapon1 = -1;
            }
            if (invader.RightHand2 != "")
            {
                Weapon rightHandWeapon2 = GetRandomWeaponFromSubclass(invader.RightHand2);
                invaderChr.RightHandWeapon2 = rightHandWeapon2;
                itemIDs.Add(invaderChr.RightHandWeapon2);
                itemCategories.Add(ItemLotCategory.Weapon);
                EnsureRequiredWeaponStats(invaderChr, rightHandWeapon2);
            }
            else
            {
                invaderChr.RightHandWeapon2 = -1;
            }
            if (invader.LeftHand1 != "")
            {
                Weapon leftHandWeapon1 = GetRandomWeaponFromSubclass(invader.LeftHand1);
                invaderChr.LeftHandWeapon1 = leftHandWeapon1;
                itemIDs.Add(invaderChr.LeftHandWeapon1);
                itemCategories.Add(ItemLotCategory.Weapon);
                EnsureRequiredWeaponStats(invaderChr, leftHandWeapon1);
            }
            else
            {
                invaderChr.LeftHandWeapon1 = -1;
            }
            if (invader.LeftHand2 != "")
            {
                Weapon leftHandWeapon2 = GetRandomWeaponFromSubclass(invader.LeftHand2);
                invaderChr.LeftHandWeapon2 = leftHandWeapon2;
                itemIDs.Add(invaderChr.LeftHandWeapon2);
                itemCategories.Add(ItemLotCategory.Weapon);
                EnsureRequiredWeaponStats(invaderChr, leftHandWeapon2);
            }
            else
            {
                invaderChr.LeftHandWeapon2 = -1;
            }

            // Assign random armor.
            if (invader.ArmorWeight != "")
            {
                int headArmorID = GetRandomHeadArmorIDFromWeight(invader.ArmorWeight);
                if (noHelm)
                {
                    invaderChr.HeadArmor = -1;
                }
                else
                {
                    invaderChr.HeadArmor = headArmorID;
                    itemIDs.Add(invaderChr.HeadArmor);
                    itemCategories.Add(ItemLotCategory.Armor);
                }

                invaderChr.BodyArmor = headArmorID + 1000;
                itemIDs.Add(invaderChr.BodyArmor);
                itemCategories.Add(ItemLotCategory.Armor);

                if (Mod.GPARAM.Armor.ContainsKey(headArmorID + 2000))
                {
                    // Arms may be missing from set.
                    invaderChr.ArmsArmor = headArmorID + 2000;
                    itemIDs.Add(invaderChr.ArmsArmor);
                    itemCategories.Add(ItemLotCategory.Armor);
                }
                else
                {
                    invaderChr.ArmsArmor = -1;
                }

                invaderChr.LegsArmor = headArmorID + 3000;
                itemIDs.Add(invaderChr.LegsArmor);
                itemCategories.Add(ItemLotCategory.Armor);
            }

            List<uint> counts = new List<uint>(Enumerable.Repeat((uint)1, itemIDs.Count));
            List<uint> chancePoints = new List<uint>(Enumerable.Repeat((uint)10, itemIDs.Count));  // 10 is arbitary

            Mod.GPARAM.ItemLots.DeleteRow(invaderID);
            Mod.GPARAM.ItemLots.DeleteRow(invaderID + 1);
            ItemLot invaderLot = Mod.GPARAM.ItemLots.AddRow(invaderID);
            invaderLot.SetItemSlots(itemCategories.ToArray(), itemIDs.ToArray(), counts.ToArray(), chancePoints.ToArray());
            invaderLot.Name = $"{invaderName} Drop";
            ItemLot humanityLot = Mod.GPARAM.ItemLots.AddRow(invaderID + 1);
            humanityLot.SetSimpleItem(ItemLotCategory.Good, 500, 1, -1);  // Guaranteed humanity drop.
            humanityLot.Name = "Humanity";
            invaderLot.Name = $"{invaderName} Drop";
        }

        void EnsureRequiredWeaponStats(ChrInit character, Weapon weapon)
        {
            character.Strength = Math.Max(character.Strength, weapon.RequiredStrength);
            character.Dexterity = Math.Max(character.Dexterity, weapon.RequiredDexterity);
            character.Intelligence = Math.Max(character.Intelligence, weapon.RequiredIntelligence);
            character.Faith = Math.Max(character.Faith, weapon.RequiredFaith);
        }

        Weapon GetRandomWeaponFromSubclass(string weaponSubclass, bool matchModel = true)
        {
            // Matches model rather than base weapon, by default, since weight is important.
            if (weaponSubclass == "Flame")
            {
                int flameId = WeaponGenerator.FixedWeapons["Pyromancy Flame"];
                return Mod.GPARAM.Weapons[flameId];
            }
            string match = matchModel ? $"<{weaponSubclass}|" : $"|{weaponSubclass}>";
            List<Weapon> options = new List<Weapon>(Mod.GPARAM.Weapons.Values.Where(w => w.Row.Name.Contains(match)));
            if (!options.Any())
                // It's possible, though unlikely, that a given model will be missing. In that case, choose anything.
                return new List<Weapon>(Mod.GPARAM.Weapons.Values).GetRandomElement(Rand);
            return options.GetRandomElement(Rand);
        }

        int GetRandomHeadArmorIDFromWeight(string armorWeight)
        {
            string match = $"<{armorWeight}|";
            List<Armor> options = new List<Armor>(Mod.GPARAM.Armor.Values.Where(a => a.ArmorType == 0 && a.Row.Name.Contains(match)));
            if (!options.Any())
                // It's possible, though unlikely, that a given armor weight will be missing. In that case, choose anything.
                return new List<Armor>(Mod.GPARAM.Armor.Values.Where(a => a.ArmorType == 0)).GetRandomElement(Rand);
            return options.GetRandomElement(Rand);
        }

        void RandomizeChrInit(ChrInit invaderChr, Random random)
        {
            // Randomizes sex and randomly adds a number in [-3, 3] interval to each stat.
            // Insufficient stats for their weapons will be fixed afterward.
            foreach (string stat in CharacterStatFields)
            {
                byte oldStat = Convert.ToByte(invaderChr.Row[stat].Value);
                invaderChr.Row[stat].Value = (byte)Math.Max(1, oldStat + random.Next(-3, 4));
            }
            invaderChr.Sex = (byte)(random.NextDouble() < 0.5 ? 0 : 1);
        }
    }
}
