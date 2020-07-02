using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormats;
using SoulsFormatsMod.Extensions;
using SoulsFormatsMod.PARAMS;
using CountDict = System.Collections.Generic.Dictionary<string, int>;

namespace RoguelikeSouls.Installation
{
    class LegendaryMeleeEffects : LegendaryEffects
    {

        internal override int LegendPoints { get; } = 3;
        internal override int AbyssalPoints { get; } = 6;
        internal double AbyssalImmunityChance { get; } = 0.3;
        internal bool AllowSpecialBullet { get; }
        internal override string ItemType { get; } = "weapon";

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "DamageBoost", 0 },
            { "GuardBoost", 0 },
            { "ElementalGuardBoost", 0 },
            { "PoisonDamage", 0 },
            { "BleedDamage", 0 },
            { "ToxicDamage", 0 },
            { "CurseDamage", 0 },
            { "SpecialBullet", 0 },
            { "ElementalDamage", 0 },
            { "Light", 0 },
            { "HighImpact", 0 },
        };
        public string StatusType { get; private set; }
        public string ElementType { get; private set; }

        // Increase the max number of points for some.

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "DamageBoost", 8 },
            { "GuardBoost", 1 },
            { "ElementalGuardBoost", 1 },
            { "PoisonDamage", 2 },
            { "BleedDamage", 3 },
            { "ToxicDamage", 2 },
            { "CurseDamage", 1 },
            { "SpecialBullet", 1 },
            { "ElementalDamage", 2 },
            { "Light", 1 },
            { "HighImpact", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "DamageBoost", "deals enhanced damage" },
            { "GuardBoost", "is superior at blocking physical attacks" },
            { "ElementalGuardBoost", "better resists elemental attacks" },
            { "PoisonDamage", "inflicts poison on hit" },
            { "BleedDamage", "causes enemies to bleed" },
            { "ToxicDamage", "inflicts deadly poison on hit" },
            { "CurseDamage", "curses enemies on impact" },
            { "SpecialBullet", "possesses sorcerous power" },
            { "ElementalDamage", "is imbued with elemental force" },
            { "Light", "is unusually light" },
            { "HighImpact", "can send foes flying" },
        };
        IList<string> ElementTypes { get; } = new string[] { "Magic", "Fire", "Lightning" };
        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "SelfDamageOnHit", 0 },
            { "SelfPoisonOnHit", 0 },
            { "SelfBleedOnHit", 0 },
            { "SelfToxicOnHit", 0 },
            { "SelfCurseOnHit", 0 },
            { "LoseSoulsOnHit", 0 },
            { "Heavy", 0 },
            { "SelfSlow", 0 },
            { "BoostEnemyDamageOnHit", 0 },
            { "BoostEnemySpeedOnHit", 0 },
            { "BoostEnemyPoiseOnHit", 0 },
            { "DelayedEnemyHealOnHit", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "SelfDamageOnHit", "hurts to hold upon impact" },
            { "SelfPoisonOnHit", "poisons its wielder" },
            { "SelfBleedOnHit", "cuts deep into its wielder" },
            { "SelfToxicOnHit", "inflicts plague upon its wielder" },
            { "SelfCurseOnHit", "curses its wielder" },
            { "LoseSoulsOnHit", "drains accrued souls upon impact" },
            { "Heavy", "is excessively burdensome" },
            { "SelfSlow", "slows movement when equipment" },
            { "BoostEnemyDamageOnHit", "enrages struck enemies" },
            { "BoostEnemySpeedOnHit", "enrages struck enemies" },
            { "BoostEnemyPoiseOnHit", "enrages struck enemies" },
            { "DelayedEnemyHealOnHit", "returns vitality to enemies after a time" }
        };
        public override CountDict AbyssalImmunityPoints { get; internal set; } = new CountDict()
        {
            { "NoDemonDamage", 0 },
            { "NoSkeletonDamage", 0 },
            { "NoDragonDamage", 0 },
            { "NoAbyssDamage", 0 },
        };
        internal override Dictionary<string, string> AbyssalImmunityDescriptions { get; } = new Dictionary<string, string>()
        {
            { "NoDemonDamage", "is useless in battle with demons" },
            { "NoSkeletonDamage", "is ineffective against the reanimated" },
            { "NoDragonDamage", "is worthless against dragons" },
            { "NoAbyssDamage", "deals no damage to its abyssal kin" },
        };
        List<int> SpecialBullets { get; } = new List<int>()
        {
            1000,  // [58] Drake Sword
            1030,  // [77] Stone Greatsword
            1040,  // [79] Moonlight Greatsword (one-handed)
            1050,  // [79] Moonlight Greatsword (two-handed)
            // 1060,  // [94] Havel's Greatshield
            1070,  // [104] Golem Axe
            1080,  // [106] Dragon King Greataxe
            1090,  // [62] Grant
            1100,  // [65] Channeler's Trident
            1110,  // [68] Dragonslayer Spear
            // 1120,  // [92] Crystal Ring Shield
            1130,  // [98] Dragon Greatsword
            1170,  // [135] Obsidian Greatsword
        };

        public LegendaryMeleeEffects(bool isAbyssal, bool allowSpecialBullet = true, Random random = null) : base(isAbyssal, random)
        {
            // Currently, everything costs the same number of points (1) for simplicity.
            AllowSpecialBullet = allowSpecialBullet;

            if (IsAbyssal)
            {
                // Currently applying only one abyssal effect (and sometimes, one immunity).
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
                if (Rand.NextDouble() < AbyssalImmunityChance)
                {
                    string abyssalImmunity = AbyssalImmunityPoints.ElementAt(Rand.Next(AbyssalImmunityPoints.Count)).Key;
                    AbyssalImmunityPoints[abyssalImmunity] += 1;
                }
            }
            int points = IsAbyssal ? AbyssalPoints : LegendPoints;
            for (int i = 0; i < points; i++)
            {
                AddEffectPoint();
            }
        }

        internal override bool EffectAllowed(string effect)
        {
            // Check if effect clashes with a setting or another effect.
            // Will always find a valid set (e.g. all points in DamageBoost).
            if (effect == "SpecialBullet" && !AllowSpecialBullet)
                return false;
            if (effect == "Light" && AbyssalEffectPoints["Heavy"] > 0)
                return false;
            foreach (string statusType in new string[] { "Poison", "Bleed", "Toxic", "Curse" })
            {
                if (effect == $"{statusType}Damage" && StatusType != statusType)
                    return false;
            }
            return true;
        }

        public void ApplyEffects(Weapon weaponParam, TAE specialWeaponTAE, Behavior bulletBehaviorParam, int dummyPoly = 100)
        {
            // Applies effects to weapon param and (for special bullets) TAE.
            if (EffectPoints["DamageBoost"] > 0)
            {
                double damageMultiplier = weaponParam.BasePhysicalDamage * (1.0 + EffectPoints["DamageBoost"] * 0.05);
                weaponParam.BasePhysicalDamage = (ushort)damageMultiplier;
            }
            if (EffectPoints["GuardBoost"] == 1)
            {
                weaponParam.GuardStaminaDefense = (short)(weaponParam.GuardStaminaDefense * 1.2);
                weaponParam.PhysicalGuardPercentage += 30;
            }
            if (EffectPoints["ElementalGuardBoost"] == 1)
            {
                weaponParam.MagicGuardPercentage += 30;
                weaponParam.FireGuardPercentage += 30;
                weaponParam.LightningGuardPercentage += 30;
            }

            // Only one status effect can be active.
            if (EffectPoints["PoisonDamage"] > 0)
            {
                int level = 25 * (EffectPoints["PoisonDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Poison Damage ({level})"];
            }
            if (EffectPoints["BleedDamage"] > 0)
            {
                int level = 20 * (EffectPoints["BleedDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Bleed Damage ({level})"];
            }
            if (EffectPoints["ToxicDamage"] > 0)
            {
                int level = 20 * (EffectPoints["ToxicDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Toxic Damage ({level})"];
            }
            if (EffectPoints["CurseDamage"] > 0)
            {
                int level = 20 * (EffectPoints["CurseDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Curse Damage ({level})"];
            }

            if (EffectPoints["SpecialBullet"] == 1 && specialWeaponTAE != null)
            {
                // If specialWeaponTAE is null, this point shouldn't have been assigned.
                var bulletAnimations = new List<TAE.Animation>(specialWeaponTAE.Animations.Where(anim => anim.ID == 3300 || anim.ID == 4300));
                if (bulletAnimations.Count() > 0)
                {
                    TAE.Animation animation = bulletAnimations[Rand.Next(bulletAnimations.Count)];
                    TAE.Event attackEvent = animation.FindEvent(1);
                    if (attackEvent != null)
                    {
                        animation.NewEvent(2, attackEvent.StartTime, attackEvent.StartTime + (1.0f / 30.0f), "DummyPolyID", dummyPoly, "BehaviorSubID", bulletBehaviorParam.ID);
                        bulletBehaviorParam.RefID = SpecialBullets[Rand.Next(SpecialBullets.Count)];
                    }
                }
            }

            if (EffectPoints["ElementalDamage"] > 0)
            {
                weaponParam.BasePhysicalDamage -= (ushort)(10 * EffectPoints["ElementalDamage"]);
                switch (ElementType)
                {
                    case "Magic":
                        weaponParam.BaseMagicDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ScalingFormulaType = 1;  // Magic Melee
                        break;
                    case "Fire":
                        weaponParam.BaseFireDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
                        break;
                    case "Lightning":
                        weaponParam.BaseLightningDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Lightning;
                        break;
                }
            }

            if (EffectPoints["Light"] == 1)
                // Half stamina cost is applied to each behavior.
                weaponParam.Weight = Math.Max(0.5f, weaponParam.Weight - 5.0f);

            // High Impact is applied separately in `CheckAndApplyHighImpact`, called when each Attack param is generated.

            ApplyAbyssalEffects(weaponParam);
        }

        public void CheckAndApplyHighImpact(Attack weaponAttack)
        {
            // Must be called separately on each Attack param for the weapon.
            if (EffectPoints["HighImpact"] == 1)
            {
                switch (weaponAttack.ImpactLevel)
                {
                    case 8:  // Minimal -> Small
                        weaponAttack.ImpactLevel = 1;
                        break;
                    case 1:  // Small -> Medium
                        weaponAttack.ImpactLevel = 2;
                        break;
                    case 2:  // Medium -> Large
                        weaponAttack.ImpactLevel = 3;
                        break;
                    case 3:  // Large -> Launch
                        weaponAttack.ImpactLevel = 9;
                        break;
                }
            }
        }

        void ApplyAbyssalEffects(Weapon weaponParam)
        {
            if (AbyssalEffectPoints["SelfDamageOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Damage (10)"];
            if (AbyssalEffectPoints["SelfPoisonOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Poison (20)"];
            if (AbyssalEffectPoints["SelfBleedOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Bleed (20)"];
            if (AbyssalEffectPoints["SelfToxicOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Toxic (20)"];
            if (AbyssalEffectPoints["SelfCurseOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Curse (20)"];
            if (AbyssalEffectPoints["LoseSoulsOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Lose Souls (100)"];
            if (AbyssalEffectPoints["Heavy"] == 1)
                // Double stamina cost is applied to each behavior.
                weaponParam.Weight += 8.0f;
            if (AbyssalEffectPoints["SelfSlow"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Slow (10%, 5s)"];
            if (AbyssalEffectPoints["BoostEnemyDamageOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Damage (30%, 10s)"];
            if (AbyssalEffectPoints["BoostEnemySpeedOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Speed (20%, 5s)"];
            if (AbyssalEffectPoints["BoostEnemyPoiseOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Poise (300, 10s)"];
            if (AbyssalEffectPoints["DelayedEnemyHealOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Delayed Enemy Heal (Delay)"];

            if (AbyssalImmunityPoints["NoDemonDamage"] == 1)
                weaponParam.DamageAgainstDemonsMultiplier = 0.0f;
            if (AbyssalImmunityPoints["NoSkeletonDamage"] == 1)
                weaponParam.WeakToDivineDamageMultiplier = 0.0f;
            if (AbyssalImmunityPoints["NoDragonDamage"] == 1)
                weaponParam.GodDamageMultiplier = 0.0f;  // God == Dragon in this mod.
            if (AbyssalImmunityPoints["NoAbyssDamage"] == 1)
                weaponParam.AbyssDamageMultiplier = 0.0f;
        }

        internal override string ChooseRandomEffect()
        {
            // Weighted choice of effect based on remaining open points.
            int total = EffectPoints.Sum(t => MaxEffectPoints[t.Key] - t.Value);
            int roll = Rand.Next(total);
            long weightSum = 0;
            for (int i = 0; i < EffectPoints.Count; i++)
            {
                weightSum += MaxEffectPoints.ElementAt(i).Value - EffectPoints.ElementAt(i).Value;
                if (roll < weightSum)
                {
                    string effect = EffectPoints.ElementAt(i).Key;
                    if (effect == "ElementalDamage" && ElementType == "")
                        ElementType = ElementTypes[Rand.Next(ElementTypes.Count)];  // Choose element.
                    if (effect == "PoisonDamage" && StatusType == "")
                        StatusType = "Poison";
                    if (effect == "BleedDamage" && StatusType == "")
                        StatusType = "Bleed";
                    if (effect == "ToxicDamage" && StatusType == "")
                        StatusType = "Toxic";
                    if (effect == "CurseDamage" && StatusType == "")
                        StatusType = "Curse";
                    return effect;
                }
            }
            throw new Exception($"Failure to choose random effect (roll {roll}, weight total {total})");
        }
    }

    class LegendaryCatalystEffects : LegendaryEffects
    {
        internal override int LegendPoints { get; } = 2;
        internal override int AbyssalPoints { get; } = 3;
        internal override string ItemType { get; } = "catalyst";
        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "MagicDamageBoost", 0 },
            { "PhysicalDamageBoost", 0 },
            { "MagicBoostOnHit", 0 },
            { "CanCastPyromancy", 0 },
            { "CanCastMiracles", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "MagicDamageBoost", 3 },
            { "PhysicalDamageBoost", 2 },
            { "MagicBoostOnHit", 0 },
            { "CanCastPyromancy", 1 },
            { "CanCastMiracles", 1 },
        };
        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MagicDamageBoost", "increases damage from spells" },
            { "PhysicalDamageBoost", "is a more effective melee weapon" },
            { "MagicBoostOnHit", "greatly increases spell damage after physically striking a foe" },
            { "CanCastPyromancy", "can cast pyromancies" },
            { "CanCastMiracles", "can cast miracles" },
        };
        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "Fragile", 0 },
            { "HalfSpellCasts", 0 },
            { "Heavy", 0 },
            { "SelfSlow", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "Fragile", "is easily broken" },
            { "HalfSpellCasts", "halves spell usages" },
            { "Heavy", "is unusually burdensome" },
            { "SelfSlow", "slows movement when equipped" },
        };

        public LegendaryCatalystEffects(bool isAbyssal, Random random = null) : base(isAbyssal, random)
        {
            // Currently, everything costs the same number of points (1) for simplicity.
            int points = IsAbyssal ? AbyssalPoints : LegendPoints;
            for (int i = 0; i < points; i++)
            {
                string effect = ChooseRandomEffect();
                EffectPoints[effect] += 1;
            }
            if (isAbyssal)
            {
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
            }
        }

        public void ApplyEffects(Weapon weaponParam)
        {
            // Applies effects to weapon param and (for special bullets) TAE.
            if (EffectPoints["MagicDamageBoost"] > 0)
            {
                // INT and FAI scaling increase by 20%, 40%, or 60%.
                weaponParam.IntelligenceScaling *= 1.0f + (EffectPoints["MagicDamageBoost"] * 0.2f);
                weaponParam.FaithScaling *= 1.0f + (EffectPoints["MagicDamageBoost"] * 0.2f);
            }
            if (EffectPoints["PhysicalDamageBoost"] > 0)
                // Change physical damage from default of 45 to 100 or 200.
                weaponParam.BasePhysicalDamage = (ushort)(100 * EffectPoints["PhysicalDamageBoost"]);
            if (EffectPoints["MagicBoostOnHit"] > 0)
                // Change physical damage from default of 45 to 100 or 200.
                weaponParam.EquippedSpecialEffect1 = SpEffectGenerator.Effects["Magic Damage Up On Hit (150, 8s)"];
            if (EffectPoints["CanCastPyromancy"] == 1)
                weaponParam.CanCastPyromancy = true;
            if (EffectPoints["CanCastMiracles"] == 1)
                weaponParam.CanCastMiracles = true;

            // Positive Abyssal effect (melee special) applied by randomizer.
            ApplyAbyssalEffect(weaponParam);
        }

        void ApplyAbyssalEffect(Weapon weaponParam)
        {
            if (AbyssalEffectPoints["Fragile"] == 1)
            {
                weaponParam.InitialDurability = 5;
                weaponParam.MaxDurability = 5;
            }
            if (AbyssalEffectPoints["Heavy"] == 1)
                weaponParam.Weight += 8.0f;
            if (AbyssalEffectPoints["SelfSlow"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["Self Slow (20%)"];
            if (AbyssalEffectPoints["HalfSpellCasts"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["Half Spell Casts"];
        }
    }

    class LegendaryTalismanEffects : LegendaryEffects
    {
        internal override int LegendPoints { get; } = 2;
        internal override int AbyssalPoints { get; } = 3;
        internal override string ItemType { get; } = "talisman";
        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "MagicDamageBoost", 0 },
            { "PhysicalDamageBoost", 0 },
            { "DragonBoneFistSpecial", 0 },
            { "CanCastPyromancy", 0 },
            { "CanCastSorceries", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "MagicDamageBoost", 3 },
            { "PhysicalDamageBoost", 1 },
            { "DragonBoneFistSpecial", 1 },
            { "CanCastPyromancy", 1 },
            { "CanCastSorceries", 1 },
        };
        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MagicDamageBoost", "can deliver more powerful spells" },
            { "PhysicalDamageBoost", "is a more effective melee weapon" },
            { "DragonBoneFistSpecial", "can launch enemies skyward" },
            { "CanCastPyromancy", "can cast pyromancies" },
            { "CanCastSorceries", "can cast sorceries" },
        };
        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "Fragile", 0 },
            { "HalfSpellCasts", 0 },
            { "Heavy", 0 },
            { "SelfSlow", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "Fragile", "is easily broken" },
            { "HalfSpellCasts", "halves spell usages" },
            { "Heavy", "is quite burdensome" },
            { "SelfSlow", "slows movement when equipped" },
        };

        public LegendaryTalismanEffects(bool isAbyssal, Random random = null) : base(isAbyssal, random)
        {
            // Currently, everything costs the same number of points (1) for simplicity.
            int points = IsAbyssal ? AbyssalPoints : LegendPoints;
            for (int i = 0; i < points; i++)
            {
                string effect = ChooseRandomEffect();
                EffectPoints[effect] += 1;
            }
            if (isAbyssal)
            {
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
            }
        }

        public void ApplyEffects(Weapon weaponParam)
        {
            // Applies effects to weapon param and (for special bullets) TAE.
            if (EffectPoints["MagicDamageBoost"] > 0)
            {
                // INT and FAI scaling increase by 20%, 40%, or 60%.
                weaponParam.IntelligenceScaling *= 1.0f + (EffectPoints["MagicDamageBoost"] * 0.2f);
                weaponParam.FaithScaling *= 1.0f + (EffectPoints["MagicDamageBoost"] * 0.2f);
            }
            if (EffectPoints["PhysicalDamageBoost"] > 0)
                // Change physical damage from default of 45 to 100 or 200.
                weaponParam.BasePhysicalDamage = (ushort)(100 * EffectPoints["PhysicalDamageBoost"]);
            if (EffectPoints["CanCastPyromancy"] == 1)
                weaponParam.CanCastPyromancy = true;
            if (EffectPoints["CanCastSorceries"] == 1)
                weaponParam.CanCastSorceries = true;
            // Dragon Bone Fist melee special applied by randomizer.

            ApplyAbyssalEffect(weaponParam);
        }

        void ApplyAbyssalEffect(Weapon weaponParam)
        {
            if (AbyssalEffectPoints["Fragile"] == 1)
            {
                weaponParam.InitialDurability = 5;
                weaponParam.MaxDurability = 5;
            }
            if (AbyssalEffectPoints["Heavy"] == 1)
                weaponParam.Weight += 8.0f;
            if (AbyssalEffectPoints["SelfSlow"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["Self Slow (20%)"];
            if (AbyssalEffectPoints["HalfSpellCasts"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["Half Spell Casts"];
        }
    }

    class LegendaryBowCrossbowEffects : LegendaryEffects
    {
        internal override int LegendPoints { get; } = 3;
        internal override int AbyssalPoints { get; } = 5;
        internal double AbyssalImmunityChance { get; } = 0.3;
        internal override string ItemType { get; } = "bow";
        public bool IsCrossbow { get; }

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "IsGreatbow", 0 },  // Bow only
            { "IsAvelyn", 0 },  // Crossbow only
            { "DamageBoost", 0 },
            { "RangeBoost", 0 },
            { "PoisonDamage", 0 },
            { "BleedDamage", 0 },
            { "ToxicDamage", 0 },
            { "CurseDamage", 0 },
            { "ElementalDamage", 0 },
            { "Light", 0 },
        };
        public string StatusType { get; private set; }
        public string ElementType { get; private set; }

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "IsGreatbow", 1 },  // Bow only
            { "IsAvelyn", 1 },  // Crossbow only
            { "DamageBoost", 6 },
            { "RangeBoost", 3 },
            { "PoisonDamage", 2 },
            { "BleedDamage", 3 },
            { "ToxicDamage", 2 },
            { "CurseDamage", 1 },
            { "ElementalDamage", 2 },
            { "Light", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "IsGreatbow", "is oversized" },
            { "IsAvelyn", "fires multiple bolts" },
            { "DamageBoost", "deals enhanced damage" },
            { "RangeBoost", "can shoot over greater distances" },
            { "PoisonDamage", "inflicts poison on hit" },
            { "BleedDamage", "causes enemies to bleed" },
            { "ToxicDamage", "inflicts deadly poison on hit" },
            { "CurseDamage", "curses enemies on impact" },
            { "ElementalDamage", "is imbued with elemental power" },
            { "Light", "is unusually light" },
        };
        IList<string> ElementTypes { get; } = new string[] { "Magic", "Fire", "Lightning" };
        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "DoubleStaminaCost", 0 },
            { "SelfDamageOnHit", 0 },
            { "SelfPoisonOnHit", 0 },
            { "SelfBleedOnHit", 0 },
            { "SelfToxicOnHit", 0 },
            { "SelfCurseOnHit", 0 },
            { "LoseSoulsOnHit", 0 },
            { "Heavy", 0 },
            { "SelfSlow", 0 },
            { "ShortRange", 0 },
            { "BoostEnemyDamageOnHit", 0 },
            { "BoostEnemySpeedOnHit", 0 },
            { "BoostEnemyPoiseOnHit", 0 },
            { "DelayedEnemyHealOnHit", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "DoubleStaminaCost", "requires more stamina to wield" },
            { "SelfDamageOnHit", "hurts to hold upon impact" },
            { "SelfPoisonOnHit", "poisons its wielder" },
            { "SelfBleedOnHit", "cuts deep into its wielder" },
            { "SelfToxicOnHit", "inflicts plague upon its wielder" },
            { "SelfCurseOnHit", "curses its wielder" },
            { "LoseSoulsOnHit", "drains accrued souls upon impact" },
            { "Heavy", "is quite burdensome" },
            { "SelfSlow", "slows movement when equipment" },
            { "ShortRange", "is effective only at close range" },
            { "BoostEnemyDamageOnHit", "enrages struck enemies" },
            { "BoostEnemySpeedOnHit", "enrages struck enemies" },
            { "BoostEnemyPoiseOnHit", "enrages struck enemies" },
            { "DelayedEnemyHealOnHit", "returns vitality to enemies after a time" }
        };
        public override CountDict AbyssalImmunityPoints { get; internal set; } = new CountDict()
        {
            { "NoDemonDamage", 0 },
            { "NoSkeletonDamage", 0 },
            { "NoDragonDamage", 0 },
            { "NoAbyssDamage", 0 },
        };
        internal override Dictionary<string, string> AbyssalImmunityDescriptions { get; } = new Dictionary<string, string>()
        {
            { "NoDemonDamage", "is useless in battle with demons" },
            { "NoSkeletonDamage", "is ineffective against the reanimated" },
            { "NoDragonDamage", "is worthless against dragons" },
            { "NoAbyssDamage", "deals no damage to its abyssal kin" },
        };

        public LegendaryBowCrossbowEffects(bool isAbyssal, bool isCrossbow, Random random = null) : base(isAbyssal, random)
        {
            IsCrossbow = isCrossbow;
            if (IsCrossbow)
                ItemType = "crossbow";
            // Abyssal effect is chosen first for Bows/Crossbows, as the ShortRange effect precludes the RangeBoost positive effect.
            if (IsAbyssal)
            {
                // Currently applying only one abyssal effect (and sometimes, one immunity).
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
                if (Rand.NextDouble() < AbyssalImmunityChance)
                {
                    string abyssalImmunity = AbyssalImmunityPoints.ElementAt(Rand.Next(AbyssalImmunityPoints.Count)).Key;
                    AbyssalImmunityPoints[abyssalImmunity] += 1;
                }
            }
            int points = IsAbyssal ? AbyssalPoints : LegendPoints;
            for (int i = 0; i < points; i++)
                AddEffectPoint();
        }

        internal override bool EffectAllowed(string effect)
        {
            // Check if effect clashes with a setting or another effect.
            // Will always find a valid set (e.g. all points in DamageBoost).
            if (effect == "IsGreatbow" && IsCrossbow)
                return false;
            if (effect == "IsAvelyn" && !IsCrossbow)
                return false;
            if (effect == "Light" && AbyssalEffectPoints["Heavy"] > 0)
                return false;
            foreach (string statusType in new string[] { "Poison", "Bleed", "Toxic", "Curse" })
            {
                if (effect == $"{statusType}Damage" && StatusType != statusType)
                    return false;
            }
            if (effect == "RangeBoost" && AbyssalEffectPoints["ShortRange"] == 1)
                return false;
            return true;
        }

        public void ApplyEffects(Weapon weaponParam)
        {
            // Applies effects to weapon param.
            // Greatbow or Avelyn upgrade is applied by randomizer.
            if (EffectPoints["DamageBoost"] > 0)
            {
                double damageMultiplier = weaponParam.BasePhysicalDamage * (1.0 + EffectPoints["DamageBoost"] * 0.05);
                weaponParam.BasePhysicalDamage = (ushort)damageMultiplier;
            }
            if (EffectPoints["RangeBoost"] > 0)
                weaponParam.BowRangeChangePercentage += (short)(EffectPoints["RangeBoost"] * 20);
            // Only one status effect can be active.
            if (EffectPoints["PoisonDamage"] > 0)
            {
                int level = 25 * (EffectPoints["PoisonDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Poison Damage ({level})"];
            }
            if (EffectPoints["BleedDamage"] > 0)
            {
                int level = 20 * (EffectPoints["BleedDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Bleed Damage ({level})"];
            }
            if (EffectPoints["ToxicDamage"] > 0)
            {
                int level = 20 * (EffectPoints["ToxicDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Toxic Damage ({level})"];
            }
            if (EffectPoints["CurseDamage"] > 0)
            {
                int level = 20 * (EffectPoints["CurseDamage"] + 1);
                weaponParam.SpecialEffectOnHit1 = SpEffectGenerator.Effects[$"Curse Damage ({level})"];
            }
            if (EffectPoints["ElementalDamage"] > 0)
            {
                weaponParam.BasePhysicalDamage -= (ushort)(10 * EffectPoints["ElementalDamage"]);
                switch (ElementType)
                {
                    case "Magic":
                        weaponParam.BaseMagicDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ScalingFormulaType = 1;  // Magic Melee
                        break;
                    case "Fire":
                        weaponParam.BaseFireDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
                        break;
                    case "Lightning":
                        weaponParam.BaseLightningDamage += (ushort)(50 * EffectPoints["ElementalDamage"]);
                        weaponParam.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Lightning;
                        break;
                }
            }
            if (EffectPoints["Light"] == 1)
                // Half stamina cost is applied to each behavior.
                weaponParam.Weight = Math.Max(0.5f, weaponParam.Weight - 5.0f);

            ApplyAbyssalEffects(weaponParam);
        }

        void ApplyAbyssalEffects(Weapon weaponParam)
        {
            // TODO: Not sure if the self-damage effects will work with arrows!

            if (AbyssalEffectPoints["SelfDamageOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Damage (10)"];
            if (AbyssalEffectPoints["SelfPoisonOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Poison (20)"];
            if (AbyssalEffectPoints["SelfBleedOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Bleed (20)"];
            if (AbyssalEffectPoints["SelfToxicOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Toxic (20)"];
            if (AbyssalEffectPoints["SelfCurseOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Curse (20)"];
            if (AbyssalEffectPoints["LoseSoulsOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Lose Souls (100)"];
            if (AbyssalEffectPoints["Heavy"] == 1)
                weaponParam.Weight += 8.0f;  // Double stamina cost is applied to each behavior.
            if (AbyssalEffectPoints["ShortRange"] == 1)
                weaponParam.BowRangeChangePercentage -= 50;
            if (AbyssalEffectPoints["SelfSlow"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Self Slow (10%, 5s)"];
            if (AbyssalEffectPoints["BoostEnemyDamageOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Damage (30%, 10s)"];
            if (AbyssalEffectPoints["BoostEnemySpeedOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Speed (20%, 5s)"];
            if (AbyssalEffectPoints["BoostEnemyPoiseOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Buff Enemy Poise (300, 10s)"];
            if (AbyssalEffectPoints["DelayedEnemyHealOnHit"] == 1)
                weaponParam.SpecialEffectOnHit2 = SpEffectGenerator.Effects["Delayed Enemy Heal (Delay)"];

            if (AbyssalImmunityPoints["NoDemonDamage"] == 1)
                weaponParam.DamageAgainstDemonsMultiplier = 0.0f;
            if (AbyssalImmunityPoints["NoSkeletonDamage"] == 1)
                weaponParam.WeakToDivineDamageMultiplier = 0.0f;
            if (AbyssalImmunityPoints["NoDragonDamage"] == 1)
                weaponParam.GodDamageMultiplier = 0.0f;  // God == Dragon in this mod.
            if (AbyssalImmunityPoints["NoAbyssDamage"] == 1)
                weaponParam.AbyssDamageMultiplier = 0.0f;
        }

        internal override string ChooseRandomEffect()
        {
            // Weighted choice of effect based on remaining open points.
            int total = EffectPoints.Sum(t => MaxEffectPoints[t.Key] - t.Value);
            int roll = Rand.Next(total);
            long weightSum = 0;
            for (int i = 0; i < EffectPoints.Count; i++)
            {
                weightSum += MaxEffectPoints.ElementAt(i).Value - EffectPoints.ElementAt(i).Value;
                if (roll < weightSum)
                {
                    string effect = EffectPoints.ElementAt(i).Key;
                    if (effect == "ElementalDamage" && ElementType == "")
                        ElementType = ElementTypes[Rand.Next(ElementTypes.Count)];  // Choose element.
                    else if (effect == "PoisonDamage" && StatusType == "")
                        StatusType = "Poison";
                    else if (effect == "BleedDamage" && StatusType == "")
                        StatusType = "Bleed";
                    else if (effect == "ToxicDamage" && StatusType == "")
                        StatusType = "Toxic";
                    else if (effect == "CurseDamage" && StatusType == "")
                        StatusType = "Curse";
                    return effect;
                }
            }
            throw new Exception($"Failure to choose random effect (roll {roll}, weight total {total})");
        }
    }

    class LegendaryShieldEffects : LegendaryEffects
    {
        internal override int LegendPoints { get; } = 3;
        internal override int AbyssalPoints { get; } = 5;
        internal override string ItemType { get; } = "shield";
        internal double AbyssalImmunityChance { get; } = 0.3;

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "PhysicalGuardBoost", 0 },
            { "MagicGuardBoost", 0 },
            { "FireGuardBoost", 0 },
            { "LightningGuardBoost", 0 },
            { "StatusGuardBoost", 0 },
            { "StabilityBoost", 0 },
            { "Light", 0 },
            { "SpecialBetterParry", 0 },
            { "SpecialBonewheel", 0 },
            { "SpecialCrystalRing", 0 },
            { "SpecialHavel", 0 },
            { "SpecialSuperBash", 0 },
        };
        public string SpecialType { get; internal set; } = "";

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "PhysicalGuardBoost", 3 },
            { "MagicGuardBoost", 1 },
            { "FireGuardBoost", 1 },
            { "LightningGuardBoost", 1 },
            { "StatusGuardBoost", 2 },
            { "StabilityBoost", 2 },
            { "Light", 1 },
            { "SpecialBetterParry", 1 },
            { "SpecialBonewheel", 1 },
            { "SpecialCrystalRing", 1 },
            { "SpecialHavel", 1 },
            { "SpecialSuperBash", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PhysicalGuardBoost", "provides superior physical protection" },
            { "MagicGuardBoost", "has strong magic resistance" },
            { "FireGuardBoost", "has strong fire resistance" },
            { "LightningGuardBoost", "has strong lightning resistance" },
            { "StatusGuardBoost", "is highly resistant to ailments" },
            { "StabilityBoost", "is highly stable" },
            { "Light", "is unusually light" },
            { "SpecialBetterParry", "can parry foes more easily" },
            { "SpecialBonewheel", "can grind enemies into dust" },
            { "SpecialCrystalRing", "emits a magical force" },
            { "SpecialHavel", "can generate a stone shell" },
            { "SpecialSuperBash", "readily knocks down foes" },
        };
        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "PoorStability", 0 },
            { "WeakensAttackOnHit", 0 },
            { "CursesOnHit", 0 },
            { "LoseSoulsOnHit", 0 },
            { "Heavy", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PoorStability", "is not very stable" },
            { "WeakensAttackOnHit", "drains your attack power temporarily when hit" },
            { "CursesOnHit", "curses its wielder when absorbing blows" },
            { "LoseSoulsOnHit", "consumes souls when struck" },
            { "Heavy", "is excessively burdensome" },
        };
        public override CountDict AbyssalImmunityPoints { get; internal set; } = new CountDict()
        {
            { "NoMagicGuard", 0 },
            { "NoFireGuard", 0 },
            { "NoLightningGuard", 0 },
        };
        internal override Dictionary<string, string> AbyssalImmunityDescriptions { get; } = new Dictionary<string, string>()
        {
            { "NoMagicGuard", "provides no defense against magic" },
            { "NoFireGuard", "provides no defense against fire" },
            { "NoLightningGuard", "provides no defense against lightning" },
        };

        public LegendaryShieldEffects(bool isAbyssal, Random random = null) : base(isAbyssal, random)
        {
            if (IsAbyssal)
            {
                // Currently applying only one abyssal effect (and sometimes, one immunity).
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
                if (Rand.NextDouble() < AbyssalImmunityChance)
                {
                    string abyssalImmunity = AbyssalImmunityPoints.ElementAt(Rand.Next(AbyssalImmunityPoints.Count)).Key;
                    AbyssalImmunityPoints[abyssalImmunity] += 1;
                }
            }
            int points = IsAbyssal ? AbyssalPoints : LegendPoints;
            for (int i = 0; i < points; i++)
                AddEffectPoint();
        }

        internal override bool EffectAllowed(string effect)
        {
            // Check if effect clashes with a setting or another effect.
            // Will always find a valid set (e.g. all points in DamageBoost).
            if (effect == "Light" && AbyssalEffectPoints["Heavy"] > 0)
                return false;
            if (effect == "StabilityBoost" && AbyssalEffectPoints["PoorStability"] > 0)
                return false;
            foreach (string elementType in new string[] { "Magic", "Fire", "Lightning" })
            {
                if (effect == $"{elementType}GuardBoost" && AbyssalImmunityPoints[$"No{elementType}Guard"] > 0)
                    return false;
            }
            foreach (string specialType in new string[] { "BetterParry", "Bonewheel", "CrystalRing", "Havel", "SuperBash" })
            {
                if (effect == $"Special{specialType}" && SpecialType != specialType)
                    return false;
            }
            return true;
        }

        public void ApplyEffects(Weapon weaponParam)
        {
            if (EffectPoints["PhysicalGuardBoost"] > 0)
                weaponParam.PhysicalGuardPercentage = Math.Min(100.0f, weaponParam.PhysicalGuardPercentage + EffectPoints["PhysicalGuardBoost"] * 5.0f);
            if (EffectPoints["MagicGuardBoost"] > 0)
                weaponParam.MagicGuardPercentage = Math.Min(100.0f, weaponParam.MagicGuardPercentage + EffectPoints["MagicGuardBoost"] * 30.0f);
            if (EffectPoints["FireGuardBoost"] > 0)
                weaponParam.FireGuardPercentage = Math.Min(100.0f, weaponParam.FireGuardPercentage + EffectPoints["FireGuardBoost"] * 30.0f);
            if (EffectPoints["LightningGuardBoost"] > 0)
                weaponParam.LightningGuardPercentage = Math.Min(100.0f, weaponParam.LightningGuardPercentage + EffectPoints["LightningGuardBoost"] * 30.0f);
            if (EffectPoints["StatusGuardBoost"] > 0)
            {
                weaponParam.PoisonDamageReductionWhenGuarding = (sbyte)Math.Min(100.0f, weaponParam.PoisonDamageReductionWhenGuarding + EffectPoints["StatusGuardBoost"] * 20.0f);
                weaponParam.BleedDamageReductionWhenGuarding = (sbyte)Math.Min(100.0f, weaponParam.BleedDamageReductionWhenGuarding + EffectPoints["StatusGuardBoost"] * 20.0f);
                weaponParam.ToxicDamageReductionWhenGuarding = (sbyte)Math.Min(100.0f, weaponParam.ToxicDamageReductionWhenGuarding + EffectPoints["StatusGuardBoost"] * 20.0f);
                weaponParam.CurseDamageReductionWhenGuarding = (sbyte)Math.Min(100.0f, weaponParam.CurseDamageReductionWhenGuarding + EffectPoints["StatusGuardBoost"] * 20.0f);
            }
            if (EffectPoints["StabilityBoost"] > 0)
                // Adds 20% or 40% to guard stamina defense.
                weaponParam.GuardStaminaDefense = (short)(weaponParam.GuardStaminaDefense * (1.0 + EffectPoints["StabilityBoost"] * 0.2));
            if (EffectPoints["Light"] > 0)
                // Half stamina cost is applied to each behavior.
                weaponParam.Weight = Math.Max(0.5f, weaponParam.Weight - 5.0f);
            // Special effects are applied in randomizer through special selection and bash attack param.

            ApplyAbyssalEffects(weaponParam);
        }

        void ApplyAbyssalEffects(Weapon weaponParam)
        {
            if (AbyssalEffectPoints["PoorStability"] == 1)
                weaponParam.GuardStaminaDefense = (short)(weaponParam.GuardStaminaDefense / 2);
            // Guard hit effects are applied in EMEVD.
            if (AbyssalEffectPoints["WeakensAttackOnHit"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["On Guard Weakens Physical Attack (FLAG)"];
            if (AbyssalEffectPoints["CursesOnHit"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["On Guard Curses (FLAG)"];
            if (AbyssalEffectPoints["LoseSoulsOnHit"] == 1)
                weaponParam.EquippedSpecialEffect2 = SpEffectGenerator.Effects["On Guard Lose Souls (FLAG)"];
            if (AbyssalEffectPoints["Heavy"] == 1)
                // Double stamina cost is applied to each behavior.
                weaponParam.Weight += 8.0f;
        }

        internal override string ChooseRandomEffect()
        {
            // Weighted choice of effect based on remaining open points.
            int total = EffectPoints.Sum(t => MaxEffectPoints[t.Key] - t.Value);
            int roll = Rand.Next(total);
            long weightSum = 0;
            for (int i = 0; i < EffectPoints.Count; i++)
            {
                weightSum += MaxEffectPoints.ElementAt(i).Value - EffectPoints.ElementAt(i).Value;
                if (roll < weightSum)
                {
                    string effect = EffectPoints.ElementAt(i).Key;
                    if (effect.StartsWith("Special") && SpecialType == "")
                        SpecialType = effect.Substring(7);
                    return effect;
                }
            }
            throw new Exception($"Failure to choose random effect (roll {roll}, weight total {total})");
        }
    }
}
