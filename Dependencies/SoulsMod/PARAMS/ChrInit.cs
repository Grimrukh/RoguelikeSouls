using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class ChrInit : RowWrapper
    {
        public ChrInit() { }
        public ChrInit(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown.
        /// </summary>
        public float BaseRecMP
        {
            get => Convert.ToSingle(Row["baseRec_mp"].Value);
            set => Row["baseRec_mp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown.
        /// </summary>
        public float BaseRecSP
        {
            get => Convert.ToSingle(Row["baseRec_sp"].Value);
            set => Row["baseRec_sp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown.
        /// </summary>
        public float RedFallDamage
        {
            get => Convert.ToSingle(Row["red_Falldam"].Value);
            set => Row["red_Falldam"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Starting soul count of character.
        /// </summary>
        public int SoulCount
        {
            get => Convert.ToInt32(Row["soul"].Value);
            set => Row["soul"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First (default) weapon/shield equipped in right hand.
        /// </summary>
        public int RightHandWeapon1
        {
            get => Convert.ToInt32(Row["equip_Wep_Right"].Value);
            set => Row["equip_Wep_Right"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Second weapon/shield equipped in right hand.
        /// </summary>
        public int RightHandWeapon2
        {
            get => Convert.ToInt32(Row["equip_Subwep_Right"].Value);
            set => Row["equip_Subwep_Right"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First (default) weapon/shield equipped in left hand.
        /// </summary>
        public int LeftHandWeapon1
        {
            get => Convert.ToInt32(Row["equip_Wep_Left"].Value);
            set => Row["equip_Wep_Left"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Second weapon/shield equipped in left hand.
        /// </summary>
        public int LeftHandWeapon2
        {
            get => Convert.ToInt32(Row["equip_Subwep_Left"].Value);
            set => Row["equip_Subwep_Left"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Armor equipped to head.
        /// </summary>
        public int HeadArmor
        {
            get => Convert.ToInt32(Row["equip_Helm"].Value);
            set => Row["equip_Helm"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Armor equipped to body.
        /// </summary>
        public int BodyArmor
        {
            get => Convert.ToInt32(Row["equip_Armer"].Value);
            set => Row["equip_Armer"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Armor equipped to hands.
        /// </summary>
        public int ArmsArmor
        {
            get => Convert.ToInt32(Row["equip_Gaunt"].Value);
            set => Row["equip_Gaunt"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Armor equipped to legs.
        /// </summary>
        public int LegsArmor
        {
            get => Convert.ToInt32(Row["equip_Leg"].Value);
            set => Row["equip_Leg"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Arrows equipped in slot 1.
        /// </summary>
        public int ArrowSlot1
        {
            get => Convert.ToInt32(Row["equip_Arrow"].Value);
            set => Row["equip_Arrow"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bolts equipped in slot 1.
        /// </summary>
        public int BoltSlot1
        {
            get => Convert.ToInt32(Row["equip_Bolt"].Value);
            set => Row["equip_Bolt"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Arrows equipped in slot 2.
        /// </summary>
        public int ArrowSlot2
        {
            get => Convert.ToInt32(Row["equip_SubArrow"].Value);
            set => Row["equip_SubArrow"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bolts equipped in slot 2.
        /// </summary>
        public int BoltSlot2
        {
            get => Convert.ToInt32(Row["equip_SubBolt"].Value);
            set => Row["equip_SubBolt"].Value = value;
        }
        // LINK_STRING: <Params:Rings>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First ring equipped. Note that up to five rings can be equipped to
        /// human NPCs.
        /// </summary>
        public int RingSlot1
        {
            get => Convert.ToInt32(Row["equip_Accessory01"].Value);
            set => Row["equip_Accessory01"].Value = value;
        }
        // LINK_STRING: <Params:Rings>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Second ring equipped. Note that up to five rings can be equipped to
        /// human NPCs.
        /// </summary>
        public int RingSlot2
        {
            get => Convert.ToInt32(Row["equip_Accessory02"].Value);
            set => Row["equip_Accessory02"].Value = value;
        }
        // LINK_STRING: <Params:Rings>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Third ring equipped. Note that up to five rings can be equipped to
        /// human NPCs.
        /// </summary>
        public int RingSlot3
        {
            get => Convert.ToInt32(Row["equip_Accessory03"].Value);
            set => Row["equip_Accessory03"].Value = value;
        }
        // LINK_STRING: <Params:Rings>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fourth ring equipped. Note that up to five rings can be equipped to
        /// human NPCs.
        /// </summary>
        public int RingSlot4
        {
            get => Convert.ToInt32(Row["equip_Accessory04"].Value);
            set => Row["equip_Accessory04"].Value = value;
        }
        // LINK_STRING: <Params:Rings>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fifth ring equipped. Note that up to five rings can be equipped to
        /// human NPCs.
        /// </summary>
        public int RingSlot5
        {
            get => Convert.ToInt32(Row["equip_Accessory05"].Value);
            set => Row["equip_Accessory05"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// </summary>
        public int SkillSlot1
        {
            get => Convert.ToInt32(Row["equip_Skill_01"].Value);
            set => Row["equip_Skill_01"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// </summary>
        public int SkillSlot2
        {
            get => Convert.ToInt32(Row["equip_Skill_02"].Value);
            set => Row["equip_Skill_02"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// </summary>
        public int SkillSlot3
        {
            get => Convert.ToInt32(Row["equip_Skill_03"].Value);
            set => Row["equip_Skill_03"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First spell equipped.
        /// </summary>
        public int SpellSlot1
        {
            get => Convert.ToInt32(Row["equip_Spell_01"].Value);
            set => Row["equip_Spell_01"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Second spell equipped.
        /// </summary>
        public int SpellSlot2
        {
            get => Convert.ToInt32(Row["equip_Spell_02"].Value);
            set => Row["equip_Spell_02"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Third spell equipped.
        /// </summary>
        public int SpellSlot3
        {
            get => Convert.ToInt32(Row["equip_Spell_03"].Value);
            set => Row["equip_Spell_03"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fourth spell equipped.
        /// </summary>
        public int SpellSlot4
        {
            get => Convert.ToInt32(Row["equip_Spell_04"].Value);
            set => Row["equip_Spell_04"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fifth spell equipped.
        /// </summary>
        public int SpellSlot5
        {
            get => Convert.ToInt32(Row["equip_Spell_05"].Value);
            set => Row["equip_Spell_05"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sixth spell equipped.
        /// </summary>
        public int SpellSlot6
        {
            get => Convert.ToInt32(Row["equip_Spell_06"].Value);
            set => Row["equip_Spell_06"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Seventh spell equipped.
        /// </summary>
        public int SpellSlot7
        {
            get => Convert.ToInt32(Row["equip_Spell_07"].Value);
            set => Row["equip_Spell_07"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 1.
        /// </summary>
        public int GoodSlot1
        {
            get => Convert.ToInt32(Row["item_01"].Value);
            set => Row["item_01"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 2.
        /// </summary>
        public int GoodSlot2
        {
            get => Convert.ToInt32(Row["item_02"].Value);
            set => Row["item_02"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 3.
        /// </summary>
        public int GoodSlot3
        {
            get => Convert.ToInt32(Row["item_03"].Value);
            set => Row["item_03"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 4.
        /// </summary>
        public int GoodSlot4
        {
            get => Convert.ToInt32(Row["item_04"].Value);
            set => Row["item_04"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 5.
        /// </summary>
        public int GoodSlot5
        {
            get => Convert.ToInt32(Row["item_05"].Value);
            set => Row["item_05"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 6.
        /// </summary>
        public int GoodSlot6
        {
            get => Convert.ToInt32(Row["item_06"].Value);
            set => Row["item_06"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 7.
        /// </summary>
        public int GoodSlot7
        {
            get => Convert.ToInt32(Row["item_07"].Value);
            set => Row["item_07"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 8.
        /// </summary>
        public int GoodSlot8
        {
            get => Convert.ToInt32(Row["item_08"].Value);
            set => Row["item_08"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 9.
        /// </summary>
        public int GoodSlot9
        {
            get => Convert.ToInt32(Row["item_09"].Value);
            set => Row["item_09"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Good (item) equipped in slot 10.
        /// </summary>
        public int GoodSlot10
        {
            get => Convert.ToInt32(Row["item_10"].Value);
            set => Row["item_10"].Value = value;
        }
        // LINK_STRING: <Params:Faces>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Face parameter ID (NPCs only).
        /// </summary>
        public int FaceID
        {
            get => Convert.ToInt32(Row["npcPlayerFaceGenId"].Value);
            set => Row["npcPlayerFaceGenId"].Value = value;
        }
        // LINK_STRING: <Params:AI>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Default AI (NPCs only).
        /// </summary>
        public int DefaultAI
        {
            get => Convert.ToInt32(Row["npcPlayerThinkId"].Value);
            set => Row["npcPlayerThinkId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base amount of maximum HP (excluding effects of vitality).
        /// </summary>
        public ushort BaseMaxHP
        {
            get => Convert.ToUInt16(Row["baseHp"].Value);
            set => Row["baseHp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Base amount of maximum MP (unused in Dark Souls).
        /// </summary>
        public ushort BaseMaxMP
        {
            get => Convert.ToUInt16(Row["baseMp"].Value);
            set => Row["baseMp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base maximum stamina (excluding effects of endurance).
        /// </summary>
        public ushort BaseMaxStamina
        {
            get => Convert.ToUInt16(Row["baseSp"].Value);
            set => Row["baseSp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of arrows equipped in slot 1.
        /// </summary>
        public ushort ArrowSlot1Count
        {
            get => Convert.ToUInt16(Row["arrowNum"].Value);
            set => Row["arrowNum"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of arrows equipped in slot 2.
        /// </summary>
        public ushort BoltSlot1Count
        {
            get => Convert.ToUInt16(Row["boltNum"].Value);
            set => Row["boltNum"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of bolts equipped in slot 1.
        /// </summary>
        public ushort ArrowSlot2Count
        {
            get => Convert.ToUInt16(Row["subArrowNum"].Value);
            set => Row["subArrowNum"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of bolts equipped in slot 2.
        /// </summary>
        public ushort BoltSlot2Count
        {
            get => Convert.ToUInt16(Row["subBoltNum"].Value);
            set => Row["subBoltNum"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Likely to be unused world tendency effect.
        /// </summary>
        public short QWC_SB
        {
            get => Convert.ToInt16(Row["QWC_sb"].Value);
            set => Row["QWC_sb"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Likely to be unused world tendency effect.
        /// </summary>
        public short QWC_MW
        {
            get => Convert.ToInt16(Row["QWC_mw"].Value);
            set => Row["QWC_mw"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Likely to be unused world tendency effect.
        /// </summary>
        public short QWC_CD
        {
            get => Convert.ToInt16(Row["QWC_cd"].Value);
            set => Row["QWC_cd"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Soul level, independent of actual stats. Determines amount of souls
        /// rewarded by human NPCs.
        /// </summary>
        public short SoulLevel
        {
            get => Convert.ToInt16(Row["soulLv"].Value);
            set => Row["soulLv"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base vitality level. Determines maximum health.
        /// </summary>
        public byte Vitality
        {
            get => Convert.ToByte(Row["baseVit"].Value);
            set => Row["baseVit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base attunement level. Determines spell slots and casting speed.
        /// </summary>
        public byte Attunement
        {
            get => Convert.ToByte(Row["baseWil"].Value);
            set => Row["baseWil"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base endurance level. Determines maximum stamina and equip load.
        /// </summary>
        public byte Endurance
        {
            get => Convert.ToByte(Row["baseEnd"].Value);
            set => Row["baseEnd"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base strength level. Affects strength-based weapons and damage.
        /// </summary>
        public byte Strength
        {
            get => Convert.ToByte(Row["baseStr"].Value);
            set => Row["baseStr"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base dexterity level. Affects skill-based weapons and damage.
        /// </summary>
        public byte Dexterity
        {
            get => Convert.ToByte(Row["baseDex"].Value);
            set => Row["baseDex"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base intelligence level. Affects magic usability and effectiveness.
        /// </summary>
        public byte Intelligence
        {
            get => Convert.ToByte(Row["baseMag"].Value);
            set => Row["baseMag"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base faith level. Affects miracle usability and effectiveness.
        /// </summary>
        public byte Faith
        {
            get => Convert.ToByte(Row["baseFai"].Value);
            set => Row["baseFai"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base luck level. Improves chances of rare item drops.
        /// </summary>
        public byte Luck
        {
            get => Convert.ToByte(Row["baseLuc"].Value);
            set => Row["baseLuc"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base 'soft' humanity.
        /// </summary>
        public byte Humanity
        {
            get => Convert.ToByte(Row["baseHeroPoint"].Value);
            set => Row["baseHeroPoint"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base resistance level. Improves resistances to status ailments.
        /// </summary>
        public byte Resistance
        {
            get => Convert.ToByte(Row["baseDurability"].Value);
            set => Row["baseDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 1.
        /// </summary>
        public byte GoodSlot1Count
        {
            get => Convert.ToByte(Row["itemNum_01"].Value);
            set => Row["itemNum_01"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 2.
        /// </summary>
        public byte GoodSlot2Count
        {
            get => Convert.ToByte(Row["itemNum_02"].Value);
            set => Row["itemNum_02"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 3.
        /// </summary>
        public byte GoodSlot3Count
        {
            get => Convert.ToByte(Row["itemNum_03"].Value);
            set => Row["itemNum_03"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 4.
        /// </summary>
        public byte GoodSlot4Count
        {
            get => Convert.ToByte(Row["itemNum_04"].Value);
            set => Row["itemNum_04"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 5.
        /// </summary>
        public byte GoodSlot5Count
        {
            get => Convert.ToByte(Row["itemNum_05"].Value);
            set => Row["itemNum_05"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 6.
        /// </summary>
        public byte GoodSlot6Count
        {
            get => Convert.ToByte(Row["itemNum_06"].Value);
            set => Row["itemNum_06"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 7.
        /// </summary>
        public byte GoodSlot7Count
        {
            get => Convert.ToByte(Row["itemNum_07"].Value);
            set => Row["itemNum_07"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 8.
        /// </summary>
        public byte GoodSlot8Count
        {
            get => Convert.ToByte(Row["itemNum_08"].Value);
            set => Row["itemNum_08"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 9.
        /// </summary>
        public byte GoodSlot9Count
        {
            get => Convert.ToByte(Row["itemNum_09"].Value);
            set => Row["itemNum_09"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Count of good equipped in slot 10.
        /// </summary>
        public byte GoodSlot10Count
        {
            get => Convert.ToByte(Row["itemNum_10"].Value);
            set => Row["itemNum_10"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to head size.
        /// </summary>
        public sbyte HeadScale
        {
            get => Convert.ToSByte(Row["bodyScaleHead"].Value);
            set => Row["bodyScaleHead"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to chest size.
        /// </summary>
        public sbyte ChestScale
        {
            get => Convert.ToSByte(Row["bodyScaleBreast"].Value);
            set => Row["bodyScaleBreast"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to abdomen size.
        /// </summary>
        public sbyte AbdomenScale
        {
            get => Convert.ToSByte(Row["bodyScaleAbdomen"].Value);
            set => Row["bodyScaleAbdomen"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to arm size.
        /// </summary>
        public sbyte ArmScale
        {
            get => Convert.ToSByte(Row["bodyScaleArm"].Value);
            set => Row["bodyScaleArm"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to leg size.
        /// </summary>
        public sbyte LegScale
        {
            get => Convert.ToSByte(Row["bodyScaleLeg"].Value);
            set => Row["bodyScaleLeg"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First equipped gesture.
        /// </summary>
        public sbyte Gesture1
        {
            get => Convert.ToSByte(Row["gestureId0"].Value);
            set => Row["gestureId0"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Second equipped gesture.
        /// </summary>
        public sbyte Gesture2
        {
            get => Convert.ToSByte(Row["gestureId1"].Value);
            set => Row["gestureId1"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Third equipped gesture.
        /// </summary>
        public sbyte Gesture3
        {
            get => Convert.ToSByte(Row["gestureId2"].Value);
            set => Row["gestureId2"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fourth equipped gesture.
        /// </summary>
        public sbyte Gesture4
        {
            get => Convert.ToSByte(Row["gestureId3"].Value);
            set => Row["gestureId3"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Fifth equipped gesture.
        /// </summary>
        public sbyte Gesture5
        {
            get => Convert.ToSByte(Row["gestureId4"].Value);
            set => Row["gestureId4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sixth equipped gesture.
        /// </summary>
        public sbyte Gesture6
        {
            get => Convert.ToSByte(Row["gestureId5"].Value);
            set => Row["gestureId5"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Seventh equipped gesture.
        /// </summary>
        public sbyte Gesture7
        {
            get => Convert.ToSByte(Row["gestureId6"].Value);
            set => Row["gestureId6"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of human NPC.
        /// </summary>
        public byte NPCType
        {
            get => Convert.ToByte(Row["npcPlayerType"].Value);
            set => Row["npcPlayerType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Draw type of human NPC.
        /// </summary>
        public byte DrawType
        {
            get => Convert.ToByte(Row["npcPlayerDrawType"].Value);
            set => Row["npcPlayerDrawType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Character sex.
        /// </summary>
        public byte Sex
        {
            get => Convert.ToByte(Row["npcPlayerSex"].Value);
            set => Row["npcPlayerSex"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Character covenant.
        /// </summary>
        public byte Covenant
        {
            get => Convert.ToByte(Row["vowType:4"].Value);
            set => Row["vowType:4"].Value = value;
        }

    }
}

