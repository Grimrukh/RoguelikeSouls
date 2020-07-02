using System;
using System.Collections.Generic;
using System.Linq;
using RoguelikeSouls.Extensions;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using PieceEffectDict = System.Collections.Generic.Dictionary<string, RoguelikeSouls.Installation.LegendaryArmorEffects>;

namespace RoguelikeSouls.Installation
{
    class ArmorGenerator
    {
        private readonly Random Rand;
        private ArmorNameGenerator NameGenerator { get; }
        private ArmorDescriptionGenerator DescriptionGenerator { get; }
        private readonly SoulsMod Mod;

        private int SortIndex = 0;
        Dictionary<string, (int offset, Type legendClass)> PieceInfo { get; } = new Dictionary<string, (int, Type)>()
        {
            { "Head", (0, typeof(LegendaryHeadArmorEffects)) },
            { "Body", (1000, typeof(LegendaryBodyArmorEffects)) },
            { "Arms", (2000, typeof(LegendaryArmsArmorEffects)) },
            { "Legs", (3000, typeof(LegendaryLegsArmorEffects)) },
        };
        static Dictionary<string, List<int>> WeightClasses { get; } = new Dictionary<string, List<int>>()
        {
            { "Light", new List<int> {
                 50000,  60000, 140000, 150000, 220000, 230000, 250000, 290000,
                300000, 310000, 330000, 340000, 360000, 370000, 380000, 400000,
                410000, 460000, 500000, 540000, 550000, 640000, 670000, 700000
            } },
            { "Medium", new List<int> {
                 10000,  20000,  40000,  90000, 100000, 110000, 130000, 160000,
                170000, 180000, 200000, 210000, 240000, 270000, 280000, 350000,
                390000, 450000, 480000, 510000, 520000, 650000, 660000
            } },
            { "Heavy", new List<int> {
                 70000,  80000, 120000, 320000, 420000, 440000, 470000, 490000,
                530000, 680000, 690000
            } },
            { "SpecialHead", new List<int> {
                560000,  // Sack
                570000,  // Symbol of Avarice
                580000,  // Royal Helm
                590000,  // Mask of the Father
                600000,  // Mask of the Mother
                610000,  // Mask of the Child
                620000,  // Fang Boar Helm
                630000,  // Gargoyle Helm
                710000,  // Bloated Head
                720000,  // Bloated Sorcerer 
            } }
        };

        public static List<int> IncompleteSets { get; } = new List<int>() { 480000, 500000, 520000 };

        const double BasicLegendaryOdds = 0.7;
        const double LegendaryOdds = 0.2;
        const int LightCount = 24;
        const int MediumCount = 24;
        const int HeavyCount = 12;
        const int AbyssalLightCount = 2;
        const int AbyssalMediumCount = 2;
        const int AbyssalHeavyCount = 1;

        const int FirstRandomArmorID = 100000;

        const float ArmorUpgradeDefense = 0.25f;
        const float ArmorUpgradeResistance = 0.15f;

        string debugCurrentClass = "";

        public List<int> GenericArmor { get; } = new List<int>();
        public List<int> BasicArmor { get; } = new List<int>();
        public List<int> LegendaryArmor { get; } = new List<int>();
        public List<int> AbyssalArmor { get; } = new List<int>();

        public int GetRandomArmorID(bool generic, bool basic, bool legendary, bool abyssal, params (int upgrade, double odds)[] upgradeOptions)
        {
            List<int> options = new List<int>();
            if (generic)
                options.AddRange(GenericArmor);
            if (basic)
                options.AddRange(BasicArmor);
            if (legendary)
                options.AddRange(LegendaryArmor);
            if (abyssal)
                options.AddRange(AbyssalArmor);

            if (!options.Any())
                throw new Exception("No armor to choose from. ArmorSetup.Install() has likely not been run.");

            int chosenID = options.GetRandomElement(Rand);
            if (!upgradeOptions.Any())
                return chosenID;
            else
            {
                double roll = Rand.NextDouble();
                double oddsTotal = 0.0;
                foreach (var (upgrade, odds) in upgradeOptions)
                {
                    oddsTotal += odds;
                    if (roll < oddsTotal)
                        return chosenID + upgrade;
                }
                return chosenID;  // No upgrade.
            }
        }

        public ArmorGenerator(SoulsMod mod, Random random = null)
        {
            Rand = random ?? new Random();
            Mod = mod;
            NameGenerator = new ArmorNameGenerator(Rand);
            DescriptionGenerator = new ArmorDescriptionGenerator(Rand);
        }

        public void Install()
        {
            // Note that there's no starting armor. I'm too lazy, and this way
            // players will be encouraged to use whatever they find first.

            int armorIndex = 0;

            debugCurrentClass = "light armor";
            for (int i = 0; i < LightCount; i++)
                CreateArmorSet("Light", ref armorIndex, isAbyssal: false);

            debugCurrentClass = "medium armor";
            for (int i = 0; i < MediumCount; i++)
                CreateArmorSet("Medium", ref armorIndex, isAbyssal: false);

            debugCurrentClass = "heavy armor";
            for (int i = 0; i < HeavyCount; i++)
                CreateArmorSet("Heavy", ref armorIndex, isAbyssal: false);

            debugCurrentClass = "abyssal armor";
            for (int i = 0; i < AbyssalLightCount; i++)
                CreateArmorSet("Light", ref armorIndex, isAbyssal: true);
            for (int i = 0; i < AbyssalMediumCount; i++)
                CreateArmorSet("Medium", ref armorIndex, isAbyssal: true);
            for (int i = 0; i < AbyssalHeavyCount; i++)
                CreateArmorSet("Heavy", ref armorIndex, isAbyssal: true);

            // Delete remaining (vanilla) armor params (except naked, Dragon Head/Torso, and Egg stages).
            int lastArmorParam = FirstRandomArmorID + 10000 * (armorIndex + 1);
#if DEBUG
            Console.WriteLine($"Deleting all armor from {lastArmorParam} (except naked, dragon, and egg)");
#endif
            Mod.GPARAM.Armor.DeleteRowRange(10000, 100000);
            Mod.GPARAM.Armor.DeleteRowWhereID(id => lastArmorParam <= id && !(900000 <= id && id < 2000000));

            // Modify Armor Upgrade and armor Upgrade Material params.
            ModifyUpgradeParams();

            CreateStartingArmorSet(500000, 10000, noArms: true);  // Starting armor (Hollow Thief set).
            CreateStartingArmorSet(160000, 20000);  // Sunlight set (Solaire)
            CreateStartingArmorSet(10000, 30000);  // Catarina set (Siegmeyer)
            CreateStartingArmorSet(380000, 40000);  // Big Hat set (Logan)
            CreateStartingArmorSet(460000, 50000);  // Gold-Hemmed set (Quelana)
            CreateStartingArmorSet(440000, 60000);  // Havel's set 
        }

        void CreateArmorSet(string armorClass, ref int armorIndex, bool isAbyssal = false)
        {
            int headArmorParamId = FirstRandomArmorID + 10000 * armorIndex;
#if DEBUG
            Console.WriteLine($"Creating {debugCurrentClass} {headArmorParamId}...");
#endif

            ArmorSet modelSet = GetRandomVanillaArmorSet(armorClass);
            ArmorSet defenseSet = GetRandomVanillaArmorSet(armorClass, fullSetRequired: true);
            ArmorSet resistanceSet = GetRandomVanillaArmorSet(armorClass, fullSetRequired: true);

            PieceEffectDict armorEffects = new PieceEffectDict();
            bool isBasic = isAbyssal || Rand.NextDouble() < BasicLegendaryOdds;
            bool isLegendary = isAbyssal || Rand.NextDouble() < LegendaryOdds;
            foreach (string pieceType in PieceInfo.Keys)
            {
                if (pieceType == "Arms" && modelSet.Arms == null)
                    continue;  // Don't record missing arms.

                if (isBasic || isLegendary || isAbyssal)
                {
                    armorEffects[pieceType] = (LegendaryArmorEffects)Activator.CreateInstance(PieceInfo[pieceType].legendClass, isBasic, isLegendary, isAbyssal, Rand);
                    if (isAbyssal)
                        AbyssalArmor.Add(headArmorParamId + PieceInfo[pieceType].offset);
                    else if (isLegendary)
                        LegendaryArmor.Add(headArmorParamId + PieceInfo[pieceType].offset);
                    else if (isBasic)
                        BasicArmor.Add(headArmorParamId + PieceInfo[pieceType].offset);  // Probably won't use this, but just in case.
                }
                else
                {
                    armorEffects[pieceType] = null;
                    GenericArmor.Add(headArmorParamId + PieceInfo[pieceType].offset);
                }
            }
            BasicArmorSetup(headArmorParamId, armorEffects, modelSet, defenseSet, resistanceSet);
            armorIndex++;
        }

        void BasicArmorSetup(int newHeadParamId, PieceEffectDict legendaryEffects, ArmorSet modelSet, ArmorSet defenseSet, ArmorSet resistanceSet)
        {
            //Console.WriteLine($"\n{modelSet.Body.Name} -> {defenseSet.Body.Name} -> {resistanceSet.Body.Name}\n");

            // Delete existing IDs in new armor's parameter ranges.
            Mod.GPARAM.Armor.DeleteRow(newHeadParamId);
            Mod.GPARAM.Armor.DeleteRow(newHeadParamId + 1000);
            Mod.GPARAM.Armor.DeleteRow(newHeadParamId + 2000);
            Mod.GPARAM.Armor.DeleteRow(newHeadParamId + 3000);

            var modelPieces = modelSet.Pieces;
            var defensePieces = defenseSet.Pieces;
            var resistancePieces = resistanceSet.Pieces;

            Dictionary<string, string> legendaryDescriptions = new Dictionary<string, string>()
            {
                { "Head", "" }, { "Body", "" }, { "Arms", "" }, { "Legs", "" }
            };
            foreach (var effectPair in legendaryEffects)
            {
                if (effectPair.Value != null)
                    legendaryDescriptions[effectPair.Key] = effectPair.Value.GetEffectDescription();
            }

            Dictionary<string, string> pieceNames = NameGenerator.GetRandomSetNames(out _, legendaryEffects["Head"] != null);
            Dictionary<string, string> pieceDescriptions = DescriptionGenerator.GetRandomSetDescriptions(legendaryDescriptions, exact: false);

            foreach (string pieceType in PieceInfo.Keys)
            {
                if (pieceType == "Arms" && modelSet.Arms == null)
                    continue;  // Some Hollow sets are missing arms. Don't create arms for them.

                LegendaryArmorEffects armorEffects = legendaryEffects[pieceType];
                string armorName = pieceNames[pieceType];
                string armorDesc = pieceDescriptions[pieceType];

                Armor newArmor = Mod.GPARAM.Armor.CopyRow(modelPieces[pieceType], newHeadParamId + PieceInfo[pieceType].offset);
                CleanArmorParam(newArmor);
                OverrideDefense(newArmor, defensePieces[pieceType]);
                OverrideResistance(newArmor, resistancePieces[pieceType]);
                newArmor.Name = armorName;
                newArmor.Row.Name = $"<{modelSet.WeightClass}|{defenseSet.WeightClass}> {armorName}";
                // No summary (short description).
                newArmor.Description = armorDesc;
                newArmor.SortIndex = SortIndex;
                SortIndex++;

                if (armorEffects != null)
                    armorEffects.ApplyEffects(newArmor);  // applies basic and abyssal effects as needed

                // Create reinforcement names.
                for (int upgradeLevel = 1; upgradeLevel <= 4; upgradeLevel++)
                {
                    Mod.Text.ArmorNames[newArmor.ID + upgradeLevel] = $"{armorName}+{upgradeLevel}";
                    // Summaries and descriptions are always loaded from base ID.
                }

            }
        }

        ArmorSet GetRandomVanillaArmorSet(string weightClass = "", bool fullSetRequired = false)
        {
            List<int> options = new List<int>();
            if (weightClass == "")
            {
                foreach (string weight in new string[] { "Light", "Medium", "Heavy" })
                    options.AddRange(WeightClasses[weight]);
            }
            else
                options.AddRange(WeightClasses[weightClass]);

            if (fullSetRequired)
            {
                foreach (int incompleteSet in IncompleteSets)
                    options.Remove(incompleteSet);
            }

            int paramId = options.GetRandomElement(Rand);
            return new ArmorSet(weightClass, paramId, Mod.VanillaGPARAM);
        }

        Armor GetRandomSpecialHead()
        {
            List<int> options = WeightClasses["SpecialHead"];
            int paramId = options.GetRandomElement(Rand);
            return Mod.VanillaGPARAM.Armor[paramId];
        }

        void OverrideDefense(Armor newArmor, Armor overrideArmor)
        {
            newArmor.PhysicalDefense = overrideArmor.PhysicalDefense;
            newArmor.MagicDefense = overrideArmor.MagicDefense;
            newArmor.FireDefense = overrideArmor.FireDefense;
            newArmor.LightningDefense = overrideArmor.LightningDefense;
            newArmor.StrikeDefense = overrideArmor.StrikeDefense;
            newArmor.SlashDefense = overrideArmor.SlashDefense;
            newArmor.ThrustDefense = overrideArmor.ThrustDefense;

            // Copy sound/visual effects.
            newArmor.VisualEffectOnHit = overrideArmor.VisualEffectOnHit;
            newArmor.SoundEffectOnHit = overrideArmor.SoundEffectOnHit;
            newArmor.VisualEffectOnWeakSpotHit = overrideArmor.VisualEffectOnWeakSpotHit;
            newArmor.SoundEffectOnWeakSpotHit = overrideArmor.SoundEffectOnWeakSpotHit;

            // Copy weak spot multiplier and stamina reduction effect.
            newArmor.SiteDamageMultiplier = overrideArmor.SiteDamageMultiplier;
            newArmor.WearerSpecialEffect1 = overrideArmor.WearerSpecialEffect1;
        }

        void OverrideResistance(Armor newArmor, Armor overrideArmor)
        {
            newArmor.PoisonResistance = overrideArmor.PoisonResistance;
            newArmor.BleedResistance = overrideArmor.BleedResistance;
            newArmor.ToxicResistance = overrideArmor.ToxicResistance;
            newArmor.CurseResistance = overrideArmor.CurseResistance;

            // Copy durability.
            newArmor.InitialDurability = overrideArmor.InitialDurability;
            newArmor.MaxDurability = overrideArmor.MaxDurability;
        }

        void CleanArmorParam(Armor newArmor)
        {
            // Only four upgrade levels per armor piece.
            newArmor.UpgradeMaterialID = 7000;
            newArmor.ArmorUpgradeID = 0;
            newArmor.UpgradeOrigin0 = (int)newArmor.ID;
            newArmor.UpgradeOrigin1 = (int)newArmor.ID;
            newArmor.UpgradeOrigin2 = (int)newArmor.ID;
            newArmor.UpgradeOrigin3 = (int)newArmor.ID;
            newArmor.UpgradeOrigin4 = (int)newArmor.ID;
            newArmor.UpgradeOrigin5 = -1;
            newArmor.UpgradeOrigin6 = -1;
            newArmor.UpgradeOrigin7 = -1;
            newArmor.UpgradeOrigin8 = -1;
            newArmor.UpgradeOrigin9 = -1;
            newArmor.UpgradeOrigin10 = -1;
            newArmor.UpgradeOrigin11 = -1;
            newArmor.UpgradeOrigin12 = -1;
            newArmor.UpgradeOrigin13 = -1;
            newArmor.UpgradeOrigin14 = -1;
            newArmor.UpgradeOrigin15 = -1;

            newArmor.WearerSpecialEffect1 = -1;  // Stamina reduction change; copied from defense override.
            newArmor.WearerSpecialEffect2 = 6300;  // All armor grants this poise animation change.
            newArmor.WearerSpecialEffect3 = -1;  // Optional legendary effect.
        }

        void ModifyUpgradeParams()
        {
            for (int upgradeLevel = 1; upgradeLevel <= 4; upgradeLevel++)
            {
                int upgradeMaterialID = 7000 + upgradeLevel;
                int titaniteID = 1100 + 10 * (upgradeLevel - 1);  // Small/Large/Giant/Colossal Titanite Piece
                Mod.GPARAM.UpgradeMaterials[upgradeMaterialID].Name = $"Armor +{upgradeLevel}";
                Mod.GPARAM.UpgradeMaterials[upgradeMaterialID].ItemNum01 = 1;
                Mod.GPARAM.UpgradeMaterials[upgradeMaterialID].MaterialId01 = titaniteID;
                Mod.GPARAM.UpgradeMaterials[upgradeMaterialID].IsDisableDispNum01 = true;

                float defenseMultiplier = 1.0f + (upgradeLevel) * ArmorUpgradeDefense;
                float resistanceMultiplier = 1.0f + (upgradeLevel) * ArmorUpgradeResistance;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].PhysicalDefenseMultiplier = defenseMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].MagicDefenseMultiplier = defenseMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].FireDefenseMultiplier = defenseMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].LightningDefenseMultiplier = defenseMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].PoisonResistanceMultiplier = resistanceMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].BleedResistanceMultiplier = resistanceMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].ToxicResistanceMultiplier = resistanceMultiplier;
                Mod.GPARAM.ArmorUpgrades[upgradeLevel].CurseResistanceMultiplier = resistanceMultiplier;
            }

            // Delete remaining Upgrade Material entries in 7000 range.
            Mod.GPARAM.UpgradeMaterials.DeleteRowRange(7005, 8000);

            // Delete remaining Armor Upgrade entries.
            Mod.GPARAM.ArmorUpgrades.DeleteRowRange(5, 999);
        }

        void CreateStartingArmorSet(int oldHeadPieceID, int newHeadPieceID, bool noArms = false)
        {
            Mod.GPARAM.Armor.DeleteRowRange(newHeadPieceID, newHeadPieceID + 10000);
            foreach (var keyValue in PieceInfo)
            {
                if (noArms && keyValue.Key == "Arms")
                    continue;
                int oldID = oldHeadPieceID + keyValue.Value.offset;
                Armor oldPiece = Mod.VanillaGPARAM.Armor[oldID];
                Armor newPiece = Mod.GPARAM.Armor.CopyRow(oldPiece, newHeadPieceID + keyValue.Value.offset);
                newPiece.Name = oldPiece.Name;
                newPiece.Summary = oldPiece.Summary;
                newPiece.Description = oldPiece.Description;
                newPiece.SortIndex = SortIndex;
                SortIndex++;
                for (int i = 1; i <= 15; i++)  // Remove upgrades.
                    newPiece.Row[$"originEquipPro{i}"].Value = -1;
            }
        }
    }
}
