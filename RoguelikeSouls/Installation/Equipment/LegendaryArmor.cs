using System;
using System.Collections.Generic;
using System.Linq;
using CountDict = System.Collections.Generic.Dictionary<string, int>;

namespace RoguelikeSouls.Installation
{
    abstract class LegendaryArmorEffects : LegendaryEffects
    {
        /* Armor works differently to weapons.
         * 
         * "Basic" legendary effects can apply to any armor piece type,
         * and are quite common (about 60% of armor). Each legendary piece 
         * has one of these effects, and the "max" point dictionary is 
         * used to control their relative frequency. These don't need any
         * special effect slot.
         * 
         * "Advanced" legendary effects are less common (about 20% of armor)
         * and are unique to each armor piece type. These use the same special
         * effect slot as the stamina reduction effect (1), which is just removed
         * entirely on legendary armor. An armor piece may have this effect
         * without also rolling a "basic" effect.
         * 
         * Abyssal armor gets an *exaggerated* variant of both legendary
         * effects, rather than getting two effects, in addition to one 
         * abyssal drawback. The drawback uses special effect slot (3) if needed.
         * 
         * (TODO: Should do the same thing with weapons, rather than
         * giving abyssal weapons more points. Better to focus on less
         * abilities and be more memorable.)
         */

        public bool IsBasic { get; }
        public bool IsNormal { get; }
        internal int BasicPoints { get; } = 1;
        internal override int LegendPoints { get; } = 1;
        internal override int AbyssalPoints { get; } = 1;

        public CountDict BasicEffectPoints { get; internal set; } = new CountDict()
        {
            { "PhysicalDefBoost", 0 },
            { "MagicDefBoost", 0 },
            { "FireDefBoost", 0 },
            { "LightningDefBoost", 0 },
            { "PoisonDefBoost", 0 },  // includes toxic resistance
            { "BleedDefBoost", 0 },
            // No curse defense boost (status is too rare).
            { "PoiseBoost", 0 },
            { "Light", 0 },
        };

        internal CountDict MaxBasicEffectPoints { get; } = new CountDict()
        {
            { "PhysicalDefBoost", 1 },
            { "MagicDefBoost", 1 },
            { "FireDefBoost", 1 },
            { "LightningDefBoost", 1 },
            { "PoisonDefBoost", 1 },  // includes toxic resistance
            { "BleedDefBoost", 1 },
            // No curse defense boost (status is too rare).
            { "PoiseBoost", 1 },
            { "Light", 1 },
        };

        internal virtual Dictionary<string, string> GreatEffectDescriptions { get; }

        internal Dictionary<string, string> BasicEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PhysicalDefBoost", "has high physical defense" },
            { "MagicDefBoost", "has high magic defense" },
            { "FireDefBoost", "has high fire defense" },
            { "LightningDefBoost", "has high lightning defense" },
            { "PoisonDefBoost", "has high poison resistance" },  // includes toxic resistance
            { "BleedDefBoost", "has high bleed resistance" },
            // No curse defense boost (status is too rare).
            { "PoiseBoost", "gives its wearer high poise" },
            { "Light", "is unusually light" },
        };

        internal Dictionary<string, string> AbyssalBasicEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PhysicalDefBoost", "has incredible physical defense" },
            { "MagicDefBoost", "has incredible magic defense" },
            { "FireDefBoost", "has incredible fire defense" },
            { "LightningDefBoost", "has incredible lightning defense" },
            { "PoisonDefBoost", "has incredible poison resistance" },
            { "BleedDefBoost", "has incredible bleed resistance" },
            // No curse defense boost (status is too rare).
            { "PoiseBoost", "has extremely high poise" },
            { "Light", "is as light as a feather" },
        };

        internal LegendaryArmorEffects(bool isBasic, bool isNormal, bool isAbyssal, Random random = null) : base(isAbyssal, random) 
        {
            IsBasic = isBasic;
            IsNormal = isNormal;
            if (IsAbyssal)
            {
                string abyssalEffect = AbyssalEffectPoints.ElementAt(Rand.Next(AbyssalEffectPoints.Count)).Key;
                AbyssalEffectPoints[abyssalEffect] += 1;
            }
            if (IsBasic)
            { 
                for (int i = 0; i < BasicPoints; i++)
                    AddBasicEffectPoint();
            }
            if (IsNormal)
            {
                int points = IsAbyssal ? AbyssalPoints : LegendPoints;
                for (int i = 0; i < points; i++)
                    AddEffectPoint();
            }
        }

        internal void AddBasicEffectPoint()
        {
            string effect;
            do
            {
                effect = ChooseBasicRandomEffect();
            } while (!EffectAllowed(effect));
            BasicEffectPoints[effect] += 1;
        }

        internal string ChooseBasicRandomEffect()
        {
            // Weighted choice of effect based on remaining open points.
            int total = BasicEffectPoints.Sum(t => MaxBasicEffectPoints[t.Key] - t.Value);
            int roll = Rand.Next(total);
            long weightSum = 0;
            for (int i = 0; i < BasicEffectPoints.Count; i++)
            {
                weightSum += MaxBasicEffectPoints.ElementAt(i).Value - BasicEffectPoints.ElementAt(i).Value;
                if (roll < weightSum)
                {
                    return BasicEffectPoints.ElementAt(i).Key;
                }
            }
            throw new Exception($"Failure to choose random basic effect (roll {roll}, weight total {total})");
        }

        internal void ApplyBasicEffects(SoulsFormatsMod.PARAMS.Armor armorParam)
        {
            if (BasicEffectPoints["PhysicalDefBoost"] == 1)
                armorParam.PhysicalDefense += (ushort)(IsAbyssal ? 40 : 20);
            if (BasicEffectPoints["MagicDefBoost"] == 1)
                armorParam.MagicDefense += (ushort)(IsAbyssal ? 40 : 20);
            if (BasicEffectPoints["FireDefBoost"] == 1)
                armorParam.FireDefense += (ushort)(IsAbyssal ? 40 : 20);
            if (BasicEffectPoints["LightningDefBoost"] == 1)
                armorParam.LightningDefense += (ushort)(IsAbyssal ? 40 : 20);
            if (BasicEffectPoints["PoisonDefBoost"] == 1)
                armorParam.PoisonResistance += (ushort)(IsAbyssal ? 50 : 25);
            if (BasicEffectPoints["BleedDefBoost"] == 1)
                armorParam.BleedResistance += (ushort)(IsAbyssal ? 50 : 25);
            if (BasicEffectPoints["PoiseBoost"] == 1)
                armorParam.Poise += (short)(IsAbyssal ? 20 : 10);
            if (BasicEffectPoints["Light"] == 1)
                armorParam.Weight *= IsAbyssal ? 0.25f : 0.5f;
        }

        public override string GetEffectDescription()
        {
            // Returns (unwrapped) sentence describing the armor's effects.
            List<string> positiveDescs = new List<string>();
            if (IsAbyssal)
            {
                positiveDescs = new List<string>(AbyssalBasicEffectDescriptions.Where(kv => BasicEffectPoints[kv.Key] > 0).Select(kv => kv.Value)); ;
                positiveDescs.AddRange(GreatEffectDescriptions.Where(kv => EffectPoints[kv.Key] > 0).Select(kv => kv.Value));
            }
            else
            {
                positiveDescs = new List<string>(BasicEffectDescriptions.Where(kv => BasicEffectPoints[kv.Key] > 0).Select(kv => kv.Value));
                positiveDescs.AddRange(EffectDescriptions.Where(kv => EffectPoints[kv.Key] > 0).Select(kv => kv.Value));
            }
            
            string positive = "";
            switch (positiveDescs.Count)
            {
                case 0:
                    throw new Exception($"Found no positive effects to describe for armor.");
                case 1:
                    positive = positiveDescs[0];
                    break;
                case 2:
                    positive = string.Join(" and ", positiveDescs);
                    break;
                default:
                    positive = string.Join(", ", positiveDescs.GetRange(0, positiveDescs.Count - 1)) + $", and {positiveDescs[positiveDescs.Count - 1]}";
                    break;
            }
            List<string> negativeDescs = new List<string>(AbyssalEffectDescriptions.Where(kv => AbyssalEffectPoints[kv.Key] > 0).Select(kv => kv.Value));
            string negative = "";
            switch (negativeDescs.Count)
            {
                case 0:
                    break;
                case 1:
                    negative = negativeDescs[0];
                    break;
                case 2:
                    negative = string.Join(" and ", negativeDescs);
                    break;
                default:
                    negative = string.Join(", ", negativeDescs.GetRange(0, negativeDescs.Count - 1)) + $", and {negativeDescs[negativeDescs.Count - 1]}";
                    break;
            }
            if (negative == "")
            {
                return $"This legendary {ItemType} {positive}.";
            }
            else
            {
                return $"This abyssal {ItemType} {positive}, but {negative}.";
            }
        }

    public abstract void ApplyEffects(SoulsFormatsMod.PARAMS.Armor armorParam);
    }

    class LegendaryHeadArmorEffects : LegendaryArmorEffects
    {
        internal override string ItemType { get; } = "head armor";

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "MoreSoulsGained", 0 },
            { "BetterItemDiscovery", 0 },
            { "CounterDamageBoost", 0 },
            { "CriticalDamageBoost", 0 },
            { "BowRangeBoost", 0 },
            { "MagicDurationBoost", 0 },  // special state
            { "BetterHealing", 0 },
            { "CastLight", 0 },
            { "HasThorns", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "MoreSoulsGained", 1 },
            { "BetterItemDiscovery", 1 },
            { "CounterDamageBoost", 1 },
            { "CriticalDamageBoost", 1 },
            { "BowRangeBoost", 1 },
            { "MagicDurationBoost", 1 },  // special state
            { "BetterHealing", 1 },
            { "CastLight", 1 },
            { "HasThorns", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MoreSoulsGained", "increases collected souls" },
            { "BetterItemDiscovery", "improves its wearer's luck" },
            { "CounterDamageBoost", "increases the effectiveness of well-timed thrusting counterattacks" },
            { "CriticalDamageBoost", "increases the effectiveness of surprise attacks and ripostes" },
            { "BowRangeBoost", "improves marksmanship with bows" },
            { "MagicDurationBoost", "extends the duration of magical effects" },  // special state
            { "BetterHealing", "increases health recovery from healing effects" },
            { "CastLight", "has a luminous aura" },
            { "HasThorns", "can damage foes merely by touching them" },
        };

        internal override Dictionary<string, string> GreatEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MoreSoulsGained", "greatly increases collected souls" },
            { "BetterItemDiscovery", "improves its wearer's luck" },  // can't stack
            { "CounterDamageBoost", "greatly increases the effectiveness of well-timed thrusting counterattacks" },
            { "CriticalDamageBoost", "greatly increases the effectiveness of surprise attacks and ripostes" },
            { "BowRangeBoost", "greatly improves marksmanship with bows" },
            { "MagicDurationBoost", "greatly extends the duration of magical effects" },  // special state
            { "BetterHealing", "greatly increases health recovery from healing effects" },
            { "CastLight", "has a luminous aura" },  // can't be improved
            { "HasThorns", "can severely damage foes merely by touching them" },
        };

        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            // Had Gravity Shift here originally, but it's too painful. Invisibility is also fun.
            { "PlayerInvisible", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PlayerInvisible", "may interfere with self-perception" },
        };

        public LegendaryHeadArmorEffects(bool isBasic, bool isNormal, bool isAbyssal, Random random = null) : base(isBasic, isNormal, isAbyssal, random) { }

        public override void ApplyEffects(SoulsFormatsMod.PARAMS.Armor headArmorParam)
        {
            ApplyBasicEffects(headArmorParam);

            if (EffectPoints["MoreSoulsGained"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "More Souls Gained (50%)" : "More Souls Gained (25%)"];
            if (EffectPoints["BetterItemDiscovery"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "More Item Discovery (+)" : "More Item Discovery"];
            if (EffectPoints["CounterDamageBoost"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Counter Damage Up (80%)" : "Counter Damage Up (40%)"];
            if (EffectPoints["CriticalDamageBoost"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Critical Throws (+)" : "Critical Throws"];
            if (EffectPoints["BowRangeBoost"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Bow Range (130)" : "Bow Range (65)"];
            if (EffectPoints["MagicDurationBoost"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Magic Duration (+)" : "Magic Duration"];
            if (EffectPoints["BetterHealing"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Better Healing (100%)" : "Better Healing (50%)"];
            if (EffectPoints["CastLight"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Cast Light (+)" : "Cast Light"];
            if (EffectPoints["HasThorns"] > 0)
                headArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Head Thorns (60)" : "Head Thorns (20)"];

            ApplyAbyssalEffects(headArmorParam);
        }

        void ApplyAbyssalEffects(SoulsFormatsMod.PARAMS.Armor armorParam)
        {
            if (AbyssalEffectPoints["PlayerInvisible"] == 1)
                armorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Player Invisible (MOD FLAG)"];
        }
    }

    class LegendaryBodyArmorEffects : LegendaryArmorEffects
    {
        internal override string ItemType { get; } = "body armor";

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "MaxHealthBoost", 0 },
            { "MaxStaminaBoost", 0 },
            { "StaminaRegenBoost", 0 },
            { "GhostEffect", 0 },
            { "AttunementSlotBoost", 0 },
            { "PoiseRegenBonus", 0 },
            { "StabilityBoost", 0 },
            { "HasThorns", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "MaxHealthBoost", 1 },
            { "MaxStaminaBoost", 1 },
            { "StaminaRegenBoost", 1 },
            { "GhostEffect", 1 },
            { "AttunementSlotBoost", 1 },
            { "PoiseRegenBonus", 1 },
            { "StabilityBoost", 1 },
            { "HasThorns", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MaxHealthBoost", "increases maximum health" },
            { "MaxStaminaBoost", "increases maximum stamina" },
            { "StaminaRegenBoost", "quickens stamina regeneration" },
            { "GhostEffect", "makes its wearer harder to spot" },
            { "AttunementSlotBoost", "allows its wearer to attune more spells" },
            { "PoiseRegenBonus", "improves poise recuperation" },
            { "StabilityBoost", "improves stability when blocking" },
            { "HasThorns", "can damage foes merely by touching them" },
        };

        internal override Dictionary<string, string> GreatEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MaxHealthBoost", "greatly increases maximum health" },
            { "MaxStaminaBoost", "greatly increases maximum stamina" },
            { "StaminaRegenBoost", "greatly quickens stamina regeneration" },
            { "GhostEffect", "makes its wearer almost invisible" },
            { "AttunementSlotBoost", "allows its wearer to attune many more spells" },
            { "PoiseRegenBonus", "greatly improves poise recuperation" },
            { "StabilityBoost", "greatly improves stability when blocking" },
            { "HasThorns", "can severely damage foes merely by touching them" },
        };

        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            // TODO: Test if negative sight/hearing reduction can make the player MORE visible/louder.
            // TODO: Test if -99 attunement slots just eliminates them completely (for head, probably).

            { "ReducedHealing", 0 },
            { "HealthDrain", 0 },
            { "Heavy", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "ReducedHealing", "limits recovery when healing" },
            { "HealthDrain", "drains health slowly over time" },
            { "Heavy", "is unusually heavy" },
        };

        public LegendaryBodyArmorEffects(bool isBasic, bool isNormal, bool isAbyssal, Random random = null) : base(isBasic, isNormal, isAbyssal, random) { }

        public override void ApplyEffects(SoulsFormatsMod.PARAMS.Armor bodyArmorParam)
        {
            ApplyBasicEffects(bodyArmorParam);

            if (EffectPoints["MaxHealthBoost"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Max Health Up (40%)" : "Max Health Up (20%)"];
            if (EffectPoints["MaxStaminaBoost"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Max Stamina Up (40%)" : "Max Stamina Up (20%)"];
            if (EffectPoints["StaminaRegenBoost"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Stamina Regen Up (40)" : "Stamina Regen Up (20)"];
            if (EffectPoints["GhostEffect"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Ghost (90%)" : "Ghost (70%)"];
            if (EffectPoints["AttunementSlotBoost"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Attunement Slots Up (4)" : "Attunement Slots Up (2)"];
            if (EffectPoints["PoiseRegenBonus"] > 0)
                bodyArmorParam.PoiseRecoveryTimeModifier -= 0.2f;
            if (EffectPoints["StabilityBoost"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Stability Up (40%)" : "Stability Up (20%)"];
            if (EffectPoints["HasThorns"] > 0)
                bodyArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Body Thorns (180)" : "Body Thorns (60)"];

            ApplyAbyssalEffects(bodyArmorParam);
        }

        void ApplyAbyssalEffects(SoulsFormatsMod.PARAMS.Armor bodyArmorParam)
        {
            if (AbyssalEffectPoints["ReducedHealing"] == 1)
                bodyArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Reduced Healing (-50%)"];
            if (AbyssalEffectPoints["HealthDrain"] == 1)
                bodyArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Health Drain (5 / 1s)"];
            if (AbyssalEffectPoints["Heavy"] == 1)
                bodyArmorParam.Weight += 8.0f;
        }
    }

    class LegendaryArmsArmorEffects : LegendaryArmorEffects
    {
        internal override string ItemType { get; } = "hand armor";

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "PhysicalAttackBoost", 0 },
            { "MagicAttackBoost", 0 },
            { "FireAttackBoost", 0 },
            { "LightningAttackBoost", 0 },
            { "SlowDurabilityLoss", 0 },
            { "FlipDodges", 0 },  // on arms rather than legs so you can combo it with damage rolls
            { "HasThorns", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "PhysicalAttackBoost", 1 },
            { "MagicAttackBoost", 1 },
            { "FireAttackBoost", 1 },
            { "LightningAttackBoost", 1 },
            { "SlowDurabilityLoss", 1 },
            { "FlipDodges", 1 },  // on arms rather than legs so you can combo it with damage rolls
            { "HasThorns", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PhysicalAttackBoost", "increases physical attack damage" },
            { "MagicAttackBoost", "increases magic attack damage" },
            { "FireAttackBoost", "increases fire attack damage" },
            { "LightningAttackBoost", "increases lightning attack damage" },
            { "SlowDurabilityLoss", "slows all durability loss" },
            { "FlipDodges", "let their wearer to backflip with ease" },
            { "HasThorns", "can damage foes merely by touching them" },
        };

        internal override Dictionary<string, string> GreatEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PhysicalAttackBoost", "greatly increases physical attack damage" },
            { "MagicAttackBoost", "greatly increases magic attack damage" },
            { "FireAttackBoost", "greatly increases fire attack damage" },
            { "LightningAttackBoost", "greatly increases lightning attack damage" },
            { "SlowDurabilityLoss", "slows all durability loss" },  // no change
            { "FlipDodges", "let their wearer to backflip with ease" },  // no change
            { "HasThorns", "can severely damage foes merely by touching them" },
        };

        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "PoisonResistanceDown", 0 },  // includes toxic
            { "BleedResistanceDown", 0 },
            { "LessSoulsGained", 0 },
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "PoisonResistanceDown", "have imperfections that leave their wearer more vulnerable to poison" },  // includes toxic
            { "BleedResistanceDown", "are extremely poor at stopping bleeding" },
            { "LessSoulsGained", "take a portion of souls for themselves" },
        };

        public LegendaryArmsArmorEffects(bool isBasic, bool isNormal, bool isAbyssal, Random random = null) : base(isBasic, isNormal, isAbyssal, random) { }

        public override void ApplyEffects(SoulsFormatsMod.PARAMS.Armor armsArmorParam)
        {
            ApplyBasicEffects(armsArmorParam);

            if (EffectPoints["PhysicalAttackBoost"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Physical Attack Up (150)" : "Physical Attack Up (75)"];
            if (EffectPoints["MagicAttackBoost"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Magic Attack Up (150)" : "Magic Attack Up (75)"];
            if (EffectPoints["FireAttackBoost"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Fire Attack Up (150)" : "Fire Attack Up (75)"];
            if (EffectPoints["LightningAttackBoost"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Lightning Attack Up (150)" : "Lightning Attack Up (75)"];
            if (EffectPoints["SlowDurabilityLoss"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Slower Durability Loss (20)" : "Slower Durability Loss (10)"];
            if (EffectPoints["FlipDodges"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Flip Dodge (+)" : "Flip Dodge"];
            if (EffectPoints["HasThorns"] > 0)
                armsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Arms Thorns (60)" : "Arms Thorns (20)"];

            ApplyAbyssalEffects(armsArmorParam);
        }

        void ApplyAbyssalEffects(SoulsFormatsMod.PARAMS.Armor armsArmorParam)
        {
            if (AbyssalEffectPoints["PoisonResistanceDown"] == 1)
                armsArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Poison Resistance Down (-75%)"];
            if (AbyssalEffectPoints["BleedResistanceDown"] == 1)
                armsArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Bleed Resistance Down (-75%)"];
            if (AbyssalEffectPoints["LessSoulsGained"] == 1)
                armsArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Less Souls Gained (-40%)"];
        }
    }

    class LegendaryLegsArmorEffects : LegendaryArmorEffects
    {
        internal override string ItemType { get; } = "leg armor";

        public override CountDict EffectPoints { get; internal set; } = new CountDict()
        {
            { "MaxEquipBoost", 0 },
            { "RustedIronRing", 0 },
            { "LavaResistance", 0 },
            { "QuietFootsteps", 0 },
            { "HighImpactKick", 0 },
            { "HasThorns", 0 },
        };

        internal override CountDict MaxEffectPoints { get; } = new CountDict()
        {
            { "MaxEquipBoost", 1 },
            { "RustedIronRing", 1 },
            { "LavaResistance", 1 },
            { "QuietFootsteps", 1 },
            { "HighImpactKick", 1 },
            { "HasThorns", 1 },
        };

        internal override Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MaxEquipBoost", "let their wearer carry more equipment" },
            { "RustedIronRing", "allows their wearer to move unimpeded in poor terrain" },
            { "LavaResistance", "lessens injuries from walking on lava" },
            { "QuietFootsteps", "makes footsteps silent" },
            { "HighImpactKick", "can kick with greater force" },
            { "HasThorns", "can damage foes merely by touching them" },
        };

        internal override Dictionary<string, string> GreatEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "MaxEquipBoost", "let their wearer carry much more equipment" },
            { "RustedIronRing", "allows their wearer to move unimpeded in poor terrain" },  // no change
            { "LavaResistance", "completely eliminates injuries from walking on lava" },
            { "QuietFootsteps", "makes footsteps silent" },  // no change
            { "HighImpactKick", "can kick with extreme force" },
            { "HasThorns", "can severely damage foes merely by touching them" },
        };

        public override CountDict AbyssalEffectPoints { get; internal set; } = new CountDict()
        {
            { "SelfDamageOnRoll", 0 },
            { "SlowerStaminaRegen", 0 },
            // TODO: Feels like I'm missing an interesting not-terrible third one.
        };
        internal override Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>()
        {
            { "SelfDamageOnRoll", "make rolling quite painful" },
            { "SlowerStaminaRegen", "reduce stamina regeneration speed" },
        };

        public LegendaryLegsArmorEffects(bool isBasic, bool isNormal, bool isAbyssal, Random random = null) : base(isBasic, isNormal, isAbyssal, random) { }

        public override void ApplyEffects(SoulsFormatsMod.PARAMS.Armor legsArmorParam)
        {
            ApplyBasicEffects(legsArmorParam);

            if (EffectPoints["MaxEquipBoost"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Max Equip Up (80%)" : "Max Equip Up (40%)"];
            if (EffectPoints["RustedIronRing"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "No Liquid Slowdown (+)" : "No Liquid Slowdown"];
            if (EffectPoints["LavaResistance"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Lava Resistance (100%)" : "Lava Resistance (80%)"];
            if (EffectPoints["QuietFootsteps"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Quiet Footsteps (+)" : "Quiet Footsteps"];
            if (EffectPoints["HighImpactKick"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "High Impact Kick (Blow Backward)" : "High Impact Kick (Strike)"];
            if (EffectPoints["HasThorns"] > 0)
                legsArmorParam.WearerSpecialEffect1 = SpEffectGenerator.Effects[IsAbyssal ? "Legs Thorns (60)" : "Legs Thorns (20)"];

            ApplyAbyssalEffects(legsArmorParam);
        }

        void ApplyAbyssalEffects(SoulsFormatsMod.PARAMS.Armor legsArmorParam)
        {
            if (AbyssalEffectPoints["SelfDamageOnRoll"] == 1)
                legsArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Rolling Damage (EMEVD FLAG)"];
            if (AbyssalEffectPoints["SlowerStaminaRegen"] == 1)
                legsArmorParam.WearerSpecialEffect3 = SpEffectGenerator.Effects["Stamina Regen Down (-20)"];
        }
    }
}
