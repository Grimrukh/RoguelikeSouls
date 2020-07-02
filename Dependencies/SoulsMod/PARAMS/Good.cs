using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Good : RowWrapper
    {
        public Good() { }
        public Good(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public new string Name
        {
            get => Text.GoodsNames[ID];
            set
            {
                Row.Name = value;
                Text.GoodsNames[ID] = value;
            }
        }

        public string Summary
        {
            get => Text.GoodsDescriptions[ID];
            set => Text.GoodsDescriptions[ID] = value;
        }

        public string Description
        {
            get => Text.GoodsLongDescriptions[ID];
            set => Text.GoodsLongDescriptions[ID] = value;
        }

        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
        public int RefID
        {
            get => Convert.ToInt32(Row["refId"].Value);
            set => Row["refId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation variation ID to combine with the base usage animation.
        /// </summary>
        public int AnimationVariationID
        {
            get => Convert.ToInt32(Row["sfxVariationId"].Value);
            set => Row["sfxVariationId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Weight of good. Never used in vanilla Dark Souls.
        /// </summary>
        public float Weight
        {
            get => Convert.ToSingle(Row["weight"].Value);
            set => Row["weight"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unsure. Does not appear to be used.
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
        // LINK_STRING: <Params:Behaviors>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Behavior triggered by good use. Never used.
        /// </summary>
        public int Behavior
        {
            get => Convert.ToInt32(Row["behaviorId"].Value);
            set => Row["behaviorId"].Value = value;
        }
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good to replace when this item is obtained. Used only for full/empty
        /// Estus Flask exchange.
        /// </summary>
        public int GoodToReplace
        {
            get => Convert.ToInt32(Row["replaceItemId"].Value);
            set => Row["replaceItemId"].Value = value;
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
        // LINK_STRING: <Text:EventText>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Message displayed in yes/no dialog box to confirm use of good.
        /// </summary>
        public int ConfirmationMessage
        {
            get => Convert.ToInt32(Row["yesNoDialogMessageId"].Value);
            set => Row["yesNoDialogMessageId"].Value = value;
        }
        // LINK_STRING: <Params:Spells>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Spell unlocked in attunement menu by possession of this good. (Usually
        /// matches the good ID.)
        /// </summary>
        public int Spell
        {
            get => Convert.ToInt32(Row["magicId"].Value);
            set => Row["magicId"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good icon texture ID.
        /// </summary>
        public ushort GoodIcon
        {
            get => Convert.ToUInt16(Row["iconId"].Value);
            set => Row["iconId"].Value = value;
        }
        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Model of good. Never used.
        /// </summary>
        public ushort ModelID
        {
            get => Convert.ToUInt16(Row["modelId"].Value);
            set => Row["modelId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Level of good that can be sold in 'the shop'. Always -1 or 0. Probably
        /// unused.
        /// </summary>
        public short ShopLevel
        {
            get => Convert.ToInt16(Row["shopLv"].Value);
            set => Row["shopLv"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Collection achievement (e.g. all spells) to which obtaining this good
        /// contributes.
        /// </summary>
        public short CollectionAchievementID
        {
            get => Convert.ToInt16(Row["compTrophySedId"].Value);
            set => Row["compTrophySedId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Achievement unlocked when this good is first obtained (e.g. Estus
        /// Flask).
        /// </summary>
        public short AchievementID
        {
            get => Convert.ToInt16(Row["trophySeqId"].Value);
            set => Row["trophySeqId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum number of good that can be held at once.
        /// </summary>
        public short MaxHoldQuantity
        {
            get => Convert.ToInt16(Row["maxNum"].Value);
            set => Row["maxNum"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Humanity cost of using good. Always zero.
        /// </summary>
        public byte HumanityCost
        {
            get => Convert.ToByte(Row["consumeHeroPoint"].Value);
            set => Row["consumeHeroPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// 'Skill over start value'. Unknown effect; set to 0 for spells and 50
        /// otherwise.
        /// </summary>
        public byte OverDexterity
        {
            get => Convert.ToByte(Row["overDexterity"].Value);
            set => Row["overDexterity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this is a basic good, upgrade material, key item, or
        /// spell.
        /// </summary>
        public byte GoodType
        {
            get => Convert.ToByte(Row["goodsType"].Value);
            set => Row["goodsType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if this good triggers a Bullet or Special Effect. (Attacks
        /// are possible, but unused.)
        /// </summary>
        public byte ReferenceType
        {
            get => Convert.ToByte(Row["refCategory"].Value);
            set => Row["refCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines compatibility with special effects that affect certain
        /// types of attacks. Set to 'Basic' for thrown goods and 'No Category'
        /// otherwise.
        /// </summary>
        public byte SpecialEffectCategory
        {
            get => Convert.ToByte(Row["spEffectCategory"].Value);
            set => Row["spEffectCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Never used. Only one value (0) used.
        /// </summary>
        public byte GoodCategory
        {
            get => Convert.ToByte(Row["goodsCategory"].Value);
            set => Row["goodsCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Points to basic animation used when good is used. Visual/sound effects
        /// are set by the variation ID.
        /// </summary>
        public byte UseAnimation
        {
            get => Convert.ToByte(Row["goodsUseAnim"].Value);
            set => Row["goodsUseAnim"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Menu activated (if any) when good is used. Generally only 'No Menu' or
        /// 'Yes or No Menu' will be useful.
        /// </summary>
        public byte MenuActivated
        {
            get => Convert.ToByte(Row["opmeMenuType"].Value);
            set => Row["opmeMenuType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Only one good-triggered special effect with this category can be
        /// active at once. Additional attempts to use goods in this category will
        /// be prevented. (Unclear how Dragon Stones work, though.)
        /// </summary>
        public byte LimitCategory
        {
            get => Convert.ToByte(Row["useLimitCategory"].Value);
            set => Row["useLimitCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// The special effect triggered by this good will replace any special
        /// effects in the same category as this one. Used only by Dragon Stones.
        /// </summary>
        public byte ReplaceCategory
        {
            get => Convert.ToByte(Row["replaceCategory"].Value);
            set => Row["replaceCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters with no covenant.
        /// </summary>
        public bool UseableByNoCovenant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType0"].Value));
            set => Row["vowType0"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Way of White.
        /// </summary>
        public bool UseableByWayOfWhite
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType1"].Value));
            set => Row["vowType1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Princess's
        /// Guard.
        /// </summary>
        public bool UseableByPrincessGuard
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType2"].Value));
            set => Row["vowType2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Warriors of
        /// Sunlight.
        /// </summary>
        public bool UseableByWarriorsOfSunlight
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType3"].Value));
            set => Row["vowType3"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Darkwraith
        /// covenant.
        /// </summary>
        public bool UseableByDarkwraith
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType4"].Value));
            set => Row["vowType4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Path of the
        /// Dragon.
        /// </summary>
        public bool UseableByPathOfTheDragon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType5"].Value));
            set => Row["vowType5"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Gravelord
        /// Servants.
        /// </summary>
        public bool UseableByGravelordServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType6"].Value));
            set => Row["vowType6"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Forest
        /// Hunters.
        /// </summary>
        public bool UseableByForestHunter
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType7"].Value));
            set => Row["vowType7"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Blades of the
        /// Darkmoon.
        /// </summary>
        public bool UseableByDarkmoonBlade
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType8"].Value));
            set => Row["vowType8"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters in the Chaos Servant
        /// covenant.
        /// </summary>
        public bool UseableByChaosServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType9"].Value));
            set => Row["vowType9"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 10.
        /// </summary>
        public bool UseableByCovenant10
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType10"].Value));
            set => Row["vowType10"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 11.
        /// </summary>
        public bool UseableByCovenant11
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType11"].Value));
            set => Row["vowType11"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 12.
        /// </summary>
        public bool UseableByCovenant12
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType12"].Value));
            set => Row["vowType12"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 13.
        /// </summary>
        public bool UseableByCovenant13
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType13"].Value));
            set => Row["vowType13"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 14.
        /// </summary>
        public bool UseableByCovenant14
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType14"].Value));
            set => Row["vowType14"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this good can be used by characters in unused covenant
        /// 15.
        /// </summary>
        public bool UseableByCovenant15
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType15"].Value));
            set => Row["vowType15"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters who have revived to
        /// Human status.
        /// </summary>
        public bool UseableByHumans
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_live"].Value));
            set => Row["enable_live"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by characters who are Hollow.
        /// </summary>
        public bool UseableByHollows
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_gray"].Value));
            set => Row["enable_gray"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by White Phantoms (summons).
        /// </summary>
        public bool UseableByWhitePhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_white"].Value));
            set => Row["enable_white"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used by Black Phantoms (invaders).
        /// </summary>
        public bool UseableByBlackPhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_black"].Value));
            set => Row["enable_black"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used while multiple players are
        /// together.
        /// </summary>
        public bool UseableInMultiplayer
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_multi"].Value));
            set => Row["enable_multi"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// <DSR> Determines if this good can be used in 'PVP' multiplayer. Not
        /// sure exactly what that refers to.
        /// </summary>
        public bool UseableInPVP
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_pvp"].Value));
            set => Row["enable_pvp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be used while the game is disconnected
        /// from the network.
        /// </summary>
        public bool DisabledOffline
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disable_offline"].Value));
            set => Row["disable_offline"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good can be equipped in a quick item slot.
        /// </summary>
        public bool CanBeEquipped
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEquip"].Value));
            set => Row["isEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good is consumed (count decreases) when used.
        /// </summary>
        public bool ConsumedOnUse
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isConsume"].Value));
            set => Row["isConsume"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this good will be equipped in an available quick slot
        /// when obtained.
        /// </summary>
        public bool AutomaticallyEquipped
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isAutoEquip"].Value));
            set => Row["isAutoEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unknown; need to look at usage.
        /// </summary>
        public bool IsStationary
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEstablishment"].Value));
            set => Row["isEstablishment"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if only one of this good exists in the game.
        /// </summary>
        public bool IsUnique
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isOnlyOne"].Value));
            set => Row["isOnlyOne"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this item can be dropped.
        /// </summary>
        public bool CanBeDropped
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDrop"].Value));
            set => Row["isDrop"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if good can be stored in Bottomless Box.
        /// </summary>
        public bool CanBeStored
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDeposit"].Value));
            set => Row["isDeposit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Not sure. Could disable model hand when good is used?
        /// </summary>
        public bool IsDisableHand
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDisableHand"].Value));
            set => Row["isDisableHand"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Not sure. Could flag items that warp the player.
        /// </summary>
        public bool IsTravelItem
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["IsTravelItem"].Value));
            set => Row["IsTravelItem"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Not sure. Only enabled for empty Estus Flask.
        /// </summary>
        public bool IsEmptyEstusFlask
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isSuppleItem"].Value));
            set => Row["isSuppleItem"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Not sure. Only enabled for non-empty Estus Flask.
        /// </summary>
        public bool IsNonEmptyEstusFlask
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isFullSuppleItem"].Value));
            set => Row["isFullSuppleItem"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this is an upgrade material.
        /// </summary>
        public bool IsUpgradeMaterial
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEnhance"].Value));
            set => Row["isEnhance"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Probably True for Repair Powder, etc.
        /// </summary>
        public bool IsFixItem
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isFixItem"].Value));
            set => Row["isFixItem"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this good cannot be given to other players by dropping it.
        /// </summary>
        public bool DisableMultiplayerShare
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableMultiDropShare"].Value));
            set => Row["disableMultiDropShare"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this good cannot be used in the PvP Arena in Oolacile.
        /// </summary>
        public bool DisabledInArena
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableUseAtColiseum"].Value));
            set => Row["disableUseAtColiseum"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this good cannot be used outside the PvP Arena in Oolacile.
        /// </summary>
        public bool DisabledOutsideArena
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableUseAtOutOfColiseum"].Value));
            set => Row["disableUseAtOutOfColiseum"].Value = value;
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
    }
}
