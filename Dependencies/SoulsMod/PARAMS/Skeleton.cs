using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Skeleton : RowWrapper
    {
		public Skeleton() { }
		public Skeleton(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		public float NeckTurnGain
		{
			get => Convert.ToSingle(Row["neckTurnGain"].Value);
			set => Row["neckTurnGain"].Value = value;
		}
		public short OriginalGroundHeightMS
		{
			get => Convert.ToInt16(Row["originalGroundHeightMS"].Value);
			set => Row["originalGroundHeightMS"].Value = value;
		}
		public short MinAnkleHeightMS
		{
			get => Convert.ToInt16(Row["minAnkleHeightMS"].Value);
			set => Row["minAnkleHeightMS"].Value = value;
		}
		public short MaxAnkleHeightMS
		{
			get => Convert.ToInt16(Row["maxAnkleHeightMS"].Value);
			set => Row["maxAnkleHeightMS"].Value = value;
		}
		public short CosineMaxKneeAngle
		{
			get => Convert.ToInt16(Row["cosineMaxKneeAngle"].Value);
			set => Row["cosineMaxKneeAngle"].Value = value;
		}
		public short CosineMinKneeAngle
		{
			get => Convert.ToInt16(Row["cosineMinKneeAngle"].Value);
			set => Row["cosineMinKneeAngle"].Value = value;
		}
		public short FootPlantedAnkleHeightMS
		{
			get => Convert.ToInt16(Row["footPlantedAnkleHeightMS"].Value);
			set => Row["footPlantedAnkleHeightMS"].Value = value;
		}
		public short FootRaisedAnkleHeightMS
		{
			get => Convert.ToInt16(Row["footRaisedAnkleHeightMS"].Value);
			set => Row["footRaisedAnkleHeightMS"].Value = value;
		}
		public short RaycastDistanceUp
		{
			get => Convert.ToInt16(Row["raycastDistanceUp"].Value);
			set => Row["raycastDistanceUp"].Value = value;
		}
		public short RaycastDistanceDown
		{
			get => Convert.ToInt16(Row["raycastDistanceDown"].Value);
			set => Row["raycastDistanceDown"].Value = value;
		}
		public short FootEndLS_X
		{
			get => Convert.ToInt16(Row["footEndLS_X"].Value);
			set => Row["footEndLS_X"].Value = value;
		}
		public short FootEndLS_Y
		{
			get => Convert.ToInt16(Row["footEndLS_Y"].Value);
			set => Row["footEndLS_Y"].Value = value;
		}
		public short FootEndLS_Z
		{
			get => Convert.ToInt16(Row["footEndLS_Z"].Value);
			set => Row["footEndLS_Z"].Value = value;
		}
		public short OnOffGain
		{
			get => Convert.ToInt16(Row["onOffGain"].Value);
			set => Row["onOffGain"].Value = value;
		}
		public short GroundAscendingGain
		{
			get => Convert.ToInt16(Row["groundAscendingGain"].Value);
			set => Row["groundAscendingGain"].Value = value;
		}
		public short GroundDescendingGain
		{
			get => Convert.ToInt16(Row["groundDescendingGain"].Value);
			set => Row["groundDescendingGain"].Value = value;
		}
		public short FootRaisedGain
		{
			get => Convert.ToInt16(Row["footRaisedGain"].Value);
			set => Row["footRaisedGain"].Value = value;
		}
		public short FootPlantedGain
		{
			get => Convert.ToInt16(Row["footPlantedGain"].Value);
			set => Row["footPlantedGain"].Value = value;
		}
		public short FootUnlockGain
		{
			get => Convert.ToInt16(Row["footUnlockGain"].Value);
			set => Row["footUnlockGain"].Value = value;
		}
		public byte KneeAxisType
		{
			get => Convert.ToByte(Row["kneeAxisType"].Value);
			set => Row["kneeAxisType"].Value = value;
		}
		public byte UseFootLocking
		{
			get => Convert.ToByte(Row["useFootLocking"].Value);
			set => Row["useFootLocking"].Value = value;
		}
		public byte FootPlacementOn
		{
			get => Convert.ToByte(Row["footPlacementOn"].Value);
			set => Row["footPlacementOn"].Value = value;
		}
		public byte TwistKneeAxisType
		{
			get => Convert.ToByte(Row["twistKneeAxisType"].Value);
			set => Row["twistKneeAxisType"].Value = value;
		}
		public sbyte NeckTurnPriority
		{
			get => Convert.ToSByte(Row["neckTurnPriority"].Value);
			set => Row["neckTurnPriority"].Value = value;
		}
		public byte NeckTurnMaxAngle
		{
			get => Convert.ToByte(Row["neckTurnMaxAngle"].Value);
			set => Row["neckTurnMaxAngle"].Value = value;
		}

	}
}