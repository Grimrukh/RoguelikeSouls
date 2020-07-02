using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class GameObject : RowWrapper
    {
        public GameObject() { }
        public GameObject(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of damage object can take before it is destroyed. (Set to -1
        /// for invulnerability.)
        /// </summary>
        public short ObjectHP
        {
            get => Convert.ToInt16(Row["hp"].Value);
            set => Row["hp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum attack power required to damage object. Attacks with less
        /// power than this will deal no damage.
        /// </summary>
        public ushort MinAttackForDamage
        {
            get => Convert.ToUInt16(Row["defense"].Value);
            set => Row["defense"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'mAA / mAA_????.tpf (-1: None) (AA: Area
        /// number)'.
        /// </summary>
        public short ExternalTextureID
        {
            get => Convert.ToInt16(Row["extRefTexId"].Value);
            set => Row["extRefTexId"].Value = value;
        }
        // LINK_STRING: <Params:Terrains>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Treated the same as floor material. (Set to -1 to use default.)
        /// </summary>
        public short MaterialID
        {
            get => Convert.ToInt16(Row["materialId"].Value);
            set => Row["materialId"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Upper limit of range of destruction animations, which seem to always
        /// start at 0.
        /// </summary>
        public byte MaxDestructionAnimationID
        {
            get => Convert.ToByte(Row["animBreakIdMax"].Value);
            set => Row["animBreakIdMax"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the camera will collide with this object.
        /// </summary>
        public bool CollidesWithCamera
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isCamHit"].Value));
            set => Row["isCamHit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the player will break the object just by touching it.
        /// </summary>
        public bool BrokenByPlayerCollision
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isBreakByPlayerCollide"].Value));
            set => Row["isBreakByPlayerCollide"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the object will use an animation when destroyed rather than
        /// using physics-based destruction.
        /// </summary>
        public bool HasDestructionAnimation
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isAnimBreak"].Value));
            set => Row["isAnimBreak"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the object can be damaged by Bullets with target-piercing
        /// enabled.
        /// </summary>
        public bool HitByPiercingBullets
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isPenetrationBulletHit"].Value));
            set => Row["isPenetrationBulletHit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If False, characters will pass through the object (e.g. branches).
        /// </summary>
        public bool CharacterCollision
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isChrHit"].Value));
            set => Row["isChrHit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, attacks will bounce off the object as though it were a wall.
        /// </summary>
        public bool DeflectsAttacks
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isAttackBacklash"].Value));
            set => Row["isAttackBacklash"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the object cannot be destroyed when the player first spawns.
        /// </summary>
        public bool CannotSpawnBroken
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableBreakForFirstAppear"].Value));
            set => Row["isDisableBreakForFirstAppear"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Object is a ladder.
        /// </summary>
        public bool IsLadder
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isLadder"].Value));
            set => Row["isLadder"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, object animation will not play in cutscenes.
        /// </summary>
        public bool StopAnimationDuringCutscenes
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isAnimPauseOnRemoPlay"].Value));
            set => Row["isAnimPauseOnRemoPlay"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all damage to the object will be prevented. (Not sure if this
        /// is the same effet as settings its HP to -1.)
        /// </summary>
        public bool PreventAllDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDamageNoHit"].Value));
            set => Row["isDamageNoHit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this object can move.
        /// </summary>
        public bool IsMovingObject
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isMoveObj"].Value));
            set => Row["isMoveObj"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Default LOD (level of default) parameter.
        /// </summary>
        public sbyte DefaultLOD
        {
            get => Convert.ToSByte(Row["defaultLodParamId"].Value);
            set => Row["defaultLodParamId"].Value = value;
        }
        // LINK_STRING: <Sound:SFX>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sound effect played upon destruction. (Set to -1 to use default value,
        /// which is apparently 80.)
        /// </summary>
        public int DestructionSoundEffect
        {
            get => Convert.ToInt32(Row["breakSfxId"].Value);
            set => Row["breakSfxId"].Value = value;
        }

    }
}