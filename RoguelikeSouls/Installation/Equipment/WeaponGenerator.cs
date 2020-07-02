using SoulsFormats;
using SoulsFormatsMod.PARAMS;
using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormatsMod;
using RoguelikeSouls.Extensions;

namespace RoguelikeSouls.Installation
{
    enum Upgrade
    {
        Normal = 0,
        Crystal = 100,
        Lightning = 200,
        Refined = 300,
        Magic = 400,
        Enchanted = 500,
        Divine = 600,
        Dire = 700,
        Fire = 800,
        Draconic = 900,
    }

    class WeaponStats
    {
        // Contains all the GPARAM and TAE information about a weapon.
        public string Name{ get; }  // Bandit's Knife, Greatsword of Artorias, Spiked Shield...
        public string WeaponClass { get; }  // Melee, Bow, Crossbow, Catalyst, Talisman, Flame, Shield, Special  
        public string WeaponSubclass { get; }  // e.g. Dagger, StraightSword, Greatsword... or Bow, Greatbow... or Shield, Greatshield...
        public int ParamId { get; }  // for Weapon param
        public int ModelId { get; }
        public int BehaviorVariationId { get; }  // 1000-1999 for arrows/bolts, 2000-5101 for weapons
        public int OneHandedAnimationCategory { get; }  // 0, 2, 3
        public int TwoHandedAnimationCategory { get; }  // 10, 12, 13, 14, 15, 16
        public int BaseAttackAnimationCategory { get; }  // 20 to 48
        public int SpecialAttackAnimationCategory { get; }  // 50+

        public string NameID { get => $"{Name} ({ParamId})"; }
        
        public WeaponStats(string weaponName, string weaponClass, string weaponSubclass, int paramId, int modelId, int behVarId, int oneHandAnim, int twoHandAnim, int baseAttackAnim, int specialAttackAnim)
        {
            Name = weaponName;
            WeaponClass = weaponClass;
            WeaponSubclass = weaponSubclass;
            ParamId = paramId;
            ModelId = modelId;
            BehaviorVariationId = behVarId;
            OneHandedAnimationCategory = oneHandAnim;
            TwoHandedAnimationCategory = twoHandAnim;
            BaseAttackAnimationCategory = baseAttackAnim;
            SpecialAttackAnimationCategory = specialAttackAnim;
        }

        public Weapon GetWeaponParam(GameParamHandler gParam)
        {
            return gParam.Weapons[ParamId];  // Should never be null.
        }

        public Behavior GetBehaviorParam(GameParamHandler gParam, int behaviorSubId)
        {
            int behaviorParamId = 100000000 + 1000 * BehaviorVariationId + behaviorSubId;
            gParam.BehaviorsPC.TryGetValue(behaviorParamId, out Behavior behavior);
            return behavior;  // may be null
        }
        public Attack GetAttackParam(GameParamHandler gParam, int behaviorSubId)
        {
            // Get attack param referenced by given behavior. Throws an exception if a Bullet is referenced.
            int behaviorParamId = 100000000 + 1000 * BehaviorVariationId + behaviorSubId;
            Behavior behavior = gParam.BehaviorsPC[behaviorParamId];
            if (behavior == null)
                throw new ArgumentException($"Missing behavior param: {behaviorSubId}");
            if (behavior.ReferenceType != 0)
                throw new ArgumentException($"Behavior param {behaviorSubId} has reference type {behavior.ReferenceType}, not 0 (Attack).");
            gParam.AttacksPC.TryGetValue(behavior.RefID, out Attack attack);
            return attack;  // may be null
        }
        public Bullet GetBulletParam(GameParamHandler gParam, int behaviorSubId)
        {
            // Get attack param referenced by given behavior. Throws an exception if an Attack is referenced.
            int behaviorParamId = 100000000 + 1000 * BehaviorVariationId + behaviorSubId;
            Behavior behavior = gParam.BehaviorsPC[behaviorParamId];
            if (behavior == null)
                throw new ArgumentException($"Missing behavior param: {behaviorSubId}");
            if (behavior.ReferenceType != 1)
                throw new ArgumentException($"Behavior param {behaviorSubId} has reference type {behavior.ReferenceType}, not 1 (Bullet).");
            gParam.Bullets.TryGetValue(behavior.RefID, out Bullet bullet);
            return bullet;
        }
    }

    class WeaponGenerator
    {
        public static Dictionary<string, WeaponStats> VanillaWeapons { get; } = new Dictionary<string, WeaponStats>()
        {
            // Daggers
            { "Dagger", new WeaponStats("Dagger", "Melee", "Dagger", 100000, 100, 2000, 0, 10, 20, 0) },
            { "ParryingDagger", new WeaponStats("ParryingDagger", "Melee", "Dagger", 101000, 107, 2000, 0, 10, 20, 71) },
            { "GhostBlade", new WeaponStats("GhostBlade", "Melee", "Dagger", 102000, 103, 2003, 0, 10, 20, 120) },
            { "BanditsKnife", new WeaponStats("BanditsKnife", "Melee", "Dagger", 103000, 101, 2001, 0, 10, 20, 72) },
            { "PriscillasDagger", new WeaponStats("PriscillasDagger", "Melee", "Dagger", 104000, 104, 2002, 0, 10, 20, 73) },
            { "DarkSilverTracer", new WeaponStats("DarkSilverTracer", "Melee", "Dagger", 9011000, 111, 2004, 0, 10, 20, 130) },

            // Straight Swords
            { "Shortsword", new WeaponStats("Shortsword", "Melee", "StraightSword", 200000, 207, 2300, 0, 10, 23, 0) },
            { "Longsword", new WeaponStats("Longsword", "Melee", "StraightSword", 201000, 201, 2300, 0, 10, 23, 0) },
            { "Broadsword", new WeaponStats("Broadsword", "Melee", "StraightSword", 202000, 204, 2301, 0, 10, 23, 53) },
            { "BrokenStraightSword", new WeaponStats("BrokenStraightSword", "Melee", "StraightSword", 203000, 200, 2300, 0, 10, 23, 0) },
            { "BalderSideSword", new WeaponStats("BalderSideSword", "Melee", "StraightSword", 204000, 202, 2302, 0, 10, 23, 54) },
            { "CrystalStraightSword", new WeaponStats("CrystalStraightSword", "Melee", "StraightSword", 205000, 203, 2300, 0, 10, 23, 0) },
            { "SunlightStraightSword", new WeaponStats("SunlightStraightSword", "Melee", "StraightSword", 206000, 231, 2300, 0, 10, 23, 0) },
            { "BarbedStraightSword", new WeaponStats("BarbedStraightSword", "Melee", "StraightSword", 207000, 264, 2301, 0, 10, 23, 53) },
            { "SilvKnightStrSword", new WeaponStats("SilvKnightStrSword", "Melee", "StraightSword", 208000, 212, 2303, 0, 10, 23, 55) },
            { "AstorasStraightSword", new WeaponStats("AstorasStraightSword", "Melee", "StraightSword", 209000, 271, 2300, 0, 10, 23, 0) },
            { "Darksword", new WeaponStats("Darksword", "Melee", "StraightSword", 210000, 260, 2304, 0, 10, 23, 57) },
            { "DrakeSword", new WeaponStats("DrakeSword", "Melee", "StraightSword", 211000, 291, 2305, 0, 10, 23, 58) },
            { "StraightSwordHilt", new WeaponStats("StraightSwordHilt", "Melee", "StraightSword", 212000, 272, 2301, 0, 10, 23, 53) },

            // Greatswords
            { "BastardSword", new WeaponStats("BastardSword", "Melee", "Greatsword", 300000, 206, 2500, 2, 12, 25, 0) },
            { "Claymore", new WeaponStats("Claymore", "Melee", "Greatsword", 301000, 266, 2505, 2, 12, 25, 74) },
            { "ManserpentGreatsword", new WeaponStats("ManserpentGreatsword", "Melee", "Greatsword", 302000, 210, 2500, 2, 12, 25, 0) },
            { "Flamberge", new WeaponStats("Flamberge", "Melee", "Greatsword", 303000, 211, 2502, 2, 12, 25, 75) },
            { "CrystalGreatsword", new WeaponStats("CrystalGreatsword", "Melee", "Greatsword", 304000, 263, 2500, 2, 12, 25, 0) },
            { "StoneGreatsword", new WeaponStats("StoneGreatsword", "Melee", "Greatsword", 306000, 220, 2503, 2, 12, 25, 77) },
            { "GreatswordofArtorias", new WeaponStats("GreatswordofArtorias", "Melee", "Greatsword", 307000, 267, 2506, 2, 12, 25, 78) },
            { "MoonlightGreatsword", new WeaponStats("MoonlightGreatsword", "Melee", "Greatsword", 309000, 258, 2504, 2, 12, 25, 79) },
            { "BlackKnightSword", new WeaponStats("BlackKnightSword", "Melee", "Greatsword", 310000, 259, 2501, 2, 12, 25, 80) },
            { "GreatswordofArtoriasCursed", new WeaponStats("GreatswordofArtoriasCursed", "Melee", "Greatsword", 311000, 269, 2506, 2, 12, 25, 78) },
            { "GreatLordGreatsword", new WeaponStats("GreatLordGreatsword", "Melee", "Greatsword", 314000, 268, 2507, 2, 12, 25, 97) },
            { "ObsidianGreatsword", new WeaponStats("ObsidianGreatsword", "Melee", "Greatsword", 9020000, 240, 2509, 2, 12, 25, 135) },
            { "AbyssGreatsword", new WeaponStats("AbyssGreatsword", "Melee", "Greatsword", 9012000, 274, 2508, 2, 12, 25, 131) },

            // Ultra Greatswords
            { "Zweihander", new WeaponStats("Zweihander", "Melee", "UltraGreatsword", 350000, 208, 2600, 2, 12, 26, 0) },
            { "Greatsword", new WeaponStats("Greatsword", "Melee", "UltraGreatsword", 351000, 251, 2602, 2, 12, 26, 95) },
            { "DemonGreatMachete", new WeaponStats("DemonGreatMachete", "Melee", "UltraGreatsword", 352000, 270, 2603, 2, 12, 26, 96) },
            { "DragonGreatsword", new WeaponStats("DragonGreatsword", "Melee", "UltraGreatsword", 354000, 281, 2601, 2, 12, 26, 98) },
            { "BlackKnightGreatsword", new WeaponStats("BlackKnightGreatsword", "Melee", "UltraGreatsword", 355000, 221, 2604, 2, 12, 26, 128) },

            // Curved Swords
            { "Scimitar", new WeaponStats("Scimitar", "Melee", "CurvedSword", 400000, 400, 2800, 0, 10, 28, 0) },
            { "Falchion", new WeaponStats("Falchion", "Melee", "CurvedSword", 401000, 401, 2800, 0, 10, 28, 0) },
            { "Shotel", new WeaponStats("Shotel", "Melee", "CurvedSword", 402000, 403, 2801, 0, 10, 28, 99) },
            { "JaggedGhostBlade", new WeaponStats("JaggedGhostBlade", "Melee", "CurvedSword", 403000, 102, 2802, 0, 10, 28, 100) },
            { "PaintingGuardianSword", new WeaponStats("PaintingGuardianSword", "Melee", "CurvedSword", 405000, 406, 2803, 0, 10, 28, 101) },
            { "QuelaagsFurysword", new WeaponStats("QuelaagsFurysword", "Melee", "CurvedSword", 406000, 213, 2804, 0, 10, 28, 56) },
            { "GoldTracer", new WeaponStats("GoldTracer", "Melee", "CurvedSword", 9010000, 110, 2805, 0, 10, 28, 132) },

            // Curved Greatswords
            { "Server", new WeaponStats("Server", "Melee", "CurvedGreatsword", 450000, 280, 5100, 2, 12, 25, 51) },
            { "Murakumo", new WeaponStats("Murakumo", "Melee", "CurvedGreatsword", 451000, 284, 5100, 2, 12, 25, 51) },
            { "GravelordSword", new WeaponStats("GravelordSword", "Melee", "CurvedGreatsword", 453000, 282, 5101, 2, 12, 25, 116) },

            // Piercing Swords
            { "MailBreaker", new WeaponStats("MailBreaker", "Melee", "ThrustingSword", 600000, 106, 2701, 0, 10, 27, 119) },
            { "Rapier", new WeaponStats("Rapier", "Melee", "ThrustingSword", 601000, 300, 2700, 0, 10, 27, 0) },
            { "Estoc", new WeaponStats("Estoc", "Melee", "ThrustingSword", 602000, 301, 2702, 0, 10, 27, 113) },
            { "VelkasRapier", new WeaponStats("VelkasRapier", "Melee", "ThrustingSword", 603000, 230, 2703, 0, 10, 27, 114) },
            { "RicardsRapier", new WeaponStats("RicardsRapier", "Melee", "ThrustingSword", 604000, 302, 2704, 0, 10, 27, 115) },

            // Katanas
            { "Uchigatana", new WeaponStats("Uchigatana", "Melee", "Katana", 500000, 402, 2900, 0, 10, 29, 0) },
            { "WashingPole", new WeaponStats("WashingPole", "Melee", "Katana", 501000, 450, 2900, 0, 10, 29, 0) },
            { "Iaito", new WeaponStats("Iaito", "Melee", "Katana", 502000, 452, 2901, 0, 10, 29, 89) },
            { "ChaosBlade", new WeaponStats("ChaosBlade", "Melee", "Katana", 503000, 451, 2902, 0, 10, 29, 90) },

            // Axes
            { "HandAxe", new WeaponStats("HandAxe", "Melee", "Axe", 700000, 502, 3001, 0, 10, 30, 102) },
            { "BattleAxe", new WeaponStats("BattleAxe", "Melee", "Axe", 701000, 505, 3000, 0, 10, 30, 0) },
            { "CrescentAxe", new WeaponStats("CrescentAxe", "Melee", "Axe", 702000, 503, 3000, 0, 10, 32, 118) },
            { "ButcherKnife", new WeaponStats("ButcherKnife", "Melee", "Axe", 703000, 252, 3003, 0, 10, 30, 103) },
            { "GolemAxe", new WeaponStats("GolemAxe", "Melee", "Axe", 704000, 508, 3002, 0, 10, 30, 104) },
            { "GargoyleTailAxe", new WeaponStats("GargoyleTailAxe", "Melee", "Axe", 705000, 509, 3004, 0, 10, 30, 125) },

            // Greataxes
            { "Greataxe", new WeaponStats("Greataxe", "Melee", "Greataxe", 750000, 504, 3200, 2, 12, 32, 0) },
            { "DemonsGreataxe", new WeaponStats("DemonsGreataxe", "Melee", "Greataxe", 751000, 651, 3202, 2, 12, 32, 105) },
            { "DragonKingGreataxe", new WeaponStats("DragonKingGreataxe", "Melee", "Greataxe", 752000, 506, 3201, 2, 12, 32, 106) },
            { "BlackKnightGreataxe", new WeaponStats("BlackKnightGreataxe", "Melee", "Greataxe", 753000, 507, 3203, 2, 12, 32, 107) },
            { "StoneGreataxe", new WeaponStats("StoneGreataxe", "Melee", "Greataxe", 9015000, 510, 3204, 2, 12, 32, 133) },

            // Hammers
            { "Club", new WeaponStats("Club", "Melee", "Hammer", 800000, 600, 3302, 0, 10, 33, 0) },
            { "Mace", new WeaponStats("Mace", "Melee", "Hammer", 801000, 606, 3300, 0, 10, 33, 59) },
            { "MorningStar", new WeaponStats("MorningStar", "Melee", "Hammer", 802000, 603, 3300, 0, 10, 33, 59) },
            { "Warpick", new WeaponStats("Warpick", "Melee", "Hammer", 803000, 604, 3301, 0, 10, 33, 60) },
            { "Pickaxe", new WeaponStats("Pickaxe", "Melee", "Hammer", 804000, 605, 3303, 0, 10, 33, 61) },
            { "ReinforcedClub", new WeaponStats("ReinforcedClub", "Melee", "Hammer", 809000, 602, 3302, 0, 10, 33, 0) },
            { "BlacksmithHammer", new WeaponStats("BlacksmithHammer", "Melee", "Hammer", 810000, 656, 3300, 0, 10, 33, 59) },
            { "BlacksmithGiantHammer", new WeaponStats("BlacksmithGiantHammer", "Melee", "Hammer", 811000, 657, 3302, 0, 10, 33, 0) },
            { "HammerofVamos", new WeaponStats("HammerofVamos", "Melee", "Hammer", 812000, 658, 3300, 0, 10, 33, 59) },

            // Great Hammers
            { "GreatClub", new WeaponStats("GreatClub", "Melee", "GreatHammer", 850000, 607, 3501, 2, 12, 35, 69) },
            { "Grant", new WeaponStats("Grant", "Melee", "GreatHammer", 851000, 608, 3500, 2, 12, 35, 62) },
            { "DemonsGreatHammer", new WeaponStats("DemonsGreatHammer", "Melee", "GreatHammer", 852000, 654, 3500, 2, 12, 35, 0) },
            { "DragonTooth", new WeaponStats("DragonTooth", "Melee", "GreatHammer", 854000, 655, 3500, 2, 12, 35, 0) },
            { "LargeClub", new WeaponStats("LargeClub", "Melee", "GreatHammer", 855000, 659, 3502, 2, 12, 35, 124) },
            { "SmoughsHammer", new WeaponStats("SmoughsHammer", "Melee", "GreatHammer", 856000, 652, 3503, 2, 12, 35, 70) },

            // Fists
            { "Fists", new WeaponStats("Fists", "Melee", "Fists", 900000, 1005, 4201, 0, 10, 42, 0) },
            { "Caestus", new WeaponStats("Caestus", "Melee", "Fists", 901000, 1000, 4200, 0, 10, 42, 0) },
            { "Claw", new WeaponStats("Claw", "Melee", "Fists", 902000, 1002, 4202, 0, 10, 42, 86) },
            { "DragonBoneFist", new WeaponStats("DragonBoneFist", "Melee", "Fists", 903000, 1003, 4204, 0, 10, 42, 87) },
            { "DarkHand", new WeaponStats("DarkHand", "Melee", "Fists", 904000, 1004, 4203, 0, 10, 42, 123) },

            // Spears
            { "Spear", new WeaponStats("Spear", "Melee", "Spear", 1000000, 700, 3600, 3, 13, 36, 0) },
            { "WingedSpear", new WeaponStats("WingedSpear", "Melee", "Spear", 1001000, 702, 3600, 3, 13, 36, 0) },
            { "Partizan", new WeaponStats("Partizan", "Melee", "Spear", 1002000, 703, 3604, 3, 13, 36, 63) },
            { "DemonsSpear", new WeaponStats("DemonsSpear", "Melee", "Spear", 1003000, 710, 3605, 3, 13, 36, 64) },
            { "ChannelersTrident", new WeaponStats("ChannelersTrident", "Melee", "Spear", 1004000, 720, 3602, 3, 13, 36, 65) },
            { "FourprongedPlow", new WeaponStats("FourprongedPlow", "Melee", "Spear", 9016000, 740, 3607, 3, 13, 36, 134) },
            { "Pike", new WeaponStats("Pike", "Melee", "Spear", 1050000, 1100, 3601, 3, 13, 36, 67) },
            { "SilverKnightSpear", new WeaponStats("SilverKnightSpear", "Melee", "Spear", 1006000, 1101, 3606, 3, 13, 36, 66) },
            { "DragonslayerSpear", new WeaponStats("DragonslayerSpear", "Melee", "Spear", 1051000, 1102, 3603, 3, 13, 36, 68) },
            { "MoonlightButterflyHorn", new WeaponStats("MoonlightButterflyHorn", "Melee", "Spear", 1052000, 1103, 3600, 3, 13, 36, 0) },

            // Halberds
            { "TitaniteCatchPole", new WeaponStats("TitaniteCatchPole", "Melee", "Halberd", 1102000, 730, 3804, 3, 13, 38, 111) },
            { "BlackKnightHalberd", new WeaponStats("BlackKnightHalberd", "Melee", "Halberd", 1105000, 731, 3805, 3, 13, 38, 112) },
            { "Lucerne", new WeaponStats("Lucerne", "Melee", "Halberd", 1106000, 802, 3802, 3, 13, 38, 109) },
            { "Halberd", new WeaponStats("Halberd", "Melee", "Halberd", 1100000, 804, 3800, 3, 13, 38, 108) },
            { "GiantsHalberd", new WeaponStats("GiantsHalberd", "Melee", "Halberd", 1101000, 805, 3803, 3, 13, 38, 110) },
            { "GargoylesHalberd", new WeaponStats("GargoylesHalberd", "Melee", "Halberd", 1103000, 811, 3800, 3, 13, 38, 0) },

            // Scythes (considered Halberds in-game)
            { "GreatScythe", new WeaponStats("GreatScythe", "Melee", "Scythe", 1150000, 801, 5000, 0, 13, 38, 50) },
            { "Scythe", new WeaponStats("Scythe", "Melee", "Scythe", 1107000, 803, 3801, 3, 13, 38, 0) },
            { "LifehuntScythe", new WeaponStats("LifehuntScythe", "Melee", "Scythe", 1151000, 810, 5000, 0, 13, 38, 50) },
            
            // Whips
            { "Whip", new WeaponStats("Whip", "Melee", "Whip", 1600000, 1200, 4300, 0, 10, 43, 0) },
            { "NotchedWhip", new WeaponStats("NotchedWhip", "Melee", "Whip", 1601000, 1201, 4300, 0, 10, 43, 0) },
            { "GuardianTail", new WeaponStats("GuardianTail", "Melee", "Whip", 9019000, 1210, 4300, 0, 10, 43, 0) },

            // Catalysts
            { "DemonsCatalyst", new WeaponStats("DemonsCatalyst", "Catalyst", "Catalyst", 1307000, 653, 4102, 0, 10, 41, 127) },
            { "TinBanishmentCatalyst", new WeaponStats("TinBanishmentCatalyst", "Catalyst", "Catalyst", 1302000, 721, 4102, 0, 10, 41, 127) },
            { "LogansCatalyst", new WeaponStats("LogansCatalyst", "Catalyst", "Catalyst", 1303000, 901, 4101, 0, 10, 41, 0) },
            { "SorcerersCatalyst", new WeaponStats("SorcerersCatalyst", "Catalyst", "Catalyst", 1300000, 910, 4101, 0, 10, 41, 0) },
            { "BeatricesCatalyst", new WeaponStats("BeatricesCatalyst", "Catalyst", "Catalyst", 1301000, 912, 4101, 0, 10, 41, 0) },
            { "TinDarkmoonCatalyst", new WeaponStats("TinDarkmoonCatalyst", "Catalyst", "Catalyst", 1304000, 913, 4101, 0, 10, 41, 0) },
            { "OolacileIvoryCatalyst", new WeaponStats("OolacileIvoryCatalyst", "Catalyst", "Catalyst", 1305000, 914, 4101, 0, 10, 41, 0) },
            { "TinCrystallizationCtlyst", new WeaponStats("TinCrystallizationCtlyst", "Catalyst", "Catalyst", 1306000, 915, 4102, 0, 10, 41, 127) },
            { "IzalithCatalyst", new WeaponStats("IzalithCatalyst", "Catalyst", "Catalyst", 1308000, 916, 4101, 0, 10, 41, 0) },
            { "OolacileCatalyst", new WeaponStats("OolacileCatalyst", "Catalyst", "Catalyst", 9018000, 920, 4101, 0, 10, 41, 0) },
            { "ManusCatalyst", new WeaponStats("ManusCatalyst", "Catalyst", "Catalyst", 9017000, 921, 4104, 0, 10, 41, 136) },

            // Talismans
            { "Talisman", new WeaponStats("Talisman", "Talisman", "Talisman", 1360000, 902, 4100, 0, 10, 41, 52) },
            { "CanvasTalisman", new WeaponStats("CanvasTalisman", "Talisman", "Talisman", 1361000, 903, 4100, 0, 10, 41, 52) },
            { "ThorolundTalisman", new WeaponStats("ThorolundTalisman", "Talisman", "Talisman", 1362000, 904, 4100, 0, 10, 41, 52) },
            { "IvoryTalisman", new WeaponStats("IvoryTalisman", "Talisman", "Talisman", 1363000, 905, 4100, 0, 10, 41, 52) },
            { "SunlightTalisman", new WeaponStats("SunlightTalisman", "Talisman", "Talisman", 1365000, 907, 4100, 0, 10, 41, 52) },
            { "DarkmoonTalisman", new WeaponStats("DarkmoonTalisman", "Talisman", "Talisman", 1366000, 908, 4100, 0, 10, 41, 52) },
            { "VelkasTalisman", new WeaponStats("VelkasTalisman", "Talisman", "Talisman", 1367000, 909, 4100, 0, 10, 41, 52) },

            // Pyromancy Flame
            { "PyromancyFlame", new WeaponStats("PyromancyFlame", "Flame", "Flame", 1330000, 911, 4100, 0, 10, 41, 52) },

            // Special
            { "SkullLantern", new WeaponStats("SkullLantern", "Special", "Special", 1396000, 1801, 4103, 0, 10, 41, 121) },

            // Bows
            { "ShortBow", new WeaponStats("ShortBow", "Bow", "Bow", 1200000, 1300, 4400, 0, 14, 44, 81) },
            { "Longbow", new WeaponStats("Longbow", "Bow", "Bow", 1201000, 1301, 4400, 0, 14, 44, 0) },
            { "CompositeBow", new WeaponStats("CompositeBow", "Bow", "Bow", 1204000, 1302, 4400, 0, 14, 44, 81) },
            { "BlackBowofPharis", new WeaponStats("BlackBowofPharis", "Bow", "Bow", 1202000, 1304, 4400, 0, 14, 44, 82) },
            { "DarkmoonBow", new WeaponStats("DarkmoonBow", "Bow", "Bow", 1205000, 1305, 4400, 0, 14, 44, 81) },

            // Greatbows
            { "DragonslayerGreatbow", new WeaponStats("DragonslayerGreatbow", "Bow", "Greatbow", 1203000, 1360, 4400, 0, 14, 44, 83) },
            { "GoughsGreatbow", new WeaponStats("GoughsGreatbow", "Bow", "Greatbow", 9021000, 1361, 4400, 0, 14, 44, 83) },

            // Crossbows
            { "LightCrossbow", new WeaponStats("LightCrossbow", "Crossbow", "Crossbow", 1250000, 1401, 4600, 0, 16, 46, 0) },
            { "HeavyCrossbow", new WeaponStats("HeavyCrossbow", "Crossbow", "Crossbow", 1251000, 1402, 4600, 0, 16, 46, 129) },
            { "SniperCrossbow", new WeaponStats("SniperCrossbow", "Crossbow", "Crossbow", 1253000, 1404, 4600, 0, 16, 46, 85) },
            { "Avelyn", new WeaponStats("Avelyn", "Crossbow", "Crossbow", 1252000, 1405, 4600, 0, 16, 46, 84) },

            // Shields
            { "TargetShield", new WeaponStats("TargetShield", "Shield", "Shield", 1404000, 1501, 4801, 0, 15, 48, 91) },
            { "HollowSoldierShield", new WeaponStats("HollowSoldierShield", "Shield", "Shield", 1454000, 1502, 4800, 0, 15, 48, 0) },
            { "CrackedRoundShield", new WeaponStats("CrackedRoundShield", "Shield", "Shield", 1406000, 1503, 4801, 0, 15, 48, 0) },
            { "BalderShield", new WeaponStats("BalderShield", "Shield", "Shield", 1455000, 1504, 4800, 0, 15, 48, 0) },
            { "SpikedShield", new WeaponStats("SpikedShield", "Shield", "Shield", 1470000, 1507, 4803, 0, 15, 48, 93) },
            { "CrystalShield", new WeaponStats("CrystalShield", "Shield", "Shield", 1471000, 1509, 4800, 0, 15, 48, 93) },
            { "SunlightShield", new WeaponStats("SunlightShield", "Shield", "Shield", 1472000, 1511, 4800, 0, 15, 48, 0) },
            { "TowerKiteShield", new WeaponStats("TowerKiteShield", "Shield", "Shield", 1452000, 1513, 4800, 0, 15, 48, 0) },
            { "BlackKnightShield", new WeaponStats("BlackKnightShield", "Shield", "Shield", 1474000, 1514, 4800, 0, 15, 48, 0) },
            { "HeaterShield", new WeaponStats("HeaterShield", "Shield", "Shield", 1450000, 1515, 4800, 0, 15, 48, 0) },
            { "KnightShield", new WeaponStats("KnightShield", "Shield", "Shield", 1451000, 1516, 4800, 0, 15, 48, 0) },
            { "GrassCrestShield", new WeaponStats("GrassCrestShield", "Shield", "Shield", 1453000, 1517, 4800, 0, 15, 48, 0) },
            { "RedandWhiteRoundShield", new WeaponStats("RedandWhiteRoundShield", "Shield", "Shield", 1476000, 1518, 4801, 0, 15, 48, 0) },
            { "IronRoundShield", new WeaponStats("IronRoundShield", "Shield", "Shield", 1461000, 1519, 4800, 0, 15, 48, 0) },
            { "SpiderShield", new WeaponStats("SpiderShield", "Shield", "Shield", 1462000, 1520, 4800, 0, 15, 48, 0) },
            { "EastWestShield", new WeaponStats("EastWestShield", "Shield", "Shield", 1400000, 1521, 4800, 0, 15, 48, 0) },
            { "WoodenShield", new WeaponStats("WoodenShield", "Shield", "Shield", 1401000, 1522, 4800, 0, 15, 48, 0) },
            { "PlankShield", new WeaponStats("PlankShield", "Shield", "Shield", 1409000, 1523, 4801, 0, 15, 48, 0) },
            { "LargeLeatherShield", new WeaponStats("LargeLeatherShield", "Shield", "Shield", 1402000, 1524, 4800, 0, 15, 48, 0) },
            { "SmallLeatherShield", new WeaponStats("SmallLeatherShield", "Shield", "Shield", 1403000, 1525, 4801, 0, 15, 48, 0) },
            { "LeatherShield", new WeaponStats("LeatherShield", "Shield", "Shield", 1408000, 1526, 4801, 0, 15, 48, 0) },
            { "Buckler", new WeaponStats("Buckler", "Shield", "Shield", 1405000, 1528, 4801, 0, 15, 48, 91) },
            { "PierceShield", new WeaponStats("PierceShield", "Shield", "Shield", 1475000, 1530, 4803, 0, 15, 48, 93) },
            { "CrystalRingShield", new WeaponStats("CrystalRingShield", "Shield", "Shield", 1411000, 1531, 4802, 0, 15, 48, 92) },
            { "SilverKnightShield", new WeaponStats("SilverKnightShield", "Shield", "Shield", 1473000, 1533, 4800, 0, 15, 48, 0) },
            { "CrestShield", new WeaponStats("CrestShield", "Shield", "Shield", 1456000, 1535, 4800, 0, 15, 48, 0) },
            { "WarriorsRoundShield", new WeaponStats("WarriorsRoundShield", "Shield", "Shield", 1460000, 1536, 4801, 0, 15, 48, 0) },
            { "CaduceusKiteShield", new WeaponStats("CaduceusKiteShield", "Shield", "Shield", 1477000, 1537, 4800, 0, 15, 48, 0) },
            { "CaduceusRoundShield", new WeaponStats("CaduceusRoundShield", "Shield", "Shield", 1410000, 1538, 4801, 0, 15, 48, 0) },
            { "GargoylesShield", new WeaponStats("GargoylesShield", "Shield", "Shield", 1478000, 1539, 4800, 0, 15, 48, 0) },
            { "DragonCrestShield", new WeaponStats("DragonCrestShield", "Shield", "Shield", 1457000, 1541, 4800, 0, 15, 48, 0) },
            { "EffigyShield", new WeaponStats("EffigyShield", "Shield", "Shield", 9000000, 1542, 4801, 0, 15, 48, 0) },
            { "Sanctus", new WeaponStats("Sanctus", "Shield", "Shield", 9001000, 1543, 4800, 0, 15, 48, 0) },
            { "Bloodshield", new WeaponStats("Bloodshield", "Shield", "Shield", 9002000, 1544, 4800, 0, 15, 48, 0) },

            // Greatshields
            { "TowerShield", new WeaponStats("TowerShield", "Shield", "Greatshield", 1501000, 1505, 4700, 0, 15, 47, 0) },
            { "StoneGreatshield", new WeaponStats("StoneGreatshield", "Shield", "Greatshield", 1503000, 1510, 4700, 0, 15, 47, 0) },
            { "GiantShield", new WeaponStats("GiantShield", "Shield", "Greatshield", 1502000, 1527, 4700, 0, 15, 47, 0) },
            { "HavelsGreatshield", new WeaponStats("HavelsGreatshield", "Shield", "Greatshield", 1505000, 1532, 4700, 0, 15, 47, 94) },
            { "GreatshieldofArtorias", new WeaponStats("GreatshieldofArtorias", "Shield", "Greatshield", 1507000, 1534, 4700, 0, 15, 47, 0) },
            { "EagleShield", new WeaponStats("EagleShield", "Shield", "Greatshield", 1500000, 1529, 4701, 0, 15, 47, 0) },
            { "BonewheelShield", new WeaponStats("BonewheelShield", "Shield", "Greatshield", 1506000, 1540, 4702, 0, 15, 47, 126) },
            { "BlackIronGreatshield", new WeaponStats("BlackIronGreatshield", "Shield", "Greatshield", 9003000, 1545, 4700, 0, 15, 47, 0) },
            { "CleansingGreatshield", new WeaponStats("CleansingGreatshield", "Shield", "Greatshield", 9014000, 1550, 4700, 0, 15, 47, 0) },

            // Ammo
            { "GoughsGreatArrow", new WeaponStats("GoughsGreatArrow", "Ammo", "Arrow", 2008000, 1399, 1008, 0, 0, 0, 0) },
            { "Arrow", new WeaponStats("Arrow", "Ammo", "Arrow", 2099000, 2025, 1000, 0, 0, 0, 0) },
            { "Bolt", new WeaponStats("Bolt", "Ammo", "Bolt", 2199000, 2026, 1100, 0, 0, 0, 0) },
            { "LightningBolt", new WeaponStats("LightningBolt", "Ammo", "Bolt", 2104000, 1700, 1104, 0, 0, 0, 0) },
        };

        public static Dictionary<int, string> MeleeBehaviorSubNames = new Dictionary<int, string>()
        {
            { 0, "1H normal attack 1" },  // 3000 / 3030 (too heavy)
            { 1, "1H normal attack 1 (AoE)" },  // 3300 usually
            { 10, "1H normal attack 2" },  // 3001
            { 20, "1H normal attack 3" },  // 3002
            { 30, "1H jump attack" },  // 3600
            { 40, "1H plunging attack (in air)" },  // 3800 / 3801
            { 50, "1H plunging attack (hit ground)" },  // 3810
            { 100, "1H strong attack 1" },  // 3300 / 3301 / 3305 (not enough dur. for special attack)
            { 101, "1H strong attack 1 (AoE)" },
            { 110, "1H strong attack 2" },  // 3310
            { 120, "1H strong attack 1 (special)" },  // 3300 / 3301
            { 130, "1H strong attack 2 (special)" },  // probably 3310 (param exists for most special weapons but never called in TAE)
            { 200, "2H normal attack 1" },  // 4000 / 4030
            { 210, "2H normal attack 2" },  // 4001
            { 220, "2H normal attack 3" },  // 4002
            { 230, "2H jump attack" },  // 4600
            { 240, "2H plunging attack (in air)" },
            { 250, "2H plunging attack (impact)" },
            { 300, "2H strong attack 1" },  // 4300 / 4305 (not enough durability for special attack)
            { 301, "2H strong attack 1 (AoE)" },  // for bit hits. 4300 / 4305 (not enough durability for special attack)
            { 310, "2H strong attack 2" },  // 4310 / 4315 (not enough durability for special attack)
            { 311, "2H strong attack 2 (strong)" },  // 4310 (Gold Tracer)
            { 320, "2H strong attack 1 (special)" },  // 4300 (special attacks)
            { 330, "2H strong attack 2 (special)" },  // 4310 (Dragon Greatsword special attack)
            { 400, "Left-handed" },  // 5000+
            { 401, "Left-handed strong" },  // 5000+ (Gold Tracer)
            { 405, "Left-handed (with special)" },  // 5000+ (Dark Hand and Crystal Ring Shield)
            { 410, "1H kick" },  // 3100
            { 420, "2H kick" },  // 4100
            { 430, "1H guard" },
            { 440, "2H guard" },
            { 450, "Parry" },  // 5100
            { 460, "Guarding attack" },  // 3010 / 3011 / 3012
            { 490, "Plunging attack" },  // 3820
            { 500, "Backstab" },  // 3400
            { 501, "Backstab (second hit)" },  // 3400 (some weapons)
            { 505, "Strong backstab" },
            { 506, "Strong backstab (second hit)" },  // 3400 (some weapons)
            { 510, "Riposte" },  // 3201 / 3203 / 3980 (coffin stab)
            { 511, "Riposte (second hit)" },  // 3201 / 3203 (some weapons)
            { 515, "Strong riposte" },  // 3202, possibly?
            { 516, "Strong riposte (second hit)" },  // 3202 (most weapons)
            { 517, "Strong riposte (third hit)" },  // 3202 (some weapons)
            { 520, "1H running attack" },  // 3500
            { 521, "1H running attack (end of charge)" },  // 3500 (Pike, shields)
            { 530, "2H running attack" },  // 4500
            { 531, "2H running attack (end of charge)" },  // 3500 (Pike, shields)
            { 540, "1H backstep attack" },  // 3900
            { 580, "2H backstep attack" },  // 4900
            { 600, "Parry guard" },  // "failed parry" guard I think
            { 700, "Ladder (right hand)" },
            { 701, "Ladder (left hand)" },
            { 702, "Ladder (right foot)" },
            { 703, "Ladder (left foot)" },
            { 800, "Special bullet" },  // used by some special weapons, like Dragonslayer Spear R2 (3300)
            // Animations 900 to 908 are some kind of "Ryuken" Fists variant. Not using this special category (117).
        };


        Random Rand { get; }
        WeaponNameGenerator NameGenerator { get; }
        WeaponDescriptionGenerator DescriptionGenerator { get; }
        SoulsMod Mod { get; }

        string DebugCurrentClass { get; set; } = "";
        int SortIndex { get; set; } = 0;

        const double LegendaryOdds = 0.2;
        const double WeaponSpecialAnimationOdds = 0.75;
        const double CatalystSpecialAnimationOdds = 0.4;
        const double ShieldSpecialAnimationOdds = 0.8;
        // Talisman, Bow, and Crossbow specials depend on legendary status.

        List<int> LegendaryShieldSpecials { get; } = new List<int>() { 92, 94, 126 };  // Crystal Ring, Havel's, Bonewheel
        Behavior BulletBehaviorTemplate { get => Mod.VanillaGPARAM.BehaviorsPC[103603800]; }

        const int MeleeWeaponCount = 90;
        const int CatalystCount = 15;
        const int TalismanCount = 12;
        const int BowCount = 10;
        const int CrossbowCount = 8;
        const int ShieldCount = 65;

        const int AbyssalMeleeWeaponCount = 10;
        const int AbyssalCatalystCount = 2;
        const int AbyssalTalismanCount = 2;
        const int AbyssalBowCount = 2;
        const int AbyssalCrossbowCount = 1;
        const int AbyssalShieldCount = 7;

        List<int> UsedSpecialCategories { get; } = new List<int>();
        public List<int> GenericWeapons { get; } = new List<int>();
        public List<int> LegendaryWeapons { get; } = new List<int>();
        public List<int> AbyssalWeapons { get; } = new List<int>();

        public int GetRandomWeaponID(bool generic, bool legendary, bool abyssal, (Upgrade upgrade, double odds)[] upgradeOptions)
        {
            List<int> options = new List<int>();
            if (generic)
                options.AddRange(GenericWeapons);
            if (legendary)
                options.AddRange(LegendaryWeapons);
            if (abyssal)
                options.AddRange(AbyssalWeapons);

            if (!options.Any())
                throw new Exception("No weapons to choose from. WeaponSetup.Install() has likely not been run.");

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
                    {
                        if (Mod.GPARAM.Weapons.Keys.Contains(chosenID + (int)upgrade))
                            return chosenID + (int)upgrade;
                        else
                            return chosenID;  // no upgrade available (e.g. Catalyst)
                    }
                }
                return chosenID;  // No upgrade.
            }
        }

        public WeaponGenerator(SoulsMod mod, Random random = null)
        {
            Rand = random ?? new Random();
            Mod = mod;
            NameGenerator = new WeaponNameGenerator(Rand);
            DescriptionGenerator = new WeaponDescriptionGenerator(Rand);
        }

        public void Install()
        {
            CreateRandomWeapons();
            AdjustWeaponUpgrades();
            CreateStartingWeapons();
        }


        public static Dictionary<string, int> FixedWeapons { get; } = new Dictionary<string, int>()
        {
            { "Longsword",              1000 },
            { "Wooden Shield",          2000 },
            { "Broadsword",             3000 },
            { "Tower Kite Shield",      4000 },
            { "Scimitar",               5000 },
            { "Leather Shield",         6000 },
            { "Bandit's Knife",         7000 },
            { "Target Shield",          8000 },
            { "Battle Axe",             9000 },
            { "Spider Shield",          10000 },
            { "Pyromancy Flame",        11000 },
            { "Shortsword",             12000 },
            { "Short Bow",              13000 },
            { "Large Leather Shield",   14000 },
            { "Dagger",       15000 },
            { "Small Leather Shield",   16000 },
            { "Sorcerer's Catalyst",    17000 },
            { "Mace",                   18000 },
            { "East-West Shield",       19000 },
            { "Canvas Talisman",        20000 },
            { "Skull Lantern",          21000 },
        };

        void CreateStartingWeapons()
        {
            // Warrior class
            int behaviorVarId = 500;
            Weapon longsword = StartingWeaponSetup(201000, FixedWeapons["Longsword"], ref behaviorVarId);
            CreateAllMeleeUpgrades(longsword);
            Weapon woodenShield = StartingWeaponSetup(1401000, FixedWeapons["Wooden Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(woodenShield);

            // Knight class
            Weapon broadsword = StartingWeaponSetup(202000, FixedWeapons["Broadsword"], ref behaviorVarId);
            CreateAllMeleeUpgrades(broadsword);
            Weapon towerKiteShield = StartingWeaponSetup(1452000, FixedWeapons["Tower Kite Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(towerKiteShield);

            // Wanderer class
            Weapon scimitar = StartingWeaponSetup(400000, FixedWeapons["Scimitar"], ref behaviorVarId);
            scimitar.RequiredDexterity = 12;
            CreateAllMeleeUpgrades(scimitar);
            Weapon leatherShield = StartingWeaponSetup(1408000, FixedWeapons["Leather Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(leatherShield);

            // Thief class
            Weapon banditsKnife = StartingWeaponSetup(103000, FixedWeapons["Bandit's Knife"], ref behaviorVarId);
            CreateAllMeleeUpgrades(banditsKnife);
            Weapon targetShield = StartingWeaponSetup(1404000, FixedWeapons["Target Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(targetShield);

            // Barbarian class
            Weapon battleAxe = StartingWeaponSetup(701000, FixedWeapons["Battle Axe"], ref behaviorVarId);
            CreateAllMeleeUpgrades(battleAxe);
            Weapon spiderShield = StartingWeaponSetup(1462000, FixedWeapons["Spider Shield"], ref behaviorVarId);
            spiderShield.PhysicalGuardPercentage = 90.0f;
            CreateAllShieldUpgrades(spiderShield);
            StartingWeaponSetup(1330000, FixedWeapons["Pyromancy Flame"], ref behaviorVarId);
            // Does NOT start with any pyromancies.

            // Hunter class
            Weapon shortsword = StartingWeaponSetup(200000, FixedWeapons["Shortsword"], ref behaviorVarId);
            CreateAllMeleeUpgrades(shortsword);
            Weapon shortBow = StartingWeaponSetup(1200000, FixedWeapons["Short Bow"], ref behaviorVarId);
            CreateAllBowUpgrades(shortBow);
            Weapon largeLeatherShield = StartingWeaponSetup(1402000, FixedWeapons["Large Leather Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(largeLeatherShield);
            // Also starts with 40 Standard Arrows.

            // Sorcerer class
            Weapon dagger = StartingWeaponSetup(100000, FixedWeapons["Dagger"], ref behaviorVarId);
            CreateAllMeleeUpgrades(dagger);
            Weapon smallLeatherShield = StartingWeaponSetup(1403000, FixedWeapons["Small Leather Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(smallLeatherShield);
            StartingWeaponSetup(1300000, FixedWeapons["Sorcerer's Catalyst"], ref behaviorVarId);
            
            // Cleric class
            Weapon mace = StartingWeaponSetup(801000, FixedWeapons["Mace"], ref behaviorVarId);
            CreateAllMeleeUpgrades(mace);
            Weapon eastWestShield = StartingWeaponSetup(1400000, FixedWeapons["East-West Shield"], ref behaviorVarId);
            CreateAllShieldUpgrades(eastWestShield);
            StartingWeaponSetup(1361000, FixedWeapons["Canvas Talisman"], ref behaviorVarId);
            
            StartingWeaponSetup(1396000, FixedWeapons["Skull Lantern"], ref behaviorVarId);

            // Solaire
            behaviorVarId = 600;
            StartingWeaponSetup(206000, 50000, ref behaviorVarId);  // Sunlight Straight Sword
            StartingWeaponSetup(1365000, 51000, ref behaviorVarId);  // Sunlight Shield
            StartingWeaponSetup(1472000, 52000, ref behaviorVarId);  // Sunlight Talisman

            // Siegmeyer
            StartingWeaponSetup(350000, 53000, ref behaviorVarId);  // Zweihander
            StartingWeaponSetup(1475000, 54000, ref behaviorVarId);  // Pierce Shield

            // Logan
            StartingWeaponSetup(1303000, 55000, ref behaviorVarId);  // Logan's Catalyst
            StartingWeaponSetup(400000, 56000, ref behaviorVarId);
            StartingWeaponSetup(1403000, 57000, ref behaviorVarId);

            // Quelana
            StartingWeaponSetup(1332000, 58000, ref behaviorVarId);  // Pyromancy Flame (Ascended)

            // Havel
            StartingWeaponSetup(854000, 59000, ref behaviorVarId);  // Dragon Tooth
            StartingWeaponSetup(1505000, 60000, ref behaviorVarId);  // Havel's Greatshield
        }

        void CreateRandomWeapons()
        {
            int weaponIndex = 0;
            DebugCurrentClass = "melee weapon";
            for (int i = 0; i < MeleeWeaponCount; i++)
                CreateWeaponFromFunction(CreateMeleeWeapon, ref weaponIndex, false);

            DebugCurrentClass = "catalyst";
            for (int i = 0; i < CatalystCount; i++)
                CreateWeaponFromFunction(CreateCatalyst, ref weaponIndex, false);

            DebugCurrentClass = "talisman";
            for (int i = 0; i < TalismanCount; i++)
                CreateWeaponFromFunction(CreateTalisman, ref weaponIndex, false);

            DebugCurrentClass = "bow";
            for (int i = 0; i < BowCount; i++)
                CreateWeaponFromFunction(CreateBow, ref weaponIndex, false);

            DebugCurrentClass = "crossbow";
            for (int i = 0; i < CrossbowCount; i++)
                CreateWeaponFromFunction(CreateCrossbow, ref weaponIndex, false);

            DebugCurrentClass = "shield";
            for (int i = 0; i < ShieldCount; i++)
                CreateWeaponFromFunction(CreateShield, ref weaponIndex, false);

            DebugCurrentClass = "abyssal weapon/shield";
            for (int i = 0; i < AbyssalMeleeWeaponCount; i++)
                CreateWeaponFromFunction(CreateMeleeWeapon, ref weaponIndex, true);
            for (int i = 0; i < AbyssalCatalystCount; i++)
                CreateWeaponFromFunction(CreateCatalyst, ref weaponIndex, true);
            for (int i = 0; i < AbyssalTalismanCount; i++)
                CreateWeaponFromFunction(CreateTalisman, ref weaponIndex, true);
            for (int i = 0; i < AbyssalBowCount; i++)
                CreateWeaponFromFunction(CreateBow, ref weaponIndex, true);
            for (int i = 0; i < AbyssalCrossbowCount; i++)
                CreateWeaponFromFunction(CreateCrossbow, ref weaponIndex, true);
            for (int i = 0; i < AbyssalShieldCount; i++)
                CreateWeaponFromFunction(CreateShield, ref weaponIndex, true);

            // Delete remaining (vanilla) weapon params (except Fists, arrows, and bolts).
            int lastWeaponParam = 100000 + (1000 * (weaponIndex + 1));
#if DEBUG
            Console.WriteLine($"Deleting all weapons from {lastWeaponParam} (except Fists, arrows, and bolts)");
#endif
            Mod.GPARAM.Weapons.DeleteRowWhereID(id => id >= lastWeaponParam && id < 2000000 && id != VanillaWeapons["Fists"].ParamId);

            // Delete remaining (vanilla) behavior params (except Fists).
            int lastBehaviorParam = 102000000 + (1000 * (weaponIndex + 1));
#if DEBUG
            Console.WriteLine($"Deleting all PC behaviors from {lastBehaviorParam}");
#endif
            Mod.GPARAM.BehaviorsPC.DeleteRowWhereID(id => id >= lastBehaviorParam && !(104201000 <= id && id < 104202000));

            // Delete remaining (vanilla) attack params (except Fists).
            int lastAttackParam = 2000000 + (1000 * (weaponIndex + 1));
#if DEBUG
            Console.WriteLine($"Deleting all PC attacks from {lastAttackParam}");
#endif
            Mod.GPARAM.AttacksPC.DeleteRowWhereID(id => id >= lastAttackParam && !(4200000 <= id && id < 4201000));
        }

        void CreateWeaponFromFunction(Action<int, int, bool, bool> createWeaponFunc, ref int weaponIndex, bool isAbyssal = false)
        {
            int weaponParamId = 100000 + (1000 * weaponIndex);
#if DEBUG
            Console.WriteLine($"Creating {DebugCurrentClass} {weaponParamId}...");
#endif
            int behaviorVarId = 2000 + weaponIndex;
            bool isLegendary = Rand.NextDouble() < LegendaryOdds;
            createWeaponFunc(weaponParamId, behaviorVarId, isLegendary, isAbyssal);
            if (isAbyssal)
                AbyssalWeapons.Add(weaponParamId);
            else if (isLegendary)
                LegendaryWeapons.Add(weaponParamId);
            else
                GenericWeapons.Add(weaponParamId);
            weaponIndex++;
        }

        WeaponStats GetRandomVanillaWeapon(string weaponClass, string weaponSubclass = "")
        {
            List<KeyValuePair<string, WeaponStats>> meleeWeapons;
            if (weaponSubclass == "")
            {
                meleeWeapons = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == weaponClass));
            }
            else
            {
                meleeWeapons = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == weaponClass && kv.Value.WeaponSubclass == weaponSubclass));
            }
            return meleeWeapons.GetRandomElement(Rand).Value;
        }

        public void CreateMeleeWeapon(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            // TODO: Some special attacks may not be compatible with some models (e.g. Dragonslayer Spear R2 with sword).

            WeaponStats modelWeaponStats = GetRandomVanillaWeapon("Melee");
            WeaponStats baseWeaponStats = GetRandomVanillaWeapon("Melee");
            WeaponStats specialWeaponStats = null;
            if (Rand.NextDouble() < WeaponSpecialAnimationOdds)
            {
                var specialWeaponChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == "Melee" && kv.Value.SpecialAttackAnimationCategory > 0 && !UsedSpecialCategories.Contains(kv.Value.SpecialAttackAnimationCategory)));
                if (specialWeaponChoices.Count > 0)
                    specialWeaponStats = specialWeaponChoices.GetRandomElement(Rand).Value;
            }


            isLegendary |= isAbyssal;
            LegendaryMeleeEffects legendaryEffects = isLegendary ? new LegendaryMeleeEffects(isAbyssal, specialWeaponStats != null, Rand) : null;
            double staminaCostMultiplier = legendaryEffects != null ? legendaryEffects.GetStaminaMultiplier() : 1.0;

            Weapon newWeapon = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);

            // Behaviors and Attacks are copied from special weapon if present, and base weapon otherwise,
            // except that Attack hitbox information is taken from model weapon. Special bullet (800) is ignored.
            for (int subId = 0; subId < 1000; subId++)
            {
                if (subId == 800 || subId == 801)
                    continue;  // Special bullet; don't copy it.
                if (subId >= 900)
                    continue;  // Unused "Ryuken" Fists variant from TAE category 117; ignore.
                string behaviorName = $"{newWeapon.Name} ({subId})";
                Attack newAttack = BasicBehaviorAttackSetup(behaviorVarId, subId, behaviorName, modelWeaponStats, baseWeaponStats, specialWeaponStats, staminaCostMultiplier);
                if (newAttack != null && !MeleeBehaviorSubNames.ContainsKey(subId))
                    throw new Exception($"Unrecognized melee attack sub ID: {subId} ({baseWeaponStats.NameID} | {specialWeaponStats?.NameID}");
                if (newAttack != null && legendaryEffects != null)
                    legendaryEffects.CheckAndApplyHighImpact(newAttack);
            }

            if (isLegendary)
            {
                // Apply standard legendary effects (including Special Bullet) after behavior setup.
                TAE specialAnimationTAE = specialWeaponStats != null ? Mod.Player.GetTAE(specialWeaponStats.SpecialAttackAnimationCategory) : null;
                Behavior bulletBehavior = null;
                if (specialAnimationTAE != null)
                {
                    int bulletBehaviorId = 100000000 + 1000 * behaviorVarId + 800;
                    // Create bullet. (Existing behavior 800 should not have been copied.)
                    bulletBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(BulletBehaviorTemplate, bulletBehaviorId);
                    bulletBehavior.VariationID = behaviorVarId;
                    bulletBehavior.DurabilityCost = 20;
                    bulletBehavior.BehaviorSubID = 800;
                }
                legendaryEffects.ApplyEffects(newWeapon, specialAnimationTAE, bulletBehavior);
            }

            // Generate all upgrade weapon param IDs.
            CreateAllMeleeUpgrades(newWeapon);
        }

        public void CreateCatalyst(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            isLegendary |= isAbyssal;
            LegendaryCatalystEffects legendaryEffects = isLegendary ? new LegendaryCatalystEffects(isAbyssal, Rand) : null;

            // Basically the same algorithm as melee weapons. Random model, random base, random special.
            // Special override can come from any melee weapon for Abyssal Talismans.
            WeaponStats modelWeaponStats = GetRandomVanillaWeapon("Catalyst");
            WeaponStats baseWeaponStats = GetRandomVanillaWeapon("Catalyst");
            WeaponStats specialWeaponStats = null;
            if (isAbyssal)
            {
                // Special animations from melee weapon.
                var specialWeaponChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == "Melee" && kv.Value.SpecialAttackAnimationCategory > 0));
                if (specialWeaponChoices.Count > 0)
                    specialWeaponStats = specialWeaponChoices.GetRandomElement(Rand).Value;
            }
            else if (Rand.NextDouble() < CatalystSpecialAnimationOdds)
            {
                var specialWeaponChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == "Catalyst" && kv.Value.SpecialAttackAnimationCategory > 0));
                if (specialWeaponChoices.Count > 0)
                    specialWeaponStats = specialWeaponChoices.GetRandomElement(Rand).Value;
            }

            Weapon newWeapon = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);

            for (int subId = 0; subId < 1000; subId++)
            {
                if (specialWeaponStats != null && specialWeaponStats.WeaponClass == "Melee" && subId >= 800)
                    continue;  // Skip melee bullets and Ryuken stuff.
                BasicBehaviorAttackSetup(behaviorVarId, subId, $"{newWeapon.Name} ({subId})", modelWeaponStats, baseWeaponStats, specialWeaponStats);
            }

            if (isLegendary)
                legendaryEffects.ApplyEffects(newWeapon);

            // No upgrade variants.
        }

        public void CreateTalisman(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            isLegendary |= isAbyssal;
            LegendaryTalismanEffects legendaryEffects = isLegendary ? new LegendaryTalismanEffects(isAbyssal, Rand) : null;

            // TODO: Need to confirm that Talisman can still cast spells with base as Fists!

            // Model is any Talisman. Base is Fists (if legendary) or random Talisman (all the same anyway).
            // Special may be Dragon Bone Fist for legendary weapons; null otherwise.
            WeaponStats modelWeaponStats = GetRandomVanillaWeapon("Talisman");
            WeaponStats baseWeaponStats = VanillaWeapons["Fists"];  // TODO: isLegendary ? VanillaWeapons["Fists"] : GetRandomVanillaWeapon("Talisman");
            WeaponStats specialWeaponStats = (legendaryEffects != null && legendaryEffects.EffectPoints["DragonBoneFistSpecial"] == 1) ? VanillaWeapons["DragonBoneFist"] : null;

            Weapon newWeapon = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);

            for (int subId = 0; subId < 1000; subId++)
            {
                if (subId >= 800 && (baseWeaponStats.WeaponClass == "Melee" || (specialWeaponStats != null && specialWeaponStats.WeaponClass == "Melee")))
                    continue;  // if Fists were chosen, skip unused Ryuken Fists variant.
                BasicBehaviorAttackSetup(behaviorVarId, subId, $"{newWeapon.Name} ({subId})", modelWeaponStats, baseWeaponStats, specialWeaponStats);
            }

            if (isLegendary)
                legendaryEffects.ApplyEffects(newWeapon);

            // No upgrade variants.
        }

        public void CreateBow(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            isLegendary |= isAbyssal;
            LegendaryBowCrossbowEffects legendaryEffects = isLegendary ? new LegendaryBowCrossbowEffects(isAbyssal, isCrossbow: false, Rand) : null;
            bool isGreatbow = legendaryEffects != null && legendaryEffects.EffectPoints["IsGreatbow"] == 1;
            double staminaCostMultiplier = legendaryEffects != null ? legendaryEffects.GetStaminaMultiplier() : 1.0;

            WeaponStats modelWeaponStats = GetRandomVanillaWeapon("Bow", isGreatbow ? "Greatbow" : "Bow");
            WeaponStats baseWeaponStats = GetRandomVanillaWeapon("Bow", isGreatbow ? "Greatbow" : "Bow");
            WeaponStats specialWeaponStats = GetRandomVanillaWeapon("Bow", isGreatbow ? "Greatbow" : "Bow");

            Weapon newBow = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);
            newBow.BowRangeChangePercentage = specialWeaponStats.GetWeaponParam(Mod.VanillaGPARAM).BowRangeChangePercentage;

            // Behaviors and Attacks are copied from special weapon if present, and base weapon otherwise,
            // except that Attack hitbox information is taken from model weapon.
            for (int subId = 0; subId < 1000; subId++)
            {
                if (subId == 300)
                {
                    // Arrow bullet. Just points to bullet 200 ("versatile treatment"), which somehow triggers the arrow projectile.
                    // Arrow choice/launch could be handled in character ESD. But this could still trigger stamina loss.
                    Behavior sourceBehavior = (specialWeaponStats ?? baseWeaponStats).GetBehaviorParam(Mod.VanillaGPARAM, subId);
                    Behavior newBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(sourceBehavior, 100000000 + 1000 * behaviorVarId + subId);
                    newBehavior.BehaviorSubID = subId;
                    newBehavior.VariationID = behaviorVarId;
                    newBehavior.Name = $"{newBow.Name} (Shoot)";
                    newBehavior.StaminaCost = (int)(newBehavior.StaminaCost * staminaCostMultiplier);
                }
                else
                {
                    BasicBehaviorAttackSetup(behaviorVarId, subId, $"{newBow.Name} ({subId})", modelWeaponStats, baseWeaponStats, specialWeaponStats, staminaCostMultiplier);
                }
            }

            if (isLegendary)
                legendaryEffects.ApplyEffects(newBow);

            // Generate all upgrade weapon param IDs.
            CreateAllBowUpgrades(newBow);
        }

        public void CreateCrossbow(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            isLegendary |= isAbyssal;
            LegendaryBowCrossbowEffects legendaryEffects = isLegendary ? new LegendaryBowCrossbowEffects(isAbyssal, isCrossbow: true, Rand) : null;
            bool isAvelyn = legendaryEffects != null && legendaryEffects.EffectPoints["IsAvelyn"] == 1;

            WeaponStats modelWeaponStats;
            WeaponStats baseWeaponStats;
            WeaponStats specialWeaponStats;
            if (isAvelyn)
            {
                modelWeaponStats = VanillaWeapons["Avelyn"];
                baseWeaponStats = VanillaWeapons["Avelyn"];
                specialWeaponStats = VanillaWeapons["Avelyn"];
            }
            else
            {
                // Model, base, and special are independently drawn from Light/Heavy/Sniper crossbow.
                var crossbowChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == "Crossbow" && kv.Key != "Avelyn"));
                modelWeaponStats = crossbowChoices.GetRandomElement(Rand).Value;
                baseWeaponStats = crossbowChoices.GetRandomElement(Rand).Value;
                specialWeaponStats = crossbowChoices.GetRandomElement(Rand).Value;
            }

            Weapon newCrossbow = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);
            newCrossbow.BowRangeChangePercentage = specialWeaponStats.GetWeaponParam(Mod.VanillaGPARAM).BowRangeChangePercentage;
            double staminaCostMultiplier = legendaryEffects != null ? legendaryEffects.GetStaminaMultiplier() : 1.0;

            // Behaviors and Attacks are copied from special weapon if present, and base weapon otherwise,
            // except that Attack hitbox information is taken from model weapon.
            for (int subId = 0; subId < 1000; subId++)
            {
                if (subId == 0 || subId == 300 || subId == 400)
                {
                    // Bolt bullet. Just points to bullet 200 ("versatile treatment"), which somehow triggers the bolt projectile,
                    // or is just a dummy and ESD triggers the bolt (more likely).
                    Behavior sourceBehavior = (specialWeaponStats ?? baseWeaponStats).GetBehaviorParam(Mod.VanillaGPARAM, subId);
                    Behavior newBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(sourceBehavior, 100000000 + 1000 * behaviorVarId + subId);
                    newBehavior.BehaviorSubID = subId;
                    newBehavior.VariationID = behaviorVarId;
                    newBehavior.Name = $"{newCrossbow.Name} (Shoot)";
                    newBehavior.StaminaCost = (int)(newBehavior.StaminaCost * staminaCostMultiplier);
                    newBehavior.Category = (byte)(subId == 400 ? 2 : 1);  // 1 (right hand) for 0 and 300, 2 (left hand) for 400
                }
                else
                {
                    BasicBehaviorAttackSetup(behaviorVarId, subId, $"{newCrossbow.Name} ({subId})", modelWeaponStats, baseWeaponStats, specialWeaponStats);
                }
            }

            if (isLegendary)
                legendaryEffects.ApplyEffects(newCrossbow);

            // Generate upgrade weapon param IDs (excludes some categories).
            CreateCrystalVariant(newCrossbow, 8000);
            CreateLightningVariant(newCrossbow, 8000);
            // CreateRefinedVariant(newWeapon, 8000);
            CreateMagicVariant(newCrossbow, 8000);
            // CreateEnchantedVariant(newWeapon, 8000);
            CreateDivineVariant(newCrossbow, 8000);
            // CreateDireVariant(newWeapon, 8000);
            CreateFireVariant(newCrossbow, 8000);
            // CreateDraconicVariant(newWeapon, 8000);
        }

        public void CreateShield(int weaponParamId, int behaviorVarId, bool isLegendary = false, bool isAbyssal = false)
        {
            isLegendary |= isAbyssal;
            LegendaryShieldEffects legendaryEffects = isLegendary ? new LegendaryShieldEffects(isAbyssal, Rand) : null;

            WeaponStats modelWeaponStats = GetRandomVanillaWeapon("Shield");
            WeaponStats baseWeaponStats = GetRandomVanillaWeapon("Shield", modelWeaponStats.WeaponSubclass);
            WeaponStats specialWeaponStats = null;
            if (legendaryEffects != null)
            {
                if (legendaryEffects.EffectPoints["SpecialBetterParry"] == 1)
                    specialWeaponStats = VanillaWeapons[Rand.NextDouble() < 0.5 ? "Buckler" : "TargetShield"];
                else if (legendaryEffects.EffectPoints["SpecialBonewheel"] == 1)
                    specialWeaponStats = VanillaWeapons["BonewheelShield"];
                else if (legendaryEffects.EffectPoints["SpecialCrystalRing"] == 1)
                    specialWeaponStats = VanillaWeapons["CrystalRingShield"];
                else if (legendaryEffects.EffectPoints["SpecialHavel"] == 1)
                    specialWeaponStats = VanillaWeapons["HavelsGreatshield"];
                else if (legendaryEffects.EffectPoints["SpecialSuperBash"] == 1)
                {
                    // Special comes from a bashing shield (a non-special Greatshield or one of the three medium bashing shields with special 93).
                    var bashingShieldChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                        kv => kv.Value.WeaponClass == "Shield" && !LegendaryShieldSpecials.Contains(kv.Value.SpecialAttackAnimationCategory) &&
                        (kv.Value.WeaponSubclass == "Greatshield" || kv.Value.SpecialAttackAnimationCategory == 93)));
                    specialWeaponStats = bashingShieldChoices.GetRandomElement(Rand).Value;
                }
                else if (modelWeaponStats.WeaponSubclass == "Greatshield" && legendaryEffects.EffectPoints["Light"] == 1)
                {
                    // Special comes from ANY (non-special) shield.
                    var nonSpecialShieldChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                        kv => kv.Value.WeaponClass == "Shield" && !LegendaryShieldSpecials.Contains(kv.Value.SpecialAttackAnimationCategory)));
                    specialWeaponStats = nonSpecialShieldChoices.GetRandomElement(Rand).Value;
                }
            }
            if (specialWeaponStats == null && Rand.NextDouble() < ShieldSpecialAnimationOdds)
            {
                // Special comes from any shield in the same subclass except a special Greatshield.
                var nonSpecialShieldChoices = new List<KeyValuePair<string, WeaponStats>>(VanillaWeapons.Where(
                    kv => kv.Value.WeaponClass == "Shield" && kv.Value.WeaponSubclass == modelWeaponStats.WeaponSubclass
                    && !LegendaryShieldSpecials.Contains(kv.Value.SpecialAttackAnimationCategory)));
                specialWeaponStats = nonSpecialShieldChoices.GetRandomElement(Rand).Value;
            }

            Weapon newWeapon = BasicWeaponSetup(weaponParamId, behaviorVarId, legendaryEffects, modelWeaponStats, baseWeaponStats, specialWeaponStats);
            newWeapon.PhysicalGuardPercentage -= 10.0f;  // Default physical guard is reduced by 10, so only legendary shields can reach 100.
            double staminaCostMultiplier = legendaryEffects != null ? legendaryEffects.GetStaminaMultiplier() : 1.0;

            for (int subId = 0; subId < 1000; subId++)
            {
                if (subId == 800)
                {
                    if (specialWeaponStats != null && specialWeaponStats.SpecialAttackAnimationCategory == 92)
                    {
                        // Copy Crystal Ring bullet if legendary effect present.
                        Behavior sourceBehavior = specialWeaponStats.GetBehaviorParam(Mod.VanillaGPARAM, 800);
                        Behavior newBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(sourceBehavior, 100000000 + 1000 * behaviorVarId + 800);
                        newBehavior.VariationID = behaviorVarId;
                        newBehavior.Name = $"{newWeapon.Name} (Special Bullet)";
                        newBehavior.StaminaCost = (int)(newBehavior.StaminaCost * staminaCostMultiplier);
                    }
                    else
                    {
                        continue;  // Skip behavior 800 otherwise.
                    }
                }
                else
                {
                    BasicBehaviorAttackSetup(behaviorVarId, subId, $"{newWeapon.Name} ({subId})", modelWeaponStats, baseWeaponStats, specialWeaponStats, staminaCostMultiplier);
                }
            }

            if (isLegendary)
                legendaryEffects.ApplyEffects(newWeapon);

            // Offensive medium shields (93) or Bonewheel (126) use the same upgrade system as weapons (0).
            // All other shields use upgrade offset 5000.
            int upgradeOffset = (specialWeaponStats != null && specialWeaponStats.SpecialAttackAnimationCategory.In(93, 126)) ? 0 : 5000;
            // Generate upgrade weapon param IDs (excludes some categories).
            CreateAllShieldUpgrades(newWeapon, upgradeOffset);
        }

        void CreateAllShieldUpgrades(Weapon shield, int upgradeOffset = 5000)
        {
            CreateCrystalVariant(shield, upgradeOffset);
            CreateLightningVariant(shield, upgradeOffset);
            CreateMagicVariant(shield, upgradeOffset);
            CreateDivineVariant(shield, upgradeOffset);
            CreateFireVariant(shield, upgradeOffset);
        }

        void CreateAllBowUpgrades(Weapon bow)
        {
            // TODO: Would be cleaner to use 9000 for all bow upgrades! Can just copy 0 at least.
            CreateCrystalVariant(bow);
            CreateLightningVariant(bow, 9000);
            CreateRefinedVariant(bow);
            CreateMagicVariant(bow);
            CreateEnchantedVariant(bow, 9000);
            CreateDivineVariant(bow);
            CreateDireVariant(bow);
            CreateFireVariant(bow, 9000);
            CreateDraconicVariant(bow, 9000);
        }

        Weapon BasicWeaponSetup(int weaponParamId, int behaviorVarId, LegendaryEffects legendaryEffects,
            WeaponStats modelWeaponStats, WeaponStats baseWeaponStats, WeaponStats specialWeaponStats)
        {
            string weaponName = NameGenerator.GetRandomName(out _, modelWeaponStats.WeaponSubclass, legendaryEffects != null, exact: false);
            string legendaryDescription = legendaryEffects != null ? legendaryEffects.GetEffectDescription() : "";
            string weaponDesc = DescriptionGenerator.GetRandomDescription(extraParagraph: legendaryDescription, exact: false);

#if DEBUG
            //Console.WriteLine($"{modelWeaponStats.Name} -> {baseWeaponStats.Name} -> {specialWeaponStats?.Name}\n");
            //Console.WriteLine($"{weaponName}" + (legendaryEffects != null ? " (LEGENDARY)" : ""));
            //Console.WriteLine("\n" + weaponDesc);
#endif

            // Delete existing IDs in new weapon's parameter ranges.
            Mod.GPARAM.Weapons.DeleteRowRange(weaponParamId, weaponParamId + 1000);
            Mod.GPARAM.BehaviorsPC.DeleteRowRange(100000000 + 1000 * behaviorVarId, 100000000 + 1000 * (behaviorVarId + 1));
            Mod.GPARAM.AttacksPC.DeleteRowRange(1000 * behaviorVarId, 1000 * (behaviorVarId + 1));

            // Set up Weapon param entry. Most values are taken from model weapon. Some are reset to default values,
            // and animation categories and physical damage types are taken from base/special weapons.
            Weapon newWeapon = Mod.GPARAM.Weapons.CopyRow(modelWeaponStats.GetWeaponParam(Mod.VanillaGPARAM), weaponParamId);
            CleanWeaponParam(newWeapon, modelWeaponStats.WeaponSubclass);  // removes default elements, special effects, etc.
            newWeapon.Name = weaponName;
            newWeapon.Row.Name = $"<{modelWeaponStats.WeaponSubclass}|{baseWeaponStats.WeaponSubclass}> {weaponName}";
            newWeapon.Summary = modelWeaponStats.WeaponSubclass;  // TODO: Correct?
            newWeapon.Description = weaponDesc;
            newWeapon.BehaviorVariationID = behaviorVarId;
            newWeapon.SortIndex = SortIndex;
            SortIndex++;
            ApplyWeaponAnimations(newWeapon, baseWeaponStats, specialWeaponStats?.SpecialAttackAnimationCategory);
            // Physical damage type bools are each just (base || special).
            Weapon baseWeapon = baseWeaponStats.GetWeaponParam(Mod.VanillaGPARAM);
            newWeapon.DealsNeutralDamage = baseWeapon.DealsNeutralDamage;
            newWeapon.DealsStrikeDamage = baseWeapon.DealsStrikeDamage;
            newWeapon.DealsSlashDamage = baseWeapon.DealsSlashDamage;
            newWeapon.DealsThrustDamage = baseWeapon.DealsThrustDamage;
            Weapon specialWeapon = specialWeaponStats?.GetWeaponParam(Mod.VanillaGPARAM);
            if (specialWeapon != null)
            {
                newWeapon.DealsNeutralDamage |= specialWeapon.DealsNeutralDamage;
                newWeapon.DealsStrikeDamage |= specialWeapon.DealsStrikeDamage;
                newWeapon.DealsSlashDamage |= specialWeapon.DealsSlashDamage;
                newWeapon.DealsThrustDamage |= specialWeapon.DealsThrustDamage;
            }
            return newWeapon;
        }

        Weapon StartingWeaponSetup(int oldWeaponParamID, int newWeaponParamID, ref int newBehaviorVarId)
        {
            Weapon oldWeapon = Mod.VanillaGPARAM.Weapons[oldWeaponParamID];

            int newBehaviorBaseID = 100000000 + 1000 * newBehaviorVarId;
            int newAttackBaseID = 1000 * newBehaviorVarId;
#if DEBUG
            Console.WriteLine($"Creating starting weapon {newWeaponParamID} (base behavior ID {newBehaviorBaseID}, base attack ID {newAttackBaseID})");
#endif

            // Delete existing IDs in new weapon's parameter ranges (+100 only for starting weapons).
            Mod.GPARAM.Weapons.DeleteRowRange(newWeaponParamID, newWeaponParamID + 100);
            Mod.GPARAM.BehaviorsPC.DeleteRowRange(newBehaviorBaseID, 100000000 + 1000 * (newBehaviorVarId + 1));
            Mod.GPARAM.AttacksPC.DeleteRowRange(newAttackBaseID, 1000 * (newBehaviorVarId + 1));

            // Set up Weapon param entry. Most values are taken from model weapon. Some are reset to default values,
            // and animation categories and physical damage types are taken from base/special weapons.
            Weapon newWeapon = Mod.GPARAM.Weapons.CopyRow(oldWeapon, newWeaponParamID);
            CleanWeaponParam(newWeapon, "", isStartingWeapon: true);  // removes upgrades, not but special effects
            newWeapon.Name = oldWeapon.Name;
            newWeapon.Summary = oldWeapon.Summary;
            newWeapon.Description = oldWeapon.Description;
            newWeapon.BehaviorVariationID = newBehaviorVarId;
            newWeapon.SortIndex = SortIndex;
            SortIndex++;

            for (int i = 0; i < 1000; i++)
            {
                int oldBehaviorParamID = 100000000 + 1000 * oldWeapon.BehaviorVariationID + i;
                if (Mod.VanillaGPARAM.BehaviorsPC.Keys.Contains(oldBehaviorParamID))
                {
                    Behavior newBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(Mod.VanillaGPARAM.BehaviorsPC[oldBehaviorParamID], newBehaviorBaseID + i);
                    newBehavior.RefID = newAttackBaseID + i;
                    newBehavior.VariationID = newBehaviorVarId;
                    int oldAttackParamID = Mod.VanillaGPARAM.BehaviorsPC[oldBehaviorParamID].RefID;
                    if (Mod.VanillaGPARAM.AttacksPC.Keys.Contains(oldAttackParamID))
                        Mod.GPARAM.AttacksPC.CopyRow(Mod.VanillaGPARAM.AttacksPC[oldAttackParamID], newAttackBaseID + i);
                }               
            }

            newBehaviorVarId++;
            return newWeapon;
        }

        void CreateAllMeleeUpgrades(Weapon weapon)
        {
            // Generate all upgrade weapon param IDs.
            CreateCrystalVariant(weapon);
            CreateLightningVariant(weapon);
            CreateRefinedVariant(weapon);
            CreateMagicVariant(weapon);
            CreateEnchantedVariant(weapon);
            CreateDivineVariant(weapon);
            CreateDireVariant(weapon);
            CreateFireVariant(weapon);
            CreateDraconicVariant(weapon);
        }

        Weapon CreateWeaponUpgrade(Weapon weapon, int upgradeOffset, int upgradeIdOffset = 0)
        {
            Weapon variant = Mod.GPARAM.Weapons.CopyRow(weapon, (int)weapon.ID + upgradeOffset);
            variant.SortIndex = SortIndex;
            SortIndex++;
            variant.UpgradeOrigin0 = (int)weapon.ID;
            variant.UpgradeMaterialsID = upgradeOffset;
            variant.WeaponUpgradeID = (short)(upgradeIdOffset + upgradeOffset);
            return variant;
        }
        void CreateCrystalVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon crystalWeapon = CreateWeaponUpgrade(weapon, 100, upgradeIdOffset);
            crystalWeapon.Name = "Crys. " + weapon.Name;
            crystalWeapon.Summary = weapon.Summary;
            crystalWeapon.Description = weapon.Description;
            crystalWeapon.InitialDurability = (ushort)(weapon.InitialDurability / 10);
            crystalWeapon.MaxDurability = (ushort)(weapon.MaxDurability / 10);
            crystalWeapon.IsUpgraded = true;  // not sure what this does
            crystalWeapon.DisableBaseChangeReset = true;
            crystalWeapon.DisableRepairs = true;
            crystalWeapon.BaseChangeCategory = 5;
        }
        void CreateLightningVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon lightningWeapon = CreateWeaponUpgrade(weapon, 200, upgradeIdOffset);
            lightningWeapon.Name = "Ltn. " + weapon.Name;
            lightningWeapon.Summary = weapon.Summary;
            lightningWeapon.Description = weapon.Description;
            lightningWeapon.StrengthScaling = 0.0f;
            lightningWeapon.DexterityScaling = 0.0f;
            lightningWeapon.IntelligenceScaling = 0.0f;
            lightningWeapon.FaithScaling = 0.0f;
            lightningWeapon.BaseLightningDamage += (ushort)(0.75 * lightningWeapon.BasePhysicalDamage);
            lightningWeapon.BasePhysicalDamage = (ushort)(0.75 * lightningWeapon.BasePhysicalDamage);
            if (weapon.GodDamageMultiplier != 0.0f)
                lightningWeapon.GodDamageMultiplier = 0.9f;  // Better than normal (unless Abyssal curse).
            lightningWeapon.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Lightning;
            lightningWeapon.BaseChangeCategory = 10;
        }
        void CreateRefinedVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon refinedWeapon = CreateWeaponUpgrade(weapon, 300, upgradeIdOffset);
            refinedWeapon.Name = "Refn. " + weapon.Name;
            refinedWeapon.Summary = weapon.Summary;
            refinedWeapon.Description = weapon.Description;
            refinedWeapon.BaseChangeCategory = 15;
        }
        void CreateMagicVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon magicWeapon = CreateWeaponUpgrade(weapon, 400, upgradeIdOffset);
            // Total scaling stays the same, but 70% of current STR, DEX, and FAI scaling goes to INT.
            magicWeapon.Name = "Mag. " + weapon.Name;
            magicWeapon.Summary = weapon.Summary;
            magicWeapon.Description = weapon.Description;
            magicWeapon.IntelligenceScaling += 0.35f * (magicWeapon.StrengthScaling + magicWeapon.DexterityScaling + magicWeapon.FaithScaling);
            magicWeapon.StrengthScaling *= 0.29f;
            magicWeapon.DexterityScaling *= 0.29f;
            magicWeapon.FaithScaling *= 0.29f;
            magicWeapon.BaseMagicDamage += (ushort)(magicWeapon.BasePhysicalDamage * 0.82);
            magicWeapon.BasePhysicalDamage = (ushort)(magicWeapon.BasePhysicalDamage * 0.75);
            magicWeapon.BaseChangeCategory = 20;
        }
        void CreateEnchantedVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon enchantedWeapon = CreateWeaponUpgrade(weapon, 500, upgradeIdOffset);
            // 70% of current STR, DEX, and FAI scaling goes to INT.
            // Then STR, DEX, and FAI are multiplied by 0.72 (so 0.21 combined), and INT is multiplied by 0.98.
            enchantedWeapon.Name = "Ench. " + weapon.Name;
            enchantedWeapon.Summary = weapon.Summary;
            enchantedWeapon.Description = weapon.Description;
            enchantedWeapon.SpecialEffectOnHit0 = SpEffectGenerator.Effects["Enchanted (MOD HIT FLAG)"];  // Recharges spell usages (through mod hook).
            enchantedWeapon.IntelligenceScaling += 0.98f * 0.35f * (enchantedWeapon.StrengthScaling + enchantedWeapon.DexterityScaling + enchantedWeapon.FaithScaling);
            enchantedWeapon.StrengthScaling *= 0.21f;
            enchantedWeapon.DexterityScaling *= 0.21f;
            enchantedWeapon.FaithScaling *= 0.21f;
            enchantedWeapon.BaseMagicDamage += (ushort)(enchantedWeapon.BasePhysicalDamage * 0.79);
            enchantedWeapon.BasePhysicalDamage = (ushort)(enchantedWeapon.BasePhysicalDamage * 0.75);
            enchantedWeapon.BaseChangeCategory = 22;
        }
        void CreateDivineVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon divineWeapon = CreateWeaponUpgrade(weapon, 600, upgradeIdOffset);
            divineWeapon.Name = "Div. " + weapon.Name;
            divineWeapon.Summary = weapon.Summary;
            divineWeapon.Description = weapon.Description;
            divineWeapon.FaithScaling += 0.35f * (divineWeapon.StrengthScaling + divineWeapon.DexterityScaling + divineWeapon.IntelligenceScaling);
            divineWeapon.StrengthScaling *= 0.29f;
            divineWeapon.DexterityScaling *= 0.29f;
            divineWeapon.IntelligenceScaling *= 0.29f;
            divineWeapon.BaseMagicDamage += (ushort)(divineWeapon.BasePhysicalDamage * 0.84);
            divineWeapon.BasePhysicalDamage = (ushort)(divineWeapon.BasePhysicalDamage * 0.67);
            if (weapon.WeakToDivineDamageMultiplier != 0.0f)
                divineWeapon.WeakToDivineDamageMultiplier = 1.2f;  // note increase from vanilla 1.1 (unless Abyssal curse).
            divineWeapon.ScalingFormulaType = 1;  // Magic Melee
            divineWeapon.BaseChangeCategory = 25;
        }
        void CreateDireVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon direWeapon = CreateWeaponUpgrade(weapon, 700, upgradeIdOffset);
            direWeapon.Name = "Dire " + weapon.Name;
            direWeapon.Summary = weapon.Summary;
            direWeapon.Description = weapon.Description;
            direWeapon.EquippedSpecialEffect0 = SpEffectGenerator.Effects["Dire (EMEVD FLAG)"];
            direWeapon.ScalingFormulaType = 1;  // Magic Melee
            direWeapon.BaseChangeCategory = 30;
        }
        void CreateFireVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon fireWeapon = CreateWeaponUpgrade(weapon, 800, upgradeIdOffset);
            fireWeapon.Name = "Fire " + weapon.Name;
            fireWeapon.Summary = weapon.Summary;
            fireWeapon.Description = weapon.Description;
            fireWeapon.StrengthScaling = 0.0f;
            fireWeapon.DexterityScaling = 0.0f;
            fireWeapon.IntelligenceScaling = 0.0f;
            fireWeapon.FaithScaling = 0.0f;
            fireWeapon.BaseFireDamage += (ushort)(0.75 * fireWeapon.BasePhysicalDamage);
            fireWeapon.BasePhysicalDamage = (ushort)(0.75 * fireWeapon.BasePhysicalDamage);
            fireWeapon.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
            fireWeapon.BaseChangeCategory = 35;
        }
        void CreateDraconicVariant(Weapon weapon, int upgradeIdOffset = 0)
        {
            Weapon draconicWeapon = CreateWeaponUpgrade(weapon, 900, upgradeIdOffset);
            draconicWeapon.Name = "Drac. " + weapon.Name;
            draconicWeapon.Summary = weapon.Summary;
            draconicWeapon.Description = weapon.Description;
            draconicWeapon.StrengthScaling = 0.0f;
            draconicWeapon.DexterityScaling = 0.0f;
            draconicWeapon.IntelligenceScaling = 0.0f;
            draconicWeapon.FaithScaling = 0.0f;
            draconicWeapon.BaseFireDamage += (ushort)(0.7 * draconicWeapon.BasePhysicalDamage);
            draconicWeapon.BasePhysicalDamage = (ushort)(0.7 * draconicWeapon.BasePhysicalDamage);
            if (weapon.GodDamageMultiplier != 0.0f)
                draconicWeapon.GodDamageMultiplier = 1.2f;  // unless Abyssal curse
            draconicWeapon.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
            draconicWeapon.EquippedSpecialEffect0 = SpEffectGenerator.Effects["Draconic Burn (Apply)"];  // Enemy Burn (via attack trigger)
            draconicWeapon.SpecialEffectOnHit1 = SpEffectGenerator.Effects["Draconic Burn Self (20 / 5s)"];  // Self Burn
            draconicWeapon.BaseChangeCategory = 40;
        }

        void AdjustWeaponUpgrades()
        {
            // TODO: This, and also Bow/Crossbow variants 3200, 8200, 9200, etc., some of which have higher scaling for some reason.
            foreach (int offset in new int[] { 0, 8000 })
            {
                WeaponUpgrade crystal = Mod.GPARAM.WeaponUpgrades[offset + 100];
                crystal.ReinforcementLevel = 0;
                crystal.Name = "Crystal Ascension";
                crystal.PhysicsAtkRate = 1.5f;
                crystal.StaminaAtkRate = 1.5f;
                crystal.CorrectStrengthRate = 1.1f;
                crystal.CorrectAgilityRate = 1.1f;
            }

            foreach (int offset in new int[] { 0, 3000, 8000, 9000 })
            {
                WeaponUpgrade lightning = Mod.GPARAM.WeaponUpgrades[offset + 200];
                lightning.ReinforcementLevel = 0;
                lightning.Name = "Lightning Ascension";
                lightning.PhysicsAtkRate = 1.0f;
                lightning.ThunderAtkRate = 1.0f;
                lightning.StaminaAtkRate = 1.1f;
            }

            WeaponUpgrade refined = Mod.GPARAM.WeaponUpgrades[300];
            refined.ReinforcementLevel = 0;
            refined.Name = "Refined Ascension";
            refined.PhysicsAtkRate = 1.3f;
            refined.StaminaAtkRate = 1.3f;
            refined.CorrectStrengthRate = 1.1f;
            refined.CorrectAgilityRate = 1.1f;

            foreach (int offset in new int[] { 0, 8000 })
            {
                WeaponUpgrade magic = Mod.GPARAM.WeaponUpgrades[offset + 400];
                magic.ReinforcementLevel = 0;
                magic.Name = "Magic Ascension";
                magic.PhysicsAtkRate = 1.0f;
                magic.MagicAtkRate = 1.0f;
                magic.StaminaAtkRate = 1.1f;
                magic.CorrectStrengthRate = 1.1f;
                magic.CorrectAgilityRate = 1.1f;
                magic.CorrectMagicRate = 1.1f;
            }

            foreach (int offset in new int[] { 0, 9000 })
            {
                WeaponUpgrade enchanted = Mod.GPARAM.WeaponUpgrades[offset + 500];
                enchanted.ReinforcementLevel = 0;
                enchanted.Name = "Enchanted Ascension";
                enchanted.PhysicsAtkRate = 1.0f;
                enchanted.MagicAtkRate = 1.0f;
                enchanted.StaminaAtkRate = 1.1f;
                enchanted.CorrectStrengthRate = 1.1f;
                enchanted.CorrectAgilityRate = 1.1f;
                enchanted.CorrectMagicRate = 1.1f;
            }

            foreach (int offset in new int[] { 0, 8000 })
            {
                WeaponUpgrade divine = Mod.GPARAM.WeaponUpgrades[offset + 600];
                divine.ReinforcementLevel = 0;
                divine.Name = "Divine Ascension";
                divine.PhysicsAtkRate = 1.0f;
                divine.MagicAtkRate = 1.0f;
                divine.StaminaAtkRate = 1.1f;
                divine.CorrectStrengthRate = 1.1f;
                divine.CorrectAgilityRate = 1.1f;
                divine.CorrectFaithRate = 1.1f;
            }

            WeaponUpgrade dire = Mod.GPARAM.WeaponUpgrades[700];
            dire.ReinforcementLevel = 0;
            dire.Name = "Dire Ascension";
            dire.PhysicsAtkRate = 1.0f;
            dire.StaminaAtkRate = 1.0f;
            dire.CorrectStrengthRate = 1.1f;
            dire.CorrectAgilityRate = 1.1f;

            foreach (int offset in new int[] { 0, 3000, 8000, 9000 })
            {
                WeaponUpgrade fire = Mod.GPARAM.WeaponUpgrades[offset + 800];
                fire.Name = "Fire Ascension";
                fire.ReinforcementLevel = 0;
                fire.PhysicsAtkRate = 1.0f;
                fire.FireAtkRate = 1.1f;
                fire.StaminaAtkRate = 1.0f;
            }

            foreach (int offset in new int[] { 0, 3000, 9000 })
            {
                WeaponUpgrade draconic = Mod.GPARAM.WeaponUpgrades[offset + 900];
                draconic.ReinforcementLevel = 0;
                draconic.Name = "Draconic Ascension";
                draconic.PhysicsAtkRate = 1.0f;
                draconic.FireAtkRate = 1.1f;
                draconic.StaminaAtkRate = 1.0f;
            }

            Mod.GPARAM.UpgradeMaterials[100].MaterialId01 = 1010;
            Mod.GPARAM.UpgradeMaterials[100].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[200].MaterialId01 = 1040;
            Mod.GPARAM.UpgradeMaterials[200].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[300].MaterialId01 = 1000;
            Mod.GPARAM.UpgradeMaterials[300].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[400].MaterialId01 = 1020;
            Mod.GPARAM.UpgradeMaterials[400].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[500].MaterialId01 = 1030;
            Mod.GPARAM.UpgradeMaterials[500].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[600].MaterialId01 = 1050;
            Mod.GPARAM.UpgradeMaterials[600].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[700].MaterialId01 = 1060;
            Mod.GPARAM.UpgradeMaterials[700].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[800].MaterialId01 = 1070;
            Mod.GPARAM.UpgradeMaterials[800].IsDisableDispNum01 = false;
            Mod.GPARAM.UpgradeMaterials[900].MaterialId01 = 1080;
            Mod.GPARAM.UpgradeMaterials[900].IsDisableDispNum01 = false;
        }

        void ApplyWeaponAnimations(Weapon newWeapon, WeaponStats baseWeaponStats, int? specialAnimationCategory)
        {
            newWeapon.AttackAnimationCategory = (byte)baseWeaponStats.BaseAttackAnimationCategory;
            newWeapon.OneHandedAnimationCategory = (byte)baseWeaponStats.OneHandedAnimationCategory;
            newWeapon.TwoHandedAnimationCategory = (byte)baseWeaponStats.TwoHandedAnimationCategory;
            if (specialAnimationCategory is int value)
                newWeapon.SpecialAttackCategory = (byte)value;
        }
        void ApplyModelHitboxes(Attack newAttack, Attack modelAttack)
        {
            for (int hitboxIndex = 0; hitboxIndex < 4; hitboxIndex++)
            {
                foreach (string hitboxStat in new string[] { "Radius", "DmyPoly1", "DmyPoly2", "hitType" })
                {
                    newAttack.CopyField(modelAttack, $"hit{hitboxIndex}_{hitboxStat}");
                }
                // Priority field has a typo ("hti").
                newAttack.CopyField(modelAttack, $"hti{hitboxIndex}_Priority");
            }
        }

        Attack BasicBehaviorAttackSetup(int newBehaviorVarId, int behaviorSubId, string behaviorName, WeaponStats modelWeaponStats, WeaponStats baseWeaponStats, WeaponStats specialWeaponStats,
            double staminaCostMultiplier = 1.0)
        {
            // Behaviors and Attacks are copied from special weapon if present, and base weapon otherwise,
            // except that Attack hitbox information is taken from model weapon.
            Behavior sourceBehavior = (specialWeaponStats ?? baseWeaponStats).GetBehaviorParam(Mod.VanillaGPARAM, behaviorSubId);
            if (sourceBehavior == null)
                return null;
            Attack sourceAttack = (specialWeaponStats ?? baseWeaponStats).GetAttackParam(Mod.VanillaGPARAM, behaviorSubId);
            int newAttackId = 1000 * newBehaviorVarId + behaviorSubId;
            Behavior newBehavior = Mod.GPARAM.BehaviorsPC.CopyRow(sourceBehavior, 100000000 + 1000 * newBehaviorVarId + behaviorSubId);
            // Bullet behaviors are disabled (reference -1). It will be re-added by a legendary effect if appropriate.
            newBehavior.RefID = newBehavior.ReferenceType == 1 ? 0 : newAttackId;
            Attack newAttack = null;
            if (sourceAttack != null)
            {
                newAttack = Mod.GPARAM.AttacksPC.CopyRow(sourceAttack, newAttackId);
                newAttack.Name = behaviorName;
                Behavior modelBehavior = modelWeaponStats.GetBehaviorParam(Mod.VanillaGPARAM, behaviorSubId);
                if (modelBehavior != null)
                {
                    Attack modelAttack = modelWeaponStats.GetAttackParam(Mod.VanillaGPARAM, behaviorSubId);
                    if (modelAttack != null)
                        ApplyModelHitboxes(newAttack, modelAttack);
                }
            }
            newBehavior.BehaviorSubID = behaviorSubId;
            newBehavior.VariationID = newBehaviorVarId;
            newBehavior.Name = behaviorName;
            newBehavior.StaminaCost = (int)(newBehavior.StaminaCost * staminaCostMultiplier);
            return newAttack;
        }

        void CleanWeaponParam(Weapon weapon, string weaponSubclass, bool isStartingWeapon = false)
        {
            // Remove all non-zero upgrade origins (for base weapon).
            weapon.UpgradeMaterialsID = 0;  // TODO: Confirm this doesn't interfere with ember upgrade (it shouldn't).
            weapon.WeaponUpgradeID = 0;  // All base weapons use default upgrade path (and only level 0, so effectively none).
            weapon.UpgradeOrigin0 = (int)weapon.ID;  // Probably redundant, but harmless.
            weapon.UpgradeOrigin1 = -1;
            weapon.UpgradeOrigin2 = -1;
            weapon.UpgradeOrigin3 = -1;
            weapon.UpgradeOrigin4 = -1;
            weapon.UpgradeOrigin5 = -1;
            weapon.UpgradeOrigin6 = -1;
            weapon.UpgradeOrigin7 = -1;
            weapon.UpgradeOrigin8 = -1;
            weapon.UpgradeOrigin9 = -1;
            weapon.UpgradeOrigin10 = -1;
            weapon.UpgradeOrigin11 = -1;
            weapon.UpgradeOrigin12 = -1;
            weapon.UpgradeOrigin13 = -1;
            weapon.UpgradeOrigin14 = -1;
            weapon.UpgradeOrigin15 = -1;

            // Reset special enemy type effectiveness.
            weapon.DamageAgainstDemonsMultiplier = 1.0f;
            weapon.WeakToDivineDamageMultiplier = 1.0f;
            weapon.GodDamageMultiplier = 0.5f;  // Used with Dragons. Default is 50% damage.
            weapon.AbyssDamageMultiplier = 1.0f;

            // All weapons in subclass have the same stats.
            switch (weaponSubclass)
            {
                case "Dagger":
                    weapon.RequiredStrength = 9;
                    weapon.RequiredDexterity = 11;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "StraightSword":
                    weapon.RequiredStrength = 12;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Greatsword":
                    weapon.RequiredStrength = 20;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "UltraGreatsword":
                    weapon.RequiredStrength = 30;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "CurvedSword":
                    weapon.RequiredStrength = 10;
                    weapon.RequiredDexterity = 12;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "CurvedGreatsword":
                    weapon.RequiredStrength = 18;
                    weapon.RequiredDexterity = 16;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "ThrustingSword":
                    weapon.RequiredStrength = 12;
                    weapon.RequiredDexterity = 14;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Katana":
                    weapon.RequiredStrength = 16;
                    weapon.RequiredDexterity = 18;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Axe":
                    weapon.RequiredStrength = 16;
                    weapon.RequiredDexterity = 8;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Greataxe":
                    weapon.RequiredStrength = 32;
                    weapon.RequiredDexterity = 8;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Hammer":
                    weapon.RequiredStrength = 12;
                    weapon.RequiredDexterity = 11;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "GreatHammer":
                    weapon.RequiredStrength = 30;
                    weapon.RequiredDexterity = 11;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Fists":
                    weapon.RequiredStrength = 10;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Spear":
                    weapon.RequiredStrength = 14;
                    weapon.RequiredDexterity = 14;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Halberd":
                    weapon.RequiredStrength = 16;
                    weapon.RequiredDexterity = 14;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Scythe":
                    weapon.RequiredStrength = 14;
                    weapon.RequiredDexterity = 16;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Whip":
                    weapon.RequiredStrength = 10;
                    weapon.RequiredDexterity = 16;
                    weapon.RequiredIntelligence = 8;
                    weapon.RequiredFaith = 8;
                    break;
                case "Catalyst":
                    weapon.RequiredStrength = 8;
                    weapon.RequiredDexterity = 8;
                    weapon.RequiredIntelligence = 14;
                    weapon.RequiredFaith = 10;
                    break;
                case "Talisman":
                    weapon.RequiredStrength = 8;
                    weapon.RequiredDexterity = 8;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 14;
                    break;
                case "Bow":
                    weapon.RequiredStrength = 12;
                    weapon.RequiredDexterity = 12;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 8;
                    break;
                case "Greatbow":
                    weapon.RequiredStrength = 20;
                    weapon.RequiredDexterity = 20;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 8;
                    break;
                case "Crossbow":
                    weapon.RequiredStrength = 14;
                    weapon.RequiredDexterity = 14;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 8;
                    break;
                case "Shield":
                    weapon.RequiredStrength = 10;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 8;
                    break;
                case "Greatshield":
                    weapon.RequiredStrength = 22;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 8;
                    break;
                default:
                    weapon.RequiredStrength = 10;
                    weapon.RequiredDexterity = 10;
                    weapon.RequiredIntelligence = 10;
                    weapon.RequiredFaith = 10;
                    break;
            }

            if (!isStartingWeapon)
            {
                // Remove special effects.
                weapon.SpecialEffectOnHit0 = -1;  // Reserved for upgrade variant on-hit effect (Enchanted/Draconic).
                weapon.SpecialEffectOnHit1 = -1;  // Reserved for positive on-hit legendary effect (e.g. poison damage). 
                weapon.SpecialEffectOnHit2 = -1;  // Reserved for negative on-hit abyssal effect (e.g. self-damage).
                weapon.EquippedSpecialEffect0 = -1;  // Reserved for upgrade variant passive effect (Dire).
                weapon.EquippedSpecialEffect1 = -1;  // Reserved for positive passive legendary effect (e.g. damage boost).
                weapon.EquippedSpecialEffect2 = -1;  // Reserved for negative passive abyssal effect (e.g. slow movement).

                // Intrinsic elemental damage is zeroed out, but a third of their base damage is added to physical.
                weapon.BasePhysicalDamage += (ushort)(weapon.BaseMagicDamage / 3 + weapon.BaseFireDamage / 3 + weapon.BaseLightningDamage / 3);
                weapon.BaseMagicDamage = 0;
                weapon.BaseFireDamage = 0;
                weapon.BaseLightningDamage = 0;
                weapon.ScalingFormulaType = 0;  // Physical Melee
                weapon.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Physical;

                // Enable "IsCustom". In vanilla, this is disabled for Skull Lantern, all Talismans, and a few Catalysts.
                // Its effect is unknown, but when in doubt, we probably want it on, given that all weapons
                // are being treated fairly equally now.
                weapon.IsCustom = true;
            }
        }

        public string GetRandomName(string weaponClass = "", bool isLegendary = false)
        {
            return NameGenerator.GetRandomName(out _, weaponClass, isLegendary, exact: false);
        }
        public string GetRandomDescription()
        {
            return DescriptionGenerator.GetRandomDescription(exact: false);
        }
        public void RunNameDescriptionDemoLoop()
        {
            Console.WriteLine(
                "Press enter to get a new weapon name and description.\n" +
                "Weapons will alternate between common and legendary.\n" +
                "Type 'exit' before pressing Enter to stop generating.");
            bool isLegendary = false;
            while (true)
            {
                isLegendary = !isLegendary;
                if (Console.ReadLine() == "exit")
                    break;
                Console.WriteLine(GetRandomName("Random", isLegendary));
                Console.WriteLine("----------------");
                Console.WriteLine(GetRandomDescription());
            }
        }
    }
}
