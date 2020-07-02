using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Attack : RowWrapper
    {
        public Attack() { }
        public Attack(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Radius of sphere/capsule hitbox (slot 0).
        /// </summary>
        public float Hitbox0Radius
        {
            get => Convert.ToSingle(Row["hit0_Radius"].Value);
            set => Row["hit0_Radius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Radius of sphere/capsule hitbox (slot 1).
        /// </summary>
        public float Hitbox1Radius
        {
            get => Convert.ToSingle(Row["hit1_Radius"].Value);
            set => Row["hit1_Radius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Radius of sphere/capsule hitbox (slot 2).
        /// </summary>
        public float Hitbox2Radius
        {
            get => Convert.ToSingle(Row["hit2_Radius"].Value);
            set => Row["hit2_Radius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Radius of sphere/capsule hitbox (slot 3).
        /// </summary>
        public float Hitbox3Radius
        {
            get => Convert.ToSingle(Row["hit3_Radius"].Value);
            set => Row["hit3_Radius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Knockback distance of attack.
        /// </summary>
        public float KnockbackDistance
        {
            get => Convert.ToSingle(Row["knockbackDist"].Value);
            set => Row["knockbackDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unclear. This isn't hitbox duration, which is determined by the
        /// duration of the triggering TAE event. It may be the duration of the
        /// 'hit' flag on the target. Always set to 0, 0.08. or 0.11.
        /// </summary>
        public float HitStopTime
        {
            get => Convert.ToSingle(Row["hitStopTime"].Value);
            set => Row["hitStopTime"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target on hit (slot 0).
        /// </summary>
        public int SpecialEffectOnHit0
        {
            get => Convert.ToInt32(Row["spEffectId0"].Value);
            set => Row["spEffectId0"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target on hit (slot 1).
        /// </summary>
        public int SpecialEffectOnHit1
        {
            get => Convert.ToInt32(Row["spEffectId1"].Value);
            set => Row["spEffectId1"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target on hit (slot 2).
        /// </summary>
        public int SpecialEffectOnHit2
        {
            get => Convert.ToInt32(Row["spEffectId2"].Value);
            set => Row["spEffectId2"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target on hit (slot 3).
        /// </summary>
        public int SpecialEffectOnHit3
        {
            get => Convert.ToInt32(Row["spEffectId3"].Value);
            set => Row["spEffectId3"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target on hit (slot 4).
        /// </summary>
        public int SpecialEffectOnHit4
        {
            get => Convert.ToInt32(Row["spEffectId4"].Value);
            set => Row["spEffectId4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at origin of hitbox (slot 0). If Hitbox0EndModelPoint is
        /// not -1, the hitbox will be a capsule with hemispherical caps
        /// positioned at these origins (with a joining cylinder).
        /// </summary>
        public short Hitbox0StartModelPoint
        {
            get => Convert.ToInt16(Row["hit0_DmyPoly1"].Value);
            set => Row["hit0_DmyPoly1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at origin of hitbox (slot 1). If Hitbox1EndModelPoint is
        /// not -1, the hitbox will be a capsule with hemispherical caps
        /// positioned at these origins (with a joining cylinder).
        /// </summary>
        public short Hitbox1StartModelPoint
        {
            get => Convert.ToInt16(Row["hit1_DmyPoly1"].Value);
            set => Row["hit1_DmyPoly1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at origin of hitbox (slot 2). If Hitbox2EndModelPoint is
        /// not -1, the hitbox will be a capsule with hemispherical caps
        /// positioned at these origins (with a joining cylinder).
        /// </summary>
        public short Hitbox2StartModelPoint
        {
            get => Convert.ToInt16(Row["hit2_DmyPoly1"].Value);
            set => Row["hit2_DmyPoly1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at origin of hitbox (slot 3). If Hitbox3EndModelPoint is
        /// not -1, the hitbox will be a capsule with hemispherical caps
        /// positioned at these origins (with a joining cylinder).
        /// </summary>
        public short Hitbox3StartModelPoint
        {
            get => Convert.ToInt16(Row["hit3_DmyPoly1"].Value);
            set => Row["hit3_DmyPoly1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at end of capsule hitbox (slot 0). If this is -1, the
        /// hitbox will be a sphere placed at Hitbox0StartModelPoint.
        /// </summary>
        public short Hitbox0EndModelPoint
        {
            get => Convert.ToInt16(Row["hit0_DmyPoly2"].Value);
            set => Row["hit0_DmyPoly2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at end of capsule hitbox (slot 1). If this is -1, the
        /// hitbox will be a sphere placed at Hitbox1StartModelPoint.
        /// </summary>
        public short Hitbox1EndModelPoint
        {
            get => Convert.ToInt16(Row["hit1_DmyPoly2"].Value);
            set => Row["hit1_DmyPoly2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at end of capsule hitbox (slot 2). If this is -1, the
        /// hitbox will be a sphere placed at Hitbox2StartModelPoint.
        /// </summary>
        public short Hitbox2EndModelPoint
        {
            get => Convert.ToInt16(Row["hit2_DmyPoly2"].Value);
            set => Row["hit2_DmyPoly2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point at end of capsule hitbox (slot 3). If this is -1, the
        /// hitbox will be a sphere placed at Hitbox3StartModelPoint.
        /// </summary>
        public short Hitbox3EndModelPoint
        {
            get => Convert.ToInt16(Row["hit3_DmyPoly2"].Value);
            set => Row["hit3_DmyPoly2"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Never used.
        /// </summary>
        public ushort BlowOffCorrection
        {
            get => Convert.ToUInt16(Row["blowingCorrection"].Value);
            set => Row["blowingCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character attack
        /// power to calculate physical attack damage.
        /// </summary>
        public ushort PhysicalAttackPowerPercentage
        {
            get => Convert.ToUInt16(Row["atkPhysCorrection"].Value);
            set => Row["atkPhysCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character attack
        /// power to calculate magic attack damage.
        /// </summary>
        public ushort MagicAttackPowerPercentage
        {
            get => Convert.ToUInt16(Row["atkMagCorrection"].Value);
            set => Row["atkMagCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character attack
        /// power to calculate fire attack damage.
        /// </summary>
        public ushort FireAttackPowerPercentage
        {
            get => Convert.ToUInt16(Row["atkFireCorrection"].Value);
            set => Row["atkFireCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character attack
        /// power to calculate lightning attack damage.
        /// </summary>
        public ushort LightningAttackPowerPercentage
        {
            get => Convert.ToUInt16(Row["atkThunCorrection"].Value);
            set => Row["atkThunCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character attack
        /// power to calculate stamina damage.
        /// </summary>
        public ushort StaminaAttackPowerPercentage
        {
            get => Convert.ToUInt16(Row["atkStamCorrection"].Value);
            set => Row["atkStamCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character guard
        /// attack power. Throw attacks have a value of 9900, which must
        /// essentially ignore blocking completely.
        /// </summary>
        public ushort GuardAttackPercentage
        {
            get => Convert.ToUInt16(Row["guardAtkRateCorrection"].Value);
            set => Row["guardAtkRateCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to character guard
        /// breaking power. Not sure what that is, exactly, but this is set to 0
        /// for parries and 100 for all other attacks.
        /// </summary>
        public ushort GuardBreakPercentage
        {
            get => Convert.ToUInt16(Row["guardBreakCorrection"].Value);
            set => Row["guardBreakCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to weapon attacks
        /// during throws. Generally set to 100, except for throw attacks
        /// themselves.
        /// </summary>
        public ushort AttackDuringThrowPercentage
        {
            get => Convert.ToUInt16(Row["atkThrowEscapeCorrection"].Value);
            set => Row["atkThrowEscapeCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier (as percentage from 0 upwards) applied to damage to target
        /// poise. Generally set to 100, except for throw attacks themselves.
        /// </summary>
        public ushort PoiseAttackPercentage
        {
            get => Convert.ToUInt16(Row["atkSuperArmorCorrection"].Value);
            set => Row["atkSuperArmorCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute physical attack power of attack.
        /// </summary>
        public ushort PhysicalAttackPower
        {
            get => Convert.ToUInt16(Row["atkPhys"].Value);
            set => Row["atkPhys"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute magic attack power of attack.
        /// </summary>
        public ushort MagicAttackPower
        {
            get => Convert.ToUInt16(Row["atkMag"].Value);
            set => Row["atkMag"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute fire attack power of attack.
        /// </summary>
        public ushort FireAttackPower
        {
            get => Convert.ToUInt16(Row["atkFire"].Value);
            set => Row["atkFire"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute lightning attack power of attack.
        /// </summary>
        public ushort LightningAttackPower
        {
            get => Convert.ToUInt16(Row["atkThun"].Value);
            set => Row["atkThun"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute stamina attack power of attack.
        /// </summary>
        public ushort StaminaAttackPower
        {
            get => Convert.ToUInt16(Row["atkStam"].Value);
            set => Row["atkStam"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute guard attack power of attack.
        /// </summary>
        public ushort GuardAttackPower
        {
            get => Convert.ToUInt16(Row["guardAtkRate"].Value);
            set => Row["guardAtkRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute guard breaking power of attack.
        /// </summary>
        public ushort GuardBreakPower
        {
            get => Convert.ToUInt16(Row["guardBreakRate"].Value);
            set => Row["guardBreakRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute poise attack power of attack.
        /// </summary>
        public ushort PoiseAttackPower
        {
            get => Convert.ToUInt16(Row["atkSuperArmor"].Value);
            set => Row["atkSuperArmor"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Absolute attack power of attack. Never used.
        /// </summary>
        public ushort AttackPowerDuringThrows
        {
            get => Convert.ToUInt16(Row["atkThrowEscape"].Value);
            set => Row["atkThrowEscape"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of damage dealt to objects by this attack.
        /// </summary>
        public ushort ObjectDamage
        {
            get => Convert.ToUInt16(Row["atkObj"].Value);
            set => Row["atkObj"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Correction applied to the stamina required to block this attack (I
        /// presume). Never used.
        /// </summary>
        public short GuardStaminaPercentage
        {
            get => Convert.ToInt16(Row["guardStaminaCutRate"].Value);
            set => Row["guardStaminaCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage correction made to the guarding ability of the attack, as
        /// set in weapon parameters or NPC parameters. Only used to halve the
        /// guarding ability of parries (-50).
        /// </summary>
        public short GuardPercentage
        {
            get => Convert.ToInt16(Row["guardRate"].Value);
            set => Row["guardRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Throw to trigger when attack hits. For some reason, throws are
        /// triggered using this ID, which is a field within each Throw table
        /// entry rather than the ID of the Throw table entry itself.
        /// </summary>
        public ushort ThrowID
        {
            get => Convert.ToUInt16(Row["throwTypeId"].Value);
            set => Row["throwTypeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Type of hit applied by hitbox (slot 0). Always zero, except for some
        /// whip attacks.
        /// </summary>
        public byte Hitbox0HitType
        {
            get => Convert.ToByte(Row["hit0_hitType"].Value);
            set => Row["hit0_hitType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Type of hit applied by hitbox (slot 1). Always zero, except for some
        /// whip attacks.
        /// </summary>
        public byte Hitbox1HitType
        {
            get => Convert.ToByte(Row["hit1_hitType"].Value);
            set => Row["hit1_hitType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Type of hit applied by hitbox (slot 2). Always zero, except for some
        /// whip attacks.
        /// </summary>
        public byte Hitbox2HitType
        {
            get => Convert.ToByte(Row["hit2_hitType"].Value);
            set => Row["hit2_hitType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Type of hit applied by hitbox (slot 3). Always zero, except for some
        /// whip attacks.
        /// </summary>
        public byte Hitbox3HitType
        {
            get => Convert.ToByte(Row["hit3_hitType"].Value);
            set => Row["hit3_hitType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Priority of hitbox (slot 0). If two hits occur simultaneously, only
        /// the highest priority hit occurs. Never used.
        /// </summary>
        public byte Hitbox0Priority
        {
            get => Convert.ToByte(Row["hti0_Priority"].Value);
            set => Row["hti0_Priority"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Priority of hitbox (slot 1). If two hits occur simultaneously, only
        /// the highest priority hit occurs. Never used.
        /// </summary>
        public byte Hitbox1Priority
        {
            get => Convert.ToByte(Row["hti1_Priority"].Value);
            set => Row["hti1_Priority"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Priority of hitbox (slot 2). If two hits occur simultaneously, only
        /// the highest priority hit occurs. Never used.
        /// </summary>
        public byte Hitbox2Priority
        {
            get => Convert.ToByte(Row["hti2_Priority"].Value);
            set => Row["hti2_Priority"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Priority of hitbox (slot 3). If two hits occur simultaneously, only
        /// the highest priority hit occurs. Never used.
        /// </summary>
        public byte Hitbox3Priority
        {
            get => Convert.ToByte(Row["hti3_Priority"].Value);
            set => Row["hti3_Priority"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level of attack, which determines how the target reacts to it
        /// (e.g. knocked backward, launched into the air, etc.). Certain special
        /// effects on the target (e.g. Iron Flesh) may re-map this impact level
        /// to a different one.
        /// </summary>
        public byte ImpactLevel
        {
            get => Convert.ToByte(Row["dmgLevel"].Value);
            set => Row["dmgLevel"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines how this attack interacts with the map.
        /// </summary>
        public byte MapHitType
        {
            get => Convert.ToByte(Row["mapHitType"].Value);
            set => Row["mapHitType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Percentage (from -100 to 100) of target's current guard rate to
        /// ignore. A value of 100 will ignore guarding completely, and a value of
        /// -100 will double their guarding effectiveness. Never used, in favor of
        /// the simple 'IgnoreGuard' boolean field.
        /// </summary>
        public sbyte IgnoreGuardPercentage
        {
            get => Convert.ToSByte(Row["guardCutCancelRate"].Value);
            set => Row["guardCutCancelRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of physical damage done by attack.
        /// </summary>
        public byte AttackAttribute
        {
            get => Convert.ToByte(Row["atkAttribute"].Value);
            set => Row["atkAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of elemental damage done by attack. (Attacks can apply any
        /// combination of damage types, but this value will determine what visual
        /// effects the attack generates, etc.)
        /// </summary>
        public byte ElementAttribute
        {
            get => Convert.ToByte(Row["spAttribute"].Value);
            set => Row["spAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the sounds and visual effects generated by the attack
        /// itself (before hit).
        /// </summary>
        public byte VisualSoundEffectsOnAttack
        {
            get => Convert.ToByte(Row["atkType"].Value);
            set => Row["atkType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the sounds and visual effects generated when the attack
        /// hits. A value of 255 uses the weapon default.
        /// </summary>
        public byte VisualSoundEffectsOnHit
        {
            get => Convert.ToByte(Row["atkMaterial"].Value);
            set => Row["atkMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description says this determines the size of sounds and
        /// visual effects, but it is never used.
        /// </summary>
        public byte AttackSize
        {
            get => Convert.ToByte(Row["atkSize"].Value);
            set => Row["atkSize"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines the sound effects used when guarding. Usually 255 for
        /// Player Attacks and 0 (if not a block) or 50 (if blocking) for Non-
        /// Player Attacks.
        /// </summary>
        public byte SoundEffectsWhileBlocking
        {
            get => Convert.ToByte(Row["defMaterial"].Value);
            set => Row["defMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines the visual effects used when guarding. Usually 255 for
        /// Player Attacks and 0 (if not a block) or 50 (if blocking) for Non-
        /// Player Attacks.
        /// </summary>
        public byte VisualEffectsWhileBlocking
        {
            get => Convert.ToByte(Row["defSfxMaterial"].Value);
            set => Row["defSfxMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description says 'specify where you get the model point for
        /// attack'. Set to 1 for parries, ripostes, and basic body attacks
        /// (falling, rolling, etc.), and zero otherwise. Use that pattern.
        /// </summary>
        public byte ModelPointSource
        {
            get => Convert.ToByte(Row["hitSourceType"].Value);
            set => Row["hitSourceType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines how this attack relates to throws: not at all, a throw
        /// trigger, or a throw damage parameter.
        /// </summary>
        public byte ThrowFlag
        {
            get => Convert.ToByte(Row["throwFlag"].Value);
            set => Row["throwFlag"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this attack cannot be blocked (e.g. throws).
        /// </summary>
        public bool IgnoreGuard
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableGuard"].Value));
            set => Row["disableGuard"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this attack will deal no stamina damage, regardless of its
        /// stamina attack power.
        /// </summary>
        public bool NoStaminaDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableStaminaAttack"].Value));
            set => Row["disableStaminaAttack"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this attack will trigger no special effects on the target.
        /// Internal description mentions this is an 'SCE bug countermeasure'
        /// (referring to the original Dark Souls demo).
        /// </summary>
        public bool NoSpecialEffects
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableHitSpEffect"].Value));
            set => Row["disableHitSpEffect"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the character's AI will not be informed when this attack
        /// misses. Enabled for basic body attacks (falling, rolling, ladder
        /// punches, etc.) that are generally not considered to be serious
        /// attacks.
        /// </summary>
        public bool NoMissNotificationForAI
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["IgnoreNotifyMissSwingForAI"].Value));
            set => Row["IgnoreNotifyMissSwingForAI"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, sound effects will supposedly be repeated as long as the
        /// attack continuously hits a wall. Never enabled, which is probably a
        /// good thing.
        /// </summary>
        public bool RepeatHitSoundEffects
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["repeatHitSfx"].Value));
            set => Row["repeatHitSfx"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Flags if this is the attack damage parameter of a physical projectile
        /// (arrow, bolt, or throwing knife).
        /// </summary>
        public bool IsPhysicalProjectile
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isArrowAtk"].Value));
            set => Row["isArrowAtk"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Flags if this is an attack of a ghost, which presumably disables wall
        /// collision, etc.
        /// </summary>
        public bool IsAttackByGhost
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isGhostAtk"].Value));
            set => Row["isGhostAtk"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this attack will ignore invincibility frames from rolling or
        /// backstepping (but not other sources of invincibility such as TAE or
        /// events).
        /// </summary>
        public bool IgnoreInvincibilityFrames
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableNoDamage"].Value));
            set => Row["isDisableNoDamage"].Value = value;
        }
    }
}
