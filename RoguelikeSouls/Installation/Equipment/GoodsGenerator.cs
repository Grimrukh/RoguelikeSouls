using SoulsFormatsMod;
using System;
using System.Collections.Generic;
using SoulsFormatsMod.PARAMS;
using RoguelikeSouls.Utils;
using RoguelikeSouls.Extensions;
using System.Linq;

namespace RoguelikeSouls.Installation
{
    enum TreasureType
    {
        None = 0,  // no reward (used in random selection)
        CommonItem = 1,  // e.g. Firebomb
        UncommonItem = 2,  // e.g. Black Firebomb
        RareItem = 3,  // e.g. Divine Blessing, Mote
        VeryRareItem = 4,  // e.g. Soul of a Hero, Tome
        BasicWeapon = 5,
        BasicArmor = 6,
        LegendaryWeapon = 7,
        LegendaryArmor = 8,
        AbyssalWeapon = 9,
        AbyssalArmor = 10,
        Spell = 11,
        Ember = 13,
        Key = 14,
        CorpseRenewable = 15,  // Common/Uncommon/Rare/VeryRare, depending on map rating
        ChestRenewable = 16,  // Common/Uncommon/Rare/VeryRare, depending on map rating
    }

    class Treasure
    {
        public string Name { get; }
        public ItemLotCategory Category;
        public int ItemID { get; }
        public TreasureType Type { get; }
        public int MaxCount { get; }
        public Label[] Labels { get; }
        
        public Treasure(string name, ItemLotCategory category, int itemID, TreasureType rewardType, int maxCount, params Label[] labels)
        {
            Name = name;
            Category = category;
            ItemID = itemID;
            Type = rewardType;
            MaxCount = maxCount;
            Labels = labels;
        }
    }

    static class Treasures
    {
        public static List<Treasure> RenewableList { get; } = new List<Treasure>()
        {
            // Rewards that can be used in multiple item lots ("renewable").
            new Treasure("Elizabeth's Mushroom",                  ItemLotCategory.Good, 230, TreasureType.RareItem, 1, Label.Divine, Label.Plant),
            new Treasure("Divine Blessing",                       ItemLotCategory.Good, 240, TreasureType.RareItem, 1, Label.Divine, Label.Sapient, Label.Mimic),
            new Treasure("Green Blossom",                         ItemLotCategory.Good, 260, TreasureType.UncommonItem, 1, Label.Plant),
            new Treasure("Bloodred Moss Clump",                   ItemLotCategory.Good, 270, TreasureType.CommonItem, 1, Label.Infested, Label.Plant),
            new Treasure("Purple Moss Clump",                     ItemLotCategory.Good, 271, TreasureType.CommonItem, 1, Label.Poison, Label.Infested, Label.Plant),
            new Treasure("Blooming Purple Moss Clump",            ItemLotCategory.Good, 272, TreasureType.UncommonItem, 1, Label.Poison, Label.Infested, Label.Plant),
            new Treasure("Purging Stone",                         ItemLotCategory.Good, 274, TreasureType.RareItem, 1, Label.Divine, Label.Stone),
            new Treasure("Egg Vermifuge",                         ItemLotCategory.Good, 275, TreasureType.RareItem, 1, Label.Bug, Label.Infested),
            new Treasure("Repair Powder",                         ItemLotCategory.Good, 280, TreasureType.RareItem, 1, Label.Metal, Label.Sapient),
            new Treasure("Throwing Knife",                        ItemLotCategory.Good, 290, TreasureType.CommonItem, 10, Label.Sapient),
            new Treasure("Poison Throwing Knife",                 ItemLotCategory.Good, 291, TreasureType.UncommonItem, 5, Label.Sapient, Label.Poison),
            new Treasure("Firebomb",                              ItemLotCategory.Good, 292, TreasureType.CommonItem, 5, Label.Sapient, Label.Fire),
            new Treasure("Dung Pie",                              ItemLotCategory.Good, 293, TreasureType.UncommonItem, 1, Label.Poison, Label.Infested),
            new Treasure("Alluring Skull",                        ItemLotCategory.Good, 294, TreasureType.UncommonItem, 1, Label.Sapient, Label.Magic),
            new Treasure("Lloyd's Talisman",                      ItemLotCategory.Good, 296, TreasureType.UncommonItem, 1, Label.Sapient, Label.Divine),
            new Treasure("Black Firebomb",                        ItemLotCategory.Good, 297, TreasureType.UncommonItem, 5, Label.Sapient, Label.Fire),
            new Treasure("Charcoal Pine Resin",                   ItemLotCategory.Good, 310, TreasureType.RareItem, 1, Label.Fire, Label.Plant),
            new Treasure("Gold Pine Resin",                       ItemLotCategory.Good, 311, TreasureType.RareItem, 1, Label.Lightning, Label.Plant),
            new Treasure("Transient Curse",                       ItemLotCategory.Good, 312, TreasureType.UncommonItem, 1, Label.Ghost),
            new Treasure("Rotten Pine Resin",                     ItemLotCategory.Good, 313, TreasureType.RareItem, 1, Label.Poison, Label.Plant),
            new Treasure("Homeward Bone",                         ItemLotCategory.Good, 330, TreasureType.UncommonItem, 1, Label.Sapient, Label.Skeleton),
            new Treasure("Prism Stone",                           ItemLotCategory.Good, 370, TreasureType.UncommonItem, 3, Label.Sapient, Label.Crystal, Label.Stone),
            new Treasure("Soul of a Lost Undead",                 ItemLotCategory.Good, 400, TreasureType.CommonItem, 1, Label.Hollow),
            new Treasure("Large Soul of a Lost Undead",           ItemLotCategory.Good, 401, TreasureType.CommonItem, 1, Label.Hollow),
            new Treasure("Soul of a Nameless Soldier",            ItemLotCategory.Good, 402, TreasureType.CommonItem, 1, Label.Hollow),
            new Treasure("Large Soul of a Nameless Soldier",      ItemLotCategory.Good, 403, TreasureType.UncommonItem, 1, Label.Hollow),
            new Treasure("Soul of a Proud Knight",                ItemLotCategory.Good, 404, TreasureType.UncommonItem, 1, Label.Hollow),
            new Treasure("Large Soul of a Proud Knight",          ItemLotCategory.Good, 405, TreasureType.UncommonItem, 1, Label.Hollow),
            new Treasure("Soul of a Brave Warrior",               ItemLotCategory.Good, 406, TreasureType.RareItem, 1, Label.Hollow),
            new Treasure("Large Soul of a Brave Warrior",         ItemLotCategory.Good, 407, TreasureType.RareItem, 1, Label.Hollow),
            new Treasure("Soul of a Hero",                        ItemLotCategory.Good, 408, TreasureType.VeryRareItem, 1, Label.Hollow),
            new Treasure("Soul of a Great Hero",                  ItemLotCategory.Good, 409, TreasureType.VeryRareItem, 1, Label.Hollow),
            new Treasure("Humanity",                              ItemLotCategory.Good, 500, TreasureType.UncommonItem, 1, Label.Abyssal, Label.Sapient),
            new Treasure("Twin Humanities",                       ItemLotCategory.Good, 501, TreasureType.RareItem, 1, Label.Abyssal, Label.Sapient),
            
            new Treasure("Mote of Vitality",                      ItemLotCategory.Good, 650, TreasureType.RareItem, 1),
            new Treasure("Mote of Attunement",                    ItemLotCategory.Good, 651, TreasureType.RareItem, 1),
            new Treasure("Mote of Endurance",                     ItemLotCategory.Good, 652, TreasureType.RareItem, 1),
            new Treasure("Mote of Strength",                      ItemLotCategory.Good, 653, TreasureType.RareItem, 1),
            new Treasure("Mote of Dexterity",                     ItemLotCategory.Good, 654, TreasureType.RareItem, 1),
            new Treasure("Mote of Resistance",                    ItemLotCategory.Good, 655, TreasureType.RareItem, 1),
            new Treasure("Mote of Intelligence",                  ItemLotCategory.Good, 656, TreasureType.RareItem, 1),
            new Treasure("Mote of Faith",                         ItemLotCategory.Good, 657, TreasureType.RareItem, 1),

            new Treasure("Tome of Vitality",                      ItemLotCategory.Good, 660, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Attunement",                    ItemLotCategory.Good, 661, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Endurance",                     ItemLotCategory.Good, 662, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Strength",                      ItemLotCategory.Good, 663, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Dexterity",                     ItemLotCategory.Good, 664, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Resistance",                    ItemLotCategory.Good, 665, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Intelligence",                  ItemLotCategory.Good, 666, TreasureType.VeryRareItem, 1),
            new Treasure("Tome of Faith",                         ItemLotCategory.Good, 667, TreasureType.VeryRareItem, 1),

            // new Treasure("Standard Arrow",                        ItemLotCategory.Weapon, 2000000, TreasureType.CommonItem, 20, Label.Sapient, Label.Archer),
            // new Treasure("Large Arrow",                           ItemLotCategory.Weapon, 2001000, TreasureType.CommonItem, 20, Label.Sapient, Label.Archer),
            new Treasure("Feather Arrow",                         ItemLotCategory.Weapon, 2002000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer),
            new Treasure("Fire Arrow",                            ItemLotCategory.Weapon, 2003000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer, Label.Poison),
            new Treasure("Poison Arrow",                          ItemLotCategory.Weapon, 2004000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer, Label.Fire),
            new Treasure("Moonlight Arrow",                       ItemLotCategory.Weapon, 2005000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer, Label.Divine),
            // new Treasure("Wooden Arrow",                          ItemLotCategory.Weapon, 2006000, TreasureType.CommonItem, 20, Label.Sapient, Label.Archer, Label.Infested),
            new Treasure("Dragonslayer Arrow",                    ItemLotCategory.Weapon, 2007000, TreasureType.RareItem, 10, Label.Sapient, Label.Archer, Label.Dragon),
            new Treasure("Gough's Great Arrow",                   ItemLotCategory.Weapon, 2008000, TreasureType.RareItem, 10, Label.Sapient, Label.Archer, Label.Dragon),

            // new Treasure("Standard Bolt",                         ItemLotCategory.Weapon, 2100000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer),
            new Treasure("Heavy Bolt",                            ItemLotCategory.Weapon, 2101000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer, Label.Metal),
            new Treasure("Sniper Bolt",                           ItemLotCategory.Weapon, 2102000, TreasureType.UncommonItem, 20, Label.Sapient, Label.Archer),
            // new Treasure("Wood Bolt",                             ItemLotCategory.Weapon, 2103000, TreasureType.CommonItem, 20, Label.Sapient, Label.Archer),
            new Treasure("Lightning Bolt",                        ItemLotCategory.Weapon, 2104000, TreasureType.RareItem, 15, Label.Sapient, Label.Archer, Label.Lightning),

            new Treasure("Refined Ember",                         ItemLotCategory.Good, 1000, TreasureType.Ember, 1, Label.Metal),
            new Treasure("Crystal Ember",                         ItemLotCategory.Good, 1010, TreasureType.Ember, 1, Label.Crystal),
            new Treasure("Magic Ember",                           ItemLotCategory.Good, 1020, TreasureType.Ember, 1, Label.Magic),
            new Treasure("Enchanted Ember",                       ItemLotCategory.Good, 1030, TreasureType.Ember, 1, Label.Magic),
            new Treasure("Lightning Ember",                       ItemLotCategory.Good, 1040, TreasureType.Ember, 1, Label.Lightning),
            new Treasure("Divine Ember",                          ItemLotCategory.Good, 1050, TreasureType.Ember, 1, Label.Divine),
            new Treasure("Dire Ember",                            ItemLotCategory.Good, 1060, TreasureType.Ember, 1, Label.Divine),
            new Treasure("Blazing Ember",                         ItemLotCategory.Good, 1070, TreasureType.Ember, 1, Label.Fire),
            new Treasure("Dragonfire Ember",                      ItemLotCategory.Good, 1080, TreasureType.Ember, 1, Label.Dragon),

            new Treasure("Small Titanite Piece",                  ItemLotCategory.Good, 1100, TreasureType.CommonItem, 1, Label.Stone, Label.Metal),
            new Treasure("Large Titanite Piece",                  ItemLotCategory.Good, 1110, TreasureType.UncommonItem, 1, Label.Stone, Label.Metal),
            new Treasure("Giant Titanite Piece",                  ItemLotCategory.Good, 1120, TreasureType.RareItem, 1, Label.Stone, Label.Metal),
            new Treasure("Colossal Titanite Piece",               ItemLotCategory.Good, 1130, TreasureType.VeryRareItem, 1, Label.Stone, Label.Metal),
        };

        public static Treasure GetCorpseRenewable(int mapRating, Random random)
        {
            double roll = random.NextDouble();
            if (roll < (0.01 * Math.Abs(mapRating)))
                return GetRandomReward(TreasureType.VeryRareItem, random);
            else if (roll < (0.05 * Math.Abs(mapRating)))
                return GetRandomReward(TreasureType.RareItem, random);
            else if (roll < (0.25 * Math.Abs(mapRating)))
                return GetRandomReward(TreasureType.UncommonItem, random);
            else
                return GetRandomReward(TreasureType.CommonItem, random);
        }

        public static Treasure GetChestRenewable(int mapRating, Random random)
        {
            double roll = random.NextDouble();
            if (roll < (0.05 * Math.Abs(mapRating)))
                return GetRandomReward(TreasureType.VeryRareItem, random);
            else if (roll < (0.3 * Math.Abs(mapRating)))
                return GetRandomReward(TreasureType.RareItem, random);
            else
                return GetRandomReward(TreasureType.UncommonItem, random);
        }

        public static Treasure GetRandomReward(TreasureType treasureType, Random random)
        {
            List<Treasure> options = new List<Treasure>(RenewableList.Where(treasure => treasure.Type == treasureType));
            return options.GetRandomElement(random);
        }

        public static Treasure GetRandomReward(TreasureType treasureType, Label[] labels, List<(ItemLotCategory, int)> usedItems, Random random)
        {
            List<Treasure> options = new List<Treasure>(RenewableList.Where(
                            treasure => treasure.Type == treasureType && treasure.Labels.Intersect(labels).Any()));
            if (!options.Any())
                // No items of this rarity for this list of labels (e.g. Demonic only). Any label is permitted.
                options = new List<Treasure>(RenewableList.Where(treasure => treasure.Type == treasureType));
            // Exclude used treasure.
            options = new List<Treasure>(options.Where(treasure => !usedItems.Contains((treasure.Category, treasure.ItemID))));
            return options.Any() ? options.GetRandomElement(random) : null;  // If all available treasure is used, no item in this slot.
        }

        public static Treasure GetRandomRewardWeightedByLabel(TreasureType type, Label[] labels, Random random)
        {
            // Returns a random "renewable" reward for an enemy drop with any of the given labels. 
            // Rewards that share more labels with the given list are proportionately 
            // more likely to be chosen.
            Dictionary<Treasure, int> weightDict = new Dictionary<Treasure, int>();
            foreach (Treasure reward in RenewableList)
            {
                IEnumerable<Label> sharedLabels = reward.Labels.Intersect(labels);
                if (reward.Type == type && sharedLabels.Any())
                    weightDict[reward] = sharedLabels.Count();
            }
            return weightDict.GetWeightedRandomElement(random);
        }
    }

    class GoodsGenerator
    {
        public static Dictionary<string, string> Summaries { get; } = new Dictionary<string, string>()
        {
            { "Hand of Cessation", "Deathly relic with nefarious intent" },
            { "Undead Flame", "Bonfire kindling spark" },
            { "Mark of Death", "Item accrued upon demise" },
            { "Heart of St. Jude", "Blazing core that forges bonds" },

            { "Refined Ember", "Weapon ascension ember" },
            { "Crystal Ember", "Weapon ascension ember" },
            { "Magic Ember", "Weapon ascension ember" },
            { "Enchanted Ember", "Weapon ascension ember" },
            { "Lightning Ember", "Weapon ascension ember" },
            { "Divine Ember", "Weapon ascension ember" },
            { "Dire Ember", "Weapon ascension ember" },
            { "Blazing Ember", "Weapon ascension ember" },
            { "Dragonfire Ember", "Weapon ascension ember" },

            { "Small Titanite Piece", "Armor upgrade material" },
            { "Large Titanite Piece", "Armor upgrade material" },
            { "Giant Titanite Piece", "Armor upgrade material" },
            { "Colossal Titanite Piece", "Armor upgrade material" },

            { "Rusted Key", "Key to old wooden doors" },
            { "Tarnished Key", "Key to reinforced doors"},
            { "Polished Key", "Key to some metal gates" },
            { "Giant Key", "Key to massive door" },
            { "Holy Sigil", "Sigil granting elevator use" },
            { "Piercing Eye", "Breaker of illusions" },
            { "Skeleton Keys", "Keys to most locks" },

            { "Mote of Vitality", "Increases vitality" },
            { "Mote of Attunement", "Increases attunement" },
            { "Mote of Endurance", "Increases endurance" },
            { "Mote of Strength", "Increases strength" },
            { "Mote of Dexterity", "Increases dexterity" },
            { "Mote of Resistance", "Increases resistance" },
            { "Mote of Intelligence", "Increases intelligence" },
            { "Mote of Faith", "Increases faith" },

            { "Tome of Vitality", "Greatly increases vitality" },
            { "Tome of Attunement", "Greatly increases attunement" },
            { "Tome of Endurance", "Greatly increases endurance" },
            { "Tome of Strength", "Greatly increases strength" },
            { "Tome of Dexterity", "Greatly increases dexterity" },
            { "Tome of Resistance", "Greatly increases resistance" },
            { "Tome of Intelligence", "Greatly increases intelligence" },
            { "Tome of Faith", "Greatly increases faith" },
        };

        public static Dictionary<string, string> Descriptions { get; } = new Dictionary<string, string>()
        {
            { "Hand of Cessation", "Part of a gnarled limb of some eldritch creature. The fingers seem to curl, one by one, whenever its Undead bearer faces death in Lordran. " +
                "Crush them together manually to return to Firelink Shrine prematurely." },
            { "Undead Flame", "Undying spark of fire, not unlike the ring of the Darksign. Use to create a bonfire in Lordran, but be wary that " +
                "only one bonfire can be kindled in each area." },
            { "Mark of Death", "Unsettling sentient eye that appears in one's inventory upon death. Only the light of Firelink Shrine seems to scare these ethereal beings away." },
            { "Heart of St. Jude", "Burning flame at the heart of all comradery. It is said that by staring into the flames, one may glimpse a future where " +
                "no one ever need be alone. Unleash it to permanently increase enemy difficulty." },

            { "Refined Ember", "One of the ancient smithing embers. Use it to refine the edge or heft of any basic weapon, which provides a modest " +
                "increase in attack power." },
            { "Crystal Ember", "One of the ancient smithing embers. Use it to refine the edge or heft of any basic weapon with solid crystal, which provides a sharp increase " +
                "in damage at the cost of durability. Crystal weapons cannot be repaired." },
            { "Magic Ember", "One of the ancient smithing embers. Use it to imbue a weapon with magical power, which increases magic damage." },
            { "Enchanted Ember", "One of the ancient smithing embers. Use it to imbue a weapon with a sorcerous hunger that modestly increases magic damage and recharges " +
                "spells when enemies are struck." },
            { "Lightning Ember", "One of the ancient smithing embers. Use it to imbue a weapon with thunderous might, which is particularly damaging to armored foes " +
                "and moderately effective against dragons." },
            { "Divine Ember", "One of the ancient smithing embers. Use it to imbue a weapon with divine power, which increases holy magical damage and is particularly " +
                "effective against the reanimated dead." },
            { "Dire Ember", "One of the ancient smithing embers, thought lost to time. Use it to imbue a weapon with a piece of one's own mortality, which provides an increase in damage " +
                "that is proportional to one's proximity to their final demise." },
            { "Blazing Ember", "One of the ancient smithing embers. Use it to imbue a weapon with a scorching heat that can burn unarmored " +
                "foes to a crisp." },
            { "Dragonfire Ember", "One of the ancient smithing embers, thought lost to time. Use it to imbue a weapon with the incredible heat of draconic fire, which deals " +
                "lasting damage to struck foes and can melt clean through dragon scales. Be wary of wielding such a flame." },

            { "Small Titanite Piece", "A small piece of broken titanite, which can be used for slight armor reinforcement." },
            { "Large Titanite Piece", "A large piece of broken titanite, which can be used for moderate armor reinforcement." },
            { "Giant Titanite Piece", "A giant piece of broken titanite, which can be used for great armor reinforcement." },
            { "Colossal Titanite Piece", "A slab of nearly flawless titanite, which can be used for extreme armor reinforcement." },

            { "Rusted Key", "Simple key, poorly maintained and eventually discarded. Can open basic locks on some older wooden doors." },
            { "Tarnished Key", "Simple key beginning to show many signs of age. Can open locks on some newer wooden doors. "},
            { "Polished Key", "Simple key with a few scrape marks. Can open locks on some metal gates." },
            { "Giant Key", "Large key to the massive door in the Depths, and perhaps others." },
            { "Holy Sigil", "Sacred stone sigil required for the use of many elevators in Lordran." },
            { "Piercing Eye", "Unsettling blue orb. Allows its holder to break through some illusions." },
            { "Skeleton Keys", "Ring with multiple keys, which together can open most doors in Lordran." },

            { "Mote of Vitality", "Wooden carving. For some reason, gnawing on it grants a small increase in vitality, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Attunement", "Wooden carving. For some reason, gnawing on it grants a small increase in attunement, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Endurance", "Wooden carving. For some reason, gnawing on it grants a small increase in endurance, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Strength", "Wooden carving. For some reason, gnawing on it grants a small increase in strength, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Dexterity", "Wooden carving. For some reason, gnawing on it grants a small increase in dexterity, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Resistance", "Wooden carving. For some reason, gnawing on it grants a small increase in resistance, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Intelligence", "Wooden carving. For some reason, gnawing on it grants a small increase in intelligence, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Mote of Faith", "Wooden carving. For some reason, gnawing on it grants a small increase in faith, though " +
                "this boon is lost upon returning to Firelink Shrine." },

            { "Tome of Vitality", "Page from an old book. Can impart power that grants a large increase in vitality, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Attunement", "Page from an old book. Can impart power that grants a large increase in attunement, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Endurance", "Page from an old book. Can impart power that grants a large increase in endurance, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Strength", "Page from an old book. Can impart power that grants a large increase in strength, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Dexterity", "Page from an old book. Can impart power that grants a large increase in dexterity, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Resistance", "Page from an old book. Can impart power that grants a large increase in resistance, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Intelligence", "Page from an old book. Can impart power that grants a large increase in intelligence, though " +
                "this boon is lost upon returning to Firelink Shrine." },
            { "Tome of Faith", "Page from an old book. Can impart power that grants a large increase in faith, though " +
                "this boon is lost upon returning to Firelink Shrine." },

            { "Alvina's Ring", "Ring marking friendship with the mysterious Alvina. Slows the decay of the Hand of Cessation, " +
                "increasing the number of Undead lives outside Firelink Shrine from five to nine." },
            { "Solaire's Ring", "Ring marking friendship with the jolly Solaire. Allows its wearer to move a bonfire after " +
                "placing it, though only once in each region." },
            { "Siegmeyer's Ring", "Ring marking friendship with the relentless Siegmeyer. Bestows a care package of sorts " +
                "upon its wearer when they venture out from Firelink Shrine. Has no other effect, except to remind one of " +
                "the joys of stoic companionship." },
            { "Logan's Ring", "Ring marking friendship wtih the inquistive Logan. Increases the occurrence of portals to the " +
                "Abyss, which should not be entered lightly." },
            { "Quelana's Ring", "Ring marking friendship with the ancient Quelana. Grants two pyromancies to its wearer " +
                "when their journey begins and provides some resistance against lava." },
            { "Havel's Ring", "Ring marking friendship with the indomitable Havel. Greatly increases its wearer's maximum equip " +
                "load, making for easier travels." },
            { "Mornstein's Ring", "Ring marking friendship with Mornstein, King of Leonia and fearless warrior. Increases the " +
                "chances of encountering powerful enemies, whose defeat can lead to superior treasure." },
            { "Lobos Jr's Ring", "Ring marking friendship with Lobos Jr, eternal ally of adventurers. Its wearer will find " +
                "their journey through Lordran longer and more arduous, but more rewarding." },
        };

        public static Dictionary<string, ushort> Icons = new Dictionary<string, ushort>()
        {
            { "White Sign Soapstone", 2000 },
            { "Red Sign Soapstone", 2001 },
            { "Red Eye Orb", 2002 },
            { "Black Separation Crystal", 2003 },
            { "Orange Guidance Soapstone", 2082 },
            { "Book of the Guilty", 2009 },
            { "Eye of Death", 2087 },
            { "Cracked Red Eye Orb", 2006 },
            { "Servant Roster", 2007 },
            { "Blue Eye Orb", 2010 },
            { "Dragon Eye", 2011 },
            { "Black Eye Orb", 2132 },
            { "Darksign", 2145 },
            { "Purple Coward's Crystal", 2148 },
            { "Estus Flask Empty", 2004 },
            { "Estus Flask", 2005 },
            { "Silver Pendant", 2157 },
            { "Elizabeth's Mushroom", 2158 },
            { "Divine Blessing", 2012 },
            { "Green Blossom", 2014 },
            { "Bloodred Moss Clump", 2015 },
            { "Purple Moss Clump", 2016 },
            { "Blooming Purple Moss Clump", 2017 },
            { "Purging Stone", 2019 },
            { "Egg Vermifuge", 2013 },
            { "Repair Powder", 2020 },
            { "Throwing Knife", 2021 },
            { "Poison Throwing Knife", 2022 },
            { "Firebomb", 2023 },
            { "Dung Pie", 2024 },
            { "Alluring Skull", 2025 },
            { "Lloyd's Talisman", 2027 },
            { "Black Firebomb", 2026 },
            { "Charcoal Pine Resin", 2028 },
            { "Gold Pine Resin", 2029 },
            { "Transient Curse", 2030 },
            { "Rotten Pine Resin", 2031 },
            { "Homeward Bone", 2034 },
            { "Prism Stone", 2042 },
            { "Binoculars", 2043 },
            { "Indictment", 2041 },
            { "Souvenir of Reprisal", 2032 },
            { "Sunlight Medal", 2035 },
            { "Pendant", 2037 },
            { "Dragon Head Stone", 2121 },
            { "Dragon Torso Stone", 2122 },
            { "Rubbish", 2038 },
            { "Copper Coin", 2039 },
            { "Silver Coin", 2040 },
            { "Gold Coin", 2055 },
            { "Peculiar Doll", 2146 },
            { "Dried Finger", 2129 },
            { "Fire Keeper Soul", 2086 },
            { "Soul of a Lost Undead", 2045 },
            { "Large Soul of a Lost Undead", 2046 },
            { "Soul of a Nameless Soldier", 2047 },
            { "Large Soul of a Nameless Soldier", 2048 },
            { "Soul of a Proud Knight", 2049 },
            { "Large Soul of a Proud Knight", 2050 },
            { "Soul of a Brave Warrior", 2051 },
            { "Large Soul of a Brave Warrior", 2052 },
            { "Soul of a Hero", 2053 },
            { "Soul of a Great Hero", 2054 },
            { "Humanity", 2112 },
            { "Twin Humanities", 2113 },
            { "Hello Carving", 2149 },
            { "Thank you Carving", 2150 },
            { "Very good! Carving", 2151 },
            { "I'm sorry Carving", 2152 },
            { "Help me! Carving", 2153 },
            { "Soul of Quelaag", 2114 },
            { "Soul of Sif", 2115 },
            { "Soul of Gwyn, Lord of Cinder", 2116 },
            { "Core of an Iron Golem", 2117 },
            { "Soul of Ornstein", 2118 },
            { "Soul of the Moonlight Butterfly", 2119 },
            { "Soul of Smough", 2120 },
            { "Soul of Priscilla", 2133 },
            { "Soul of Gwyndolin", 2134 },
            { "Guardian Soul", 2154 },
            { "Soul of Artorias", 2155 },
            { "Soul of Manus", 2156 },

            { "Large Ember", 2109 },
            { "Very Large Ember", 2070 },
            { "Crystal Large Ember", 2071 },
            { "Large Magic Ember", 2073 },
            { "Enchanted Ember", 2074 },
            { "Divine Ember", 2110 },
            { "Large Divine Ember", 2075 },
            { "Dark Ember", 2076 },
            { "Large Flame Ember", 2077 },
            { "Chaos Flame Ember", 2078 },

            { "Titanite Shard", 2090 },
            { "Large Titanite Shard", 2091 },
            { "Green Titanite Shard", 2092 },
            { "Titanite Chunk", 2093 },
            { "Blue Titanite Chunk", 2094 },
            { "White Titanite Chunk", 2095 },
            { "Red Titanite Chunk", 2096 },
            { "Titanite Slab", 2097 },
            { "Blue Titanite Slab", 2098 },
            { "White Titanite Slab", 2099 },
            { "Red Titanite Slab", 2100 },
            { "Dragon Scale", 2111 },
            { "Demon Titanite", 2036 },
            { "Twinkling Titanite", 2123 },

            { "Basement Key", 2135 },
            { "Crest of Artorias", 2136 },
            { "Cage Key", 2137 },
            { "Archive Tower Cell Key", 2138 },
            { "Archive Tower Giant Door Key", 2139 },
            { "Archive Tower Giant Cell Key", 2140 },
            { "Blighttown Key", 2141 },
            { "Key to New Londo Ruins", 2061 },
            { "Annex Key", 2062 },
            { "Dungeon Cell Key", 2079 },
            { "Big Pilgrim's Key", 2080 },
            { "Undead Asylum F2 East Key", 2081 },
            { "Key to the Seal", 2102 },
            { "Key to Depths", 2103 },
            { "Lift Chamber Key", 2104 },
            { "Undead Asylum F2 West Key", 2105 },
            { "Mystery Key", 2106 },
            { "Sewer Chamber Key", 2124 },
            { "Watchtower Basement Key", 2125 },
            { "Archive Prison Extra Key", 2126 },
            { "Residence Key", 2127 },
            { "Crest Key", 2128 },
            { "Master Key", 2142 },
            { "Lord Soul", 2056 },
            { "Bequeathed Lord Soul Shard", 2058 },
            { "None", 2060 },
            { "Lordvessel", 2085 },
            { "Broken Pendant", 2147 },
            { "Weapon Smithbox", 2063 },
            { "Armor Smithbox", 2064 },
            { "Repairbox", 2065 },
            { "Rite of Kindling", 2084 },
            { "Bottomless Box", 2088 },
        };

        SoulsMod Mod { get; }
        Good SystemItemTemplate { get => Mod.VanillaGPARAM.Goods[117]; }  // Darksign
        Good MarkerItemTemplate { get => Mod.VanillaGPARAM.Goods[2012]; }  // Key
        Good ConsumableTemplate { get => Mod.VanillaGPARAM.Goods[260]; }  // Green Blossom
        Good ReinforcementTemplate { get => Mod.VanillaGPARAM.Goods[1000]; }  // Titanite Shard
        Good KeyItemTemplate { get => Mod.VanillaGPARAM.Goods[2001]; }  // Basement Key
        Accessory RingTemplate { get => Mod.VanillaGPARAM.Rings[100]; }  // Havel's Ring
        ItemLot ItemLotTemplate { get => Mod.VanillaGPARAM.ItemLots[1000]; }  // Solaire's Soapstone gift

        public GoodsGenerator(SoulsMod mod)
        {
            // No randomization involved.
            Mod = mod;
        }

        public void Install()
        {
            ModifyObjActs();
            CreateGoods();
            CreateUniqueItemLots();
            CreateRings();
            ModifyObjects();
        }

        void ModifyObjActs()
        {
            // Forgot to change Parish cell lock.
            Mod.GPARAM.ObjActs[1308].SpQualifiedId = 2003;  // Polished Key
        }

        void ModifyObjects()
        {
            // Give chests 200 HP, so they can be destroyed if necessary. Also disable deflection on them.
            // (I assume their ObjAct event won't work if they're destroyed, which is fine. Not sure about
            // attached treasure events.)
            Mod.GPARAM.Objects[110].ObjectHP = 200;
            Mod.GPARAM.Objects[110].DeflectsAttacks = false;
        }

        void CreateRings()
        {
            // No better place to put this. They're basically goods.
            // Only wearing Quelana's and Havel's rings actually does anything.
            CreateRing(100, "Alvina's Ring", 1, 4041, 8800);
            CreateRing(101, "Solaire's Ring", 2, 4011, 8801);
            CreateRing(102, "Siegmeyer's Ring", 3, 4020, 8802);
            CreateRing(103, "Logan's Ring", 4, 4008, 8803);
            CreateRing(104, "Quelana's Ring", 5, 4003, 8804);
            CreateRing(105, "Havel's Ring", 6, 4000, 8805);
            CreateRing(106, "Mornstein's Ring", 7, 4031, 8806);
            CreateRing(107, "Lobos Jr's Ring", 8, 4035, 8807);
        }

        Accessory CreateRing(int ringID, string ringName, int sortIndex, ushort iconID, int spEffect)
        {
            Mod.GPARAM.Rings.DeleteRow(ringID);
            Accessory newRing = Mod.GPARAM.Rings.CopyRow(RingTemplate, ringID);
            newRing.Name = ringName;
            if (!Descriptions.ContainsKey(ringName))
                throw new Exception($"No description for ring {ringName}.");
            newRing.Summary = "Ring symbolizing an unbreakable friendship";
            newRing.Description = string.Join("\n", WordWrapper.WordWrap(Descriptions[ringName], 39));
            newRing.SortIndex = sortIndex;
            newRing.MenuIcon = iconID;
            newRing.SpecialEffect = spEffect;
            return newRing;
        }

        void CreateUniqueItemLots()
        {
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50010);
            Mod.GPARAM.ItemLots[50010].SetSimpleItem(ItemLotCategory.Good, 2001, 1, 50050010);
            Mod.GPARAM.ItemLots[50010].Name = "Rusted Key";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50020);
            Mod.GPARAM.ItemLots[50020].SetSimpleItem(ItemLotCategory.Good, 2002, 1, 50050020);
            Mod.GPARAM.ItemLots[50020].Name = "Tarnished Key";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50030);
            Mod.GPARAM.ItemLots[50030].SetSimpleItem(ItemLotCategory.Good, 2003, 1, 50050030);
            Mod.GPARAM.ItemLots[50030].Name = "Polished Key";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50050);
            Mod.GPARAM.ItemLots[50050].SetSimpleItem(ItemLotCategory.Good, 2005, 1, 50050050);
            Mod.GPARAM.ItemLots[50050].Name = "Giant Key";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50060);
            Mod.GPARAM.ItemLots[50060].SetSimpleItem(ItemLotCategory.Good, 2006, 1, 50050060);
            Mod.GPARAM.ItemLots[50060].Name = "Holy Sigil";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50070);
            Mod.GPARAM.ItemLots[50070].SetSimpleItem(ItemLotCategory.Good, 2007, 1, 50050070);
            Mod.GPARAM.ItemLots[50070].Name = "Piercing Eye";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 50100);
            Mod.GPARAM.ItemLots[50100].SetSimpleItem(ItemLotCategory.Good, 2100, 1, 50050100);
            Mod.GPARAM.ItemLots[50100].Name = "Skeleton Keys";

            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51000);
            Mod.GPARAM.ItemLots[51000].SetSimpleItem(ItemLotCategory.Ring, 100, 1, 50051000);
            Mod.GPARAM.ItemLots[51000].Name = "Alvina's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51010);
            Mod.GPARAM.ItemLots[51010].SetSimpleItem(ItemLotCategory.Ring, 101, 1, 50051010);
            Mod.GPARAM.ItemLots[51010].Name = "Solaire's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51020);
            Mod.GPARAM.ItemLots[51020].SetSimpleItem(ItemLotCategory.Ring, 102, 1, 50051020);
            Mod.GPARAM.ItemLots[51020].Name = "Siegmeyer's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51030);
            Mod.GPARAM.ItemLots[51030].SetSimpleItem(ItemLotCategory.Ring, 103, 1, 50051030);
            Mod.GPARAM.ItemLots[51030].Name = "Logan's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51040);
            Mod.GPARAM.ItemLots[51040].SetSimpleItem(ItemLotCategory.Ring, 104, 1, 50051040);
            Mod.GPARAM.ItemLots[51040].Name = "Quelana's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51050);
            Mod.GPARAM.ItemLots[51050].SetSimpleItem(ItemLotCategory.Ring, 105, 1, 50051050);
            Mod.GPARAM.ItemLots[51050].Name = "Havel's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51060);
            Mod.GPARAM.ItemLots[51060].SetSimpleItem(ItemLotCategory.Ring, 106, 1, 50051060);
            Mod.GPARAM.ItemLots[51060].Name = "Mornstein's Ring";
            Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, 51070);
            Mod.GPARAM.ItemLots[51070].SetSimpleItem(ItemLotCategory.Ring, 107, 1, 50051070);
            Mod.GPARAM.ItemLots[51070].Name = "LobosJr's Ring";
        }

        void CreateGoods()
        {
            // Consumables are all largely the same.
            CreateReinforcementGoods();
            CreateKeys();
        }

        void CreateKeys()
        {
            Good hand = CreateGood(600, "Hand of Cessation", 3, Icons["Dried Finger"], SystemItemTemplate);
            hand.RefID = 8898;
            hand.ConfirmationMessage = 80008;

            Good flame = CreateGood(601, "Undead Flame", 4, Icons["Rite of Kindling"], SystemItemTemplate);
            flame.RefID = 8899;
            flame.ConfirmationMessage = 80033;
            flame.AutomaticallyEquipped = true;

            Good endGame = CreateGood(602, "Heart of St. Jude", 5, Icons["Soul of Gwyn, Lord of Cinder"], SystemItemTemplate);
            endGame.RefID = 8897;
            endGame.ConfirmationMessage = 80034;
            endGame.ConsumedOnUse = true;

            Good markOfDeath = CreateGood(603, "Mark of Death", 9999, Icons["Eye of Death"], MarkerItemTemplate);
            markOfDeath.GoodType = 0;
            markOfDeath.UseableByHumans = false;
            markOfDeath.UseableByHollows = false;
            markOfDeath.MaxHoldQuantity = 99;

            Good mote;
            mote = CreateGood(650, "Mote of Vitality", 60, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8901;
            mote.LimitCategory = 0;
            mote = CreateGood(651, "Mote of Attunement", 61, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8911;
            mote.LimitCategory = 0;
            mote = CreateGood(652, "Mote of Endurance", 62, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8921;
            mote.LimitCategory = 0;
            mote = CreateGood(653, "Mote of Strength", 63, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8931;
            mote.LimitCategory = 0;
            mote = CreateGood(654, "Mote of Dexterity", 64, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8941;
            mote.LimitCategory = 0;
            mote = CreateGood(655, "Mote of Resistance", 65, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8951;
            mote.LimitCategory = 0;
            mote = CreateGood(656, "Mote of Intelligence", 66, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8961;
            mote.LimitCategory = 0;
            mote = CreateGood(657, "Mote of Faith", 67, Icons["Very good! Carving"], ConsumableTemplate);
            mote.RefID = 8971;
            mote.LimitCategory = 0;

            Good tome;
            tome = CreateGood(660, "Tome of Vitality", 68, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8904;
            tome.LimitCategory = 0;
            tome = CreateGood(661, "Tome of Attunement", 69, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8914;
            tome.LimitCategory = 0;
            tome = CreateGood(662, "Tome of Endurance", 70, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8924;
            tome.LimitCategory = 0;
            tome = CreateGood(663, "Tome of Strength", 71, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8934;
            tome.LimitCategory = 0;
            tome = CreateGood(664, "Tome of Dexterity", 72, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8944;
            tome.LimitCategory = 0;
            tome = CreateGood(665, "Tome of Resistance", 73, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8954;
            tome.LimitCategory = 0;
            tome = CreateGood(666, "Tome of Intelligence", 74, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8964;
            tome.LimitCategory = 0;
            tome = CreateGood(667, "Tome of Faith", 75, Icons["Servant Roster"], ConsumableTemplate);
            tome.RefID = 8974;
            tome.LimitCategory = 0;

            // CreateGood(384, "Peculiar Doll", 4030, Icons["Peculiar Doll"], KeyItemTemplate);  // the Painting will always appear
            Good key;
            key = CreateGood(2001, "Rusted Key", 4021, Icons["Watchtower Basement Key"], KeyItemTemplate);  // unlocks basic wooden doors
            key.IsUnique = true;
            key = CreateGood(2002, "Tarnished Key", 4022, Icons["Key to Depths"], KeyItemTemplate);  // unlocks reinforced wooden doors (e.g. Depths)
            key.IsUnique = true;
            key = CreateGood(2003, "Polished Key", 4023, Icons["Basement Key"], KeyItemTemplate);  // unlocks basic metal gates
            key.IsUnique = true;
            // CreateGood(2004, "Mechanism Key", 4024, Icons["Crest Key"], KeyItemTemplate);  // allows use of most levers/mechanisms
            key = CreateGood(2005, "Giant Key", 4025, Icons["Blighttown Key"], KeyItemTemplate);  // unlocks a few giant doors
            key.IsUnique = true;
            key = CreateGood(2006, "Holy Sigil", 4026, Icons["Crest of Artorias"], KeyItemTemplate);  // allows use of most button-triggered elevators and Darkroot door
            key.IsUnique = true;
            key = CreateGood(2007, "Piercing Eye", 4027, Icons["Blue Eye Orb"], KeyItemTemplate);  // allows one to break illusory walls
            key.IsUnique = true;
            // CreateGood(2008, "Palace Key", 4028, Icons["Big Pilgrim's Key"], KeyItemTemplate);  // allows one to break illusory walls
            key = CreateGood(2100, "Skeleton Keys", 4029, Icons["Master Key"], KeyItemTemplate);
            key.IsUnique = true;
        }

        void CreateReinforcementGoods()
        {
            // Create reinforcement materials: nine Embers and three Titanite types for armor reinforcement.
            CreateGood(1000, "Refined Ember", 1000, Icons["Large Ember"], ReinforcementTemplate);
            CreateGood(1010, "Crystal Ember", 1001, Icons["Crystal Large Ember"], ReinforcementTemplate);
            CreateGood(1020, "Magic Ember", 1002, Icons["Large Magic Ember"], ReinforcementTemplate);
            CreateGood(1030, "Enchanted Ember", 1003, Icons["Enchanted Ember"], ReinforcementTemplate);
            CreateGood(1040, "Lightning Ember", 1004, Icons["Very Large Ember"], ReinforcementTemplate);
            CreateGood(1050, "Divine Ember", 1005, Icons["Large Divine Ember"], ReinforcementTemplate);
            CreateGood(1060, "Dire Ember", 1006, Icons["Dark Ember"], ReinforcementTemplate);
            CreateGood(1070, "Blazing Ember", 1007, Icons["Large Flame Ember"], ReinforcementTemplate);
            CreateGood(1080, "Dragonfire Ember", 1008, Icons["Chaos Flame Ember"], ReinforcementTemplate);

            CreateGood(1100, "Small Titanite Piece", 1010, Icons["Titanite Shard"], ReinforcementTemplate);
            CreateGood(1110, "Large Titanite Piece", 1011, Icons["Large Titanite Shard"], ReinforcementTemplate);
            CreateGood(1120, "Giant Titanite Piece", 1012, Icons["Titanite Chunk"], ReinforcementTemplate);
            CreateGood(1130, "Colossal Titanite Piece", 1013, Icons["Titanite Slab"], ReinforcementTemplate);
            // Delete remaining reinforcement materials params.
            Mod.GPARAM.Goods.DeleteRowRange(1140, 2000);
        }

        Good CreateGood(int goodID, string goodName, int sortIndex, ushort iconID, Good goodTemplate)
        {
            Mod.GPARAM.Goods.DeleteRow(goodID);
            Good newGood = Mod.GPARAM.Goods.CopyRow(goodTemplate, goodID);
            newGood.Name = goodName;
            if (!Summaries.ContainsKey(goodName))
                throw new Exception($"No summary for good {goodName}.");
            if (!Descriptions.ContainsKey(goodName))
                throw new Exception($"No description for good {goodName}.");
            newGood.Summary = Summaries[goodName];
            newGood.Description = string.Join("\n", WordWrapper.WordWrap(Descriptions[goodName], 39));
            newGood.SortIndex = sortIndex;
            newGood.GoodIcon = iconID;
            return newGood;
        }
    }
}
