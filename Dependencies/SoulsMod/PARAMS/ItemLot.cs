using SoulsFormats;
using SoulsFormatsMod;
using System;
using System.Linq;

namespace SoulsFormatsMod.PARAMS
{
    public class ItemLot : RowWrapper
    {
		public ItemLot() { }
		public ItemLot(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		public void SetSimpleItem(ItemLotCategory category, int itemID, int count = 1, int itemFlag = -1)
		{
			// Configure item lot to simply drop some number of a given item, guaranteed.
			int i = 1;
			while (i <= 8)
			{
				Row[$"lotItemId0{i}"].Value = i == 1 ? itemID : 0;
				Row[$"lotItemCategory0{i}"].Value = i == 1 ? (int)category : -1;
				Row[$"lotItemBasePoint0{i}"].Value = (ushort)(i == 1 ? 100 : 0);
				Row[$"cumulateLotPoint0{i}"].Value = (ushort)0;
				Row[$"lotItemNum0{i}"].Value = (byte)(i == 1 ? count : 0);
				Row[$"enableLuck0{i}"].Value = false;
				i++;
			}
			GetItemFlagId = itemFlag;
		}
		public void SetItemSlots(ItemLotCategory[] categories, int[] itemIDs, uint[] counts, uint[] chancePoints, bool setLuckOnFirstOnly = true)
		{
			// Simple way to set multiple item IDs, their relative chance points, and their categories
			// simultaneously. All unused fields will be set to default (null) values. Flag is untouched.
			
			// If `setLuckOnFirstOnly` is true, luck will be disabled for all lots except the first.
			// This is standard practice, as the worst drop (e.g. nothing) is usually in the first slot.

			if (itemIDs.Length != chancePoints.Length || itemIDs.Length != counts.Length || itemIDs.Length != categories.Length)
				throw new ArgumentException("Items, chance points, counts, and categories must have the same length");
			if (itemIDs.Length > 8)
				throw new ArgumentException("Cannot have more than eight items in an Item Lot.");
			int i = 1;
			while (i <= itemIDs.Length)
			{
				Row[$"lotItemId0{i}"].Value = itemIDs[i - 1];
				Row[$"lotItemCategory0{i}"].Value = (int)categories[i - 1];
				Row[$"lotItemBasePoint0{i}"].Value = (ushort)chancePoints[i - 1];
				Row[$"cumulateLotPoint0{i}"].Value = (ushort)0;
				Row[$"lotItemNum0{i}"].Value = (byte)counts[i - 1];
				if (setLuckOnFirstOnly)
					Row[$"enableLuck0{i}"].Value = i == 1;
				i++;
			}
			while (i <= 8)
			{
				// Clear remaining slots.
				Row[$"lotItemId0{i}"].Value = 0;
				Row[$"lotItemCategory0{i}"].Value = 0;
				Row[$"lotItemBasePoint0{i}"].Value = (ushort)0;
				Row[$"cumulateLotPoint0{i}"].Value = (ushort)0;
				Row[$"lotItemNum0{i}"].Value = (byte)0;
				Row[$"enableLuck0{i}"].Value = false;
				i++;
			}
		}

		public void EnableLuckSlots(params int[] slots)
		{
			// Enable luck on all given slots, and disable luck for the rest.
			// Remember that enabling luck on a slot *reduces* the odds of getting
			// that slot (by some unknown positive function of luck) as luck increases.
			for (int i = 1; i <= 8; i++)
				Row[$"enableLuck0{i}"].Value = slots.Contains(i);
		}

		// TODO: MULTI_TYPE_FIELD
		/// <summary>
		/// TODO
		// </summary>
		public int LotItemId01
		{
			get => Convert.ToInt32(Row["lotItemId01"].Value);
			set => Row["lotItemId01"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId02
		{
			get => Convert.ToInt32(Row["lotItemId02"].Value);
			set => Row["lotItemId02"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId03
		{
			get => Convert.ToInt32(Row["lotItemId03"].Value);
			set => Row["lotItemId03"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId04
		{
			get => Convert.ToInt32(Row["lotItemId04"].Value);
			set => Row["lotItemId04"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId05
		{
			get => Convert.ToInt32(Row["lotItemId05"].Value);
			set => Row["lotItemId05"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId06
		{
			get => Convert.ToInt32(Row["lotItemId06"].Value);
			set => Row["lotItemId06"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId07
		{
			get => Convert.ToInt32(Row["lotItemId07"].Value);
			set => Row["lotItemId07"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public int LotItemId08
		{
			get => Convert.ToInt32(Row["lotItemId08"].Value);
			set => Row["lotItemId08"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 1).
        /// </summary>
		public int LotItemCategory01
		{
			get => Convert.ToInt32(Row["lotItemCategory01"].Value);
			set => Row["lotItemCategory01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 2).
        /// </summary>
		public int LotItemCategory02
		{
			get => Convert.ToInt32(Row["lotItemCategory02"].Value);
			set => Row["lotItemCategory02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 3).
        /// </summary>
		public int LotItemCategory03
		{
			get => Convert.ToInt32(Row["lotItemCategory03"].Value);
			set => Row["lotItemCategory03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 4).
        /// </summary>
		public int LotItemCategory04
		{
			get => Convert.ToInt32(Row["lotItemCategory04"].Value);
			set => Row["lotItemCategory04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 5).
        /// </summary>
		public int LotItemCategory05
		{
			get => Convert.ToInt32(Row["lotItemCategory05"].Value);
			set => Row["lotItemCategory05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 6).
        /// </summary>
		public int LotItemCategory06
		{
			get => Convert.ToInt32(Row["lotItemCategory06"].Value);
			set => Row["lotItemCategory06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 7).
        /// </summary>
		public int LotItemCategory07
		{
			get => Convert.ToInt32(Row["lotItemCategory07"].Value);
			set => Row["lotItemCategory07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of item (slot 8).
        /// </summary>
		public int LotItemCategory08
		{
			get => Convert.ToInt32(Row["lotItemCategory08"].Value);
			set => Row["lotItemCategory08"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint01
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint01"].Value);
			set => Row["lotItemBasePoint01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint02
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint02"].Value);
			set => Row["lotItemBasePoint02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint03
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint03"].Value);
			set => Row["lotItemBasePoint03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint04
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint04"].Value);
			set => Row["lotItemBasePoint04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint05
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint05"].Value);
			set => Row["lotItemBasePoint05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint06
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint06"].Value);
			set => Row["lotItemBasePoint06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint07
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint07"].Value);
			set => Row["lotItemBasePoint07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Relative chance (divided by total chance points across all eight
        /// slots) that this item will be dropped.
        /// </summary>
		public ushort LotItemBasePoint08
		{
			get => Convert.ToUInt16(Row["lotItemBasePoint08"].Value);
			set => Row["lotItemBasePoint08"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint01
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint01"].Value);
			set => Row["cumulateLotPoint01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint02
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint02"].Value);
			set => Row["cumulateLotPoint02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint03
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint03"].Value);
			set => Row["cumulateLotPoint03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint04
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint04"].Value);
			set => Row["cumulateLotPoint04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint05
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint05"].Value);
			set => Row["cumulateLotPoint05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint06
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint06"].Value);
			set => Row["cumulateLotPoint06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint07
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint07"].Value);
			set => Row["cumulateLotPoint07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points that will be cumulatively added to this slot's chance points
        /// every time the item lot is rolled. This
        /// </summary>
		public ushort CumulateLotPoint08
		{
			get => Convert.ToUInt16(Row["cumulateLotPoint08"].Value);
			set => Row["cumulateLotPoint08"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId01
		{
			get => Convert.ToInt32(Row["getItemFlagId01"].Value);
			set => Row["getItemFlagId01"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId02
		{
			get => Convert.ToInt32(Row["getItemFlagId02"].Value);
			set => Row["getItemFlagId02"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId03
		{
			get => Convert.ToInt32(Row["getItemFlagId03"].Value);
			set => Row["getItemFlagId03"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId04
		{
			get => Convert.ToInt32(Row["getItemFlagId04"].Value);
			set => Row["getItemFlagId04"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId05
		{
			get => Convert.ToInt32(Row["getItemFlagId05"].Value);
			set => Row["getItemFlagId05"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId06
		{
			get => Convert.ToInt32(Row["getItemFlagId06"].Value);
			set => Row["getItemFlagId06"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId07
		{
			get => Convert.ToInt32(Row["getItemFlagId07"].Value);
			set => Row["getItemFlagId07"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that will be enabled when this exact item slot is dropped (and
        /// presumably picked up). Never used.
        /// </summary>
		public int GetItemFlagId08
		{
			get => Convert.ToInt32(Row["getItemFlagId08"].Value);
			set => Row["getItemFlagId08"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Flag enabled when any item from this item lot is picked up.
        /// </summary>
		public int GetItemFlagId
		{
			get => Convert.ToInt32(Row["getItemFlagId"].Value);
			set => Row["getItemFlagId"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First of eight consecutive flags used to store the cumulative points
        /// for this item lot.
        /// </summary>
		public int CumulateNumFlagId
		{
			get => Convert.ToInt32(Row["cumulateNumFlagId"].Value);
			set => Row["cumulateNumFlagId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum number of times that cumulative points will be added to the
        /// total. I suspect that the cumulative slot may be awarded automatically
        /// after this; if not, I don't know how the Symbol of Avarice always
        /// drops after all seven Mimics are killed.
        /// </summary>
		public byte CumulateNumMax
		{
			get => Convert.ToByte(Row["cumulateNumMax"].Value);
			set => Row["cumulateNumMax"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Overall rarity of item lot, from 0 to 3. Used fairly consistently, but
        /// seems to have no effect. Set to 2 for all character drops except
        /// Crystal Lizards, who have 3.
        /// </summary>
		public byte LotItem_Rarity
		{
			get => Convert.ToByte(Row["lotItem_Rarity"].Value);
			set => Row["lotItem_Rarity"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 1).
        /// </summary>
		public byte LotItemNum01
		{
			get => Convert.ToByte(Row["lotItemNum01"].Value);
			set => Row["lotItemNum01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 2).
        /// </summary>
		public byte LotItemNum02
		{
			get => Convert.ToByte(Row["lotItemNum02"].Value);
			set => Row["lotItemNum02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 3).
        /// </summary>
		public byte LotItemNum03
		{
			get => Convert.ToByte(Row["lotItemNum03"].Value);
			set => Row["lotItemNum03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 4).
        /// </summary>
		public byte LotItemNum04
		{
			get => Convert.ToByte(Row["lotItemNum04"].Value);
			set => Row["lotItemNum04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 5).
        /// </summary>
		public byte LotItemNum05
		{
			get => Convert.ToByte(Row["lotItemNum05"].Value);
			set => Row["lotItemNum05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 6).
        /// </summary>
		public byte LotItemNum06
		{
			get => Convert.ToByte(Row["lotItemNum06"].Value);
			set => Row["lotItemNum06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 7).
        /// </summary>
		public byte LotItemNum07
		{
			get => Convert.ToByte(Row["lotItemNum07"].Value);
			set => Row["lotItemNum07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of item (slot 8).
        /// </summary>
		public byte LotItemNum08
		{
			get => Convert.ToByte(Row["lotItemNum08"].Value);
			set => Row["lotItemNum08"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck01
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck01"].Value));
			set => Row["enableLuck01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck02
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck02"].Value));
			set => Row["enableLuck02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck03
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck03"].Value));
			set => Row["enableLuck03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck04
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck04"].Value));
			set => Row["enableLuck04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck05
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck05"].Value));
			set => Row["enableLuck05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck06
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck06"].Value));
			set => Row["enableLuck06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck07
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck07"].Value));
			set => Row["enableLuck07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, increased player luck will *reduce* the chance points of this
        /// slot. Usually used on the empty item slot so that rarer items have a
        /// relatively better chance of dropping.
        /// </summary>
		public bool EnableLuck08
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableLuck08"].Value));
			set => Row["enableLuck08"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset01
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset01"].Value));
			set => Row["cumulateReset01"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset02
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset02"].Value));
			set => Row["cumulateReset02"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset03
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset03"].Value));
			set => Row["cumulateReset03"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset04
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset04"].Value));
			set => Row["cumulateReset04"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset05
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset05"].Value));
			set => Row["cumulateReset05"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset06
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset06"].Value));
			set => Row["cumulateReset06"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset07
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset07"].Value));
			set => Row["cumulateReset07"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, all cumulative points in this slot will be reset when the
        /// slot is actually dropped.
        /// </summary>
		public bool CumulateReset08
		{
			get => MiscUtil.AsBoolean(Convert.ToByte(Row["cumulateReset08"].Value));
			set => Row["cumulateReset08"].Value = value;
		}
	}
}
