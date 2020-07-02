using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Accessory : RowWrapper
    {
        public Accessory() { }
        public Accessory(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public new string Name
        {
            get => Text.AccessoryNames[ID];
            set
            {
                Row.Name = value;
                Text.AccessoryNames[ID] = value;
            }
        }

        public string Summary
        {
            get => Text.AccessoryDescriptions[ID];
            set => Text.AccessoryDescriptions[ID] = value;
        }

        public string Description
        {
            get => Text.AccessoryLongDescriptions[ID];
            set => Text.AccessoryLongDescriptions[ID] = value;
        }

        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied when ring is equipped.
        /// </summary>
        public int SpecialEffect
        {
            get => Convert.ToInt32(Row["refId"].Value);
            set => Row["refId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// SFX variation ID combined with the value specified in TAE animation
        /// data. Always -1; likely works with unused Behavior parameter below.
        /// </summary>
        public int SFXVariation
        {
            get => Convert.ToInt32(Row["sfxVariationId"].Value);
            set => Row["sfxVariationId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Weight of ring. Always set to zero in vanilla Dark Souls, but likely
        /// works just like other equipment.
        /// </summary>
        public float Weight
        {
            get => Convert.ToSingle(Row["weight"].Value);
            set => Row["weight"].Value = value;
        }
        // LINK_STRING: <Params:Behaviors>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Behavior of ring 'skill'. Always zero in the vanilla game.
        /// </summary>
        public int Behavior
        {
            get => Convert.ToInt32(Row["behaviorId"].Value);
            set => Row["behaviorId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown purpose, and unused.
        /// </summary>
        public int BasicCost
        {
            get => Convert.ToInt32(Row["basicPrice"].Value);
            set => Row["basicPrice"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of souls received when fed to Frampt. (Set to -1 to prevent it
        /// from being sold.
        /// </summary>
        public int FramptSellValue
        {
            get => Convert.ToInt32(Row["sellValue"].Value);
            set => Row["sellValue"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Index for automatic inventory sorting.
        /// </summary>
        public int SortIndex
        {
            get => Convert.ToInt32(Row["sortId"].Value);
            set => Row["sortId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unused world tendency remnant.
        /// </summary>
        public int QWCID
        {
            get => Convert.ToInt32(Row["qwcId"].Value);
            set => Row["qwcId"].Value = value;
        }
        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero. (Rings have no model, presumably.)
        /// </summary>
        public ushort EquipmentModel
        {
            get => Convert.ToUInt16(Row["equipModelId"].Value);
            set => Row["equipModelId"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Icon ID of ring in menu.
        /// </summary>
        public ushort MenuIcon
        {
            get => Convert.ToUInt16(Row["iconId"].Value);
            set => Row["iconId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'Level that can be solved in the shop.' Unknown
        /// and unused (rings have no level).
        /// </summary>
        public short ShopLevel
        {
            get => Convert.ToInt16(Row["shopLv"].Value);
            set => Row["shopLv"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Index of ring as it contributes to certain multi-item achievements
        /// (none for rings).
        /// </summary>
        public short AchievementContributionID
        {
            get => Convert.ToInt16(Row["trophySGradeId"].Value);
            set => Row["trophySGradeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Achievement unlocked when ring is acquired (Covenant of Artorias).
        /// </summary>
        public short AchievementUnlockID
        {
            get => Convert.ToInt16(Row["trophySeqId"].Value);
            set => Row["trophySeqId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte EquipmentModelCategory
        {
            get => Convert.ToByte(Row["equipModelCategory"].Value);
            set => Row["equipModelCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte EquipmentModelGender
        {
            get => Convert.ToByte(Row["equipModelGender"].Value);
            set => Row["equipModelGender"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte AccessoryCategory
        {
            get => Convert.ToByte(Row["accessoryCategory"].Value);
            set => Row["accessoryCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always set to Special Effects. No idea what happens if you set it to
        /// Attacks for a ring...
        /// </summary>
        public byte ReferenceType
        {
            get => Convert.ToByte(Row["refCategory"].Value);
            set => Row["refCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines what type of special effects affect the stats of this
        /// equipment. Unused for rings.
        /// </summary>
        public byte SpecialEffectCategory
        {
            get => Convert.ToByte(Row["spEffectCategory"].Value);
            set => Row["spEffectCategory"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantItemLot
        {
            get => Convert.ToInt32(Row["vagrantItemLotId"].Value);
            set => Row["vagrantItemLotId"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantBonusEnemyDropItemLot
        {
            get => Convert.ToInt32(Row["vagrantBonusEneDropItemLotId"].Value);
            set => Row["vagrantBonusEneDropItemLotId"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantItemEnemyDropItemLot
        {
            get => Convert.ToInt32(Row["vagrantItemEneDropItemLotId"].Value);
            set => Row["vagrantItemEneDropItemLotId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this ring can be stored in the Bottomless Box. Always True
        /// for rings.
        /// </summary>
        public bool CanBeStored
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDeposit"].Value));
            set => Row["isDeposit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this ring will break when it is unequipped (e.g. Ring of
        /// Favor and Protection).
        /// </summary>
        public bool BreaksWhenUnequipped
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEquipOutBrake"].Value));
            set => Row["isEquipOutBrake"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this ring cannot be given to other players by dropping it.
        /// Always False in vanilla.
        /// </summary>
        public bool DisableMultiplayerShare
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableMultiDropShare"].Value));
            set => Row["disableMultiDropShare"].Value = value;
        }
    }
}
