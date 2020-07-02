using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class SpEffectVFX : RowWrapper
    {
        public SpEffectVFX() { }
        public SpEffectVFX(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <VisualEffect>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Ongoing visual effect for special effect. -1 is no effect.
        /// </summary>
        public int OngoingVisualEffect
        {
            get => Convert.ToInt32(Row["midstSfxId"].Value);
            set => Row["midstSfxId"].Value = value;
        }
        // LINK_STRING: <Sound.SFX>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Ongoing sound effect for special effect. -1 is no effect.
        /// </summary>
        public int OngoingSoundEffect
        {
            get => Convert.ToInt32(Row["midstSeId"].Value);
            set => Row["midstSeId"].Value = value;
        }
        // LINK_STRING: <VisualEffect>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// One-off visual effect when special effect begins. -1 is no effect.
        /// </summary>
        public int InitialVisualEffect
        {
            get => Convert.ToInt32(Row["initSfxId"].Value);
            set => Row["initSfxId"].Value = value;
        }
        // LINK_STRING: <Sound.SFX>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// One-off sound effect when special effect begins. -1 is no effect.
        /// (Does not appear to work.)
        /// </summary>
        public int InitialSoundEffect
        {
            get => Convert.ToInt32(Row["initSeId"].Value);
            set => Row["initSeId"].Value = value;
        }
        // LINK_STRING: <VisualEffect>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// One-off visual effect when special effect ends. -1 is no effect.
        /// </summary>
        public int FinishVisualEffect
        {
            get => Convert.ToInt32(Row["finishSfxId"].Value);
            set => Row["finishSfxId"].Value = value;
        }
        // LINK_STRING: <Sound.SFX>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// One-off sound effect when special effect ends. -1 is no effect. (Does
        /// not appear to work.)
        /// </summary>
        public int FinishSoundEffect
        {
            get => Convert.ToInt32(Row["finishSeId"].Value);
            set => Row["finishSeId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Closest distance at which effect is disabled.
        /// </summary>
        public float HideStartDistance
        {
            get => Convert.ToSingle(Row["camouflageBeginDist"].Value);
            set => Row["camouflageBeginDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Furthest distance at which effect is disabled.
        /// </summary>
        public float HideEndDistance
        {
            get => Convert.ToSingle(Row["camouflageEndDist"].Value);
            set => Row["camouflageEndDist"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Transformation armor ID. Unknown effect. -1 is no armor.
        /// </summary>
        public int TransformationArmorID
        {
            get => Convert.ToInt32(Row["transformProtectorId"].Value);
            set => Row["transformProtectorId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point where ongoing effects are centered. -1 is model root.
        /// </summary>
        public short OngoingModelPoint
        {
            get => Convert.ToInt16(Row["midstDmyId"].Value);
            set => Row["midstDmyId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point where initial effect is centered. -1 is model root.
        /// </summary>
        public short InitialModelPoint
        {
            get => Convert.ToInt16(Row["initDmyId"].Value);
            set => Row["initDmyId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point where finish effect is centered. -1 is model root.
        /// </summary>
        public short FinishModelPoint
        {
            get => Convert.ToInt16(Row["finishDmyId"].Value);
            set => Row["finishDmyId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of effect. Enum not yet mapped.
        /// </summary>
        public byte EffectType
        {
            get => Convert.ToByte(Row["effectType"].Value);
            set => Row["effectType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'Soul Param ID for weapon enchantment.' Enum not
        /// yet mapped.
        /// </summary>
        public byte WeaponEnchantmentSoulParam
        {
            get => Convert.ToByte(Row["soulParamIdForWepEnchant"].Value);
            set => Row["soulParamIdForWepEnchant"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Only one effect in each category can be active at once (determined by
        /// PlaybackPriority).
        /// </summary>
        public byte PlaybackCategory
        {
            get => Convert.ToByte(Row["playCategory"].Value);
            set => Row["playCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Only the lowest-numbered-priority effect in each PlaybackCategory will
        /// be active at once.
        /// </summary>
        public byte PlaybackPriority
        {
            get => Convert.ToByte(Row["playPriority"].Value);
            set => Row["playPriority"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if a large version of the effect exists.
        /// </summary>
        public bool LargeEffectExists
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["existEffectForLarge"].Value));
            set => Row["existEffectForLarge"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if a 'soul version' of the effect exists.
        /// </summary>
        public bool SoulEffectExists
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["existEffectForSoul"].Value));
            set => Row["existEffectForSoul"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if the effect should be invisible when hidden (unclear
        /// exactly what this means).
        /// </summary>
        public bool InvisibleWhenHidden
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["effectInvisibleAtCamouflage"].Value));
            set => Row["effectInvisibleAtCamouflage"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// I believe this determines if the hiding range fields are actually
        /// used.
        /// </summary>
        public bool HidingActive
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["useCamouflage"].Value));
            set => Row["useCamouflage"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unclear.
        /// </summary>
        public bool InvisibleWhenFriendHidden
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleAtFriendCamouflage"].Value));
            set => Row["invisibleAtFriendCamouflage"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If enabled, the three-digit area/block number for the current map will
        /// be added to all effect IDs (e.g. m13_02 -> adds 132).
        /// </summary>
        public bool AddMapAreaBlockOffset
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["addMapAreaBlockOffset"].Value));
            set => Row["addMapAreaBlockOffset"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If enabled, effects are made semi-transparent rather than fully
        /// hidden.
        /// </summary>
        public bool HalfHiddenOnly
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["halfCamouflage"].Value));
            set => Row["halfCamouflage"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates whether the armor transformation should be applied to the
        /// whole body.
        /// </summary>
        public bool ArmorTransformationIsFullBody
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isFullBodyTransformProtectorId"].Value));
            set => Row["isFullBodyTransformProtectorId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon is invisible if enabled.
        /// </summary>
        public bool HideWeapon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isInvisibleWeapon"].Value));
            set => Row["isInvisibleWeapon"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Movement noises are silenced if enabled.
        /// </summary>
        public bool IsSilent
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isSilence"].Value));
            set => Row["isSilence"].Value = value;
        }
    }
}
