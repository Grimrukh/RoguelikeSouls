using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class LockCam : RowWrapper
    {
        public LockCam() { }
        public LockCam(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance maintained from target by camera in meters. (Default value is
        /// 4.)
        /// </summary>
		public float CamDistTarget
		{
			get => Convert.ToSingle(Row["camDistTarget"].Value);
			set => Row["camDistTarget"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum angle of elevation (X-axis rotation) permitted for camera.
        /// </summary>
		public float RotRangeMinX
		{
			get => Convert.ToSingle(Row["rotRangeMinX"].Value);
			set => Row["rotRangeMinX"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// 'Lock X-rotation shift ratio (0.0 to 1.0).' Unclear effect. Default
        /// value is 0.6.
        /// </summary>
		public float LockRotXShiftRatio
		{
			get => Convert.ToSingle(Row["lockRotXShiftRatio"].Value);
			set => Row["lockRotXShiftRatio"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Vertical offset of camera target from character's base. Default value
        /// is 1.42.
        /// </summary>
		public float ChrOrgOffset_Y
		{
			get => Convert.ToSingle(Row["chrOrgOffset_Y"].Value);
			set => Row["chrOrgOffset_Y"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance ('radius') of camera from character in meters.
        /// Default value is 15; only other value used is 7.
        /// </summary>
		public float ChrLockRangeMaxRadius
		{
			get => Convert.ToSingle(Row["chrLockRangeMaxRadius"].Value);
			set => Row["chrLockRangeMaxRadius"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Vertical field of view of camera in degrees. Default value is 43.
        /// Never goes above 48 (Lost Izalith).
        /// </summary>
		public float CamFovY
		{
			get => Convert.ToSingle(Row["camFovY"].Value);
			set => Row["camFovY"].Value = value;
		}

	}
}
