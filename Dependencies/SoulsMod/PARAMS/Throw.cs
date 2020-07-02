using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Throw : RowWrapper
    {
        public Throw() { }
        public Throw(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model ID of attacking character.
        /// </summary>
        public int AttackingCharacterModel
        {
            get => Convert.ToInt32(Row["AtkChrId"].Value);
            set => Row["AtkChrId"].Value = value;
        }
        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model ID of defending character.
        /// </summary>
        public int DefendingCharacterModel
        {
            get => Convert.ToInt32(Row["DefChrId"].Value);
            set => Row["DefChrId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance at which throw can be triggered.
        /// </summary>
        public float MaxDistance
        {
            get => Convert.ToSingle(Row["Dist"].Value);
            set => Row["Dist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum angular difference between attacker's facing direction and
        /// defender's facing direction.
        /// </summary>
        public float MinDifferenceInFacingAngle
        {
            get => Convert.ToSingle(Row["DiffAngMin"].Value);
            set => Row["DiffAngMin"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum angular difference between attacker's facing direction and
        /// defender's facing direction.
        /// </summary>
        public float MaxDifferenceInFacingAngle
        {
            get => Convert.ToSingle(Row["DiffAngMax"].Value);
            set => Row["DiffAngMax"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance that defender can be above attacker.
        /// </summary>
        public float MaxDistanceAbove
        {
            get => Convert.ToSingle(Row["upperYRange"].Value);
            set => Row["upperYRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance that defender can be below attacker.
        /// </summary>
        public float MaxDistanceBelow
        {
            get => Convert.ToSingle(Row["lowerYRange"].Value);
            set => Row["lowerYRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum angular difference between attacker's direction and the
        /// direction of the defender.
        /// </summary>
        public float MaxAngleToDefender
        {
            get => Convert.ToSingle(Row["diffAngMyToDef"].Value);
            set => Row["diffAngMyToDef"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Throw ID that should be specified in Attacks to use this throw.
        /// </summary>
        public int ThrowID
        {
            get => Convert.ToInt32(Row["throwTypeId"].Value);
            set => Row["throwTypeId"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation played by attacker during throw.
        /// </summary>
        public int AttackerAnimation
        {
            get => Convert.ToInt32(Row["atkAnimId"].Value);
            set => Row["atkAnimId"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation played by defender during throw.
        /// </summary>
        public int DefenderAnimation
        {
            get => Convert.ToInt32(Row["defAnimId"].Value);
            set => Row["defAnimId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum HP percentage required to escape the throw early by mashing
        /// buttons. (Not sure if 0 prevents any escape, or if escapes are
        /// disabled by another parameter like
        /// </summary>
        public ushort MinHPPercentageForEscape
        {
            get => Convert.ToUInt16(Row["escHp"].Value);
            set => Row["escHp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time of escape cycle, in milliseconds. Not sure exactly what it does.
        /// Set to 100 milliseconds for throws that can be escaped, and zero
        /// otherwise.
        /// </summary>
        public ushort EscapeCycleTime
        {
            get => Convert.ToUInt16(Row["selfEscCycleTime"].Value);
            set => Row["selfEscCycleTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines size of upper hemisphere of spherecast. I believe this is a
        /// percentage relative to the model size, so a value of 80 will send out
        /// a sphere with a radius that is 0.8 times the attacker's model size.
        /// </summary>
        public ushort SphereCastUpperRadiusRatio
        {
            get => Convert.ToUInt16(Row["sphereCastRadiusRateTop"].Value);
            set => Row["sphereCastRadiusRateTop"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines size of lower hemisphere of spherecast. I believe this is a
        /// percentage relative to the model size, so a value of 80 will send out
        /// a sphere with a radius that is 0.8 times the attacker's model size.
        /// </summary>
        public ushort SphereCastLowerRadiusRatio
        {
            get => Convert.ToUInt16(Row["sphereCastRadiusRateLow"].Value);
            set => Row["sphereCastRadiusRateLow"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines buttons that can be mashed to escape. Enumeration is
        /// unknown, but it is set to 3 for the Centipede Demon grab, Male Ghost
        /// grab, and Dark Hand grab, and 1 for every other throw.
        /// </summary>
        public byte ButtonMashType
        {
            get => Convert.ToByte(Row["PadType"].Value);
            set => Row["PadType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description says 'Set the throwable throwable state type'
        /// (?). Set to 1 for all player backstabs and ripostes, and 0 otherwise
        /// (including player plunging attacks and all enemy throws).
        /// </summary>
        public byte AttackEnabled
        {
            get => Convert.ToByte(Row["AtkEnableState"].Value);
            set => Row["AtkEnableState"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point ID on attacker that defender will be snapped to. If this
        /// is zero, 'Snap To Defender Model Point' should be non-zero, and vice
        /// versa.
        /// </summary>
        public byte SnapToAttackerModelPoint
        {
            get => Convert.ToByte(Row["atkSorbDmyId"].Value);
            set => Row["atkSorbDmyId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point ID on defender that attacker will be snapped to. If this
        /// is zero, 'Snap To Attacker Model Point' should be non-zero, and vice
        /// versa.
        /// </summary>
        public byte SnapToDefenderModelPoint
        {
            get => Convert.ToByte(Row["defSorbDmyId"].Value);
            set => Row["defSorbDmyId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of throw. Not sure what uses this, but it could affect various
        /// things.
        /// </summary>
        public byte ThrowType
        {
            get => Convert.ToByte(Row["throwType"].Value);
            set => Row["throwType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description says 'number of self-throwing cycles'. Always set
        /// to 1 when EscapeCycleTime is set to 100 (and MinHPPercentageForEscape
        /// is almost always 25). Not sure how it determines *when* you can escape
        /// the throw.
        /// </summary>
        public byte EscapeCycleCount
        {
            get => Convert.ToByte(Row["selfEscCycleCnt"].Value);
            set => Row["selfEscCycleCnt"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// 'Direction of model point possessed character when thrown'. Set to 1
        /// for the Armored Tusk backstab, 255 for the Iron Golem and Gaping
        /// Dragon grabs, and 0 otherwise.
        /// </summary>
        public byte ModelPointCharacterDirectionType
        {
            get => Convert.ToByte(Row["dmyHasChrDirType"].Value);
            set => Row["dmyHasChrDirType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Attacker will turn when throw begins (presumably before model point
        /// snapping occurs).
        /// </summary>
        public bool AttackerTurns
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isTurnAtker"].Value));
            set => Row["isTurnAtker"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the weapon category check for the attacker will be skipped.
        /// Enabled only for Dark Hand drain.
        /// </summary>
        public bool SkipAttackerWeaponCategoryCheck
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isSkipWepCate"].Value));
            set => Row["isSkipWepCate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the sphere cast check will be skipped. Usually False, but
        /// True for the coffin stab, Armored Tusk backstab, and a few large enemy
        /// grabs. (Presumably, if False, the throw trigger relies on distance and
        /// character angles only and is generally easier to trigger.)
        /// </summary>
        public bool SkipSphereCast
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isSkipSphereCast"].Value));
            set => Row["isSkipSphereCast"].Value = value;
        }
    }
}
