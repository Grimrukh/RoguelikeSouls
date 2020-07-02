using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Ragdoll : RowWrapper
    {
		public Ragdoll() { }
		public Ragdoll(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		public float HierarchyGain
		{
			get => Convert.ToSingle(Row["hierarchyGain"].Value);
			set => Row["hierarchyGain"].Value = value;
		}
		public float VelocityDamping
		{
			get => Convert.ToSingle(Row["velocityDamping"].Value);
			set => Row["velocityDamping"].Value = value;
		}
		public float AccelGain
		{
			get => Convert.ToSingle(Row["accelGain"].Value);
			set => Row["accelGain"].Value = value;
		}
		public float VelocityGain
		{
			get => Convert.ToSingle(Row["velocityGain"].Value);
			set => Row["velocityGain"].Value = value;
		}
		public float PositionGain
		{
			get => Convert.ToSingle(Row["positionGain"].Value);
			set => Row["positionGain"].Value = value;
		}
		public float MaxLinerVelocity
		{
			get => Convert.ToSingle(Row["maxLinerVelocity"].Value);
			set => Row["maxLinerVelocity"].Value = value;
		}

		public float MaxAngularVelocity
		{
			get => Convert.ToSingle(Row["maxAngularVelocity"].Value);
			set => Row["maxAngularVelocity"].Value = value;
		}
		public float SnapGain
		{
			get => Convert.ToSingle(Row["snapGain"].Value);
			set => Row["snapGain"].Value = value;
		}
		public byte Enable
		{
			get => Convert.ToByte(Row["enable"].Value);
			set => Row["enable"].Value = value;
		}
		public sbyte PartsHitMaskNo
		{
			get => Convert.ToSByte(Row["partsHitMaskNo"].Value);
			set => Row["partsHitMaskNo"].Value = value;
		}
	}
}