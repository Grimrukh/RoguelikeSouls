using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class DefaultEnemyBehavior : RowWrapper
    {
        public DefaultEnemyBehavior() { }
        public DefaultEnemyBehavior(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public int EnemyBehaviorID
        {
            get => Convert.ToInt32(Row["EnemyBehaviorID"].Value);
            set => Row["EnemyBehaviorID"].Value = value;
        }
        public ushort HP
        {
            get => Convert.ToUInt16(Row["HP"].Value);
            set => Row["HP"].Value = value;
        }
        public ushort AttackPower
        {
            get => Convert.ToUInt16(Row["AttackPower"].Value);
            set => Row["AttackPower"].Value = value;
        }
        public int ChrType
        {
            get => Convert.ToInt32(Row["ChrType"].Value);
            set => Row["ChrType"].Value = value;
        }
        public float HitHeight
        {
            get => Convert.ToSingle(Row["HitHeight"].Value);
            set => Row["HitHeight"].Value = value;
        }
        public float HitRadius
        {
            get => Convert.ToSingle(Row["HitRadius"].Value);
            set => Row["HitRadius"].Value = value;
        }
        public float Weight
        {
            get => Convert.ToSingle(Row["Weight"].Value);
            set => Row["Weight"].Value = value;
        }
        public float DynamicFriction
        {
            get => Convert.ToSingle(Row["DynamicFriction"].Value);
            set => Row["DynamicFriction"].Value = value;
        }
        public float StaticFriction
        {
            get => Convert.ToSingle(Row["StaticFriction"].Value);
            set => Row["StaticFriction"].Value = value;
        }
        public int UpperDefState
        {
            get => Convert.ToInt32(Row["UpperDefState"].Value);
            set => Row["UpperDefState"].Value = value;
        }
        public int ActionDefState
        {
            get => Convert.ToInt32(Row["ActionDefState"].Value);
            set => Row["ActionDefState"].Value = value;
        }
        public float RotY_per_Second
        {
            get => Convert.ToSingle(Row["RotY_per_Second"].Value);
            set => Row["RotY_per_Second"].Value = value;
        }
        public byte RotY_per_Second_old
        {
            get => Convert.ToByte(Row["RotY_per_Second_old"].Value);
            set => Row["RotY_per_Second_old"].Value = value;
        }
        public byte EnableSideStep
        {
            get => Convert.ToByte(Row["EnableSideStep"].Value);
            set => Row["EnableSideStep"].Value = value;
        }
        public byte UseRagdollHit
        {
            get => Convert.ToByte(Row["UseRagdollHit"].Value);
            set => Row["UseRagdollHit"].Value = value;
        }
        public ushort Stamina
        {
            get => Convert.ToUInt16(Row["stamina"].Value);
            set => Row["stamina"].Value = value;
        }
        public ushort StaminaRecover
        {
            get => Convert.ToUInt16(Row["staminaRecover"].Value);
            set => Row["staminaRecover"].Value = value;
        }
        public ushort StaminaConsumption
        {
            get => Convert.ToUInt16(Row["staminaConsumption"].Value);
            set => Row["staminaConsumption"].Value = value;
        }
        public ushort Deffenct_Phys
        {
            get => Convert.ToUInt16(Row["deffenct_Phys"].Value);
            set => Row["deffenct_Phys"].Value = value;
        }
    }
}
