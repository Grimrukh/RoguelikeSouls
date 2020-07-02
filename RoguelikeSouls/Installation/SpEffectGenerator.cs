using SoulsFormatsMod.PARAMS;
using System.Collections.Generic;
using SoulsFormatsMod;
using EntryDict = System.Collections.Generic.Dictionary<string, int>;
using System;

namespace RoguelikeSouls.Installation
{
    enum ATTACK_ATTRIBUTE : byte
    {
        NoDamage = 0,  // some Attacks are guarding actions
        Slash = 1,
        Strike = 2,
        Thrust = 3,
        Neutral = 4,  // most common
    }

    enum SAVE_CATEGORY : sbyte
    {
        NoSave = -1,
        Poison = 0,
        Bleed = 1,
        Toxic = 2,
        Egg = 3,
        DragonHeadStone = 4,
        DragonTorsoStone = 5,
    }
    enum SPECIAL_ATTRIBUTE : byte
    {
        NoType = 0,
        Physical = 1,  // used for parries, ripostes, guarding, falls, Force miracles
        Fire = 2,
        Magic = 3,
        Poison = 4,
        // 5 is not used.
        Lightning = 6,
        StoneCurse = 7,  // e.g. Basilisk breath
        CrystalCurse = 8,  // e.g. Seath's crystal attacks
        Default = 255,  // most basic physical attacks; could default to Physical?
    }
    enum AFFECTED_WEAPON : byte
    {
        All = 0,
        CurrentRightHand = 1,  // effect will end if weapon is changed
        CurrentLeftHand = 2,  // effect will end if weapon is changed
        Self = 3,  // affects character directly (i.e. status damage) rather than being applied to hits
        FootDamage = 4,  // from kicking or landing, e.g. Orange Charred Ring effect
    }

    class SpEffectGenerator
    {
        SpEffect SpEffectTemplate { get => Mod.VanillaGPARAM.SpEffects[81001]; }  // duration -1, update interval 0, affects all characters except White/Black/Invader phantoms.
        readonly SoulsMod Mod;

        public static EntryDict Effects = new EntryDict()
        {
            // Weapon Upgrades

            { "Dire (EMEVD FLAG)", 8000 },
            { "Dire Damage (-20%)", 8001 },  // First four lives from Cat Ring still apply this.
            { "Dire Damage (-10%)", 8002 },
            { "Dire Damage (+0%)",  8003 },  // Still applied, for simplicity and potential balancing.
            { "Dire Damage (+20%)", 8004 },
            { "Dire Damage (+40%)", 8005 },  // Last life.
        
            { "Draconic Burn (Apply)",        8010 },
            { "Draconic Burn (60 / 5s)",      8011 },
            { "Draconic Burn Self (20 / 5s)", 8012 },

            { "Enchanted (MOD HIT FLAG)", 8015 },

            // Positive Weapon Effects
            
            { "Poison Damage (25)",  8020 },
            { "Poison Damage (50)",  8021 },
            { "Poison Damage (75)",  8022 },
            { "Poison Damage (100)", 8023 },
            { "Poison Damage (125)", 8024 },

            { "Bleed Damage (20)",  8030 },
            { "Bleed Damage (40)",  8031 },
            { "Bleed Damage (60)",  8032 },
            { "Bleed Damage (80)",  8033 },
            { "Bleed Damage (100)", 8034 },

            { "Toxic Damage (20)",  8040 },
            { "Toxic Damage (40)",  8041 },
            { "Toxic Damage (60)",  8042 },
            { "Toxic Damage (80)",  8043 },
            { "Toxic Damage (100)", 8044 },

            { "Curse Damage (20)",  8050 },
            { "Curse Damage (40)",  8051 },
            { "Curse Damage (60)",  8052 },
            { "Curse Damage (80)",  8053 },
            { "Curse Damage (100)", 8054 },

            { "Magic Damage Up On Hit (30%, 8s)", 8060 },

            // Negative Weapon Effects

            { "Self Damage (10)", 8070 },
            { "Self Poison (20)", 8071 },
            { "Self Bleed (20)",  8072 },
            { "Self Toxic (20)",  8073 },
            { "Self Curse (20)",  8074 },
            { "Lose Souls (100)",  8075 },
            { "Self Slow (10%, 5s)",  8076 },
            { "Buff Enemy Damage (30%, 10s)",  8077 },
            { "Buff Enemy Speed (20%, 5s)",  8078 },
            { "Buff Enemy Poise (300, 10s)",  8079 },
            { "Delayed Enemy Heal (Delay)",  8080 },
            { "Delayed Enemy Heal (100)",  8081 },
            { "Self Slow (20%)", 8082 },
            { "Half Spell Casts", 8083 },
            { "On Guard (TAE TRIGGER)", 8084 },  // Always applied by TAE.
            { "On Guard Weakens Physical Attack (FLAG)", 8085 },
            { "On Guard Weakens Physical Attack (80%, 5s)", 8086 },
            { "On Guard Curses (FLAG)", 8087 },
            { "On Guard Curses (20)", 8088 },
            { "On Guard Lose Souls (FLAG)", 8089 },
            { "On Guard Lose Souls (200)", 8090 },

            // Positive Head Armor Effects

            { "More Souls Gained (25%)", 8100 },
            { "More Souls Gained (50%)", 8150 },
            { "More Item Discovery", 8101 },
            { "More Item Discovery (+)", 8151 },
            { "Counter Damage Up (40%)", 8102 },
            { "Counter Damage Up (80%)", 8152 },
            { "Critical Throws", 8103 },
            { "Critical Throws (+)", 8153 },
            { "Bow Range (65)", 8104 },
            { "Bow Range (130)", 8154 },
            { "Magic Duration", 8105 },
            { "Magic Duration (+)", 8155 },
            { "Better Healing (50%)", 8106 },
            { "Better Healing (100%)", 8156 },
            { "Cast Light", 8107 },
            { "Cast Light (+)", 8157 },
            { "Head Thorns (20)", 8110 },
            { "Head Thorns (60)", 8160 },

            // Negative Head Armor Effects

            { "Player Invisible (MOD FLAG)", 8190 },

            // Positive Body Armor Effects
            
            { "Max Health Up (20%)", 8200 },
            { "Max Health Up (40%)", 8250 },
            { "Max Stamina Up (20%)", 8201 },
            { "Max Stamina Up (40%)", 8251 },
            { "Stamina Regen Up (20)", 8202 },
            { "Stamina Regen Up (40)", 8252 },
            { "Ghost (70%)", 8203 },
            { "Ghost (90%)", 8253 },
            { "Attunement Slots Up (2)", 8204 },
            { "Attunement Slots Up (4)", 8254 },
            { "Stability Up (20%)", 8205 },
            { "Stability Up (40%)", 8255 },
            { "Body Thorns (60)", 8206 },
            { "Body Thorns (180)", 8256 },

            // Negative Body Armor Effects

            { "Reduced Healing (-50%)", 8290 },
            { "Health Drain (5 / 1s)", 8291 },

            // Positive Arms Armor Effects

            { "Physical Attack Up (75)", 8300 },
            { "Physical Attack Up (150)", 8350 },
            { "Magic Attack Up (75)", 8301 },
            { "Magic Attack Up (150)", 8351 },
            { "Fire Attack Up (75)", 8302 },
            { "Fire Attack Up (150)", 8352 },
            { "Lightning Attack Up (75)", 8303 },
            { "Lightning Attack Up (150)", 8353 },
            { "Slower Durability Loss (10)", 8304 },
            { "Slower Durability Loss (20)", 8354 },
            { "Flip Dodge", 8305 },
            { "Flip Dodge (+)", 8355 },
            { "Arms Thorns (20)", 8310 },
            { "Arms Thorns (60)", 8360 },

            // Negative Arms Armor Effects
            
            { "Poison Resistance Down (-75%)", 8390 },
            { "Bleed Resistance Down (-75%)", 8391 },
            { "Less Souls Gained (-40%)", 8392 },

            // Positive Legs Armor Effects

            { "Max Equip Up (40%)", 8400 },
            { "Max Equip Up (80%)", 8450 },
            { "No Liquid Slowdown", 8401 },
            { "No Liquid Slowdown (+)", 8451 },
            { "Lava Resistance (80%)", 8402 },
            { "Lava Resistance (100%)", 8452 },
            { "Quiet Footsteps", 8403 },
            { "Quiet Footsteps (+)", 8453 },
            { "High Impact Kick (Strike)", 8404 },
            { "High Impact Kick (Blow Backward)", 8454 },
            { "Legs Thorns (20)", 8410 },
            { "Legs Thorns (60)", 8460 },
            
            // Negative Legs Armor Effects

            { "Rolling Damage (TAE TRIGGER)", 8490 },
            { "Rolling Damage (EMEVD FLAG)", 8491 },
            { "Rolling Damage (5)", 8492 },
            { "Stamina Regen Down (-20)", 8493 },


            // Ring effects (mostly just flag triggers checked at run start)

            { "Alvina Ring", 8800 },  // nine lives
            { "Solaire Ring", 8801 },  // two bonfire creations per level
            { "Siegmeyer Ring", 8802 },  // start run with humanity, moss, titanite, and divine blessing
            { "Logan Ring", 8803 },  // abyssal portals more likely to appear
            { "Quelana Ring", 8804 },  // start run with a random pyromancy
            { "Havel Ring", 8805 },  // boosts equip load
            { "Mornstein Ring", 8806 },  // get a Lightning Ember after defeating the first boss
            { "LobosJr Ring", 8807 },  // LobosJr will always be summoned in boss battles on your last life


            // Flag triggers

            { "Boost Vitality Base", 8900 },
            { "Boost Attunement Base", 8910 },
            { "Boost Endurance Base", 8920 },
            { "Boost Strength Base", 8930 },
            { "Boost Dexterity Base", 8940 },
            { "Boost Resistance Base", 8950 },
            { "Boost Intelligence Base", 8960 },
            { "Boost Faith Base", 8970 },

            { "Go to NG+", 8897 },
            { "Reset Run", 8898 },
            { "Create Bonfire", 8899},

        };

        static void ValidateUniqueEffectIDs()
        {
            Dictionary<int, string> usedEffects = new Dictionary<int, string>();
            foreach (var nameID in Effects)
            {
                if (usedEffects.ContainsKey(nameID.Value))
                    throw new Exception($"ID {nameID.Value} ({nameID.Key}) already used by effect name {usedEffects[nameID.Value]}.");
            }

            Console.WriteLine("All SpEffect dictionaries validated successfully (all new IDs are unique).");
        }

        public SpEffectGenerator(SoulsMod mod)
        {
            Mod = mod;
        }

        public void Install()
        {
            //SpEffectIDs.ValidateUniqueEffectIDs();

            ModifySpEffects();
            CreateWeaponUpgradeEffects();
            CreateWeaponLegendaryEffects();
            CreateHeadArmorLegendaryEffects();
            CreateBodyArmorLegendaryEffects();
            CreateArmsArmorLegendaryEffects();
            CreateLegsArmorLegendaryEffects();
            CreateOtherEffects();
            CreateSpEffectVFX();
        }

        void CreateSpEffectVFX()
        {
            // TODO: Not sure if this will work.
            SpEffectVFX invisible = Mod.GPARAM.SpEffectVFXs.CopyRow(Mod.VanillaGPARAM.SpEffectVFXs[8], 243);
            invisible.HalfHiddenOnly = false;
        }

        void ModifySpEffects()
        {
            // Make a few miscellaneous modifications.

            // Delete useless conflicting SpEffects 8000 and 8001.
            Mod.GPARAM.SpEffects.DeleteRow(8000);
            Mod.GPARAM.SpEffects.DeleteRow(8001);

            // Change priority of "Orange Charred Ring-piercing" lava damage so a second lava resistance effect 
            // can now override BOTH lava damage effects.
            SpEffect lavaDamageWithResistance = Mod.GPARAM.SpEffects[4031];
            lavaDamageWithResistance.SpecialEffectCategory = 1002;
            lavaDamageWithResistance.SpecialEffectPriority = 2;  // higher than normal override (3) but lower than upgraded (1)

            // "Level" effects in 7000 range also multiply soul rewards (10% per level after 7001).
            for (int i = 1; i <= 15; i++)
                Mod.GPARAM.SpEffects[7000 + i].SoulRewardMultiplier = 1.0f + (0.1f * (i - 1));

            // Estus Flask effect (level 0) restores 70% of max health rather than a fixed amount.
            Mod.GPARAM.SpEffects[3020].HPPointsLost = 0;
            Mod.GPARAM.SpEffects[3020].HPReductionPercentage = -70;
        }

        void CreateWeaponUpgradeEffects()
        {
            SpEffect e;
            e = CreateEffect("Enchanted (MOD HIT FLAG)");
            // Triggers (partial) restoration of spell usages by mod program.

            // TODO: Mod program knows the max (initial) spell count of each spell,
            //    and restores some fixed percentage of max, distributed over all
            //    attuned spells, on each hit (hit type doesn't matter).
            //    For example, it might restore 5% of a single spell (which may be
            //    less than one usage - mod program tracks that partial progress),
            //    but 2.5% of each of two spells if you have two attuned.
            //    In practise, spell distribution shouldn't be so linear - otherwise
            //    you're restoring like 1% with five spells equipped. Maybe it can be
            //    something more like 5% of one spell, 0.75 * 5% of two spells, 
            //    (0.75 ^ 2) * 5% of three spells, etc...
            //    Obviously, spell usage can never go over the initial max.
            {
                e.EffectDuration = 0.5f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                // TODO: Use a different SpecialState with a different (magical) VFX if possible.
                e.SpecialState = 199;  // Ring of the Evil Eye
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Dire (EMEVD FLAG)");
            // Toggles a remaining-life-dependent damage buff in common EMEVD.
            {
                e.EffectDuration = -1.0f;
            }
            e = CreateEffect("Dire Damage (-20%)");
            {
                e.EffectDuration = -1.0f;
                e.AllAttackPowerMultipliers = 0.8f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Dire Damage (-10%)");
            {
                e.EffectDuration = -1.0f;
                e.AllAttackPowerMultipliers = 0.9f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Dire Damage (+0%)");
            {
                e.EffectDuration = -1.0f;
                e.AllAttackPowerMultipliers = 1.0f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Dire Damage (+20%)");
            {
                e.EffectDuration = -1.0f;
                e.AllAttackPowerMultipliers = 1.2f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Dire Damage (+40%)");
            {
                e.EffectDuration = -1.0f;
                e.AllAttackPowerMultipliers = 1.4f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }

            e = CreateEffect("Draconic Burn (Apply)");
            {
                e.EffectDuration = -1.0f;
                e.SpecialEffectOnAttack = Effects["Draconic Burn (60 / 5s)"];
                e.SpecialState = 152;  // Rotten Pine Resin (but no VFX)
            }

            e = CreateEffect("Draconic Burn (60 / 5s)");
            {
                e.EffectDuration = 5.0f;
                e.UpdateInterval = 0.25f;
                e.HPPointsLost = 3;
            }

            e = CreateEffect("Draconic Burn Self (20 / 5s)");
            {
                e.EffectDuration = 5.0f;
                e.UpdateInterval = 0.25f;
                e.HPPointsLost = 1;
                e.CanAffectEnemy = false;
                e.CanAffectAttacker = true;
            }
        }

        void CreateWeaponLegendaryEffects()
        {
            SpEffect e;

            for (int i = 0; i < 5; i++)
            {
                e = CreateEffect($"Poison Damage ({25 * (i + 1)})");
                {
                    e.EffectDuration = 180.0f;  // poison lasts for 180 seconds
                    e.UpdateInterval = 1.02f;
                    e.HPPointsLost = 3;
                    e.PoisonDamage = (i + 1) * 25;
                    e.SpecialEffectCategory = 10004;
                    e.SaveCategory = (sbyte)SAVE_CATEGORY.Poison;
                    e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                    e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;
                    e.SpecialState = 2;  // Poison Aura
                    e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                    e.UseVisualEffect = true;
                }
            }

            for (int i = 0; i < 5; i++)
            {
                e = CreateEffect($"Bleed Damage ({20 * (i + 1)})");
                {
                    e.EffectDuration = 2.0f;
                    e.UpdateInterval = 3.0f;
                    e.HPReductionPercentage = 30.0f;
                    e.BleedDamage = (i + 1) * 20;
                    e.SpecialEffectCategory = 10003;
                    e.SaveCategory = (sbyte)SAVE_CATEGORY.Bleed;
                    e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                    e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;  // not a typo
                    e.SpecialState = 6;  // Bleed Aura
                    e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                    e.UseVisualEffect = true;
                }
            }

            for (int i = 0; i < 5; i++)
            {
                e = CreateEffect($"Toxic Damage ({20 * (i + 1)})");
                {
                    e.EffectDuration = 600.0f;  // toxic lasts for 600 seconds
                    e.UpdateInterval = 1.02f;
                    e.HPPointsLost = 7;
                    e.StaminaRecoverySpeedChange = 15;
                    e.ToxicDamage = (i + 1) * 20;
                    e.SpecialEffectCategory = 10005;
                    e.SaveCategory = (sbyte)SAVE_CATEGORY.Toxic;
                    e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                    e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;
                    e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                    e.SpecialState = 5;  // Toxic Aura
                }
            }

            for (int i = 0; i < 5; i++)
            {
                e = CreateEffect($"Curse Damage ({20 * (i + 1)})");
                {
                    e.EffectDuration = 0.0f;
                    e.CurseDamage = (i + 1) * 20;
                    e.NextSpecialEffect = 33;  // stone petrification
                    e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                    e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.StoneCurse;
                    e.SpecialState = 116;  // Curse Damage
                    e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                    e.UseVisualEffect = true;
                }
            }

            e = CreateEffect("Magic Damage Up On Hit (30%, 8s)");
            {
                e.EffectDuration = 8.0f;
                e.PhysicalAttackPowerMultiplier = 1.3f;
                e.MagicAttackPowerMultiplier = 1.3f;
                e.FireAttackPowerMultiplier = 1.3f;
                e.LightningAttackPowerMultiplier = 1.3f;
                // TODO: Confirm this works without SpecialState 199.
                //   If not, apply buff using an immediate "next" SpEffect.
                e.SpecialState = 71;  // Magic Power Up
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.AffectsMagic = true;
                e.AffectsMiracles = true;
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Damage (10)");
            {
                e.EffectDuration = 0.5f;
                e.UpdateInterval = 1.0f;
                e.HPPointsLost = 10;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.SpecialState = 199;  // Ring of the Evil Eye
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Poison (20)");
            {
                e.EffectDuration = 180.0f;
                e.UpdateInterval = 1.0f;
                e.HPPointsLost = 3;
                e.PoisonDamage = 20;
                e.SpecialEffectCategory = 10004;
                e.SaveCategory = (sbyte)SAVE_CATEGORY.Poison;
                e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;
                // TODO: Confirm this works without SpecialState 199.
                //   If not, apply poison using a "next" SpEffect.
                e.SpecialState = 2;  // Poison Aura
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Bleed (20)");
            {
                e.EffectDuration = 2.0f;
                e.UpdateInterval = 3.0f;
                e.HPReductionPercentage = 30.0f;
                e.BleedDamage = 20;
                e.SpecialEffectCategory = 10003;
                e.SaveCategory = (sbyte)SAVE_CATEGORY.Bleed;
                e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;  // not a typo
                // TODO: See previous note.
                e.SpecialState = 6;  // Bleed Aura
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Toxic (20)");
            {
                e.EffectDuration = 600.0f;  // toxic lasts for 600 seconds
                e.UpdateInterval = 1.02f;
                e.HPPointsLost = 7;
                e.StaminaRecoverySpeedChange = 15;
                e.ToxicDamage = 20;
                e.SpecialEffectCategory = 10005;
                e.SaveCategory = (sbyte)SAVE_CATEGORY.Toxic;
                e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Poison;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                // TODO: See previous note.
                e.SpecialState = 5;  // Toxic Aura
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Curse (20)");
            {
                e.EffectDuration = 0.0f;
                e.CurseDamage = 20;
                e.NextSpecialEffect = 33;  // stone petrification
                e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.StoneCurse;
                // TODO: See previous note.
                e.SpecialState = 116;  // Curse Damage
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Lose Souls (100)");
            {
                e.EffectDuration = 0.5f;
                e.UpdateInterval = 1.0f;
                e.SoulAmountChange = -100;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.SpecialState = 199;  // Ring of the Evil Eye
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Self Slow (10%, 5s)");
            {
                e.EffectDuration = 5.0f;
                e.AnimationSpeedMultiplier = 0.9f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.SpecialState = 199;  // TODO: May not need, can use a different visual effect.
                e.CanAffectAttacker = true;
            }

            e = CreateEffect("Buff Enemy Damage (30%, 10s)");
            {
                e.EffectDuration = 10.0f;
                e.PhysicalAttackPowerMultiplier = 1.4f;
                e.MagicAttackPowerMultiplier = 1.4f;
                e.FireAttackPowerMultiplier = 1.4f;
                e.LightningAttackPowerMultiplier = 1.4f;
            }

            e = CreateEffect("Buff Enemy Speed (20%, 5s)");
            {
                e.EffectDuration = 5.0f;
                e.AnimationSpeedMultiplier = 1.2f;
            }

            e = CreateEffect("Buff Enemy Poise (300, 10s)");
            {
                e.EffectDuration = 10.0f;
                e.PoiseAddition = 300;
            }

            e = CreateEffect("Delayed Enemy Heal (Delay)");
            {
                e.EffectDuration = 5.0f;
                e.NextSpecialEffect = 8051;
            }

            e = CreateEffect("Delayed Enemy Heal (100)");
            {
                e.EffectDuration = 0.0f;
                e.HPPointsLost = -100;
            }

            e = CreateEffect("Self Slow (20%)");
            {
                e.EffectDuration = -1.0f;
                e.AnimationSpeedMultiplier = 0.8f;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
            }

            e = CreateEffect("Half Spell Casts");
            {
                e.EffectDuration = -1.0f;
                e.SpecialState = 203;  // Half Spell Casts
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
            }

            e = CreateEffect("On Guard (TAE TRIGGER)");
            {
                // Always activated during guard hit TAE. Toggles a shield-effect-dependent effect in common EMEVD.
                // TODO: Make sure duration 0 (with only one TAE frame) is enough for EMEVD to trigger.
                e.EffectDuration = 0.0f;
            }

            e = CreateEffect("On Guard Weakens Physical Attack (FLAG)");
            {
                e.EffectDuration = -1.0f;
            }

            e = CreateEffect("On Guard Weakens Physical Attack (80%, 5s)");
            {
                e.EffectDuration = 5.0f;
                e.PhysicalAttackPowerMultiplier = 0.2f;
            }

            e = CreateEffect("On Guard Curses (FLAG)");
            {
                e.EffectDuration = -1.0f;
            }

            e = CreateEffect("On Guard Curses (20)");
            {
                e.EffectDuration = 0.0f;
                e.CurseDamage = 20;
                e.NextSpecialEffect = 33;  // stone petrification
                e.AttackAttribute = (byte)ATTACK_ATTRIBUTE.Neutral;
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.StoneCurse;
                e.SpecialState = 116;  // Curse Damage
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
            }

            e = CreateEffect("On Guard Lose Souls (FLAG)");
            {
                e.EffectDuration = -1.0f;
            }

            e = CreateEffect("On Guard Lose Souls (200)");
            {
                e.EffectDuration = 0.0f;
                e.SoulAmountChange = -200;
            }
        }

        void CreateHeadArmorLegendaryEffects()
        {
            SpEffect e;

            e = CreateEffect("More Souls Gained (25%)");
            {
                e.StatusIcon = 5008;
                e.SoulsFromKillsMultiplier = 1.25f;
                e.SpecialState = 76;  // Silver Serpent ring (but visual effect disabled)
            }
            e = CreateEffect("More Souls Gained (50%)");
            {
                e.StatusIcon = 5008;
                e.SoulsFromKillsMultiplier = 1.5f;
                e.SpecialState = 76;  // Silver Serpent ring (but visual effect disabled)
            }

            e = CreateEffect("More Item Discovery");
            {
                e.StatusIcon = 5008;
                e.SpecialState = 66;  // Gold Serpent Ring
            }
            e = CreateEffect("More Item Discovery (+)");  // no change
            {
                e.StatusIcon = 5008;
                e.SpecialState = 66;  // Gold Serpent Ring
            }

            e = CreateEffect("Counter Damage Up (40%)");
            {
                e.StatusIcon = 5000;
                e.PhysicalAttackPowerMultiplier = 1.4f;
                e.SpecialState = 197;
            }
            e = CreateEffect("Counter Damage Up (80%)");
            {
                e.StatusIcon = 5000;
                e.PhysicalAttackPowerMultiplier = 1.8f;  // assuming amount isn't hard-coded
                e.SpecialState = 197;
            }

            e = CreateEffect("Critical Throws");
            {
                e.StatusIcon = 5000;
                e.ThrowCondition = 5;
                e.AffectsMagic = true;
                e.AffectsMiracles = true;
            }
            e = CreateEffect("Critical Throws (+)");  // no change
            {
                e.StatusIcon = 5000;
                e.ThrowCondition = 5;
                e.AffectsMagic = true;
                e.AffectsMiracles = true;
            }

            e = CreateEffect("Bow Range (65)");
            {
                e.StatusIcon = 5000;
                e.BowRangePercentageChange = 65;
                e.SpecialState = 168;  // Hawk Ring
            }
            e = CreateEffect("Bow Range (130)");
            {
                e.StatusIcon = 5000;
                e.BowRangePercentageChange = 130;  // assuming not hard-coded
                e.SpecialState = 168;  // Hawk Ring
            }

            e = CreateEffect("Magic Duration");
            {
                e.StatusIcon = 5004;
                e.SpecialState = 193;
            }
            e = CreateEffect("Magic Duration (+)");  // no change
            {
                e.StatusIcon = 5004;
                e.SpecialState = 193;
            }

            e = CreateEffect("Better Healing (50%)");
            {
                e.HPRecoveryRate = 1.5f;
            }
            e = CreateEffect("Better Healing (100%)");
            {
                e.HPRecoveryRate = 2.0f;
            }

            e = CreateEffect("Cast Light");
            {
                e.SpecialState = 147;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
            }
            e = CreateEffect("Cast Light (+)");  // no change
            {
                e.SpecialState = 147;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.Self;
                e.UseVisualEffect = true;
            }

            e = CreateEffect("Head Thorns (20)");
            {
                e.PhysicalAttackPowerAddition = 20;
                e.SpecialState = 123;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }
            e = CreateEffect("Head Thorns (60)");
            {
                e.PhysicalAttackPowerAddition = 60;
                e.SpecialState = 123;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }

            e = CreateEffect("Player Invisible (MOD FLAG)");
            {
                // Makes player completely invisible.
                e.EffectDuration = -1.0f;
                e.SpecialState = 8;  // TODO: use custom VFX 243 if we get it working
            }
        }
        void CreateBodyArmorLegendaryEffects()
        {
            SpEffect e;

            e = CreateEffect("Max Health Up (20%)");
            {
                e.MaxHPMultiplier = 1.2f;
                e.CurrentHPIgnoresMaxHPChange = true;
            }
            e = CreateEffect("Max Health Up (40%)");
            {
                e.MaxHPMultiplier = 1.4f;
                e.CurrentHPIgnoresMaxHPChange = true;
            }

            e = CreateEffect("Max Stamina Up (20%)");
            {
                e.MaxStaminaMultiplier = 1.2f;
            }
            e = CreateEffect("Max Stamina Up (40%)");
            {
                e.MaxStaminaMultiplier = 1.4f;
            }

            e = CreateEffect("Stamina Regen Up (20)");
            {
                e.StatusIcon = 5001;
                e.StaminaRecoverySpeedChange = 20;  // not using VFX from special state 75
            }
            e = CreateEffect("Stamina Regen Up (40)");
            {
                e.StatusIcon = 5001;
                e.StaminaRecoverySpeedChange = 40;  // not using VFX from special state 75
            }
            e = CreateEffect("Ghost (70%)");
            {
                e.StatusIcon = 5009;
                e.SpecialState = 8;  // transparency
                e.EnemySightPercentageReduction = 70;
                e.UseVisualEffect = true;
            }
            e = CreateEffect("Ghost (90%)");
            {
                e.StatusIcon = 5009;
                e.SpecialState = 8;  // transparency
                e.EnemySightPercentageReduction = 90;
                e.UseVisualEffect = true;
            }

            e = CreateEffect("Attunement Slots Up (2)");
            {
                e.AttunementSlotCountChange = 2;
            }
            e = CreateEffect("Attunement Slots Up (4)");
            {
                e.AttunementSlotCountChange = 4;
            }

            e = CreateEffect("Stability Up (20%)");
            {
                // TODO: Find a good icon.
                e.GuardStaminaMultiplier = 1.2f;  // affects all weapons
            }
            e = CreateEffect("Stability Up (40%)");
            {
                e.GuardStaminaMultiplier = 1.4f;  // affects all weapons
            }

            e = CreateEffect("Body Thorns (60)");
            {
                e.PhysicalAttackPowerAddition = 60;
                e.SpecialState = 124;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }
            e = CreateEffect("Body Thorns (180)");
            {
                e.PhysicalAttackPowerAddition = 180;
                e.SpecialState = 124;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }

            e = CreateEffect("Reduced Healing (-50%)");
            {
                // TODO: Find a good icon.
                e.HPRecoveryRate = 0.5f;
            }

            e = CreateEffect("Health Drain (5 / 1s)");
            {
                // Symbol of Avarice uses a second on-cycle effect for this, but probably
                // only because it needs to apply silver/gold serpent ring effects as well.
                e.UpdateInterval = 1.0f;
                e.HPPointsLost = 5;
            }
        }

        void CreateArmsArmorLegendaryEffects()
        {
            SpEffect e;

            e = CreateEffect("Physical Attack Up (75)");
            {
                e.PhysicalAttackPowerAddition = 75;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Physical Attack Up (150)");
            {
                e.PhysicalAttackPowerAddition = 150;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }

            e = CreateEffect("Magic Attack Up (75)");
            {
                e.MagicAttackPowerAddition = 75;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Magic Attack Up (150)");
            {
                e.MagicAttackPowerAddition = 150;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }

            e = CreateEffect("Fire Attack Up (75)");
            {
                e.FireAttackPowerAddition = 75;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Fire Attack Up (150)");
            {
                e.FireAttackPowerAddition = 150;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }

            e = CreateEffect("Lightning Attack Up (75)");
            {
                e.LightningAttackPowerAddition = 75;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }
            e = CreateEffect("Lightning Attack Up (150)");
            {
                e.LightningAttackPowerAddition = 150;
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.CurrentRightHand;
            }

            e = CreateEffect("Slower Durability Loss (10)");
            {
                e.StatusIcon = 5013;
                e.MaxDurabilityAddition = 10;
            }
            e = CreateEffect("Slower Durability Loss (20)");
            {
                e.StatusIcon = 5013;
                e.MaxDurabilityAddition = 20;
            }

            e = CreateEffect("Flip Dodge");
            {
                e.SpecialState = 115;
            }
            e = CreateEffect("Flip Dodge (+)");
            {
                e.SpecialState = 115;
            }

            e = CreateEffect("Arms Thorns (20)");
            {
                e.PhysicalAttackPowerAddition = 20;
                e.SpecialState = 125;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }
            e = CreateEffect("Arms Thorns (60)");
            {
                e.PhysicalAttackPowerAddition = 60;
                e.SpecialState = 125;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }

            e = CreateEffect("Poison Resistance Down (-75%)");
            {
                e.PoisonResistanceMultiplier = 0.25f;
                e.ToxicResistanceMultiplier = 0.5f;
            }

            e = CreateEffect("Bleed Resistance Down (-75%)");
            {
                e.BleedResistanceMultiplier = 0.25f;
            }

            e = CreateEffect("Less Souls Gained (-40%)");
            {
                e.SoulsFromKillsMultiplier = 0.6f;
            }
        }

        void CreateLegsArmorLegendaryEffects()
        {
            SpEffect e;

            e = CreateEffect("Max Equip Up (40%)");
            {
                e.MaxEquipLoadMultiplier = 1.4f;
            }
            e = CreateEffect("Max Equip Up (80%)");
            {
                e.MaxEquipLoadMultiplier = 1.8f;
            }

            e = CreateEffect("No Liquid Slowdown");
            {
                e.SpecialEffectCategory = 1000;
                e.SpecialEffectPriority = 3;  // overwrites effects from terrain
            }
            e = CreateEffect("No Liquid Slowdown (+)");  // no change
            {
                e.SpecialEffectCategory = 1000;
                e.SpecialEffectPriority = 3;
            }

            e = CreateEffect("Lava Resistance (80%)");
            {
                e.StatusIcon = 5015;
                e.FireAttackPowerAddition = 80;
                e.SpecialEffectCategory = 1002;
                e.SpecialEffectPriority = 3;  // below "reduced" lava damage priority
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
                e.SpecialState = 186;  // Orange Charred Ring
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.FootDamage;
            }
            e = CreateEffect("Lava Resistance (100%)");
            {
                e.StatusIcon = 5015;
                e.FireAttackPowerAddition = 80;
                e.SpecialEffectCategory = 1002;
                e.SpecialEffectPriority = 1;  // negates even "reduced" lava damage
                e.ElementAttribute = (byte)SPECIAL_ATTRIBUTE.Fire;
                e.SpecialState = 186;  // Orange Charred Ring
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.FootDamage;
            }

            e = CreateEffect("Quiet Footsteps");
            {
                e.StatusIcon = 5009;
                e.EnemyHearingPercentageReduction = 100;
                e.SpecialState = 54;  // Silent Movement
                e.UseVisualEffect = true;
            }
            e = CreateEffect("Quiet Footsteps (+)");  // no change
            {
                e.StatusIcon = 5009;
                e.EnemyHearingPercentageReduction = 100;
                e.SpecialState = 54;  // Silent Movement
                e.UseVisualEffect = true;
            }

            // TODO: Need to confirm this affects foot damage only. (It should, based on previous usage.)
            e = CreateEffect("High Impact Kick (Strike)");
            {
                e.ReplacePushImpactLevel = 6;  // Strike
                e.SpecialState = 120;  // Animation Poise Change
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.FootDamage;
            }
            e = CreateEffect("High Impact Kick (Blow Backward)");
            {
                e.ReplacePushImpactLevel = 10;  // Blow Backward
                e.SpecialState = 120;  // Animation Poise Change
                e.AffectedWeaponType = (byte)AFFECTED_WEAPON.FootDamage;
            }

            e = CreateEffect("Legs Thorns (20)");
            {
                e.PhysicalAttackPowerAddition = 20;
                e.SpecialState = 126;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }
            e = CreateEffect("Legs Thorns (60)");
            {
                e.PhysicalAttackPowerAddition = 60;
                e.SpecialState = 126;
                e.AffectedWeaponType = 3;
                e.CanAffectAlly = false;
                e.CanAffectEnemy = false;
                e.CanAffectAI = false;
            }

            e = CreateEffect("Rolling Damage (TAE TRIGGER)");
            {
                // Triggers health loss effect (below) in EMEVD when player rolls.
                e.EffectDuration = -1.0f;
            }
            e = CreateEffect("Rolling Damage (EMEVD FLAG)");
            {
                // Triggers health loss effect (below) in EMEVD when player rolls.
                e.EffectDuration = -1.0f;
            }
            e = CreateEffect("Rolling Damage (5)");
            {
                e.EffectDuration = 0.0f;
                e.HPPointsLost = 5;
            }

            e = CreateEffect("Stamina Regen Down (-20)");
            {
                // TODO: Icon?
                e.StaminaRecoverySpeedChange = -20;
            }
        }

        void CreateOtherEffects()
        {
            SpEffect e;
            CreateEffect("Alvina Ring");
            CreateEffect("Solaire Ring");
            CreateEffect("Siegmeyer Ring");
            CreateEffect("Logan Ring");
            e = CreateEffect("Quelana Ring");
            e.SpecialEffectCategory = 1002;
            e.SpecialEffectPriority = 3;  // below "reduced" lava damage priority
            e.SpecialState = 186;  // Orange Charred Ring
            e = CreateEffect("Havel Ring");
            e.MaxEquipLoadMultiplier = 1.5f;
            CreateEffect("Mornstein Ring");
            CreateEffect("LobosJr Ring");

            CreateFlagEffectRange("Boost Vitality", 8900, 8910, 0.5f);
            CreateFlagEffectRange("Boost Attunement", 8910, 8920, 0.5f);
            CreateFlagEffectRange("Boost Endurance", 8920, 8930, 0.5f);
            CreateFlagEffectRange("Boost Strength", 8930, 8940, 0.5f);
            CreateFlagEffectRange("Boost Dexterity", 8940, 8950, 0.5f);
            CreateFlagEffectRange("Boost Resistance", 8950, 8960, 0.5f);
            CreateFlagEffectRange("Boost Intelligence", 8960, 8970, 0.5f);
            CreateFlagEffectRange("Boost Faith", 8970, 8980, 0.5f);

            CreateEffect("Go to NG+", 0.5f);
            e = CreateEffect("Reset Run", 0.5f);
            e.SoulAmountChange = -999999;
            e.HumanityDamage = 99;
            CreateEffect("Create Bonfire", 0.5f);
        }

        SpEffect CreateEffect(string effectName, float duration = -1.0f)
        {
            int effectId = Effects[effectName];
            SpEffect effect = Mod.GPARAM.SpEffects.CopyRow(SpEffectTemplate, effectId);
            effect.Name = effectName;
            effect.EffectDuration = duration;
            return effect;
        }

        void CreateFlagEffectRange(string baseName, int rangeStart, int rangeEnd, float duration)
        {
            int i = 0;
            for (int effectIndex = rangeStart; effectIndex < rangeEnd; effectIndex++)
            {
                SpEffect effect = Mod.GPARAM.SpEffects.CopyRow(SpEffectTemplate, effectIndex);
                effect.Name = $"{baseName} {i}";
                effect.EffectDuration = duration;
                i++;
            }
        }
    }
}
