using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class DefaultAI : RowWrapper
    {
        public DefaultAI() { }
        public DefaultAI(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public ushort RadarRange
        {
            get => Convert.ToUInt16(Row["RadarRange"].Value);
            set => Row["RadarRange"].Value = value;
        }
        public byte RadarAngleX
        {
            get => Convert.ToByte(Row["RadarAngleX"].Value);
            set => Row["RadarAngleX"].Value = value;
        }
        public byte RadarAngleY
        {
            get => Convert.ToByte(Row["RadarAngleY"].Value);
            set => Row["RadarAngleY"].Value = value;
        }
        public ushort TerritorySize
        {
            get => Convert.ToUInt16(Row["TerritorySize"].Value);
            set => Row["TerritorySize"].Value = value;
        }
        public byte ThreatBeforeAttackRate
        {
            get => Convert.ToByte(Row["ThreatBeforeAttackRate"].Value);
            set => Row["ThreatBeforeAttackRate"].Value = value;
        }
        public byte ForceThreatOnFirstLocked
        {
            get => Convert.ToByte(Row["ForceThreatOnFirstLocked"].Value);
            set => Row["ForceThreatOnFirstLocked"].Value = value;
        }
        public ushort Attack1_Distance
        {
            get => Convert.ToUInt16(Row["Attack1_Distance"].Value);
            set => Row["Attack1_Distance"].Value = value;
        }
        public ushort Attack1_Margin
        {
            get => Convert.ToUInt16(Row["Attack1_Margin"].Value);
            set => Row["Attack1_Margin"].Value = value;
        }
        public byte Attack1_Rate
        {
            get => Convert.ToByte(Row["Attack1_Rate"].Value);
            set => Row["Attack1_Rate"].Value = value;
        }
        public byte Attack1_ActionID
        {
            get => Convert.ToByte(Row["Attack1_ActionID"].Value);
            set => Row["Attack1_ActionID"].Value = value;
        }
        public byte Attack1_DelayMin
        {
            get => Convert.ToByte(Row["Attack1_DelayMin"].Value);
            set => Row["Attack1_DelayMin"].Value = value;
        }
        public byte Attack1_DelayMax
        {
            get => Convert.ToByte(Row["Attack1_DelayMax"].Value);
            set => Row["Attack1_DelayMax"].Value = value;
        }
        public byte Attack1_ConeAngle
        {
            get => Convert.ToByte(Row["Attack1_ConeAngle"].Value);
            set => Row["Attack1_ConeAngle"].Value = value;
        }
        public ushort Attack2_Distance
        {
            get => Convert.ToUInt16(Row["Attack2_Distance"].Value);
            set => Row["Attack2_Distance"].Value = value;
        }
        public ushort Attack2_Margin
        {
            get => Convert.ToUInt16(Row["Attack2_Margin"].Value);
            set => Row["Attack2_Margin"].Value = value;
        }
        public byte Attack2_Rate
        {
            get => Convert.ToByte(Row["Attack2_Rate"].Value);
            set => Row["Attack2_Rate"].Value = value;
        }
        public byte Attack2_ActionID
        {
            get => Convert.ToByte(Row["Attack2_ActionID"].Value);
            set => Row["Attack2_ActionID"].Value = value;
        }
        public byte Attack2_DelayMin
        {
            get => Convert.ToByte(Row["Attack2_DelayMin"].Value);
            set => Row["Attack2_DelayMin"].Value = value;
        }
        public byte Attack2_DelayMax
        {
            get => Convert.ToByte(Row["Attack2_DelayMax"].Value);
            set => Row["Attack2_DelayMax"].Value = value;
        }
        public byte Attack2_ConeAngle
        {
            get => Convert.ToByte(Row["Attack2_ConeAngle"].Value);
            set => Row["Attack2_ConeAngle"].Value = value;
        }
        public ushort Attack3_Distance
        {
            get => Convert.ToUInt16(Row["Attack3_Distance"].Value);
            set => Row["Attack3_Distance"].Value = value;
        }
        public ushort Attack3_Margin
        {
            get => Convert.ToUInt16(Row["Attack3_Margin"].Value);
            set => Row["Attack3_Margin"].Value = value;
        }
        public byte Attack3_Rate
        {
            get => Convert.ToByte(Row["Attack3_Rate"].Value);
            set => Row["Attack3_Rate"].Value = value;
        }
        public byte Attack3_ActionID
        {
            get => Convert.ToByte(Row["Attack3_ActionID"].Value);
            set => Row["Attack3_ActionID"].Value = value;
        }
        public byte Attack3_DelayMin
        {
            get => Convert.ToByte(Row["Attack3_DelayMin"].Value);
            set => Row["Attack3_DelayMin"].Value = value;
        }
        public byte Attack3_DelayMax
        {
            get => Convert.ToByte(Row["Attack3_DelayMax"].Value);
            set => Row["Attack3_DelayMax"].Value = value;
        }
        public byte Attack3_ConeAngle
        {
            get => Convert.ToByte(Row["Attack3_ConeAngle"].Value);
            set => Row["Attack3_ConeAngle"].Value = value;
        }
        public ushort Attack4_Distance
        {
            get => Convert.ToUInt16(Row["Attack4_Distance"].Value);
            set => Row["Attack4_Distance"].Value = value;
        }
        public ushort Attack4_Margin
        {
            get => Convert.ToUInt16(Row["Attack4_Margin"].Value);
            set => Row["Attack4_Margin"].Value = value;
        }
        public byte Attack4_Rate
        {
            get => Convert.ToByte(Row["Attack4_Rate"].Value);
            set => Row["Attack4_Rate"].Value = value;
        }
        public byte Attack4_ActionID
        {
            get => Convert.ToByte(Row["Attack4_ActionID"].Value);
            set => Row["Attack4_ActionID"].Value = value;
        }
        public byte Attack4_DelayMin
        {
            get => Convert.ToByte(Row["Attack4_DelayMin"].Value);
            set => Row["Attack4_DelayMin"].Value = value;
        }
        public byte Attack4_DelayMax
        {
            get => Convert.ToByte(Row["Attack4_DelayMax"].Value);
            set => Row["Attack4_DelayMax"].Value = value;
        }
        public byte Attack4_ConeAngle
        {
            get => Convert.ToByte(Row["Attack4_ConeAngle"].Value);
            set => Row["Attack4_ConeAngle"].Value = value;
        }
    }
}
