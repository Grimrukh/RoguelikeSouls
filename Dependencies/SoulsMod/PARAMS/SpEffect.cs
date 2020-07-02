using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class SpEffect : RowWrapper
    {
        public SpEffect() { }
        public SpEffect(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        /// <summary>
        /// Updates all *CanEffect* properties.
        /// </summary>
        public bool CanAffectAll
        {
            set
            {
                CanAffectAI = value;
                CanAffectEnemy = value;
                CanAffectAlly = value;
                CanAffectPhantoms = value;
                CanAffectPlayers = value;
                CanAffectPlayer = value;
                CanAffectSelf = value;
            }
        }

        /// <summary>
        /// Updates Physical, Magic, Fire, and Lightning attack power multiplier properties.
        /// </summary>
        public float AllAttackPowerMultipliers
        {
            set
            {
                PhysicalAttackPowerMultiplier = value;
                MagicAttackPowerMultiplier = value;
                FireAttackPowerMultiplier = value;
                LightningAttackPowerMultiplier = value;
            }
}

public SpEffectVFX VisualEffect => GPARAM.SpEffectVFXs[SpecialState];

        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Icon that appears in HUD under stamina bar while special effect is
        /// active. Set to -1 for no icon.
        /// </summary>
        public int StatusIcon
        {
            get => Convert.ToInt32(Row["iconId"].Value);
            set => Row["iconId"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect will only take effect if character's current HP is less
        /// than or equal to this percentage (from 0 to 100). Set to -1 for no HP
        /// condition.
        /// </summary>
        public float MaxHPPercentageForEffect
        {
            get => Convert.ToSingle(Row["conditionHp"].Value);
            set => Row["conditionHp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Duration of special effect. Set to 0 for an effect that occurs for
        /// only one frame (e.g. to award souls) or to -1 for an effect that will
        /// last until specifically removed or its source is lost (e.g. rings).
        /// </summary>
        public float EffectDuration
        {
            get => Convert.ToSingle(Row["effectEndurance"].Value);
            set => Row["effectEndurance"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time (in seconds) between applications of the special effect, while
        /// active. Set to higher values to have the effect apply less frequently.
        /// Set to 0 to have it occur every frame.
        /// </summary>
        public float UpdateInterval
        {
            get => Convert.ToSingle(Row["motionInterval"].Value);
            set => Row["motionInterval"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to maximum HP.
        /// </summary>
        public float MaxHPMultiplier
        {
            get => Convert.ToSingle(Row["maxHpRate"].Value);
            set => Row["maxHpRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier applied to maximum MP. (Unused in Dark Souls; does NOT
        /// refer to spell usages.)
        /// </summary>
        public float MaxMPMultiplier
        {
            get => Convert.ToSingle(Row["maxMpRate"].Value);
            set => Row["maxMpRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to maximum stamina.
        /// </summary>
        public float MaxStaminaMultiplier
        {
            get => Convert.ToSingle(Row["maxStaminaRate"].Value);
            set => Row["maxStaminaRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming slashing physical damage.
        /// </summary>
        public float IncomingSlashDamageMultiplier
        {
            get => Convert.ToSingle(Row["slashDamageCutRate"].Value);
            set => Row["slashDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming striking physical damage.
        /// </summary>
        public float IncomingStrikeDamageMultiplier
        {
            get => Convert.ToSingle(Row["blowDamageCutRate"].Value);
            set => Row["blowDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming thrusting physical damage.
        /// </summary>
        public float IncomingThrustDamageMultiplier
        {
            get => Convert.ToSingle(Row["thrustDamageCutRate"].Value);
            set => Row["thrustDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming neutral physical damage.
        /// </summary>
        public float IncomingNeutralDamageMultiplier
        {
            get => Convert.ToSingle(Row["neutralDamageCutRate"].Value);
            set => Row["neutralDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming magic damage.
        /// </summary>
        public float IncomingMagicDamageMultiplier
        {
            get => Convert.ToSingle(Row["magicDamageCutRate"].Value);
            set => Row["magicDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming fire damage.
        /// </summary>
        public float IncomingFireDamageMultiplier
        {
            get => Convert.ToSingle(Row["fireDamageCutRate"].Value);
            set => Row["fireDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to incoming lightning damage.
        /// </summary>
        public float IncomingLightningDamageMultiplier
        {
            get => Convert.ToSingle(Row["thunderDamageCutRate"].Value);
            set => Row["thunderDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing physical damage (of any type).
        /// </summary>
        public float OutgoingPhysicalDamageMultiplier
        {
            get => Convert.ToSingle(Row["physicsAttackRate"].Value);
            set => Row["physicsAttackRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing magic damage.
        /// </summary>
        public float OutgoingMagicDamageMultiplier
        {
            get => Convert.ToSingle(Row["magicAttackRate"].Value);
            set => Row["magicAttackRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing fire damage.
        /// </summary>
        public float OutgoingFireDamageMultiplier
        {
            get => Convert.ToSingle(Row["fireAttackRate"].Value);
            set => Row["fireAttackRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing lightning damage.
        /// </summary>
        public float OutgoingLightningDamageMultiplier
        {
            get => Convert.ToSingle(Row["thunderAttackRate"].Value);
            set => Row["thunderAttackRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's physical attack power (of any type).
        /// </summary>
        public float PhysicalAttackPowerMultiplier
        {
            get => Convert.ToSingle(Row["physicsAttackPowerRate"].Value);
            set => Row["physicsAttackPowerRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's magic attack power.
        /// </summary>
        public float MagicAttackPowerMultiplier
        {
            get => Convert.ToSingle(Row["magicAttackPowerRate"].Value);
            set => Row["magicAttackPowerRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's fire attack power.
        /// </summary>
        public float FireAttackPowerMultiplier
        {
            get => Convert.ToSingle(Row["fireAttackPowerRate"].Value);
            set => Row["fireAttackPowerRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's lightning attack power.
        /// </summary>
        public float LightningAttackPowerMultiplier
        {
            get => Convert.ToSingle(Row["thunderAttackPowerRate"].Value);
            set => Row["thunderAttackPowerRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's physical attack power (of
        /// any type).
        /// </summary>
        public int PhysicalAttackPowerAddition
        {
            get => Convert.ToInt32(Row["physicsAttackPower"].Value);
            set => Row["physicsAttackPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's magic attack power.
        /// </summary>
        public int MagicAttackPowerAddition
        {
            get => Convert.ToInt32(Row["magicAttackPower"].Value);
            set => Row["magicAttackPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's fire attack power.
        /// </summary>
        public int FireAttackPowerAddition
        {
            get => Convert.ToInt32(Row["fireAttackPower"].Value);
            set => Row["fireAttackPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's lightning attack power.
        /// </summary>
        public int LightningAttackPowerAddition
        {
            get => Convert.ToInt32(Row["thunderAttackPower"].Value);
            set => Row["thunderAttackPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's physical defense (all types).
        /// </summary>
        public float PhysicalDefenseMultiplier
        {
            get => Convert.ToSingle(Row["physicsDiffenceRate"].Value);
            set => Row["physicsDiffenceRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's magic defense.
        /// </summary>
        public float MagicDefenseMultiplier
        {
            get => Convert.ToSingle(Row["magicDiffenceRate"].Value);
            set => Row["magicDiffenceRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's fire defense.
        /// </summary>
        public float FireDefenseMultiplier
        {
            get => Convert.ToSingle(Row["fireDiffenceRate"].Value);
            set => Row["fireDiffenceRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's lightning defense.
        /// </summary>
        public float LightningDefenseMultiplier
        {
            get => Convert.ToSingle(Row["thunderDiffenceRate"].Value);
            set => Row["thunderDiffenceRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's physical defense.
        /// </summary>
        public int PhysicalDefenseAddition
        {
            get => Convert.ToInt32(Row["physicsDiffence"].Value);
            set => Row["physicsDiffence"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's magic defense.
        /// </summary>
        public int MagicDefenseAddition
        {
            get => Convert.ToInt32(Row["magicDiffence"].Value);
            set => Row["magicDiffence"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's fire defense.
        /// </summary>
        public int FireDefenseAddition
        {
            get => Convert.ToInt32(Row["fireDiffence"].Value);
            set => Row["fireDiffence"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to add to or subtract from character's lightning defense.
        /// </summary>
        public int LightningDefenseAddition
        {
            get => Convert.ToInt32(Row["thunderDiffence"].Value);
            set => Row["thunderDiffence"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier to use instead of usual multiplier if character is not
        /// guarding. (Always set to 0 in vanilla game, which must deactivate it.
        /// Only an educated guess that it refers to incoming damage, not
        /// outgoing.)
        /// </summary>
        public float NoGuardIncomingDamageMultiplier
        {
            get => Convert.ToSingle(Row["NoGuardDamageRate"].Value);
            set => Row["NoGuardDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier to use instead of usual multiplier if character is hit in a
        /// weak spot. (Always set to -1 in vanilla game, which deactivates it.
        /// Only an educated guess that it affects incoming damage.)
        /// </summary>
        public float CriticalHitIncomingDamageMultiplier
        {
            get => Convert.ToSingle(Row["vitalSpotChangeRate"].Value);
            set => Row["vitalSpotChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier to use instead of usual multiplier if character is *not*
        /// hit in a weak spot. (Always set to -1 in vanilla game, which
        /// deactivates it. Only an educated guess that it affects incoming
        /// damage.)
        /// </summary>
        public float NonCriticalHitIncomingDamageMultiplier
        {
            get => Convert.ToSingle(Row["normalSpotChangeRate"].Value);
            set => Row["normalSpotChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Appears to be an unused variant of MaxHPMultiplier. Always set to 0.
        /// </summary>
        public float MaxHPChangeRatio
        {
            get => Convert.ToSingle(Row["maxHpChangeRate"].Value);
            set => Row["maxHpChangeRate"].Value = value;
        }
        // LINK_STRING: <Params:Behaviors>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Behavior ID to trigger (which can in turn trigger an Attack or Bullet)
        /// whenever special effect is applied. Set to -1 to use no behavior.
        /// </summary>
        public int BehaviorToTrigger
        {
            get => Convert.ToInt32(Row["behaviorId"].Value);
            set => Row["behaviorId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction of maximum HP (from 0 to 100). Negative values
        /// (to -100) will restore that percentage instead. Applied every time the
        /// special effect updates.
        /// </summary>
        public float HPReductionPercentage
        {
            get => Convert.ToSingle(Row["changeHpRate"].Value);
            set => Row["changeHpRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// HP value to subtract (if positive) or add (if negative) to character's
        /// current HP on every update of the special effect.
        /// </summary>
        public int HPPointsLost
        {
            get => Convert.ToInt32(Row["changeHpPoint"].Value);
            set => Row["changeHpPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Percentage reduction of maximum MP (from 0 to 100). Negative values
        /// (to -100) will restore that percentage instead. Applied every time the
        /// special effect updates. (Unused in Dark Souls 1.)
        /// </summary>
        public float MPReductionPercentage
        {
            get => Convert.ToSingle(Row["changeMpRate"].Value);
            set => Row["changeMpRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// MP value to subtract (if positive) or add (if negative) to character's
        /// current MP on every update of the special effect. (Unused in Dark
        /// Souls 1.)
        /// </summary>
        public int MPPointsLost
        {
            get => Convert.ToInt32(Row["changeMpPoint"].Value);
            set => Row["changeMpPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Points added to or subtracted from MP recovery formula. (Unused in
        /// Dark Souls 1.)
        /// </summary>
        public int MPRecoverySpeedChange
        {
            get => Convert.ToInt32(Row["mpRecoverChangeSpeed"].Value);
            set => Row["mpRecoverChangeSpeed"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction of maximum stamina (from 0 to 100). Negative
        /// values (to -100) will restore that percentage instead. Applied every
        /// time the special effect updates.
        /// </summary>
        public float StaminaReductionPercentage
        {
            get => Convert.ToSingle(Row["changeStaminaRate"].Value);
            set => Row["changeStaminaRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Stamina value to subtract (if positive) or add (if negative) to
        /// character's current stamina on every update of the special effect.
        /// </summary>
        public int StaminaPointsLost
        {
            get => Convert.ToInt32(Row["changeStaminaPoint"].Value);
            set => Row["changeStaminaPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points added to or subtracted from stamina recovery formula. I believe
        /// this affects the amount of stamina restored every second. (For
        /// reference, a Green Blossom adds 40 points.)
        /// </summary>
        public int StaminaRecoverySpeedChange
        {
            get => Convert.ToInt32(Row["staminaRecoverChangeSpeed"].Value);
            set => Row["staminaRecoverChangeSpeed"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Name suggests this changes the duration of magic effects, but it is
        /// never used (always zero).
        /// </summary>
        public float MagicEffectTimeChange
        {
            get => Convert.ToSingle(Row["magicEffectTimeChange"].Value);
            set => Row["magicEffectTimeChange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of durability to subtract (if positive) or add (if negative) to
        /// current durability on every update of the special effect. The
        /// equipment affected is determined by...
        /// </summary>
        public int CurrentDurabilityAddition
        {
            get => Convert.ToInt32(Row["insideDurability"].Value);
            set => Row["insideDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of durability to subtract (if positive) or add (if negative) to
        /// the character's maximum durability while the special effect is active.
        /// The equipment affected is determined by...
        /// </summary>
        public int MaxDurabilityAddition
        {
            get => Convert.ToInt32(Row["maxDurability"].Value);
            set => Row["maxDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the amount of damage dealt to targets' stamina.
        /// </summary>
        public float OutgoingStaminaDamageMultiplier
        {
            get => Convert.ToSingle(Row["staminaAttackRate"].Value);
            set => Row["staminaAttackRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of poison damage (in units of resistance) added to the
        /// character on every update. Negative values will heal poison damage
        /// instead (e.g. Purple Moss Clump). Unclear how this distinguishes
        /// between reducing build-up and actually healing the status.
        /// </summary>
        public int PoisonDamage
        {
            get => Convert.ToInt32(Row["poizonAttackPower"].Value);
            set => Row["poizonAttackPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of toxic damage (in units of resistance) added to the character
        /// on every update. Negative values will heal toxic damage instead (e.g.
        /// Blooming Purple Moss Clump). Unclear how this distinguishes between
        /// reducing build-up and actually healing the status.
        /// </summary>
        public int ToxicDamage
        {
            get => Convert.ToInt32(Row["registIllness"].Value);
            set => Row["registIllness"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of bleed damage (in units of resistance) added to the character
        /// on every update. Negative values will heal bleed damage instead (e.g.
        /// Blood-Red Moss Clump). Unclear how this distinguishes between reducing
        /// build-up and actually healing the status.
        /// </summary>
        public int BleedDamage
        {
            get => Convert.ToInt32(Row["registBlood"].Value);
            set => Row["registBlood"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of curse damage (in units of resistance) added to the character
        /// on every update. Negative values will heal curse damage instead (e.g.
        /// Purging Stone). Unclear how this distinguishes between reducing build-
        /// up and actually healing the status.
        /// </summary>
        public int CurseDamage
        {
            get => Convert.ToInt32(Row["registCurse"].Value);
            set => Row["registCurse"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to amount of fall damage taken by character. Cannot
        /// prevent lethal falls.
        /// </summary>
        public float FallDamageMultiplier
        {
            get => Convert.ToSingle(Row["fallDamageRate"].Value);
            set => Row["fallDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the amount of souls received when enemies or
        /// bosses are killed.
        /// </summary>
        public float SoulsFromKillsMultiplier
        {
            get => Convert.ToSingle(Row["soulRate"].Value);
            set => Row["soulRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the character's maximum equip load.
        /// </summary>
        public float MaxEquipLoadMultiplier
        {
            get => Convert.ToSingle(Row["equipWeightChangeRate"].Value);
            set => Row["equipWeightChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier applied to how much the character can carry, equipped or
        /// not. Seems to have no effect in Dark Souls 1.
        /// </summary>
        public float MaxItemLoadMultiplier
        {
            get => Convert.ToSingle(Row["allItemWeightChangeRate"].Value);
            set => Row["allItemWeightChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of souls received (if positive) or taken away (if negative)
        /// every time the special effect is updated.
        /// </summary>
        public int SoulAmountChange
        {
            get => Convert.ToInt32(Row["soul"].Value);
            set => Row["soul"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Override default animation ID offset of character, which can change
        /// their animation set temporarily.
        /// </summary>
        public int AnimationIDOffset
        {
            get => Convert.ToInt32(Row["animIdOffset"].Value);
            set => Row["animIdOffset"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the amount of souls given to the player when
        /// they kill this character (e.g. enemies in NG+).
        /// </summary>
        public float SoulRewardMultiplier
        {
            get => Convert.ToSingle(Row["haveSoulRate"].Value);
            set => Row["haveSoulRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value added to or subtract from this character's priority in the
        /// target queue. Higher priority means they are more likely to be
        /// targeted by enemies.
        /// </summary>
        public float TargetPriorityChange
        {
            get => Convert.ToSingle(Row["targetPriority"].Value);
            set => Row["targetPriority"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in enemy sight (from 0 to 100) when looking for
        /// this character. Not sure if negative values can be used to make this
        /// character *more* visible.
        /// </summary>
        public int EnemySightPercentageReduction
        {
            get => Convert.ToInt32(Row["sightSearchEnemyCut"].Value);
            set => Row["sightSearchEnemyCut"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in enemy hearing (from 0 to 100) when looking for
        /// this character. Not sure if negative values can be used to make this
        /// character *more* audible.
        /// </summary>
        public int EnemyHearingPercentageReduction
        {
            get => Convert.ToInt32(Row["hearingSearchEnemyCut"].Value);
            set => Row["hearingSearchEnemyCut"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to all of this character's animations. Values other
        /// than 1 can lead to cool but potentially glitchy behavior (e.g.
        /// desynchronized grab animations and missed collision).
        /// </summary>
        public float AnimationSpeedMultiplier
        {
            get => Convert.ToSingle(Row["grabityRate"].Value);
            set => Row["grabityRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's maximum poison resistance.
        /// </summary>
        public float PoisonResistanceMultiplier
        {
            get => Convert.ToSingle(Row["registPoizonChangeRate"].Value);
            set => Row["registPoizonChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's maximum toxic resistance.
        /// </summary>
        public float ToxicResistanceMultiplier
        {
            get => Convert.ToSingle(Row["registIllnessChangeRate"].Value);
            set => Row["registIllnessChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's maximum bleed resistance.
        /// </summary>
        public float BleedResistanceMultiplier
        {
            get => Convert.ToSingle(Row["registBloodChangeRate"].Value);
            set => Row["registBloodChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to character's maximum curse resistance.
        /// </summary>
        public float CurseResistanceMultiplier
        {
            get => Convert.ToSingle(Row["registCurseChangeRate"].Value);
            set => Row["registCurseChangeRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description says 'defense against HP when NPCs are robbed by
        /// soul steal'. Probably unused.
        /// </summary>
        public float SoulStealMultiplier
        {
            get => Convert.ToSingle(Row["soulStealRate"].Value);
            set => Row["soulStealRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Multiplier applied to the duration of the effect specified in
        /// EffectDurationMultiplierType. Used only by Hawkeye Gough to reduce
        /// poison and toxic duration in vanilla game.
        /// </summary>
        public float EffectDurationMultiplier
        {
            get => Convert.ToSingle(Row["lifeReductionRate"].Value);
            set => Row["lifeReductionRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to any increase in character's current HP.
        /// </summary>
        public float HPRecoveryRate
        {
            get => Convert.ToSingle(Row["hpRecoverRate"].Value);
            set => Row["hpRecoverRate"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect to apply to character automatically when this special
        /// effect ends (if not terminated manually by an event).
        /// </summary>
        public int NextSpecialEffect
        {
            get => Convert.ToInt32(Row["replaceSpEffectId"].Value);
            set => Row["replaceSpEffectId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect to apply to character every time this special effect
        /// updates (e.g. Symbol of Avarice HP reduction).
        /// </summary>
        public int SpecialEffectPerUpdate
        {
            get => Convert.ToInt32(Row["cycleOccurrenceSpEffectId"].Value);
            set => Row["cycleOccurrenceSpEffectId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect to apply to any target hit by an attack.  WARNING: This
        /// will not trigger unless SpecialStateIndex is set to 152
        /// (PoisonedWeapon), and must therefore always be accompanied by the
        /// poison weapon visual effect.
        /// </summary>
        public int SpecialEffectOnAttack
        {
            get => Convert.ToInt32(Row["atkOccurrenceSpEffectId"].Value);
            set => Row["atkOccurrenceSpEffectId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown; never used.
        /// </summary>
        public float GuardDefenseFlickPowerRate
        {
            get => Convert.ToSingle(Row["guardDefFlickPowerRate"].Value);
            set => Row["guardDefFlickPowerRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to amount of stamina subtracted from stamina
        /// damage when an attack is blocked. Higher is better.
        /// </summary>
        public float GuardStaminaMultiplier
        {
            get => Convert.ToSingle(Row["guardStaminaCutRate"].Value);
            set => Row["guardStaminaCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description says 'Gaze passing: activation time
        /// (milliseconds).' Likely unused.
        /// </summary>
        public short RayCastPassingTime
        {
            get => Convert.ToInt16(Row["rayCastPassedTime"].Value);
            set => Row["rayCastPassedTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount added (if positive) or subtracted (if negative) from
        /// character's poise.
        /// </summary>
        public short PoiseAddition
        {
            get => Convert.ToInt16(Row["changeSuperArmorPoint"].Value);
            set => Row["changeSuperArmorPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage change (from 0 to 100) in bow range. Requires
        /// SpecialStateIndex BowBoostRange (168) to work.
        /// </summary>
        public short BowRangePercentageChange
        {
            get => Convert.ToInt16(Row["bowDistRate"].Value);
            set => Row["bowDistRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Category of special effect. This effect will override (i.e. cancel
        /// out) all other active effects with the same category when it is added.
        /// </summary>
        public ushort SpecialEffectCategory
        {
            get => Convert.ToUInt16(Row["spCategory"].Value);
            set => Row["spCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Priority ordering for special effect to be applied on each update
        /// (lower values are updated first).
        /// </summary>
        public byte SpecialEffectPriority
        {
            get => Convert.ToByte(Row["categoryPriority"].Value);
            set => Row["categoryPriority"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines automatic game saving behavior (used for status ailments
        /// only). Set to -1 for no saving.
        /// </summary>
        public sbyte SaveCategory
        {
            get => Convert.ToSByte(Row["saveCategory"].Value);
            set => Row["saveCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Supposed to modify attunement slots, but does nothing. You can use
        /// special state 'Extra Attunement' to get 50% extra attunment slots, if
        /// needed.
        /// </summary>
        public byte AttunementSlotCountChange
        {
            get => Convert.ToByte(Row["changeMagicSlot"].Value);
            set => Row["changeMagicSlot"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Miracle slots are not even separate from other magic slots, so this is
        /// likely an abandoned field.
        /// </summary>
        public byte AttunementMiracleSlotCountChange
        {
            get => Convert.ToByte(Row["changeMiracleSlot"].Value);
            set => Row["changeMiracleSlot"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Damage applied to soft humanity count. Negative values will add soft
        /// humanity.
        /// </summary>
        public sbyte HumanityDamage
        {
            get => Convert.ToSByte(Row["heroPointDamage"].Value);
            set => Row["heroPointDamage"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value added to or subtracted from defense against riposte attacks.
        /// </summary>
        public byte RiposteDefenseAddition
        {
            get => Convert.ToByte(Row["defFlickPower"].Value);
            set => Row["defFlickPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier to use instead of usual multiplier on incoming (I assume)
        /// riposte attacks). Never used.
        /// </summary>
        public byte FlickDamageMultiplier
        {
            get => Convert.ToByte(Row["flickDamageCutRate"].Value);
            set => Row["flickDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of incoming bleed damage received (usually 100).
        /// </summary>
        public byte IncomingBleedDamagePercentage
        {
            get => Convert.ToByte(Row["bloodDamageRate"].Value);
            set => Row["bloodDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of NoImpact level.
        /// </summary>
        public sbyte ReplaceNoImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_None"].Value);
            set => Row["dmgLv_None"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Small impact level.
        /// </summary>
        public sbyte ReplaceSmallImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_S"].Value);
            set => Row["dmgLv_S"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Medium impact level.
        /// </summary>
        public sbyte ReplaceMediumImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_M"].Value);
            set => Row["dmgLv_M"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Large impact level.
        /// </summary>
        public sbyte ReplaceLargeImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_L"].Value);
            set => Row["dmgLv_L"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Blowoff impact level.
        /// </summary>
        public sbyte ReplaceBlowoffImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_BlowM"].Value);
            set => Row["dmgLv_BlowM"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Push impact level.
        /// </summary>
        public sbyte ReplacePushImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_Push"].Value);
            set => Row["dmgLv_Push"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Strike impact level.
        /// </summary>
        public sbyte ReplaceStrikeImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_Strike"].Value);
            set => Row["dmgLv_Strike"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Blow impact level.
        /// </summary>
        public sbyte ReplaceSmallBlowImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_BlowS"].Value);
            set => Row["dmgLv_BlowS"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Minimal impact level.
        /// </summary>
        public sbyte ReplaceMinimalImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_Min"].Value);
            set => Row["dmgLv_Min"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of Launch impact level.
        /// </summary>
        public sbyte ReplaceLaunchImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_Uppercut"].Value);
            set => Row["dmgLv_Uppercut"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of BlowBackward impact level.
        /// </summary>
        public sbyte ReplaceBlowBackwardImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_BlowLL"].Value);
            set => Row["dmgLv_BlowLL"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Impact level that will occur instead of BreathBurn impact level.
        /// </summary>
        public sbyte ReplaceBreathBurnImpactLevel
        {
            get => Convert.ToSByte(Row["dmgLv_Breath"].Value);
            set => Row["dmgLv_Breath"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Attack type attached to hits while special effect is active.
        /// </summary>
        public byte AttackAttribute
        {
            get => Convert.ToByte(Row["atkAttribute"].Value);
            set => Row["atkAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Element attached to hits while special effect is active.
        /// </summary>
        public byte ElementAttribute
        {
            get => Convert.ToByte(Row["spAttribute"].Value);
            set => Row["spAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Hard-coded special state to use. Also determines visual effect from
        /// Special Effect Visuals table.
        /// </summary>
        public byte SpecialState
        {
            get => Convert.ToByte(Row["stateInfo"].Value);
            set => Row["stateInfo"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon category that is affected by special effect.
        /// </summary>
        public byte AffectedWeaponType
        {
            get => Convert.ToByte(Row["wepParamChange"].Value);
            set => Row["wepParamChange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines how movement is affected. (Does not correspond to Movement
        /// param entries.)
        /// </summary>
        public byte MovementType
        {
            get => Convert.ToByte(Row["moveType"].Value);
            set => Row["moveType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Type of effect whose duration is affected by EffectDurationMultiplier.
        /// Known values: 2 = poison, 5 = toxic.
        /// </summary>
        public byte EffectDurationMultiplierType
        {
            get => Convert.ToByte(Row["lifeReductionType"].Value);
            set => Row["lifeReductionType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines how throws are affected while special effect is active.
        /// Values still unknown (rarely used).
        /// </summary>
        public byte ThrowCondition
        {
            get => Convert.ToByte(Row["throwCondition"].Value);
            set => Row["throwCondition"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unclear; used only to manage the Hydra as more heads are cut off. All
        /// other values are -1.
        /// </summary>
        public sbyte AddBehaviorJudgeIDCondition
        {
            get => Convert.ToSByte(Row["addBehaviorJudgeId_condition"].Value);
            set => Row["addBehaviorJudgeId_condition"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero. Unknown effect. Internal description suggests that this
        /// is a constant added to all behavior judge IDs (from TAE) issued by
        /// character.
        /// </summary>
        public byte AddBehaviorJudgeIDAdd
        {
            get => Convert.ToByte(Row["addBehaviorJudgeId_add"].Value);
            set => Row["addBehaviorJudgeId_add"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target self.
        /// </summary>
        public bool CanAffectSelf
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetSelf"].Value));
            set => Row["effectTargetSelf"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target self.
        /// </summary>
        public bool CanAffectAlly
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetFriend"].Value));
            set => Row["effectTargetFriend"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target enemies.
        /// </summary>
        public bool CanAffectEnemy
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetEnemy"].Value));
            set => Row["effectTargetEnemy"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target player characters.
        /// </summary>
        public bool CanAffectPlayer
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetPlayer"].Value));
            set => Row["effectTargetPlayer"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target non-player characters.
        /// </summary>
        public bool CanAffectAI
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetAI"].Value));
            set => Row["effectTargetAI"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target humans.
        /// </summary>
        public bool CanAffectPlayers
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetLive"].Value));
            set => Row["effectTargetLive"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target phantoms (white or black).
        /// </summary>
        public bool CanAffectPhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetGhost"].Value));
            set => Row["effectTargetGhost"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target white phantoms.
        /// </summary>
        public bool CanAffectWhitePhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetWhiteGhost"].Value));
            set => Row["effectTargetWhiteGhost"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target white phantoms.
        /// </summary>
        public bool CanAffectBlackPhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetBlackGhost"].Value));
            set => Row["effectTargetBlackGhost"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Effect will target character when they attack (e.g. HP drain).
        /// </summary>
        public bool CanAffectAttacker
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectTargetAttacker"].Value));
            set => Row["effectTargetAttacker"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Display icon even when special effect is inactive (not sure what that
        /// means). Never enabled.
        /// </summary>
        public bool DisplayIconWhenInactive
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["dispIconNonactive"].Value));
            set => Row["dispIconNonactive"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Use visual effect from Special Effect Visuals table (indexed by
        /// Special State field).
        /// </summary>
        public bool UseVisualEffect
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["useSpEffectEffect"].Value));
            set => Row["useSpEffectEffect"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, special effect damage will be scaled by character
        /// intelligence (I believe).
        /// </summary>
        public bool UseIntelligenceScaling
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bAdjustMagicAblity"].Value));
            set => Row["bAdjustMagicAblity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, special effect damage will be scaled by character faith (I
        /// believe).
        /// </summary>
        public bool UseFaithScaling
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bAdjustFaithAblity"].Value));
            set => Row["bAdjustFaithAblity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this effect will be applied multiple times depending on the
        /// NG+ cycle (I think).
        /// </summary>
        public bool ForNewGamePlus
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bGameClearBonus"].Value));
            set => Row["bGameClearBonus"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, multipliers will be applied to magic attacks.
        /// </summary>
        public bool AffectsMagic
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["magParamChange"].Value));
            set => Row["magParamChange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, multipliers will be applied to miracle attacks.
        /// </summary>
        public bool AffectsMiracles
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["miracleParamChange"].Value));
            set => Row["miracleParamChange"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unused Demon's Souls remnant.
        /// </summary>
        public bool ClearSoul
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["clearSoul"].Value));
            set => Row["clearSoul"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only by White Sign Soapstone.
        /// </summary>
        public bool RequestWhitePhantomSummon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestSOS"].Value));
            set => Row["requestSOS"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only by Red Sign Soapstone.
        /// </summary>
        public bool RequestBlackPhantomSummon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestBlackSOS"].Value));
            set => Row["requestBlackSOS"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only be (Cracked) Red Eye Orb.
        /// </summary>
        public bool RequestInvasion
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestForceJoinBlackSOS"].Value));
            set => Row["requestForceJoinBlackSOS"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Not used by any item. Likely kicks all clients out of your world.
        /// </summary>
        public bool RequestKick
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestKickSession"].Value));
            set => Row["requestKickSession"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only by Black Separation Crystal.
        /// </summary>
        public bool RequestReturnToOwnWorld
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestLeaveSession"].Value));
            set => Row["requestLeaveSession"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only by Black Eye Orb (Lautrec quest and cut Shiva quest).
        /// </summary>
        public bool RequestNPCInvasion
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestNpcInveda"].Value));
            set => Row["requestNpcInveda"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, character cannot die. Never used in vanilla game.
        /// </summary>
        public bool Immortal
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["noDead"].Value));
            set => Row["noDead"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, changes to maximum HP will not affect current HP (unless it
        /// must be reduced to new maximum).
        /// </summary>
        public bool CurrentHPIgnoresMaxHPChange
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bCurrHPIndependeMaxHP"].Value));
            set => Row["bCurrHPIndependeMaxHP"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, character will ignore corrosion damage to durability. Used
        /// only by Demon's Souls junk.
        /// </summary>
        public bool IgnoreCorrosion
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["corrosionIgnore"].Value));
            set => Row["corrosionIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, character will ignore any changes to their sight range from
        /// other special effects. Used only by Demon's Souls junk.
        /// </summary>
        public bool IgnoreSightReduction
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["sightSearchCutIgnore"].Value));
            set => Row["sightSearchCutIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, character will ignore any changes to their hearing range from
        /// other special effects. Used only by Demon's Souls junk.
        /// </summary>
        public bool IgnoreHearingReduction
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["hearingSearchCutIgnore"].Value));
            set => Row["hearingSearchCutIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, character will ignore any special effect that attempts to
        /// disable their magic. Used only by Demon's Souls junk.
        /// </summary>
        public bool IgnoreMagicDisabling
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["antiMagicIgnore"].Value));
            set => Row["antiMagicIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown; never used.
        /// </summary>
        public bool IgnoreFakeTargets
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["fakeTargetIgnore"].Value));
            set => Row["fakeTargetIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown; never used.
        /// </summary>
        public bool IgnoreUndeadFakeTargets
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["fakeTargetIgnoreUndead"].Value));
            set => Row["fakeTargetIgnoreUndead"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown; never used.
        /// </summary>
        public bool IgnoreBeastFakeTargets
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["fakeTargetIgnoreAnimal"].Value));
            set => Row["fakeTargetIgnoreAnimal"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Ignore gravity. (Not sure if this actually works.)
        /// </summary>
        public bool IgnoreGravity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["grabityIgnore"].Value));
            set => Row["grabityIgnore"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Immune to poison.
        /// </summary>
        public bool PoisonImmunity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disablePoison"].Value));
            set => Row["disablePoison"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Immune to toxic.
        /// </summary>
        public bool ToxicImmunity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableDisease"].Value));
            set => Row["disableDisease"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Immune to bleed.
        /// </summary>
        public bool BleedImmunity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableBlood"].Value));
            set => Row["disableBlood"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Immune to curse.
        /// </summary>
        public bool CurseImmunity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableCurse"].Value));
            set => Row["disableCurse"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Not sure if this refers to the Alluring Skull. May not work at all.
        /// </summary>
        public bool EnableCharming
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableCharm"].Value));
            set => Row["enableCharm"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'Is the life extended when setting a flag by
        /// TAE?'. Effect unknown. Used by Dragon Head and Torso Stones and some
        /// internal summon-related effects.
        /// </summary>
        public bool EnableLifeTime
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLifeTime"].Value));
            set => Row["enableLifeTime"].Value = value;
        }
        public bool HasTarget
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// For unused 'evil eye' mechanics, probably a Demon's Souls remnant.
        /// </summary>
        {

            get => MiscUtil.AsBoolean(Convert.ToByte(Row["hasTarget : 1"].Value));
            set => Row["hasTarget"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Immune to fire damage. Never enabled, and may not actually work. Needs
        /// testing.
        /// </summary>
        public bool FireImmunity
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isFireDamageCancel"].Value));
            set => Row["isFireDamageCancel"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this special effect will be affected by the Lingering
        /// Dragoncrest Ring special state (193) that extends effect durations.
        /// </summary>
        public bool AffectedByLingeringDragoncrestRing
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isExtendSpEffectLife"].Value));
            set => Row["isExtendSpEffectLife"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Used only by Purple Coward's Crystal.
        /// </summary>
        public bool RequestColiseumExit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["requestLeaveColiseumSession"].Value));
            set => Row["requestLeaveColiseumSession"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters with no
        /// covenant.
        /// </summary>
        public bool AffectsCharactersWithNoCovenant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType0"].Value));
            set => Row["vowType0"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the Way of
        /// White covenant.
        /// </summary>
        public bool AffectsWayOfWhite
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType1"].Value));
            set => Row["vowType1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the
        /// Princess's Guard covenant.
        /// </summary>
        public bool AffectsPrincessGuard
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType2"].Value));
            set => Row["vowType2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the
        /// Warriors of Sunlight covenant.
        /// </summary>
        public bool AffectsWarriorOfSunlight
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType3"].Value));
            set => Row["vowType3"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the
        /// Darkwraith covenant.
        /// </summary>
        public bool AffectsDarkwraith
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType4"].Value));
            set => Row["vowType4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the Path
        /// of the Dragon covenant.
        /// </summary>
        public bool AffectsPathOfTheDragon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType5"].Value));
            set => Row["vowType5"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the
        /// Gravelord Servant covenant.
        /// </summary>
        public bool AffectsGravelordServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType6"].Value));
            set => Row["vowType6"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the Forest
        /// Hunters covenant.
        /// </summary>
        public bool AffectsForestHunter
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType7"].Value));
            set => Row["vowType7"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the Blades
        /// of the Darkmoon covenant.
        /// </summary>
        public bool AffectsDarkmoonBlade
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType8"].Value));
            set => Row["vowType8"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this special effect will affect characters in the Chaos
        /// Servants covenant.
        /// </summary>
        public bool AffectsChaosServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType9"].Value));
            set => Row["vowType9"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant10
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType10"].Value));
            set => Row["vowType10"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant11
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType11"].Value));
            set => Row["vowType11"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant12
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType12"].Value));
            set => Row["vowType12"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant13
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType13"].Value));
            set => Row["vowType13"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant14
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType14"].Value));
            set => Row["vowType14"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this special effect will affect characters in unused
        /// covenant.
        /// </summary>
        public bool AffectsCovenant15
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType15"].Value));
            set => Row["vowType15"].Value = value;
        }
    }
}