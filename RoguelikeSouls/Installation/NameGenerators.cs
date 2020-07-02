using System;
using System.Collections.Generic;
using System.Linq;
using Markov;
using RoguelikeSouls.Extensions;
using RoguelikeSouls.Utils;
using WeaponNameOptionDict = System.Collections.Generic.Dictionary<string, (System.Collections.Generic.List<string> common, System.Collections.Generic.List<string> legendary)>;
using ArmorNameOptionDict = System.Collections.Generic.Dictionary<string, (System.Collections.Generic.List<string> light, System.Collections.Generic.List<string> heavy)>;

namespace RoguelikeSouls.Installation
{
    class WeaponNameGenerator
    {
        public static readonly WeaponNameOptionDict ClassOptions = new WeaponNameOptionDict()
        {
            { "Dagger", (
                new List<string>() { "Dagger", "Knife", "Tracer", "Dirk", "Quickblade" },
                new List<string>() { "Stiletto", "Bloodknife", "Heartpiercer", "Razor" }
                ) },
            { "StraightSword", (
                new List<string>() { "Straight Sword", "Sword", "Blade", "Brand", "Edge" },
                new List<string>() { "Soulbrand", "Blacksword", "Crusader" }
                ) },
            { "Greatsword", (
                new List<string>() { "Greatsword", "Ironblade", "Claymore" },
                new List<string>() { "Bonehewer", "Breaker" }
                ) },
            { "UltraGreatsword", (
                new List<string>() { "Greatsword", "Giantsword" },
                new List<string>() { "Stoneblade", "Vastblade", "Skullduster" }
                ) },
            { "ThrustingSword", (
                new List<string>() { "Rapier", "Estoc", "Sabre", "Foil", "Epee" },
                new List<string>() { "Impaler", "Reaver", "Etcher" }
                ) },
            { "CurvedSword", (
                new List<string>() { "Scimitar", "Cutlass", "Falchion", "Machete", "Backsword" },
                new List<string>() { "Shamshir", "Kilij", "Shotel", "Bird-Talon" }
                ) },
            { "CurvedGreatsword", (
                new List<string>() { "Arcblade", "Giant Machete" },
                new List<string>() { "Skincarver", "Rukh-Talon" }
                ) },
            { "Katana", (
                new List<string>() { "Katana", "Iaito", "Uchigatana", "Shinken"},
                new List<string>() { "Tsurugi", "Tachi", "Odachi" }
                ) },
            { "Axe", (
                new List<string>() { "Axe", "Hatchet", "Chopper", "Battleaxe" },
                new List<string>() { "Cleaver", "Meataxe", "Bonehewer" }
                ) },
            { "Greataxe", (
                new List<string>() { "Greataxe", "Giantaxe", "Stoneaxe" },
                new List<string>() { "Skullsplitter", "Titanjaw", "Vastaxe" }
                ) },
            { "Hammer", (
                new List<string>() { "Hammer", "Club", "Cudgel", "Mace" },
                new List<string>() { "Truncheon", "Pummeler", "Crusher" }
                ) },
            { "GreatHammer", (
                new List<string>() { "Great Hammer", "Greatclub", "Giant Club", "Big Rock" },
                new List<string>() { "Colossus", "Hornhammer", "Dragontooth", "Soulgrinder" }
                ) },
            { "Spear", (
                new List<string>() { "Spear", "Pike", "Lance", "Javelin", "Partizan" },
                new List<string>() { "Skewer", "Brochette", "Ramspike" }
                ) },
            { "Halberd", (
                new List<string>() { "Halberd", "Bayonet", "Pollaxe", "Bill-Hook" },
                new List<string>() { "Spontoon", "Glaive", "Axespear" }
                ) },
            { "Scythe", (
                new List<string>() { "Scythe", "Sickle" },
                new List<string>() { "Reaper", "Grimhook", "Harvester" }
                ) },
            { "Catalyst", (
                new List<string>() { "Catalyst" },
                new List<string>() { "Catalyst" }
                ) },
            { "Talisman", (
                new List<string>() { "Talisman" },
                new List<string>() { "Talisman" }
                ) },
            { "Fists", (
                new List<string>() { "Knuckles", "Caestus" },
                new List<string>() { "Shellfist", "Stonehand" }
                ) },
            { "Whip", (
                new List<string>() { "Whip", "Lash", "Switch" },
                new List<string>() { "Bullwhip", "Cat-o'-Nine-Tails" }
                ) },
            { "Bow", (
                new List<string>() { "Bow", "Longbow", "Shortbow" },
                new List<string>() { "Heartstring", "Hawkbow" }
                ) },
            { "Greatbow", (
                new List<string>() { "Greatbow" },
                new List<string>() { "Greatbow", "Griefbow" }
                ) },
            { "Crossbow", (
                new List<string>() { "Crossbow" },
                new List<string>() { "Ballista", "Scorpion" }
                ) },
            { "Greatshield", (
                new List<string>() { "Greatshield", "Stoneshield" },
                new List<string>() { "Vastshield", "Carapace", "Wall" }
                ) },
            { "Shield", (
                new List<string>() { "Shield", "Buckler", "Protector" },
                new List<string>() { "Bloodshield", "Shell" }
                ) }
        };
        private readonly Random Rand;
        private readonly MarkovWordGenerator MarkovNames;
        private readonly List<string> CensoredWords = new List<string>() { "fuck", "shit", "cunt", "rape", "cock", "nigg", "tits", "tard" };

        const int nameUnitSize = 2;
        const int minNameLength = 10;
        const int maxNameLength = 20;  // TODO: Confirm. Should be equal to true limit minus 6 (for modifier prefixes).
        const int maxAttempts = 50;
        const double titledNameOdds = 0.2;

        public WeaponNameGenerator(Random random)
        {
            Rand = random;
            MarkovNames = new MarkovWordGenerator(Resources.TextData.AllWeaponNamesNoSuffix, unitSize: nameUnitSize, random: Rand);
        }

        public string GetRandomName(out string randomPart, string weaponClass = "", bool isLegendary = false, bool exact = false)
        {
            bool isTitled = Rand.NextDouble() < titledNameOdds;
            string className = weaponClass != "" ? GetRandomClassName(weaponClass, isLegendary) : "";
            int actualMaxNameLength = className != "" ? (maxNameLength - (className.Length + (isTitled ? 4 : 1))) : maxNameLength;
            int actualMinNameLength = Math.Min(minNameLength, actualMaxNameLength - 2);
            if (actualMaxNameLength < 3)
            {
                className = "";
                actualMaxNameLength = maxNameLength;
            }
            
            // Keeps trying to get a name that is naturally under the absolute max limit (which is affected by class name).
            string randomName;
            int attempts = 0;
            do
            {
                randomName = MarkovNames.Generate(actualMinNameLength, exact);
                attempts++;
                if (attempts >= maxAttempts)
                    break;
            } while (randomName.Length > actualMaxNameLength || randomName.ToLower().ContainsAny(CensoredWords));
            if (randomName.Length > actualMaxNameLength)
            {
                // If max attempt number is exceeded (unlikely), just trim the last name.
                randomName = TrimName(randomName, actualMaxNameLength);
            }

            randomPart = randomName;  // Can use output to affect description (TODO).

            if (className == "")
                return randomName;
            else if (isTitled)
                return $"{className} of {randomName}";
            else
                return $"{randomName} {className}";
        }

        string GetRandomClassName(string weaponClass, bool isLegendary)
        {
            if (weaponClass.ToLower() == "random")
            {
                int randomIndex = Rand.Next(ClassOptions.Count);
                weaponClass = ClassOptions.ElementAt(randomIndex).Key;
            }
            if (!ClassOptions.ContainsKey(weaponClass))
                throw new ArgumentException($"'{weaponClass}' is not a valid weapon class name.");
            if (isLegendary)
            {
                int randomIndex = Rand.Next(ClassOptions[weaponClass].legendary.Count);
                return ClassOptions[weaponClass].legendary[randomIndex];
            }
            else
            {
                int randomIndex = Rand.Next(ClassOptions[weaponClass].common.Count);
                return ClassOptions[weaponClass].common[randomIndex];
            }
        }

        static string TrimName(string randomName, int randomNameLengthLimit)
        {
            while (randomName.Length > randomNameLengthLimit)
                // Shave off letters (and trailing space) as needed.
                randomName = randomName.Substring(0, randomName.Length - 1).TrimEnd(' ');
            if (randomName.EndsWith("'"))
                // Shave off abandoned apostrophes.
                randomName = randomName.Substring(0, randomName.Length - 1);
            if (randomName[randomName.Length - 2] == ' ')
                // Shave off one-letter word.
                randomName = randomName.Substring(0, randomName.Length - 2);
            randomName = randomName.Trim(' ');  // Probably redundant, but just in case.
            return randomName;
        }
    }

    class WeaponDescriptionGenerator
    {
        private readonly Random Rand;
        private readonly SmartMarkovProseGenerator MarkovDescriptions;

        const int descriptionUnitSize = 2;
        const int requestedLength = 15;
        const int maxLineLength = 39;  // TODO: Confirm.
        const int maxCharLength = 150;

        public WeaponDescriptionGenerator(Random random)
        {
            Rand = random;
            MarkovDescriptions = new SmartMarkovProseGenerator(Resources.TextData.AllWeaponDescriptions, unitSize: descriptionUnitSize, random: Rand);
        }

        public string GetRandomDescription(string extraParagraph = "", bool exact = false)
        {
            string desc = MarkovDescriptions.Generate(requestedLength, exact);
            while (desc.Length > maxCharLength && desc.Contains(","))  // Cut off at last comma.
                desc = desc.Substring(0, desc.LastIndexOf(',')) + ".";

            string wrappedDesc = string.Join("\n", WordWrapper.WordWrap(desc, maxLineLength));
            if (extraParagraph != "")
                return string.Join("\n", WordWrapper.WordWrap(extraParagraph, maxLineLength)) + "\n\n" + wrappedDesc;
            else
                return wrappedDesc;
        }
    }

    class ArmorNameGenerator
    {
        public static ArmorNameOptionDict PieceNameOptions { get; } = new ArmorNameOptionDict()
        {
            { "Head", (
                new List<string>() { "Hood", "Hat", "Mask" },
                new List<string>() { "Helm", "Crown", "Helmet",  }
                ) },
            { "Body", (
                new List<string>() { "Robe", "Cloak", "Coat", "Overcoat" },
                new List<string>() { "Armor", "Plate", "Mail" }
                ) },
            { "Arms", (
                new List<string>() { "Manchette", "Gloves" },
                new List<string>() { "Gauntlets", "Bracelet" }
                ) },
            { "Legs", (
                new List<string>() { "Pants", "Skirt", "Waistcloth", "Tights", "Trousers" },
                new List<string>() { "Leggings", "Boots", "Anklet" }
                ) },
        };
        private readonly Random Rand;
        private readonly MarkovWordGenerator MarkovNames;
        private readonly List<string> CensoredWords = new List<string>() { "fuck", "shit", "cunt", "rape", "cock", "nigg", "tits", "tard" };

        const int nameUnitSize = 2;
        const int minNameLength = 10;
        const int maxNameLength = 20;  // TODO: Confirm. Should be equal to true limit minus 6 (for modifier prefixes).
        const int maxAttempts = 50;
        const double titledNameOdds = 0.2;

        public ArmorNameGenerator(Random random)
        {
            Rand = random;
            MarkovNames = new MarkovWordGenerator(Resources.TextData.AllArmorNames, unitSize: nameUnitSize, random: Rand);
        }

        public Dictionary<string, string> GetRandomSetNames(out string randomPart, bool isLegendary = false, bool exact = false)
        {
            // Generates a name for each armor piece type using the same random template.
            
            bool isTitled = Rand.NextDouble() < titledNameOdds;
            Dictionary<string, string> pieceNames = new Dictionary<string, string>();
            foreach (string pieceType in PieceNameOptions.Keys)
                pieceNames[pieceType] = GetRandomClassName(pieceType, isLegendary);
            
            int actualMaxNameLength = pieceNames.Values.Min(name => maxNameLength - (name.Length + (isTitled ? 4 : 1)));
            int actualMinNameLength = Math.Min(minNameLength, actualMaxNameLength - 2);

            // Tries to get a name that is naturally under the actual maximum length.
            string randomName;
            int attempts = 0;
            do
            {
                randomName = MarkovNames.Generate(actualMinNameLength, exact);
                attempts++;
                if (attempts >= maxAttempts)
                    break;
            } while (randomName.Length > actualMaxNameLength || randomName.ToLower().ContainsAny(CensoredWords));
            if (randomName.Length > actualMaxNameLength)
            {
                // If max attempt number is exceeded (unlikely), just trim the last name.
                randomName = TrimName(randomName, actualMaxNameLength);
            }

            randomPart = randomName;  // Can use output to affect description (TODO).

            Dictionary<string, string> pieceFullNames = new Dictionary<string, string>();
            foreach (string pieceType in PieceNameOptions.Keys)
                pieceFullNames[pieceType] = isTitled ? $"{pieceNames[pieceType]} of {randomName}" : $"{randomName} {pieceNames[pieceType]}";
            return pieceFullNames;
        }

        string GetRandomClassName(string armorClass, bool isHeavy)
        {
            if (armorClass.ToLower() == "random")
            {
                int randomIndex = Rand.Next(PieceNameOptions.Count);
                armorClass = PieceNameOptions.ElementAt(randomIndex).Key;
            }
            if (!PieceNameOptions.ContainsKey(armorClass))
                throw new ArgumentException($"'{armorClass}' is not a valid weapon class name.");
            if (isHeavy)
            {
                int randomIndex = Rand.Next(PieceNameOptions[armorClass].heavy.Count);
                return PieceNameOptions[armorClass].heavy[randomIndex];
            }
            else
            {
                int randomIndex = Rand.Next(PieceNameOptions[armorClass].light.Count);
                return PieceNameOptions[armorClass].light[randomIndex];
            }
        }

        static string TrimName(string randomName, int randomNameLengthLimit)
        {
            while (randomName.Length > randomNameLengthLimit)
                // Shave off letters (and trailing space) as needed.
                randomName = randomName.Substring(0, randomName.Length - 1).TrimEnd(' ');
            if (randomName.EndsWith("'"))
                // Shave off abandoned apostrophes.
                randomName = randomName.Substring(0, randomName.Length - 1);
            if (randomName[randomName.Length - 2] == ' ')
                // Shave off one-letter word.
                randomName = randomName.Substring(0, randomName.Length - 2);
            randomName = randomName.Trim(' ');  // Probably redundant, but just in case.
            return randomName;
        }
    }

    class ArmorDescriptionGenerator
    {
        private readonly Random Rand;
        private readonly SmartMarkovProseGenerator MarkovDescriptions;

        private static string[] PieceTypes { get; } = { "Head", "Body", "Arms", "Legs" };

        const int descriptionUnitSize = 2;
        const int requestedLength = 15;
        const int maxLineLength = 39;
        const int maxCharLength = 150;

        public ArmorDescriptionGenerator(Random random)
        {
            Rand = random;
            MarkovDescriptions = new SmartMarkovProseGenerator(Resources.TextData.AllArmorDescriptions, unitSize: descriptionUnitSize, random: Rand);
        }
        public Dictionary<string, string> GetRandomSetDescriptions(Dictionary<string, string> extraParagraphs, bool exact = false)
        {
            string desc = MarkovDescriptions.Generate(requestedLength, exact);
            while (desc.Length > maxCharLength && desc.Contains(","))  // Cut off at last comma.
                desc = desc.Substring(0, desc.LastIndexOf(',')) + ".";
            string wrappedDesc = string.Join("\n", WordWrapper.WordWrap(desc, maxLineLength));
            Dictionary<string, string> wrappedPieceDescriptions = new Dictionary<string, string>();
            foreach (string pieceType in PieceTypes)
            {
                if (extraParagraphs[pieceType] != "")
                {
                    string wrappedExtraParagraph = string.Join("\n", WordWrapper.WordWrap(extraParagraphs[pieceType], maxLineLength));
                    wrappedPieceDescriptions[pieceType] = wrappedExtraParagraph + "\n\n" + wrappedDesc;
                }
                else
                {
                    wrappedPieceDescriptions[pieceType] = wrappedDesc;
                }
            }
            return wrappedPieceDescriptions;
        }
    }

    class NPCNameGenerator
    {
        private readonly Random Rand;
        private readonly MarkovWordGenerator MarkovNames;
        private readonly List<string> CensoredWords = new List<string>() { "fuck", "shit", "cunt", "rape", "cock", "nigg", "tits", "tard" };

        const int nameUnitSize = 2;
        const int minNameLength = 5;
        const int maxNameLength = 25;
        const int maxAttempts = 50;
        const double surnameOdds = 0.3;
        const double titledNameOdds = 0.9;  // Knight {Name}, Sorcerer {Name}, etc.
        const double originNameOdds = 0.7;  // {Name} of {Place}
        const double suffixNameOdds = 0.3;  // "Oscar, Knight of Astora" rather than "Knight Oscar of Astora"

        public NPCNameGenerator(Random random)
        {
            Rand = random;
            MarkovNames = new MarkovWordGenerator(Resources.TextData.AllNPCNames, unitSize: nameUnitSize, random: Rand);
        }
        public string GetRandomName(string npcTitle = "", bool exact = false)
        {
            bool hasSurname = Rand.NextDouble() < surnameOdds;
            bool isTitled = npcTitle != "" && Rand.NextDouble() < titledNameOdds;
            bool hasOrigin = Rand.NextDouble() < originNameOdds;
            bool withComma = hasOrigin && Rand.NextDouble() < suffixNameOdds;

            // Keeps trying to get a name that is naturally under the absolute max limit.
            string randomName;
            int attempts = 0;
            do
            {
                string name = MarkovNames.Generate(minNameLength, exact).Split(' ')[0];
                if (hasSurname)
                    name += " " + MarkovNames.Generate(minNameLength, exact);
                if (hasOrigin)
                {
                    string placeName = MarkovNames.Generate(minNameLength, exact);
                    if (isTitled)
                        randomName = (withComma ? $"{name}, {npcTitle}" : $"{npcTitle} {name}") + $"of {placeName}";
                    else
                        randomName = $"{name} of {placeName}";
                }
                else
                    randomName = isTitled ? $"{npcTitle} {name}" : name;
                attempts++;
                if (attempts >= maxAttempts)
                    break;  // keep last name and trim
            } while (randomName.Length > maxNameLength || randomName.ToLower().ContainsAny(CensoredWords));
            
            if (randomName.Length > maxNameLength)
            {
                //Console.WriteLine("Max attempts exceeded. Getting exact name.");
                // If max attempt number is exceeded (unlikely), just use a single exact random name.
                randomName = MarkovNames.Generate(minNameLength - npcTitle.Length, exact: true);
                return isTitled ? npcTitle + " " + randomName : randomName;
            }
            return randomName;
        }
    }

    class BossNameGenerator
    {
        private readonly Random Rand;
        private readonly MarkovWordGenerator MarkovNames;
        private readonly List<string> CensoredWords = new List<string>() { "fuck", "shit", "cunt", "rape", "cock", "nigg", "tits", "tard" };

        const int nameUnitSize = 2;
        const int minNameLength = 5;
        const int maxNameLength = 30;
        const int maxAttempts = 50;

        public BossNameGenerator(Random random)
        {
            Rand = random;
            MarkovNames = new MarkovWordGenerator(Resources.TextData.AllBossNames, unitSize: nameUnitSize, random: Rand);
        }
        public string GetRandomName(bool exact = false)
        {
            // Keeps trying to get a name that is naturally under the absolute max limit.
            string randomName;
            int attempts = 0;
            do
            {
                randomName = MarkovNames.Generate(minNameLength, exact);
                attempts++;
                if (attempts >= maxAttempts)
                    break;  // keep last name and trim
            } while (randomName.Length > maxNameLength || randomName.ToLower().ContainsAny(CensoredWords));

            if (randomName.Length > maxNameLength)
            {
                // If max attempt number is exceeded (unlikely), just use a single random name.
                randomName = MarkovNames.Generate(minNameLength, exact: true);
            }
            return randomName;
        }
    }

    class SpellNameGenerator
    {
        private readonly Random Rand;
        private readonly MarkovWordGenerator MarkovNames;
        private readonly List<string> CensoredWords = new List<string>() { "fuck", "shit", "cunt", "rape", "cock", "nigg", "tits", "tard" };

        const int nameUnitSize = 2;
        const int minNameLength = 8;
        const int maxNameLength = 30;
        const int maxAttempts = 50;

        public SpellNameGenerator(Random random)
        {
            Rand = random;
            MarkovNames = new MarkovWordGenerator(Resources.TextData.AllSpellNames, unitSize: nameUnitSize, random: Rand);
        }
        public string GetRandomName(string spellType, bool exact = false)
        {
            // Keeps trying to get a name that is naturally under the absolute max limit.
            string randomName;
            int attempts = 0;
            do
            {
                randomName = $"{spellType}: {MarkovNames.Generate(minNameLength, exact)}";
                attempts++;
                if (attempts >= maxAttempts)
                    break;  // keep last name and trim
            } while (randomName.Length > maxNameLength || randomName.ToLower().ContainsAny(CensoredWords));

            if (randomName.Length > maxNameLength)
            {
                // If max attempt number is exceeded (unlikely), just use a single random name.
                randomName = $"{spellType}: {MarkovNames.Generate(minNameLength - (spellType.Length + 2), exact: true)}";
            }
            return randomName;
        }
    }

    class SpellDescriptionGenerator
    {
        private readonly Random Rand;
        private readonly SmartMarkovProseGenerator MarkovDescriptions;

        const int descriptionUnitSize = 2;
        const int requestedLength = 15;
        const int maxLineLength = 39;  // TODO: Confirm.

        public SpellDescriptionGenerator(Random random)
        {
            Rand = random;
            MarkovDescriptions = new SmartMarkovProseGenerator(Resources.TextData.AllSpellDescriptions, unitSize: descriptionUnitSize, random: Rand);
        }
        public string GetRandomDescription(bool exact = false)
        {
            string desc = MarkovDescriptions.Generate(requestedLength, exact);
            // TOOD: Trim back to a comma if desc is too many lines.
            return string.Join("\n", WordWrapper.WordWrap(desc, maxLineLength));
        }
    }
}
