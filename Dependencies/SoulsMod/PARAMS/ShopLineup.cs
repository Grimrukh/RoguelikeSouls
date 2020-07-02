using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class ShopLineup : RowWrapper
    {
        public ShopLineup() { }
        public ShopLineup(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int EquipId
		{
			get => Convert.ToInt32(Row["equipId"].Value);
			set => Row["equipId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Cost of item, in souls.
        /// </summary>
		public int Value
		{
			get => Convert.ToInt32(Row["value"].Value);
			set => Row["value"].Value = value;
		}
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good that must be possessed for item to be listed. Used to control
        /// appearance of spells in attunement menu.
        /// </summary>
		public int MtrlId
		{
			get => Convert.ToInt32(Row["mtrlId"].Value);
			set => Row["mtrlId"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Flag value that holds the count of this item that have been sold
        /// already.
        /// </summary>
		public int EventFlag
		{
			get => Convert.ToInt32(Row["eventFlag"].Value);
			set => Row["eventFlag"].Value = value;
		}
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unused world tendency condition.
        /// </summary>
		public int QwcId
		{
			get => Convert.ToInt32(Row["qwcId"].Value);
			set => Row["qwcId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Quantity of this item initially available to be sold. Set to -1 for
        /// infinite quantity.
        /// </summary>
		public short SellQuantity
		{
			get => Convert.ToInt16(Row["sellQuantity"].Value);
			set => Row["sellQuantity"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this is a standard shop menu or the spell attunement
        /// menu.
        /// </summary>
		public byte ShopType
		{
			get => Convert.ToByte(Row["shopType"].Value);
			set => Row["shopType"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item listed in menu.
        /// </summary>
		public byte EquipType
		{
			get => Convert.ToByte(Row["equipType"].Value);
			set => Row["equipType"].Value = value;
		}

	}
}