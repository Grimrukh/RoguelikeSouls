using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Magic : RowWrapper
    {
        public Magic() { }
        public Magic(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public new string Name
        {
            get => Text.MagicNames[ID];
            set
            {
                Row.Name = value;
                Text.MagicNames[ID] = value;
            }
        }

        public string Summary
        {
            get => Text.MagicDescriptions[ID];
            set => Text.MagicDescriptions[ID] = value;
        }

        public string Description
        {
            get => Text.MagicLongDescriptions[ID];
            set => Text.MagicLongDescriptions[ID] = value;
        }

        // LINK_STRING: <Text:EventText>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Message displayed in yes/no dialog box to confirm use of spell.
        /// Requires the Yes/No menu type.
        /// </summary>
        public int ConfirmationMessage
        {
            get => Convert.ToInt32(Row["yesNoDialogMessageId"].Value);
            set => Row["yesNoDialogMessageId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Never used.
        /// </summary>
        public int LimitCancelSpecialEffect
        {
            get => Convert.ToInt32(Row["limitCancelSpEffectId"].Value);
            set => Row["limitCancelSpEffectId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Index for automatic inventory sorting.
        /// </summary>
        public short SortIndex
        {
            get => Convert.ToInt16(Row["sortId"].Value);
            set => Row["sortId"].Value = value;
        }
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
        public short Refid
        {
            get => Convert.ToInt16(Row["refId"].Value);
            set => Row["refId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// MP cost of spell. Unused in Dark Souls 1 (always zero).
        /// </summary>
        public short MPCost
        {
            get => Convert.ToInt16(Row["mp"].Value);
            set => Row["mp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Stamina cost of spell. Always zero.
        /// </summary>
        public short StaminaCost
        {
            get => Convert.ToInt16(Row["stamina"].Value);
            set => Row["stamina"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Spell icon texture for inventory and equipped slot.
        /// </summary>
        public short SpellIcon
        {
            get => Convert.ToInt16(Row["iconId"].Value);
            set => Row["iconId"].Value = value;
        }
        // LINK_STRING: <Params:Behaviors>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Behavior triggered by spell. Never used.
        /// </summary>
        public short Behavior
        {
            get => Convert.ToInt16(Row["behaviorId"].Value);
            set => Row["behaviorId"].Value = value;
        }
        // LINK_STRING: <Params:Goods>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Good required for use. Never used (usability is handled in Shops
        /// parameters).
        /// </summary>
        public short RequiredGood
        {
            get => Convert.ToInt16(Row["mtrlItemId"].Value);
            set => Row["mtrlItemId"].Value = value;
        }
        // LINK_STRING: <Params:Spells>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Spell to replace 'when the state change matches'. Never used.
        /// </summary>
        public short ReplaceSpell
        {
            get => Convert.ToInt16(Row["replaceMagicId"].Value);
            set => Row["replaceMagicId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of spell casts. Note that some spells consume multiple casts
        /// per use (e.g. Firestorm).
        /// </summary>
        public short BaseCastCount
        {
            get => Convert.ToInt16(Row["maxQuantity"].Value);
            set => Row["maxQuantity"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Soft humanity consumed when casting spell. Never used.
        /// </summary>
        public byte HumanityCost
        {
            get => Convert.ToByte(Row["heroPoint"].Value);
            set => Row["heroPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown effect. Always 99.
        /// </summary>
        public byte OverDexterity
        {
            get => Convert.ToByte(Row["overDexterity"].Value);
            set => Row["overDexterity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect variation. (I believe this alters the animation ID used
        /// for casting.)
        /// </summary>
        public sbyte VisualEffectVariation
        {
            get => Convert.ToSByte(Row["sfxVariationId"].Value);
            set => Row["sfxVariationId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of attunement slots required to attune spell.
        /// </summary>
        public byte AttunementSlotsUsed
        {
            get => Convert.ToByte(Row["slotLength"].Value);
            set => Row["slotLength"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum intelligence required to cast spell.
        /// </summary>
        public byte RequiredIntelligence
        {
            get => Convert.ToByte(Row["requirementIntellect"].Value);
            set => Row["requirementIntellect"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum faith required to cast spell.
        /// </summary>
        public byte RequiredFaith
        {
            get => Convert.ToByte(Row["requirementFaith"].Value);
            set => Row["requirementFaith"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Dexterity value where casting speed starts to be affected (I think).
        /// This is always 20, but apparently speed isn't actually affected until
        /// dexterity is 35.
        /// </summary>
        public byte MinDexterityForBonus
        {
            get => Convert.ToByte(Row["analogDexiterityMin"].Value);
            set => Row["analogDexiterityMin"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Dexterity value where casting speed stops being further affected (I
        /// think). Always 45, which is consistent with the observed dexterity
        /// cap.
        /// </summary>
        public byte MaxDexterityForBonus
        {
            get => Convert.ToByte(Row["analogDexiterityMax"].Value);
            set => Row["analogDexiterityMax"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of spell.
        /// </summary>
        public byte SpellCategory
        {
            get => Convert.ToByte(Row["ezStateBehaviorType"].Value);
            set => Row["ezStateBehaviorType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell triggers a Bullet or Special Effect.
        /// ('Default' is never used, but probably triggers an Attack, which is
        /// unlikely to be useful to you.)
        /// </summary>
        public byte ReferenceType
        {
            get => Convert.ToByte(Row["refCategory"].Value);
            set => Row["refCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines what type of special effects affect the stats of this
        /// spell. (Vanilla game uses 3 for sorceries and pyromancies, and 4 for
        /// miracles.)
        /// </summary>
        public byte SpecialEffectCategory
        {
            get => Convert.ToByte(Row["spEffectCategory"].Value);
            set => Row["spEffectCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Basic animation type when casting spell. The Visual Effect Variation
        /// field further refines it.
        /// </summary>
        public byte AnimationType
        {
            get => Convert.ToByte(Row["refType"].Value);
            set => Row["refType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Menu activated (if any) when spell is cast. Only used by Homeward
        /// (Yes/No Dialog).
        /// </summary>
        public byte MenuActivated
        {
            get => Convert.ToByte(Row["opmeMenuType"].Value);
            set => Row["opmeMenuType"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines 'the state change that needs to replace the spell ID'.
        /// Never used.
        /// </summary>
        public byte HasSpecialEffectType
        {
            get => Convert.ToByte(Row["hasSpEffectType"].Value);
            set => Row["hasSpEffectType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines which existing effects this spell will replace. Only used
        /// for a few spells.
        /// </summary>
        public byte ReplaceCategory
        {
            get => Convert.ToByte(Row["replaceCategory"].Value);
            set => Row["replaceCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Only one special effect with this category can be active at once.
        /// Additional attempts to cast spells (or use goods) in this category
        /// will be prevented.
        /// </summary>
        public byte LimitCategory
        {
            get => Convert.ToByte(Row["useLimitCategory"].Value);
            set => Row["useLimitCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters with no covenant.
        /// </summary>
        public bool UseableByNoCovenant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType0"].Value));
            set => Row["vowType0"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Way of
        /// White.
        /// </summary>
        public bool UseableByWayOfWhite
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType1"].Value));
            set => Row["vowType1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Princess's
        /// Guard.
        /// </summary>
        public bool UseableByPrincessGuard
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType2"].Value));
            set => Row["vowType2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Warriors of
        /// Sunlight.
        /// </summary>
        public bool UseableByWarriorsOfSunlight
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType3"].Value));
            set => Row["vowType3"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Darkwraith
        /// covenant.
        /// </summary>
        public bool UseableByDarkwraith
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType4"].Value));
            set => Row["vowType4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Path of the
        /// Dragon.
        /// </summary>
        public bool UseableByPathOfTheDragon
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType5"].Value));
            set => Row["vowType5"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Gravelord
        /// Servants.
        /// </summary>
        public bool UseableByGravelordServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType6"].Value));
            set => Row["vowType6"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Forest
        /// Hunters.
        /// </summary>
        public bool UseableByForestHunter
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType7"].Value));
            set => Row["vowType7"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast while multiple players are
        /// together. Only disabled for Homeward in vanilla game.
        /// </summary>
        public bool UseableInMultiplayer
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_multi"].Value));
            set => Row["enable_multi"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can ONLY be cast while multiple players are
        /// together. Always False.
        /// </summary>
        public bool DisabledOutsideMultiplayer
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_multi_only"].Value));
            set => Row["enable_multi_only"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if this spell buffs your weapon.
        /// </summary>
        public bool IsWeaponBuff
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEnchant"].Value));
            set => Row["isEnchant"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Indicates if this spell buffs your shield.
        /// </summary>
        public bool IsShieldBuff
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isShieldEnchant"].Value));
            set => Row["isShieldEnchant"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by players who have revived to
        /// human.
        /// </summary>
        public bool UseableByHumans
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_live"].Value));
            set => Row["enable_live"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by players who have NOT revived
        /// to human.
        /// </summary>
        public bool UseableByHollows
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_gray"].Value));
            set => Row["enable_gray"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by White Phantoms (summons). Only
        /// disabled for Homeward and the unused Escape Death miracle in vanilla
        /// game.
        /// </summary>
        public bool UseableByWhitePhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_white"].Value));
            set => Row["enable_white"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by Black Phantoms (invaders).
        /// Only disabled for Homeward and the unused Escape Death miracle in
        /// vanilla game.
        /// </summary>
        public bool UseableByBlackPhantoms
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enable_black"].Value));
            set => Row["enable_black"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this spell cannot be cast without a network connection.
        /// Always False.
        /// </summary>
        public bool DisabledOffline
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableOffline"].Value));
            set => Row["disableOffline"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, using this spell will create a resonance ring to help players
        /// in other worlds.
        /// </summary>
        public bool CreateResonanceRing
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["castResonanceMagic"].Value));
            set => Row["castResonanceMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Blades of
        /// the Darkmoon.
        /// </summary>
        public bool UseableByDarkmoonBlade
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType8"].Value));
            set => Row["vowType8"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this spell can be cast by characters in the Chaos
        /// Servant covenant.
        /// </summary>
        public bool UseableByChaosServant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType9"].Value));
            set => Row["vowType9"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 10.
        /// </summary>
        public bool UseableByCovenant10
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType10"].Value));
            set => Row["vowType10"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 11.
        /// </summary>
        public bool UseableByCovenant11
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType11"].Value));
            set => Row["vowType11"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 12.
        /// </summary>
        public bool UseableByCovenant12
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType12"].Value));
            set => Row["vowType12"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 13.
        /// </summary>
        public bool UseableByCovenant13
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType13"].Value));
            set => Row["vowType13"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 14.
        /// </summary>
        public bool UseableByCovenant14
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType14"].Value));
            set => Row["vowType14"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Determines if this spell can be cast by characters in unused covenant
        /// 15.
        /// </summary>
        public bool UseableByCovenant15
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["vowType15"].Value));
            set => Row["vowType15"].Value = value;
        }
    }
}