using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using SoulsFormats;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using ItemList = System.Collections.Generic.List<(RoguelikeSouls.Installation.ItemType Category, int ItemID, int SoulCost, int ItemFlag, int Quantity)>;

namespace RoguelikeSouls.Installation
{
    enum Label : int
    {
        Abyssal,
        Animal,
        Aquatic,
        Archer,
        Metal,
        Bug,
        Divine,
        Crystal,
        Demon,
        Dragon,
        Fire,
        Ghost,
        Giant,
        Hollow,
        Sapient,
        Infested,
        Lightning,
        Magic,
        Mimic,
        Part,  // tail, arm, etc.
        Plant,
        Poison,
        Serpent,
        Skeleton,
        Slime,
        Snow,
        Stealth,
        Stone,
        Vagrant,
        Winged,
    }

    enum ItemType
    {
        Weapon = 0,
        Armor = 1,
        Ring = 2,
        Good = 3,
        Spell = 4,  // for attunement "shop" menus
    }

    enum WeaponType
    {
        Dagger = 0,
        StraightSword = 1,
        ThrustingSword = 2,
        CurvedSword = 3,
        Axe = 4,
        Hammer = 5,
        Spear = 6,
        Halberd = 7,
        SpellTool = 8,
        Caestus = 9,
        Bow = 10,
        Crossbow = 11,
        Shield = 12,
    }

    enum WeaponMotionType
    {
        Dagger = 20,
        StraightSword = 23,
        Greatsword = 25,
        UltraGreatsword = 26,
        Estoc = 27,
        CurvedSword = 28,
        Katana = 29,
        Axe = 30,
        Greataxe = 32,
        Hammer = 33,
        GreatHammer = 35,
        Spear = 36,
        Halberd = 38,
        SpellTool = 41,
        Fists = 42,
        Bow = 44,
        Crossbow = 46,
        Greatshield = 47,
        Shield = 48,
    }

    class EquipmentSet
    {
        public int RightHand1 { get; set; }
        public int RightHand2 { get; set; }
        public int LeftHand1 { get; set; }
        public int LeftHand2 { get; set; }
        public int HeadArmor { get; set; }
        public int BodyArmor { get; set; }
        public int ArmsArmor { get; set; }
        public int LegsArmor { get; set; }

        public EquipmentSet() { }

        public void ApplyToChrInit(ChrInit chrInit)
        {
            chrInit.RightHandWeapon1 = RightHand1;
            chrInit.RightHandWeapon2 = RightHand2;
            chrInit.LeftHandWeapon1 = LeftHand1;
            chrInit.LeftHandWeapon2 = LeftHand2;
            chrInit.HeadArmor = HeadArmor;
            chrInit.BodyArmor = BodyArmor;
            chrInit.ArmsArmor = ArmsArmor;
            chrInit.LegsArmor = LegsArmor;
            // Ally spells are untouched, and can just be copied from vanilla.
        }
    }

    class ArmorStats
    {
        // Contains all the GPARAM about an armor piece.
        public string Name { get; }
        public string ArmorClass { get; }  // Head, Body, Legs, or Arms
        public int ParamId { get; }  // for Armor param
        public int ModelId { get; }
        public string NameID { get => $"{Name} ({ParamId})"; }

        public ArmorStats(string armorName, string armorClass, int paramId, int modelId)
        {
            Name = armorName;
            ArmorClass = armorClass;
            ParamId = paramId;
            ModelId = modelId;
        }

        public Armor GetArmorParam(GameParamHandler gParam)
        {
            return gParam.Armor[ParamId];  // Should never be null.
        }
    }

    class ArmorSet
    {
        public string WeightClass { get; }
        public Armor Head { get; set; }
        public Armor Body { get; set; }
        public Armor Arms { get; set; }
        public Armor Legs { get; set; }

        public int HeadParamID { get; }

        public Dictionary<string, Armor> Pieces
        {
            get => new Dictionary<string, Armor>()
                {
                    { "Head", Head },
                    { "Body", Body },
                    { "Arms", Arms },
                    { "Legs", Legs },
                };
        }

        public ArmorSet(string weightClass, int headParamId, GameParamHandler gParam)
        {
            WeightClass = weightClass;
            HeadParamID = headParamId;
            Head = gParam.Armor[headParamId];
            Body = gParam.Armor[headParamId + 1000];
            Arms = gParam.Armor.ContainsKey(headParamId + 2000) ? gParam.Armor[headParamId + 2000] : null;  // Some sets are missing Arms armor.
            Legs = gParam.Armor[headParamId + 3000];
        }
    }

    class Ally
    {
        const int AllyNameBase = 600;
        const int AllyEntityBase = 6000;
        const int AllyParamBase = 6000;
        const int AllySummonEntityBase = 6500;
        const int AllySummonParamBase = 6500;
        public string Name { get; set; }
        public int NameID { get; set; }
        public int EntityID { get; set; }
        public int ParamID { get; set; }  // for NPC, AI, and ChrInit params
        public int OldParamID { get; set; }
        public int SummonEntityID { get; set; }
        public int SummonParamID { get; set; }
        public EquipmentSet Equipment { get; set; } = null;

        public Ally(int allyIndex)
        {
            NameID = AllyNameBase + allyIndex;
            EntityID = AllyEntityBase + allyIndex;
            ParamID = AllyParamBase + allyIndex;
            SummonEntityID = AllySummonEntityBase + allyIndex;
            SummonParamID = AllySummonParamBase + allyIndex;
        }

        public void CreateParams(GameParamHandler newParams, GameParamHandler vanillaParams, TextHandler text)
        {
            text.NPCNames[NameID] = Name;
            NPC newNonSummon = CreateAllyParams(OldParamID, ParamID, newParams, vanillaParams);
            newNonSummon.DrawType = 0;  // normal appearance
            newNonSummon.SpecialEffectID7 = 0;  // no doping
            newNonSummon.DisableRespawnOnRest = true;
            NPC newSummon = CreateAllyParams(OldParamID, SummonParamID, newParams, vanillaParams);
            newSummon.DrawType = 1;  // White Phantom effect
            newSummon.SpecialEffectID7 = 7700;  // apply "doping" to summon
            newSummon.DisableRespawnOnRest = true;
        }

        NPC CreateAllyParams(int oldID, int newID, GameParamHandler newParams, GameParamHandler vanillaParams)
        {
            // Move NPC, AI, and ChrInit params to a new number (deleting existing one there first).
            newParams.NPCs.DeleteRow(newID);
            NPC newNPC = newParams.NPCs.CopyRow(vanillaParams.NPCs[oldID], newID);
            CleanNPC(newNPC);
            newParams.AI.DeleteRow(newID);
            newParams.AI.CopyRow(vanillaParams.AI[oldID], newID);
            if (oldID < 10000)
            {
                newParams.ChrInits.DeleteRow(newID);
                ChrInit allyChrInit = newParams.ChrInits.CopyRow(vanillaParams.ChrInits[oldID], newID);
                if (Equipment != null)
                    Equipment.ApplyToChrInit(allyChrInit);
            }
            return newNPC;
        }

        static void CleanNPC(NPC newNPC)
        {
            newNPC.ItemLotID1 = -1;
            newNPC.ItemLotID2 = -1;
            newNPC.ItemLotID3 = -1;
            newNPC.ItemLotID4 = -1;
            newNPC.ItemLotID5 = -1;
            newNPC.ItemLotID6 = -1;
            newNPC.TeamType = 7;  // always on White Phantom team
        }
    }

    class Merchant
    {
        public string Name { get; set; }
        public int ModelID { get; set; }
        public int EntityID { get; set; }
        public int ParamID { get; set; }
        public int OldParamID { get; set; }
        public int EzStateOffset { get; set; }
        public int ShopLineupID { get; set; }
        public int DefaultAnimation { get; set; } = -1;
        public int HostileFlag { get; set; }
        public int DeadFlag { get; set; }
        public (ItemLotCategory category, int itemID) DropLotItem { get; set; }
        public ItemList ShopItemList { get; set; }

        public Merchant() { }

        public void CreateParams(GameParamHandler newParams, GameParamHandler vanillaParams)
        {
            // Moves NPC, AI, and ChrInit params to a new number (deleting existing one there first).
            newParams.NPCs.DeleteRow(ParamID);
            NPC merchantNPC = newParams.NPCs.CopyRow(vanillaParams.NPCs[OldParamID], ParamID);
            merchantNPC.Name = Name;
            merchantNPC.TeamType = 2;  // Ally.
            merchantNPC.ItemLotID1 = ParamID;
            newParams.ItemLots.DeleteRow(ParamID);
            ItemLot merchantDrop = newParams.ItemLots.CopyRow(vanillaParams.ItemLots[1000], ParamID);
            merchantDrop.SetSimpleItem(DropLotItem.category, DropLotItem.itemID);
            newParams.AI.DeleteRow(ParamID);
            newParams.AI.CopyRow(vanillaParams.AI[OldParamID], ParamID);
            if (ModelID == 0)
            {
                newParams.ChrInits.DeleteRow(ParamID);
                newParams.ChrInits.CopyRow(vanillaParams.ChrInits[OldParamID], ParamID);
            }

            newParams.ShopLineups.DeleteRowRange(ShopLineupID, ShopLineupID + 1000);
            int shopID = ShopLineupID;
            foreach ((ItemType itemType, int itemID, int soulCost, int itemFlag, int quantity) in ShopItemList)
            {
                ShopLineup shopEntry = newParams.ShopLineups.AddRow(shopID);
                shopEntry.Name = $"{Name}: {itemID}";
                shopEntry.EquipType = (byte)itemType;
                shopEntry.EventFlag = itemFlag;
                shopEntry.Value = soulCost;
                shopEntry.SellQuantity = (short)quantity;
                shopEntry.EquipId = itemID;
                shopID++;
            }
        }

        public MSB1.Part.Enemy GetPart(GamePoint point, float angle, int talkIDBase)
        {
            return new MSB1.Part.Enemy()
            {
                Name = Name,
                ThinkParamID = ParamID,
                NPCParamID = ParamID,  // TODO: Merchant will need level if fightable.
                TalkID = talkIDBase + EzStateOffset,
                CharaInitID = -1,
                CollisionName = point.CollisionName,
                EntityID = EntityID,
                Position = point.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),  // in degrees
                ModelName = $"c{ModelID:0000}",
                DefaultStandbyAnimation = DefaultAnimation,
            };
        }
    }

    class Invader
    {
        public int TemplateParamID { get; set; }
        public string RightHand1 { get; set; } = "";
        public string RightHand2 { get; set; } = "";
        public string LeftHand1 { get; set; } = "";
        public string LeftHand2 { get; set; } = "";
        public string ArmorWeight { get; set; }
        public string SpellType { get; set; } = "";
        public int SpellCount { get; set; } = 0;
        public int OffensiveItem { get; set; } = -1;
        public string[] TitleNames { get; set; }  // options for name generation

        public Invader() { }
    }

    // Used to match bosses to compatible arenas.
    enum ArenaSize : byte
    {
        Any = 0,
        Small = 1,  // e.g. Capra Demon, Gwyndolin
        Medium = 2,  // e.g. Artorias, Crossbreed Priscilla, Iron Golem
        Large = 3,  // e.g. Gargoyles, Centipede Demon, Ornstein & Smough
        Giant = 4,  // e.g. Sif, Kalameet, Gaping Dragon
    }

    enum ChrSize : byte
    {
        // Enum value indicates minimum NearbyCount of game point for placement.
        Small = 1,
        Normal = 10,
        Giant = 20,
        Titanic = 40,
    }

    enum EnemyRarity : byte
    {
        // Value is used as probability points.
        Boss = 0,
        VeryRare = 1,  // e.g. mob versions of bosses
        Rare = 4,  // e.g. Titanite Demon, Giant Rat, Mass of Souls, Great Feline
        Uncommon = 10,  // e.g. Channeler, Berenike Knight, Bloathead Sorcerer, Chaos Eater
        Common = 20,  // most enemies
    }

    class Enemy
    {
        public string Name { get; }
        public EnemyRarity Rarity { get; }
        public int ModelID { get; }
        public int OldNPCParamID { get; }
        public int NPCParamID { get; }  // usually same as old
        public int RedPhantomNPCParamID { get => NPCParamID + 50; }
        public int AIParamID { get; }
        public uint SoulReward { get; }
        public int ItemLotParamID
        {
            get => 100 * NPCParamID;  // same for all levels
        }
        public int RedPhantomItemLotParamID
        {
            get => 100 * (NPCParamID + 50);  // same for all levels
        }
        public ChrSize Size { get; }
        public Label[] Labels { get; }

        public Enemy(string name, EnemyRarity rarity, int modelID, int oldNPCParamID, int newNPCParamID, int aiParamID, uint soulReward, ChrSize size, params Label[] labels)
        {
            Name = name;
            Rarity = rarity;
            ModelID = modelID;
            OldNPCParamID = oldNPCParamID;
            NPCParamID = newNPCParamID;
            AIParamID = aiParamID;
            SoulReward = soulReward;
            Size = size;
            Labels = labels;
        }

        public bool HasLabel(Label label)
        {
            return Labels.Contains(label);
        }

        public int GetRealNPCParamID(int level, bool isRedPhantom = false)
        {
            // Offsets NPC param ID by level and red phantom-ness.
            if (level == 0)
                throw new ArgumentException($"Minimum enemy level is 1.");
            return NPCParamID + (level - 1) + (isRedPhantom ? 50 : 0);
        }

        public MSB1.Part.Enemy GetMSBPart(string name, int entityID, GamePoint point, float angle, int level = 1, bool isRedPhantom = false)
        {
            var part = new MSB1.Part.Enemy()
            {
                Name = name,
                ThinkParamID = AIParamID,
                NPCParamID = GetRealNPCParamID(level, isRedPhantom),
                TalkID = -1,
                CharaInitID = -1,
                CollisionName = point.CollisionName,
                EntityID = entityID,
                Position = point.Position,
                Rotation = new Vector3(0.0f, angle, 0.0f),  // in degrees
                ModelName = $"c{ModelID:0000}",
            };
            part.ClearDrawGroups();
            part.ClearDispGroups();
            return part;
        }
    }

    class Boss
    {
        public string Name { get; }
        public int Category { get; }
        public int AggressionLevel { get; }
        public short NameTextID { get; }
        public ArenaSize RequiredArenaSize { get; }
        public bool AlwaysRedPhantom { get; }

        public Boss(string name, int category, int aggressionLevel, short nameTextID, ArenaSize requiredArenaSize, bool alwaysRedPhantom)
        {
            Name = name;
            Category = category;
            AggressionLevel = aggressionLevel;
            NameTextID = nameTextID;
            RequiredArenaSize = requiredArenaSize;
            AlwaysRedPhantom = alwaysRedPhantom;
        }

        public void SetName(string newName, TextHandler text)
        {
            text.NPCNames[NameTextID] = newName;
        }
    }
}
