using RoguelikeSouls.Extensions;
using SoulsFormats;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.Design;
using System.Linq;
using System.Runtime.Remoting.Messaging;
using System.Text;
using System.Threading.Tasks;

namespace RoguelikeSouls.Installation
{
    enum SpellType
    {
        Sorcery = 3000,
        Pyromancy = 4000,
        Miracle = 5000,
    }

    class SpellGenerator
    {
        SoulsMod Mod { get; }
        Random Rand { get; }
        SpellNameGenerator NameGenerator { get; }
        SpellDescriptionGenerator DescriptionGenerator { get; }

        ShopLineup SpellShopEntryTemplate { get => Mod.VanillaGPARAM.ShopLineups[10000]; }  // Soul Arrow

        public static List<(SpellType type, int spellID)> SpellList { get; } = new List<(SpellType type, int spellID)>()
        {
            ( SpellType.Sorcery, 3000 ),  // Soul Arrow
            ( SpellType.Sorcery, 3010 ),  // Great Soul Arrow
            ( SpellType.Sorcery, 3020 ),  // Heavy Soul Arrow
            ( SpellType.Sorcery, 3030 ),  // Great Heavy Soul Arrow
            ( SpellType.Sorcery, 3040 ),  // Homing Soulmass
            ( SpellType.Sorcery, 3050 ),  // Homing Crystal Soulmass
            ( SpellType.Sorcery, 3060 ),  // Soul Spear
            ( SpellType.Sorcery, 3070 ),  // Crystal Soul Spear
            ( SpellType.Sorcery, 3100 ),  // Magic Weapon
            ( SpellType.Sorcery, 3110 ),  // Great Magic Weapon
            ( SpellType.Sorcery, 3120 ),  // Crystal Magic Weapon
            ( SpellType.Sorcery, 3300 ),  // Magic Shield
            ( SpellType.Sorcery, 3310 ),  // Strong Magic Shield
            ( SpellType.Sorcery, 3400 ),  // Hidden Weapon
            ( SpellType.Sorcery, 3410 ),  // Hidden Body
            ( SpellType.Sorcery, 3500 ),  // Cast Light
            ( SpellType.Sorcery, 3510 ),  // Hush
            ( SpellType.Sorcery, 3520 ),  // Aural Decoy
            ( SpellType.Sorcery, 3530 ),  // Repair
            ( SpellType.Sorcery, 3540 ),  // Fall Control
            ( SpellType.Sorcery, 3550 ),  // Chameleon
            ( SpellType.Sorcery, 3600 ),  // Resist Curse
            ( SpellType.Sorcery, 3610 ),  // Remedy
            ( SpellType.Sorcery, 3700 ),  // White Dragon Breath
            ( SpellType.Sorcery, 3710 ),  // Dark Orb
            ( SpellType.Sorcery, 3720 ),  // Dark Bead
            ( SpellType.Sorcery, 3730 ),  // Dark Fog
            ( SpellType.Sorcery, 3740 ),  // Pursuers
            ( SpellType.Pyromancy, 4000 ),  // Fireball
            ( SpellType.Pyromancy, 4010 ),  // Fire Orb
            ( SpellType.Pyromancy, 4020 ),  // Great Fireball
            ( SpellType.Pyromancy, 4030 ),  // Firestorm
            ( SpellType.Pyromancy, 4040 ),  // Fire Tempest
            ( SpellType.Pyromancy, 4050 ),  // Fire Surge
            ( SpellType.Pyromancy, 4060 ),  // Fire Whip
            ( SpellType.Pyromancy, 4100 ),  // Combustion
            ( SpellType.Pyromancy, 4110 ),  // Great Combustion
            ( SpellType.Pyromancy, 4200 ),  // Poison Mist
            ( SpellType.Pyromancy, 4210 ),  // Toxic Mist
            ( SpellType.Pyromancy, 4220 ),  // Acid Surge
            ( SpellType.Pyromancy, 4300 ),  // Iron Flesh
            ( SpellType.Pyromancy, 4310 ),  // Flash Sweat
            ( SpellType.Pyromancy, 4360 ),  // Undead Rapport
            ( SpellType.Pyromancy, 4400 ),  // Power Within
            ( SpellType.Pyromancy, 4500 ),  // Great Chaos Fireball
            ( SpellType.Pyromancy, 4510 ),  // Chaos Storm
            ( SpellType.Pyromancy, 4520 ),  // Chaos Fire Whip
            ( SpellType.Pyromancy, 4530 ),  // Black Flame
            ( SpellType.Miracle, 5000 ),  // Heal
            ( SpellType.Miracle, 5010 ),  // Great Heal
            ( SpellType.Miracle, 5020 ),  // Great Heal Excerpt
            ( SpellType.Miracle, 5030 ),  // Soothing Sunlight
            ( SpellType.Miracle, 5040 ),  // Replenishment
            ( SpellType.Miracle, 5050 ),  // Bountiful Sunlight
            ( SpellType.Miracle, 5100 ),  // Gravelord Sword Dance
            ( SpellType.Miracle, 5110 ),  // Gravelord Greatsword Dance
            ( SpellType.Miracle, 5200 ),  // Escape Death
            ( SpellType.Miracle, 5210 ),  // Homeward
            ( SpellType.Miracle, 5300 ),  // Force
            ( SpellType.Miracle, 5310 ),  // Wrath of the Gods
            ( SpellType.Miracle, 5320 ),  // Emit Force
            ( SpellType.Miracle, 5400 ),  // Seek Guidance
            ( SpellType.Miracle, 5500 ),  // Lightning Spear
            ( SpellType.Miracle, 5510 ),  // Great Lightning Spear
            ( SpellType.Miracle, 5520 ),  // Sunlight Spear
            ( SpellType.Miracle, 5600 ),  // Magic Barrier
            ( SpellType.Miracle, 5610 ),  // Great Magic Barrier
            ( SpellType.Miracle, 5700 ),  // Karmic Justice
            // ( SpellType.Miracle, 5710 ),  // None
            ( SpellType.Miracle, 5800 ),  // Tranquil Walk of Peace
            ( SpellType.Miracle, 5810 ),  // Vow of Silence
            ( SpellType.Miracle, 5900 ),  // Sunlight Blade
            ( SpellType.Miracle, 5910 ),  // Darkmoon Blade
        };

        // List of bullet fields that get BETTER when increased (most of them).
        public static List<string> PositiveBulletFields = new List<string>()
        {
            "life", "dist", "initVellocity", "accelInRange", "accelOutRange", "maxVellocity", "minVellocity", "accelTime",
            "hitRadius", "hitRadiusMax", "homingAngle", "SPECIAL",
        };

        // List of bullet fields that get WORSE when increased.
        public static List<string> NegativeBulletFields = new List<string>()
        {
            "shootInterval", "gravityInRange", "gravityOutRange", "hormingStopRange", "homingBeginDist", "spreadTime", "SPECIAL",
        };

        public static (bool isPositive, string field) GetRandomFieldToModify(Random random)
        {
            if (random.NextDouble() < 0.5)
                return (true, PositiveBulletFields.GetRandomElement(random));
            else
                return (false, NegativeBulletFields.GetRandomElement(random));
        }

        public static int GetRandomSpellTemplate(SpellType type, Random random)
        {
            List<int> options = new List<int>(SpellList.Where(spell => spell.type == type).Select(spell => spell.spellID));
            return options.GetRandomElement(random);
        }

        public SpellGenerator(SoulsMod mod, Random random)
        {
            Mod = mod;
            Rand = random;
            NameGenerator = new SpellNameGenerator(Rand);
            DescriptionGenerator = new SpellDescriptionGenerator(Rand);
        }

        public void Install()
        {
            Mod.GPARAM.ShopLineups.DeleteRowRange(10000, 10099);  // Delete default attunement menu entries.
            CreateAllSpells();
        }

        void CreateAllSpells()
        {
            int shopIndex = 0;

            // I was trying to generate 100 random spells of each type, but the game refuses
            // to show attunement shop options for non-vanilla spell IDs, so now I'm just copying those.
            foreach ((SpellType type, int spellID) in SpellList)
            {
                string typeName;
                switch (type)
                {
                    case SpellType.Sorcery:
                        typeName = "Sorcery";
                        break;
                    case SpellType.Pyromancy:
                        typeName = "Pyromancy";
                        break;
                    case SpellType.Miracle:
                        typeName = "Miracle";
                        break;
                    default:
                        typeName = "Unknown";
                        break;
                }
                
                int templateID = spellID;  // Currently always using the same spell ID as a template, not a random one.
                Mod.GPARAM.Goods.DeleteRow(spellID);
                Mod.GPARAM.Magic.DeleteRow(spellID);
                Good spellGood = Mod.GPARAM.Goods.CopyRow(Mod.VanillaGPARAM.Goods[templateID], spellID);
                spellGood.Spell = spellID;
                Magic spell = CreateSpellParams(templateID, spellID);
                string spellName = NameGenerator.GetRandomName(typeName);
                string spellDescription = DescriptionGenerator.GetRandomDescription();
                spellGood.Name = spellName;
                spellGood.Summary = $"Cast {typeName.ToLower()} magic";
                spellGood.Description = spellDescription;
                spell.Name = spellName;
                spell.Summary = $"Cast {typeName.ToLower()} magic";
                spell.Description = spellDescription;

                ShopLineup spellShopEntry = Mod.GPARAM.ShopLineups.CopyRow(SpellShopEntryTemplate, 10000 + shopIndex);
                shopIndex++;
                spellShopEntry.EquipId = spellID;
                spellShopEntry.MtrlId = spellID;
                spellShopEntry.Name = spellName;
            }
        }

        Magic CreateSpellParams(int templateID, int newParamID)
        {
            // Choose number of positive/negative pairs to apply (from say, 2 to 4).
            // The same value can be modified multiple times.
            // Special positive effects: 
            //   become a "soulmass" spell (first param copies Homing Soulmass with new FX and new OnHit bullet and new count.
            //   become a homing spell, if not already
            //   piece targets and/or map
            // If bullet count is > 1, modify interval randomly (if appropriate), then set starting angle appropriately.
            // OR, chance of separating in elevation instead.
            // Keep visual, element, attack attributes of template attack. Keep VFX as well for now.
            // Keep attack params as well, just no time to change them.
            Magic template = Mod.VanillaGPARAM.Magic[templateID];
            Magic newSpell = Mod.GPARAM.Magic.CopyRow(template, newParamID);
            newSpell.BaseCastCount = (short)(newSpell.BaseCastCount * (0.75 + 0.5 * Rand.NextDouble()));  // random 0.75 to 1.25 multiplier for casts

            if (newSpell.ReferenceType == 1)
            {
                int bulletID = template.Refid;
                int bulletOffset = 0;
                newSpell.Refid = (short)(newParamID + bulletOffset);
                while (bulletID != -1)
                {
                    Bullet templateBullet = Mod.VanillaGPARAM.Bullets[bulletID];
                    Mod.GPARAM.Bullets.DeleteRow(newParamID + bulletOffset);
                    Bullet newBullet = Mod.GPARAM.Bullets.CopyRow(templateBullet, newParamID + bulletOffset);
                    bool useSoulmass = ModifyBullet(newBullet, soulmassAllowed: bulletOffset == 0 && newBullet.BulletOnHit == -1);
                    if (useSoulmass)
                    {
                        // Use Soulmass as base bullet, and offset this bullet by one.
                        Mod.GPARAM.Bullets.DeleteRow(newParamID + bulletOffset + 1);
                        Mod.GPARAM.Bullets.CopyRow(newBullet, newParamID + bulletOffset + 1);
                        Mod.GPARAM.Bullets.DeleteRow(newParamID + bulletOffset);
                        newBullet = Mod.GPARAM.Bullets.CopyRow(Mod.VanillaGPARAM.Bullets[3040], newParamID + bulletOffset);
                        newBullet.BulletOnHit = newParamID + bulletOffset + 1;
                        break;
                    }
                    else
                    {
                        bulletID = newBullet.BulletOnHit;
                        bulletOffset++;
                    }
                }
            }
            else if (newSpell.ReferenceType == 2)
            {
                // Not modifying these (low priority).
                SpEffect templateEffect = Mod.VanillaGPARAM.SpEffects[template.Refid];
                Mod.GPARAM.SpEffects.DeleteRow(10000 + newParamID);  // shouldn't exist anyway
                SpEffect newEffect = Mod.GPARAM.SpEffects.CopyRow(templateEffect, 10000 + newParamID);
                newSpell.Refid = (short)(10000 + newParamID);
                ModifySpEffect(newEffect);
            }
            return newSpell;
        }

        bool ModifyBullet(Bullet newBullet, bool soulmassAllowed = false)
        {
            bool useSoulmass = false;
            int changeCount = Rand.Next(2, 5);
            for (int i = 0; i < changeCount; i++)
            {
                (bool isPositive, string field) = GetRandomFieldToModify(Rand);
                if (field == "SPECIAL")
                {
                    double roll = Rand.NextDouble();
                    if (roll < 0.2 && soulmassAllowed)
                    {
                        useSoulmass = true;
                    }
                    else if (roll < 0.5)
                    {
                        newBullet.BulletCount++;
                    }
                    else if (roll < 0.8 && newBullet.FollowType == 0)
                    {
                        newBullet.FollowType = 1;
                        // Homing defaults:
                        newBullet.HomingAnglePerSecond = 30;
                        newBullet.HomingStartDistance = 1.0f;
                        newBullet.ClosestHomingDistance = 1.0f;
                    }
                    else
                    {
                        newBullet.PiercesTargets = 1;
                        newBullet.IsMapPiercing = true;
                    }
                }
                else
                {
                    float multiplierStart = isPositive ? 1.5f : 0.25f;
                    if (field.Contains("Damp"))
                        newBullet.Row[field].Value = (sbyte)newBullet.Row[field].Value * (sbyte)(multiplierStart + 0.5f * (float)Rand.NextDouble());
                    else if (field == "homingAngle")
                        newBullet.Row[field].Value = (short)((short)newBullet.Row[field].Value * (multiplierStart + 0.5f * (float)Rand.NextDouble()));
                    else
                        newBullet.Row[field].Value = (float)newBullet.Row[field].Value * (multiplierStart + 0.5f * (float)Rand.NextDouble());
                }

                (isPositive, field) = GetRandomFieldToModify(Rand);
                if (field == "SPECIAL")
                {
                    double roll = Rand.NextDouble();
                    if (roll < 0.5)
                    {
                        newBullet.BulletCount = (ushort)Math.Max(1, newBullet.BulletCount - 1); ;
                    }
                    else if (roll < 0.8 && newBullet.FollowType == 1)
                    {
                        newBullet.FollowType = 0;
                        // Homing resets:
                        newBullet.HomingAnglePerSecond = 0;
                        newBullet.HomingStartDistance = 0.0f;
                        newBullet.ClosestHomingDistance = 0.0f;
                    }
                    else
                    {
                        newBullet.PiercesTargets = 0;
                        newBullet.IsMapPiercing = false;
                    }
                }
                else
                {
                    float multiplierStart = isPositive ? 0.25f : 1.5f;
                    if (field.Contains("Damp"))
                        newBullet.Row[field].Value = (sbyte)newBullet.Row[field].Value * (sbyte)(multiplierStart + 0.5f * (float)Rand.NextDouble());
                    else if (field == "homingAngle")
                        newBullet.Row[field].Value = (short)((short)newBullet.Row[field].Value * (multiplierStart + 0.5f * (float)Rand.NextDouble()));
                    else
                        newBullet.Row[field].Value = (float)newBullet.Row[field].Value * (multiplierStart + 0.5f * (float)Rand.NextDouble());
                }
            }

            double intervalRoll = Rand.NextDouble();
            double azimuthRoll = Rand.NextDouble();
            if (newBullet.BulletCount > 1)
            {
                if (newBullet.LaunchInterval == 0.0f && intervalRoll < 0.2)
                    newBullet.LaunchInterval = (float)Rand.NextDouble();
                if (azimuthRoll < 0.2)
                {
                    newBullet.ElevationAngleInterval = (short)Rand.Next(20, 40);
                    newBullet.FirstBulletElevationAngle = 0;
                    newBullet.GravityAfterAttenuation = 1.0f;
                }
                else
                {
                    newBullet.AzimuthAngleInterval = (short)Rand.Next(10, 30);
                    newBullet.AzimuthAngleStart = (short)(0.5 * newBullet.AzimuthAngleInterval * (newBullet.BulletCount - 1));
                }
            }
            return useSoulmass;
        }

        void ModifySpEffect(SpEffect newEffect)
        {
            // Not gonna have time to screw around here. Just gonna randomly multiply a bunch of fields, which may do nothing.
            // Using 10000 + spell ID as per-spell SpEffect offset.

            newEffect.EffectDuration *= (float)Rand.NextDouble() + 0.5f;
            newEffect.PhysicalAttackPowerAddition = (int)(newEffect.PhysicalAttackPowerAddition * (Rand.NextDouble() + 0.5));
            newEffect.MagicAttackPowerAddition = (int)(newEffect.MagicAttackPowerAddition * (Rand.NextDouble() + 0.5));
            newEffect.FireAttackPowerAddition = (int)(newEffect.FireAttackPowerAddition * (Rand.NextDouble() + 0.5));
            newEffect.LightningAttackPowerAddition = (int)(newEffect.LightningAttackPowerAddition * (Rand.NextDouble() + 0.5));

            if (newEffect.GuardStaminaMultiplier > 1.0f)
                newEffect.GuardStaminaMultiplier = 1.0f + (float)((newEffect.GuardStaminaMultiplier - 1.0f) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingSlashDamageMultiplier < 1.0f)
                newEffect.IncomingSlashDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingSlashDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingStrikeDamageMultiplier < 1.0f)
                newEffect.IncomingStrikeDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingStrikeDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingThrustDamageMultiplier < 1.0f)
                newEffect.IncomingThrustDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingThrustDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingNeutralDamageMultiplier < 1.0f)
                newEffect.IncomingNeutralDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingNeutralDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingMagicDamageMultiplier < 1.0f)
                newEffect.IncomingMagicDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingMagicDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingFireDamageMultiplier < 1.0f)
                newEffect.IncomingFireDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingFireDamageMultiplier) * (Rand.NextDouble() - 0.5));
            if (newEffect.IncomingLightningDamageMultiplier < 1.0f)
                newEffect.IncomingLightningDamageMultiplier = 1.0f - (float)((1.0f - newEffect.IncomingLightningDamageMultiplier) * (Rand.NextDouble() - 0.5));
        }
    }
}
