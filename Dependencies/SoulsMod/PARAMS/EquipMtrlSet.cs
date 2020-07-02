using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class EquipMtrlSet : RowWrapper
    {
        public EquipMtrlSet() { }
        public EquipMtrlSet(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good required to upgrade weapon.
        /// </summary>
		public int MaterialId01
		{
			get => Convert.ToInt32(Row["materialId01"].Value);
			set => Row["materialId01"].Value = value;
		}
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Second good required to upgrade weapon. Never used, and the upgrade
        /// menu can't display it (though it may still work as a requirement).
        /// </summary>
		public int MaterialId02
		{
			get => Convert.ToInt32(Row["materialId02"].Value);
			set => Row["materialId02"].Value = value;
		}
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Second good required to upgrade weapon. Never used, and the upgrade
        /// menu can't display it (though it may still work as a requirement).
        /// </summary>
		public int MaterialId03
		{
			get => Convert.ToInt32(Row["materialId03"].Value);
			set => Row["materialId03"].Value = value;
		}
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Second good required to upgrade weapon. Never used, and the upgrade
        /// menu can't display it (though it may still work as a requirement).
        /// </summary>
		public int MaterialId04
		{
			get => Convert.ToInt32(Row["materialId04"].Value);
			set => Row["materialId04"].Value = value;
		}
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Second good required to upgrade weapon. Never used, and the upgrade
        /// menu can't display it (though it may still work as a requirement).
        /// </summary>
		public int MaterialId05
		{
			get => Convert.ToInt32(Row["materialId05"].Value);
			set => Row["materialId05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of Upgrade Good required for reinforcement.
        /// </summary>
		public sbyte ItemNum01
		{
			get => Convert.ToSByte(Row["itemNum01"].Value);
			set => Row["itemNum01"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Amount of Upgrade Good 2 required for upgrade. Never used, and the
        /// upgrade menu can't display it (though it may still work as a
        /// requirement).
        /// </summary>
		public sbyte ItemNum02
		{
			get => Convert.ToSByte(Row["itemNum02"].Value);
			set => Row["itemNum02"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Amount of Upgrade Good 3 required for upgrade. Never used, and the
        /// upgrade menu can't display it (though it may still work as a
        /// requirement).
        /// </summary>
		public sbyte ItemNum03
		{
			get => Convert.ToSByte(Row["itemNum03"].Value);
			set => Row["itemNum03"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Amount of Upgrade Good 4 required for upgrade. Never used, and the
        /// upgrade menu can't display it (though it may still work as a
        /// requirement).
        /// </summary>
		public sbyte ItemNum04
		{
			get => Convert.ToSByte(Row["itemNum04"].Value);
			set => Row["itemNum04"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Amount of Upgrade Good 5 required for upgrade. Never used, and the
        /// upgrade menu can't display it (though it may still work as a
        /// requirement).
        /// </summary>
		public sbyte ItemNum05
		{
			get => Convert.ToSByte(Row["itemNum05"].Value);
			set => Row["itemNum05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the upgrade quantity will not be shown. Often used when only
        /// one of the upgrade good is needed.
        /// </summary>
		public bool IsDisableDispNum01
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableDispNum01"].Value));
			set => Row["isDisableDispNum01"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, the upgrade quantity for Upgrade Good 2 will not be shown.
        /// Often used when only one of the upgrade good is needed (though again,
        /// this slot is never used).
        /// </summary>
		public bool IsDisableDispNum02
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableDispNum02"].Value));
			set => Row["isDisableDispNum02"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, the upgrade quantity for Upgrade Good 3 will not be shown.
        /// Often used when only one of the upgrade good is needed (though again,
        /// this slot is never used).
        /// </summary>
		public bool IsDisableDispNum03
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableDispNum03"].Value));
			set => Row["isDisableDispNum03"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, the upgrade quantity for Upgrade Good 4 will not be shown.
        /// Often used when only one of the upgrade good is needed (though again,
        /// this slot is never used).
        /// </summary>
		public bool IsDisableDispNum04
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableDispNum04"].Value));
			set => Row["isDisableDispNum04"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, the upgrade quantity for Upgrade Good 5 will not be shown.
        /// Often used when only one of the upgrade good is needed (though again,
        /// this slot is never used).
        /// </summary>
		public bool IsDisableDispNum05
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableDispNum05"].Value));
			set => Row["isDisableDispNum05"].Value = value;
		}
	}
}
