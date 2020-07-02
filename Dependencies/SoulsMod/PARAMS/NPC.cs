using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class NPC : RowWrapper
    {
        public NPC() { }
        public NPC(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int BehaviorVariationID
        {
            get => Convert.ToInt32(Row["behaviorVariationId"].Value);
            set => Row["behaviorVariationId"].Value = value;
        }
        // LINK_STRING: <Params:AI>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int AiThinkID
        {
            get => Convert.ToInt32(Row["aiThinkId"].Value);
            set => Row["aiThinkId"].Value = value;
        }
        // LINK_STRING: <Text:NPCNames>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int NameID
        {
            get => Convert.ToInt32(Row["nameId"].Value);
            set => Row["nameId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float TurnVelocity
        {
            get => Convert.ToSingle(Row["turnVellocity"].Value);
            set => Row["turnVellocity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float HitHeight
        {
            get => Convert.ToSingle(Row["hitHeight"].Value);
            set => Row["hitHeight"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float HitRadius
        {
            get => Convert.ToSingle(Row["hitRadius"].Value);
            set => Row["hitRadius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public uint Weight
        {
            get => Convert.ToUInt32(Row["weight"].Value);
            set => Row["weight"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float HitYOffset
        {
            get => Convert.ToSingle(Row["hitYOffset"].Value);
            set => Row["hitYOffset"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public uint MaximumHP
        {
            get => Convert.ToUInt32(Row["hp"].Value);
            set => Row["hp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public uint MaximumMP
        {
            get => Convert.ToUInt32(Row["mp"].Value);
            set => Row["mp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public uint SoulReward
        {
            get => Convert.ToUInt32(Row["getSoul"].Value);
            set => Row["getSoul"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID1
        {
            get => Convert.ToInt32(Row["itemLotId_1"].Value);
            set => Row["itemLotId_1"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID2
        {
            get => Convert.ToInt32(Row["itemLotId_2"].Value);
            set => Row["itemLotId_2"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID3
        {
            get => Convert.ToInt32(Row["itemLotId_3"].Value);
            set => Row["itemLotId_3"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID4
        {
            get => Convert.ToInt32(Row["itemLotId_4"].Value);
            set => Row["itemLotId_4"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID5
        {
            get => Convert.ToInt32(Row["itemLotId_5"].Value);
            set => Row["itemLotId_5"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int ItemLotID6
        {
            get => Convert.ToInt32(Row["itemLotId_6"].Value);
            set => Row["itemLotId_6"].Value = value;
        }
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int HumanityLotID
        {
            get => Convert.ToInt32(Row["humanityLotId"].Value);
            set => Row["humanityLotId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID0
        {
            get => Convert.ToInt32(Row["spEffectID0"].Value);
            set => Row["spEffectID0"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID1
        {
            get => Convert.ToInt32(Row["spEffectID1"].Value);
            set => Row["spEffectID1"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID2
        {
            get => Convert.ToInt32(Row["spEffectID2"].Value);
            set => Row["spEffectID2"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID3
        {
            get => Convert.ToInt32(Row["spEffectID3"].Value);
            set => Row["spEffectID3"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID4
        {
            get => Convert.ToInt32(Row["spEffectID4"].Value);
            set => Row["spEffectID4"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID5
        {
            get => Convert.ToInt32(Row["spEffectID5"].Value);
            set => Row["spEffectID5"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID6
        {
            get => Convert.ToInt32(Row["spEffectID6"].Value);
            set => Row["spEffectID6"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialEffectID7
        {
            get => Convert.ToInt32(Row["spEffectID7"].Value);
            set => Row["spEffectID7"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int NewGamePlusSpecialEffect
        {
            get => Convert.ToInt32(Row["GameClearSpEffectID"].Value);
            set => Row["GameClearSpEffectID"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float PhysicalGuardCutRate
        {
            get => Convert.ToSingle(Row["physGuardCutRate"].Value);
            set => Row["physGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float MagicGuardCutRate
        {
            get => Convert.ToSingle(Row["magGuardCutRate"].Value);
            set => Row["magGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float FireGuardCutRate
        {
            get => Convert.ToSingle(Row["fireGuardCutRate"].Value);
            set => Row["fireGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float LightningGuardCutRate
        {
            get => Convert.ToSingle(Row["thunGuardCutRate"].Value);
            set => Row["thunGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int AnimationIDOffset
        {
            get => Convert.ToInt32(Row["animIdOffset"].Value);
            set => Row["animIdOffset"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int MoveAnimationID
        {
            get => Convert.ToInt32(Row["moveAnimId"].Value);
            set => Row["moveAnimId"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialMoveAnimationID1
        {
            get => Convert.ToInt32(Row["spMoveAnimId1"].Value);
            set => Row["spMoveAnimId1"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int SpecialMoveAnimationID2
        {
            get => Convert.ToInt32(Row["spMoveAnimId2"].Value);
            set => Row["spMoveAnimId2"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float NetworkWarpDistance
        {
            get => Convert.ToSingle(Row["networkWarpDist"].Value);
            set => Row["networkWarpDist"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorR1
        {
            get => Convert.ToInt32(Row["dbgBehaviorR1"].Value);
            set => Row["dbgBehaviorR1"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorL1
        {
            get => Convert.ToInt32(Row["dbgBehaviorL1"].Value);
            set => Row["dbgBehaviorL1"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorR2
        {
            get => Convert.ToInt32(Row["dbgBehaviorR2"].Value);
            set => Row["dbgBehaviorR2"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorL2
        {
            get => Convert.ToInt32(Row["dbgBehaviorL2"].Value);
            set => Row["dbgBehaviorL2"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorRL
        {
            get => Convert.ToInt32(Row["dbgBehaviorRL"].Value);
            set => Row["dbgBehaviorRL"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorRR
        {
            get => Convert.ToInt32(Row["dbgBehaviorRR"].Value);
            set => Row["dbgBehaviorRR"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorRD
        {
            get => Convert.ToInt32(Row["dbgBehaviorRD"].Value);
            set => Row["dbgBehaviorRD"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorRU
        {
            get => Convert.ToInt32(Row["dbgBehaviorRU"].Value);
            set => Row["dbgBehaviorRU"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorLL
        {
            get => Convert.ToInt32(Row["dbgBehaviorLL"].Value);
            set => Row["dbgBehaviorLL"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorLR
        {
            get => Convert.ToInt32(Row["dbgBehaviorLR"].Value);
            set => Row["dbgBehaviorLR"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorLD
        {
            get => Convert.ToInt32(Row["dbgBehaviorLD"].Value);
            set => Row["dbgBehaviorLD"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int DebugBehaviorLU
        {
            get => Convert.ToInt32(Row["dbgBehaviorLU"].Value);
            set => Row["dbgBehaviorLU"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int AnimationIDOffset2
        {
            get => Convert.ToInt32(Row["animIdOffset2"].Value);
            set => Row["animIdOffset2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part1DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate1"].Value);
            set => Row["partsDamageRate1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part2DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate2"].Value);
            set => Row["partsDamageRate2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part3DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate3"].Value);
            set => Row["partsDamageRate3"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part4DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate4"].Value);
            set => Row["partsDamageRate4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part5DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate5"].Value);
            set => Row["partsDamageRate5"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part6DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate6"].Value);
            set => Row["partsDamageRate6"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part7DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate7"].Value);
            set => Row["partsDamageRate7"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float Part8DamageRate
        {
            get => Convert.ToSingle(Row["partsDamageRate8"].Value);
            set => Row["partsDamageRate8"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float WeakPartsDamageRate
        {
            get => Convert.ToSingle(Row["weakPartsDamageRate"].Value);
            set => Row["weakPartsDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float PoiseRecoveryCorrection
        {
            get => Convert.ToSingle(Row["superArmorRecoverCorrection"].Value);
            set => Row["superArmorRecoverCorrection"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public float StaggerKnockbackDistance
        {
            get => Convert.ToSingle(Row["superArmorBrakeKnockbackDist"].Value);
            set => Row["superArmorBrakeKnockbackDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public ushort MaxStamina
        {
            get => Convert.ToUInt16(Row["stamina"].Value);
            set => Row["stamina"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public ushort StaminaRecoveryBaseSpeed
        {
            get => Convert.ToUInt16(Row["staminaRecoverBaseVel"].Value);
            set => Row["staminaRecoverBaseVel"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base defense applied to all physical attacks.
        /// </summary>
        public ushort PhysicalDefense
        {
            get => Convert.ToUInt16(Row["def_phys"].Value);
            set => Row["def_phys"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base defense added against slashing physical attacks.
        /// </summary>
        public short SlashDefense
        {
            get => Convert.ToInt16(Row["def_slash"].Value);
            set => Row["def_slash"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base defense added against striking physical attacks.
        /// </summary>
        public short StrikeDefense
        {
            get => Convert.ToInt16(Row["def_blow"].Value);
            set => Row["def_blow"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base defense added against thrusting physical attacks.
        /// </summary>
        public short ThrustDefense
        {
            get => Convert.ToInt16(Row["def_thrust"].Value);
            set => Row["def_thrust"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public ushort MagicDefense
        {
            get => Convert.ToUInt16(Row["def_mag"].Value);
            set => Row["def_mag"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public ushort FireDefense
        {
            get => Convert.ToUInt16(Row["def_fire"].Value);
            set => Row["def_fire"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public ushort LightningDefense
        {
            get => Convert.ToUInt16(Row["def_thunder"].Value);
            set => Row["def_thunder"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines how badly an attacker is repelled when they fail to break
        /// this NPC's poise. The Armored Tusk and Chained Prisoner have very high
        /// values (50-60), but most NPCs have 0.
        /// </summary>
        public ushort DefenseRepelPower
        {
            get => Convert.ToUInt16(Row["defFlickPower"].Value);
            set => Row["defFlickPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base poison resistance.
        /// </summary>
        public ushort PoisonResistance
        {
            get => Convert.ToUInt16(Row["resist_poison"].Value);
            set => Row["resist_poison"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base toxic resistance.
        /// </summary>
        public ushort ToxicResistance
        {
            get => Convert.ToUInt16(Row["resist_desease"].Value);
            set => Row["resist_desease"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base bleed resistance.
        /// </summary>
        public ushort BleedResistance
        {
            get => Convert.ToUInt16(Row["resist_blood"].Value);
            set => Row["resist_blood"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base curse resistance.
        /// </summary>
        public ushort CurseResistance
        {
            get => Convert.ToUInt16(Row["resist_curse"].Value);
            set => Row["resist_curse"].Value = value;
        }
        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Model to be used when this quest-related NPC appears as a ghost to
        /// other players. Defaults to -1 for almost all standard enemies, which
        /// means they do not appear as a ghost to others.
        /// </summary>
        public short GhostModelID
        {
            get => Convert.ToInt16(Row["ghostModelId"].Value);
            set => Row["ghostModelId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Always -1.
        /// </summary>
        public short NormalChangeResourceID
        {
            get => Convert.ToInt16(Row["normalChangeResouceId"].Value);
            set => Row["normalChangeResouceId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Zero for every NPC except the Phalanx Hollow (20).
        /// </summary>
        public short GuardAngle
        {
            get => Convert.ToInt16(Row["guardAngle"].Value);
            set => Row["guardAngle"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public short SlashDamageReductionWhenGuarding
        {
            get => Convert.ToInt16(Row["slashGuardCutRate"].Value);
            set => Row["slashGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public short StrikeDamageReductionWhenGuarding
        {
            get => Convert.ToInt16(Row["blowGuardCutRate"].Value);
            set => Row["blowGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public short ThrustDamageReductionWhenGuarding
        {
            get => Convert.ToInt16(Row["thrustGuardCutRate"].Value);
            set => Row["thrustGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum poise of character. Poise is reduced when attacked, but
        /// quickly refills. If reduced to zero, the character will be staggered.
        /// </summary>
        public short MaxPoise
        {
            get => Convert.ToInt16(Row["superArmorDurability"].Value);
            set => Row["superArmorDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Used for only some NPCs, where it is generally set to a
        /// number close to the NPC's character model ID.
        /// </summary>
        public short NormalChangeTextureChrID
        {
            get => Convert.ToInt16(Row["normalChangeTexChrId"].Value);
            set => Row["normalChangeTexChrId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines appearance of dropped items. 0 means the item appears to
        /// glow faintly from inside the NPC's body (e.g. Rat, Mushroom
        /// Child/Parent, Ent) and 1 means the item is a clear white orb just like
        /// regular treasure on corpses (most NPCs).
        /// </summary>
        public ushort ItemDropAppearance
        {
            get => Convert.ToUInt16(Row["dropType"].Value);
            set => Row["dropType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte KnockbackRate
        {
            get => Convert.ToByte(Row["knockbackRate"].Value);
            set => Row["knockbackRate"].Value = value;
        }
        // LINK_STRING: <Params:Knockback>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Knockback parameters were abandoned after Demons' Souls.
        /// </summary>
        public byte KnockbackID
        {
            get => Convert.ToByte(Row["knockbackParamId"].Value);
            set => Row["knockbackParamId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of fall damage to ignore.
        /// </summary>
        public byte FallDamageReduction
        {
            get => Convert.ToByte(Row["fallDamageDump"].Value);
            set => Row["fallDamageDump"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Always set to zero in the game, but presumably, increasing it will
        /// reduce the amount of stamina lost when this NPC blocks an attack.
        /// </summary>
        public byte StaminaGuardDefense
        {
            get => Convert.ToByte(Row["staminaGuardDef"].Value);
            set => Row["staminaGuardDef"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte PCAttrB
        {
            get => Convert.ToByte(Row["pcAttrB"].Value);
            set => Row["pcAttrB"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte PCAttrW
        {
            get => Convert.ToByte(Row["pcAttrW"].Value);
            set => Row["pcAttrW"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte PCAttrL
        {
            get => Convert.ToByte(Row["pcAttrL"].Value);
            set => Row["pcAttrL"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte PCAttrR
        {
            get => Convert.ToByte(Row["pcAttrR"].Value);
            set => Row["pcAttrR"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte AreaAttrB
        {
            get => Convert.ToByte(Row["areaAttrB"].Value);
            set => Row["areaAttrB"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte AreaAttrW
        {
            get => Convert.ToByte(Row["areaAttrW"].Value);
            set => Row["areaAttrW"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte AreaAttrL
        {
            get => Convert.ToByte(Row["areaAttrL"].Value);
            set => Row["areaAttrL"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Like a remnant of World Tendency. Always set to zero.
        /// </summary>
        public byte AreaAttrR
        {
            get => Convert.ToByte(Row["areaAttrR"].Value);
            set => Row["areaAttrR"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown effect, likely none. Set to zero for NPC parts (tails and
        /// Hydra heads) and 10 for everyone else.
        /// </summary>
        public byte MPRecoveryBaseSpeed
        {
            get => Convert.ToByte(Row["mpRecoverBaseVel"].Value);
            set => Row["mpRecoverBaseVel"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown effect, but it is set to zero for most enemies, 50 for very
        /// heavy enemies like Great Stone Knights and Titanite Demons, and 100
        /// for Mimics.
        /// </summary>
        public byte RepelDamageCutRate
        {
            get => Convert.ToByte(Row["flickDamageCutRate"].Value);
            set => Row["flickDamageCutRate"].Value = value;
        }
        // LINK_STRING: <Lighting:Lod>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Default lighting.
        /// </summary>
        public sbyte DefaultLightingParamID
        {
            get => Convert.ToSByte(Row["defaultLodParamId"].Value);
            set => Row["defaultLodParamId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte DrawType
        {
            get => Convert.ToByte(Row["drawType"].Value);
            set => Row["drawType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte NPCType
        {
            get => Convert.ToByte(Row["npcType"].Value);
            set => Row["npcType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// 0: enemy, 1: boss, 2: ally, 6: unused, 7: white phantom
        /// </summary>
        public byte TeamType
        {
            get => Convert.ToByte(Row["teamType"].Value);
            set => Row["teamType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte MoveType
        {
            get => Convert.ToByte(Row["moveType"].Value);
            set => Row["moveType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte LockOnDistance
        {
            get => Convert.ToByte(Row["lockDist"].Value);
            set => Row["lockDist"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte Material
        {
            get => Convert.ToByte(Row["material"].Value);
            set => Row["material"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte MaterialSFX
        {
            get => Convert.ToByte(Row["materialSfx"].Value);
            set => Row["materialSfx"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte MaterialWeak
        {
            get => Convert.ToByte(Row["material_Weak"].Value);
            set => Row["material_Weak"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public byte MaterialWeakSFX
        {
            get => Convert.ToByte(Row["materialSfx_Weak"].Value);
            set => Row["materialSfx_Weak"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Seems to be set to 1 for most enemies with multiple parts
        /// (Sentinels, Quelaag, Seath, Gaping Dragon), but not all of them (Bell
        /// Gargoyles), and 0 otherwise.
        /// </summary>
        public byte PartsDamageType
        {
            get => Convert.ToByte(Row["partsDamageType"].Value);
            set => Row["partsDamageType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown effect, but it is generally set to 30 for all four-legged
        /// enemies, and 0 for all others.
        /// </summary>
        public byte MaxUndurationAngle
        {
            get => Convert.ToByte(Row["maxUndurationAng"].Value);
            set => Row["maxUndurationAng"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Set to 4 for enemies who can guard (including Manus), except Giant
        /// Skeletons, who have a value of 3. All other NPCs have zero.
        /// </summary>
        public sbyte GuardLevel
        {
            get => Convert.ToSByte(Row["guardLevel"].Value);
            set => Row["guardLevel"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Set to 1 for Slimes and Undead Dragons, and 0 for everyone else.
        /// </summary>
        public byte BurnSFXType
        {
            get => Convert.ToByte(Row["burnSfxType"].Value);
            set => Row["burnSfxType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added poison resistance while guarding.
        /// </summary>
        public sbyte PoisonGuardResistance
        {
            get => Convert.ToSByte(Row["poisonGuardResist"].Value);
            set => Row["poisonGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added toxic resistance while guarding.
        /// </summary>
        public sbyte ToxicGuardResistance
        {
            get => Convert.ToSByte(Row["diseaseGuardResist"].Value);
            set => Row["diseaseGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added bleed resistance while guarding.
        /// </summary>
        public sbyte BleedGuardResistance
        {
            get => Convert.ToSByte(Row["bloodGuardResist"].Value);
            set => Row["bloodGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added curse resistance while guarding.
        /// </summary>
        public sbyte CurseGuardResistance
        {
            get => Convert.ToSByte(Row["curseGuardResist"].Value);
            set => Row["curseGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte ParryAttack
        {
            get => Convert.ToByte(Row["parryAttack"].Value);
            set => Row["parryAttack"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte ParryDefense
        {
            get => Convert.ToByte(Row["parryDefence"].Value);
            set => Row["parryDefence"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Set to 2 for very large enemies, 1 for large enemies, and 0 otherwise.
        /// </summary>
        public byte SFXSize
        {
            get => Convert.ToByte(Row["sfxSize"].Value);
            set => Row["sfxSize"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte PushOutCameraRegionRadius
        {
            get => Convert.ToByte(Row["pushOutCamRegionRadius"].Value);
            set => Row["pushOutCamRegionRadius"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Set to 1 or 2 for most bosses/tough enemies, and 0 otherwise. Likely
        /// related to AI triggers.
        /// </summary>
        public byte HitStopType
        {
            get => Convert.ToByte(Row["hitStopType"].Value);
            set => Row["hitStopType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Not something you want to mess with.
        /// </summary>
        public byte LadderEndCheckOffsetTop
        {
            get => Convert.ToByte(Row["ladderEndChkOffsetTop"].Value);
            set => Row["ladderEndChkOffsetTop"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Not something you want to mess with.
        /// </summary>
        public byte LadderEndCheckOffsetBottom
        {
            get => Convert.ToByte(Row["ladderEndChkOffsetLow"].Value);
            set => Row["ladderEndChkOffsetLow"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool UseRagdollCameraHit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["useRagdollCamHit"].Value));
            set => Row["useRagdollCamHit"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool DisableClothRigidHit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableClothRigidHit"].Value));
            set => Row["disableClothRigidHit"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool UseRagdoll
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["useRagdoll"].Value));
            set => Row["useRagdoll"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsDemon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDemon"].Value));
            set => Row["isDemon"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsGhost
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isGhost"].Value));
            set => Row["isGhost"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsNoDamageMotion
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isNoDamageMotion"].Value));
            set => Row["isNoDamageMotion"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsUnduration
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isUnduration"].Value));
            set => Row["isUnduration"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always false.
        /// </summary>
        public bool IsChangeWanderGhost
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isChangeWanderGhost"].Value));
            set => Row["isChangeWanderGhost"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask0
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask0"].Value));
            set => Row["modelDispMask0"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask1
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask1"].Value));
            set => Row["modelDispMask1"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask2
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask2"].Value));
            set => Row["modelDispMask2"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask3
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask3"].Value));
            set => Row["modelDispMask3"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask4
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask4"].Value));
            set => Row["modelDispMask4"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask5
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask5"].Value));
            set => Row["modelDispMask5"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask6
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask6"].Value));
            set => Row["modelDispMask6"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask7
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask7"].Value));
            set => Row["modelDispMask7"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask8
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask8"].Value));
            set => Row["modelDispMask8"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask9
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask9"].Value));
            set => Row["modelDispMask9"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask10
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask10"].Value));
            set => Row["modelDispMask10"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask11
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask11"].Value));
            set => Row["modelDispMask11"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask12
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask12"].Value));
            set => Row["modelDispMask12"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask13
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask13"].Value));
            set => Row["modelDispMask13"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask14
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask14"].Value));
            set => Row["modelDispMask14"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool ModelDisplayMask15
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["modelDispMask15"].Value));
            set => Row["modelDispMask15"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsEnableNeckTurn
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEnableNeckTurn"].Value));
            set => Row["isEnableNeckTurn"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Prevents NPC from respawning when you rest at a bonfire, though they
        /// will still respawn when you die or the map is de-loaded unless they
        /// are disabled by an event script.
        /// </summary>
        public bool DisableRespawnOnRest
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableRespawn"].Value));
            set => Row["disableRespawn"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool IsMoveAnimationWait
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isMoveAnimWait"].Value));
            set => Row["isMoveAnimWait"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always false.
        /// </summary>
        public bool IsCrowd
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isCrowd"].Value));
            set => Row["isCrowd"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// True for skeletons and friends, but not sure how it is actually used
        /// to disable their reanimation by Necromancers.
        /// </summary>
        public bool IsWeakToDivine
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isWeakSaint"].Value));
            set => Row["isWeakSaint"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// True for all Gods and most NPCs in Anor Londo.
        /// </summary>
        public bool IsWeakToOccult
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isWeakA"].Value));
            set => Row["isWeakA"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// True for Darkwraiths, Primordial Serpents, and the Four Kings, but not
        /// Manus.
        /// </summary>
        public bool IsAbyssal
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isWeakB"].Value));
            set => Row["isWeakB"].Value = value;
        }
        // LINK_STRING: <Pad:1>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public bool Pad1
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["pad1"].Value));
            set => Row["pad1"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Effects unknown. Set to 1 (Way of White) for Andre and 0 for everyone
        /// else.
        /// </summary>
        public byte VowType
        {
            get => Convert.ToByte(Row["vowType"].Value);
            set => Row["vowType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// True for bosses and non-respawning enemies that are disabled in event
        /// scripts, but its effects are unknown.
        /// </summary>
        public bool DisableInitializeDead
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableInitializeDead"].Value));
            set => Row["disableInitializeDead"].Value = value;
        }

    }
}