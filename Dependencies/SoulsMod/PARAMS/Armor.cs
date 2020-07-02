using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Armor : RowWrapper
    {
        public Armor() { }
        public Armor(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public new string Name
        {
            get => Text.ArmorNames[ID];
            set
            {
                Row.Name = value;
                Text.ArmorNames[ID] = value;
            }
        }

        public string Summary
        {
            get => Text.ArmorDescriptions[ID];
            set => Text.ArmorDescriptions[ID] = value;
        }

        public string Description
        {
            get => Text.ArmorLongDescriptions[ID];
            set => Text.ArmorLongDescriptions[ID] = value;
        }

        /// <summary>
        /// Gives this armor piece the visual appearance of another.
        /// </summary>
        /// <param name="sourceID">The ID of the armor piece from which the appearance will be copied.</param>
        public Armor UseVisualData(long sourceID, bool noInvis = false)
        {
            Armor source = GPARAM.Armor[sourceID];
            EquipmentModel = source.EquipmentModel;
            FemaleIcon = source.FemaleIcon;
            MaleIcon = source.MaleIcon;
            
            foreach (PARAM.Cell cell in source.Row.Cells)
                if (cell.Def.InternalName.Contains("Scale"))
                    Row[cell.Def.InternalName].Value = cell.Value;

            if (noInvis)
            {
                for (int i = 0; i <= 47; i++)
                {
                    string s = "invisibleFlag" + i.ToString("00");
                    Row[s].Value = 0;
                }
            } else
            {
                for (int i = 0; i <= 47; i++)
                {
                    string s = "invisibleFlag" + i.ToString("00");
                    Row[s].Value = source.Row[s].Value;
                }

            }

            return this;
        }

        public Armor UseStats(long sourceID)
        {
            Armor source = GPARAM.Armor[sourceID];

            foreach (PARAM.Cell cell in source.Row.Cells)
            {
                string name = cell.Def.InternalName;
                bool skip = name.Contains("Scale")
                    || name.StartsWith("invis")
                    || name.Contains("icon")
                    || name.Contains("Model")
                    || name.Contains("model");

                if (!skip)
                    Row[cell.Def.InternalName].Value = cell.Value;
            }

            return this;

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
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Replacement equipment for network ghosts.
        /// </summary>
        public uint GhostArmorReplacement
        {
            get => Convert.ToUInt32(Row["wanderingEquipId"].Value);
            set => Row["wanderingEquipId"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantItemLot
        {
            get => Convert.ToInt32(Row["vagrantItemLotId"].Value);
            set => Row["vagrantItemLotId"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantBonusEnemyDropItemLot
        {
            get => Convert.ToInt32(Row["vagrantBonusEneDropItemLotId"].Value);
            set => Row["vagrantBonusEneDropItemLotId"].Value = value;
        }
        // LINK_STRING: <Params:ItemLots>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// DOC-TODO
        /// </summary>
        public int VagrantItemEnemyDropItemLot
        {
            get => Convert.ToInt32(Row["vagrantItemEneDropItemLotId"].Value);
            set => Row["vagrantItemEneDropItemLotId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of souls required to repair armor fully. Actual repair cost is
        /// this multiplied by current durability over max durability.
        /// </summary>
        public int RepairCost
        {
            get => Convert.ToInt32(Row["fixPrice"].Value);
            set => Row["fixPrice"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unsure when this is used. Possibly sets the default if the cost is not
        /// specified in Shop parameters. Always set to 200.
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
        /// Weight of armor.
        /// </summary>
        public float Weight
        {
            get => Convert.ToSingle(Row["weight"].Value);
            set => Row["weight"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (first of three).
        /// </summary>
        public int WearerSpecialEffect1
        {
            get => Convert.ToInt32(Row["residentSpEffectId"].Value);
            set => Row["residentSpEffectId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (second of three).
        /// </summary>
        public int WearerSpecialEffect2
        {
            get => Convert.ToInt32(Row["residentSpEffectId2"].Value);
            set => Row["residentSpEffectId2"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (third of three).
        /// </summary>
        public int WearerSpecialEffect3
        {
            get => Convert.ToInt32(Row["residentSpEffectId3"].Value);
            set => Row["residentSpEffectId3"].Value = value;
        }
        // LINK_STRING: <Params:UpgradeMaterials>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Upgrade material set for reinforcement.
        /// </summary>
        public int UpgradeMaterialID
        {
            get => Convert.ToInt32(Row["materialSetId"].Value);
            set => Row["materialSetId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for damage taken to this part of the body. Used to specify
        /// weakness, not strength, so is never less than 1. Usually 1.5 for weak
        /// head pieces, 1.3 for strong head pieces, 1.1 for gauntlets and
        /// leggings, and 1 for torso armor.
        /// </summary>
        public float SiteDamageMultiplier
        {
            get => Convert.ToSingle(Row["partsDamageRate"].Value);
            set => Row["partsDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value added to poise recovery time (so negative values are better).
        /// -0.1 for heavy armor and 0 otherwise.
        /// </summary>
        public float PoiseRecoveryTimeModifier
        {
            get => Convert.ToSingle(Row["corectSARecover"].Value);
            set => Row["corectSARecover"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 0 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin0
        {
            get => Convert.ToInt32(Row["originEquipPro"].Value);
            set => Row["originEquipPro"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 1 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin1
        {
            get => Convert.ToInt32(Row["originEquipPro1"].Value);
            set => Row["originEquipPro1"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 2 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin2
        {
            get => Convert.ToInt32(Row["originEquipPro2"].Value);
            set => Row["originEquipPro2"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 3 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin3
        {
            get => Convert.ToInt32(Row["originEquipPro3"].Value);
            set => Row["originEquipPro3"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 4 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin4
        {
            get => Convert.ToInt32(Row["originEquipPro4"].Value);
            set => Row["originEquipPro4"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 5 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin5
        {
            get => Convert.ToInt32(Row["originEquipPro5"].Value);
            set => Row["originEquipPro5"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 6 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin6
        {
            get => Convert.ToInt32(Row["originEquipPro6"].Value);
            set => Row["originEquipPro6"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 7 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin7
        {
            get => Convert.ToInt32(Row["originEquipPro7"].Value);
            set => Row["originEquipPro7"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 8 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin8
        {
            get => Convert.ToInt32(Row["originEquipPro8"].Value);
            set => Row["originEquipPro8"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 9 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin9
        {
            get => Convert.ToInt32(Row["originEquipPro9"].Value);
            set => Row["originEquipPro9"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 10 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin10
        {
            get => Convert.ToInt32(Row["originEquipPro10"].Value);
            set => Row["originEquipPro10"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 11 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin11
        {
            get => Convert.ToInt32(Row["originEquipPro11"].Value);
            set => Row["originEquipPro11"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 12 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin12
        {
            get => Convert.ToInt32(Row["originEquipPro12"].Value);
            set => Row["originEquipPro12"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 13 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin13
        {
            get => Convert.ToInt32(Row["originEquipPro13"].Value);
            set => Row["originEquipPro13"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 14 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin14
        {
            get => Convert.ToInt32(Row["originEquipPro14"].Value);
            set => Row["originEquipPro14"].Value = value;
        }
        // LINK_STRING: <Params:Armor>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 15 of this armor (i.e. what you receive when a
        /// blacksmith removes upgrades). If -1, the armor cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin15
        {
            get => Convert.ToInt32(Row["originEquipPro15"].Value);
            set => Row["originEquipPro15"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Scale factor applied to X dimension of male faces when worn.
        /// </summary>
        public float MaleFaceScaleX
        {
            get => Convert.ToSingle(Row["faceScaleM_ScaleX"].Value);
            set => Row["faceScaleM_ScaleX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Scale factor applied to Z dimension of male faces when worn.
        /// </summary>
        public float MaleFaceScaleZ
        {
            get => Convert.ToSingle(Row["faceScaleM_ScaleZ"].Value);
            set => Row["faceScaleM_ScaleZ"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum scale permitted for X dimension of male faces when worn.
        /// </summary>
        public float MaleFaceMaxScaleX
        {
            get => Convert.ToSingle(Row["faceScaleM_MaxX"].Value);
            set => Row["faceScaleM_MaxX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum scale permitted for Z dimension of male faces when worn.
        /// </summary>
        public float MaleFaceMaxScaleZ
        {
            get => Convert.ToSingle(Row["faceScaleM_MaxZ"].Value);
            set => Row["faceScaleM_MaxZ"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Scale factor applied to X dimension of female faces when worn.
        /// </summary>
        public float FemaleFaceScaleX
        {
            get => Convert.ToSingle(Row["faceScaleF_ScaleX"].Value);
            set => Row["faceScaleF_ScaleX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Scale factor applied to Z dimension of female faces when worn.
        /// </summary>
        public float FemaleFaceScaleZ
        {
            get => Convert.ToSingle(Row["faceScaleF_ScaleZ"].Value);
            set => Row["faceScaleF_ScaleZ"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum scale permitted for X dimension of female faces when worn.
        /// </summary>
        public float FemaleFaceMaxScaleX
        {
            get => Convert.ToSingle(Row["faceScaleF_MaxX"].Value);
            set => Row["faceScaleF_MaxX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum scale permitted for Z dimension of female faces when worn.
        /// </summary>
        public float FemaleFaceMaxScaleZ
        {
            get => Convert.ToSingle(Row["faceScaleF_MaxZ"].Value);
            set => Row["faceScaleF_MaxZ"].Value = value;
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
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model ID of armor.
        /// </summary>
        public ushort EquipmentModel
        {
            get => Convert.ToUInt16(Row["equipModelId"].Value);
            set => Row["equipModelId"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Icon of male variant of armor in inventory.
        /// </summary>
        public ushort MaleIcon
        {
            get => Convert.ToUInt16(Row["iconIdM"].Value);
            set => Row["iconIdM"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Icon of female variant of armor in inventory.
        /// </summary>
        public ushort FemaleIcon
        {
            get => Convert.ToUInt16(Row["iconIdF"].Value);
            set => Row["iconIdF"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Never used. Probably the percentage of knockback reduced (from 0 to
        /// 100) when wearing armor.
        /// </summary>
        public ushort KnockbackPercentageReduction
        {
            get => Convert.ToUInt16(Row["knockBack"].Value);
            set => Row["knockBack"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Never used. Possibly affects knockback of incoming attacks.
        /// </summary>
        public ushort KnockbackBouncePercentage
        {
            get => Convert.ToUInt16(Row["knockbackBounceRate"].Value);
            set => Row["knockbackBounceRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Durability of armor when it is obtained. Always equal to max
        /// durability in vanilla game.
        /// </summary>
        public ushort InitialDurability
        {
            get => Convert.ToUInt16(Row["durability"].Value);
            set => Row["durability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum durability of armor.
        /// </summary>
        public ushort MaxDurability
        {
            get => Convert.ToUInt16(Row["durabilityMax"].Value);
            set => Row["durabilityMax"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of poise added when wearing armor.
        /// </summary>
        public short Poise
        {
            get => Convert.ToInt16(Row["saDurability"].Value);
            set => Row["saDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines when incoming attacks will bounce off.
        /// </summary>
        public ushort RepelDefense
        {
            get => Convert.ToUInt16(Row["defFlickPower"].Value);
            set => Row["defFlickPower"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against physical attack damage.
        /// </summary>
        public ushort PhysicalDefense
        {
            get => Convert.ToUInt16(Row["defensePhysics"].Value);
            set => Row["defensePhysics"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against magic attack damage.
        /// </summary>
        public ushort MagicDefense
        {
            get => Convert.ToUInt16(Row["defenseMagic"].Value);
            set => Row["defenseMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against fire attack damage.
        /// </summary>
        public ushort FireDefense
        {
            get => Convert.ToUInt16(Row["defenseFire"].Value);
            set => Row["defenseFire"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against lightning attack damage.
        /// </summary>
        public ushort LightningDefense
        {
            get => Convert.ToUInt16(Row["defenseThunder"].Value);
            set => Row["defenseThunder"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against physical slash attack damage.
        /// </summary>
        public short SlashDefense
        {
            get => Convert.ToInt16(Row["defenseSlash"].Value);
            set => Row["defenseSlash"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against physical strike attack damage.
        /// </summary>
        public short StrikeDefense
        {
            get => Convert.ToInt16(Row["defenseBlow"].Value);
            set => Row["defenseBlow"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Added defense against physical thrust attack damage.
        /// </summary>
        public short ThrustDefense
        {
            get => Convert.ToInt16(Row["defenseThrust"].Value);
            set => Row["defenseThrust"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Poison resistance added by armor.
        /// </summary>
        public ushort PoisonResistance
        {
            get => Convert.ToUInt16(Row["resistPoison"].Value);
            set => Row["resistPoison"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Toxic resistance added by armor.
        /// </summary>
        public ushort ToxicResistance
        {
            get => Convert.ToUInt16(Row["resistDisease"].Value);
            set => Row["resistDisease"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bleed resistance added by armor.
        /// </summary>
        public ushort BleedResistance
        {
            get => Convert.ToUInt16(Row["resistBlood"].Value);
            set => Row["resistBlood"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Curse resistance added by armor.
        /// </summary>
        public ushort CurseResistance
        {
            get => Convert.ToUInt16(Row["resistCurse"].Value);
            set => Row["resistCurse"].Value = value;
        }
        // LINK_STRING: <Params:ArmorUpgrades>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Upgrade materials required for reinforcement at each level.
        /// </summary>
        public short ArmorUpgradeID
        {
            get => Convert.ToInt16(Row["reinforceTypeId"].Value);
            set => Row["reinforceTypeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Index of armor as it contributes to certain multi-item achievements.
        /// </summary>
        public short AchievementContributionID
        {
            get => Convert.ToInt16(Row["trophySGradeId"].Value);
            set => Row["trophySGradeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Level of armor that can be sold in 'the shop'. Always -1 or 0.
        /// Probably unused.
        /// </summary>
        public short ShopLevel
        {
            get => Convert.ToInt16(Row["shopLv"].Value);
            set => Row["shopLv"].Value = value;
        }
        // LINK_STRING: <Params:Knockback>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Knockback entry. Always 1.
        /// </summary>
        public byte KnockbackID
        {
            get => Convert.ToByte(Row["knockbackParamId"].Value);
            set => Row["knockbackParamId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines some aspect of attack deflection. Always set to 0 (for
        /// light armor) or 255 (for heavy armor).
        /// </summary>
        public byte RepelDamagePercentageReduction
        {
            get => Convert.ToByte(Row["flickDamageCutRate"].Value);
            set => Row["flickDamageCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Body part covered by armor model.
        /// </summary>
        public byte EquipmentModelCategory
        {
            get => Convert.ToByte(Row["equipModelCategory"].Value);
            set => Row["equipModelCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Gender variant of armor.
        /// </summary>
        public byte EquipmentModelGender
        {
            get => Convert.ToByte(Row["equipModelGender"].Value);
            set => Row["equipModelGender"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of armor (equip slot).
        /// </summary>
        public byte ArmorType
        {
            get => Convert.ToByte(Row["protectorCategory"].Value);
            set => Row["protectorCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of sound effect generated when this armor is hit.
        /// </summary>
        public byte SoundEffectOnHit
        {
            get => Convert.ToByte(Row["defenseMaterial"].Value);
            set => Row["defenseMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of visual effect generated when this armor is hit.
        /// </summary>
        public byte VisualEffectOnHit
        {
            get => Convert.ToByte(Row["defenseMaterialSfx"].Value);
            set => Row["defenseMaterialSfx"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public byte PartsDamageType
        {
            get => Convert.ToByte(Row["partsDmgType"].Value);
            set => Row["partsDmgType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sound effect for when damage is taken to weak spot (used for head
        /// armor).
        /// </summary>
        public byte SoundEffectOnWeakSpotHit
        {
            get => Convert.ToByte(Row["defenseMaterial_Weak"].Value);
            set => Row["defenseMaterial_Weak"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect for when damage is taken to weak spot (used for head
        /// armor).
        /// </summary>
        public byte VisualEffectOnWeakSpotHit
        {
            get => Convert.ToByte(Row["defenseMaterialSfx_Weak"].Value);
            set => Row["defenseMaterialSfx_Weak"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this armor can be stored in the Bottomless Box.
        /// </summary>
        public bool CanBeStored
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDeposit"].Value));
            set => Row["isDeposit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// This armor is equipped to the head.
        /// </summary>
        public bool EquippedToHead
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["headEquip"].Value));
            set => Row["headEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// This armor is equipped to the body.
        /// </summary>
        public bool EquippedToBody
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bodyEquip"].Value));
            set => Row["bodyEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// This armor is equipped to the hands.
        /// </summary>
        public bool EquippedToHands
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["armEquip"].Value));
            set => Row["armEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// This armor is equipped to the legs.
        /// </summary>
        public bool EquippedToLegs
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["legEquip"].Value));
            set => Row["legEquip"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, the face-scaling parameters of this armor will be applied.
        /// </summary>
        public bool UseFaceScale
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["useFaceScale"].Value));
            set => Row["useFaceScale"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag0
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag00"].Value));
            set => Row["invisibleFlag00"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (hair fringe)
        /// </summary>
        public bool HideFlag1
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag01"].Value));
            set => Row["invisibleFlag01"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (sideburns)
        /// </summary>
        public bool HideFlag2
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag02"].Value));
            set => Row["invisibleFlag02"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (top of head)
        /// </summary>
        public bool HideFlag3
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag03"].Value));
            set => Row["invisibleFlag03"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (top of head)
        /// </summary>
        public bool HideFlag4
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag04"].Value));
            set => Row["invisibleFlag04"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (back hair)
        /// </summary>
        public bool HideFlag5
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag05"].Value));
            set => Row["invisibleFlag05"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (back hair tip)
        /// </summary>
        public bool HideFlag6
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag06"].Value));
            set => Row["invisibleFlag06"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag7
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag07"].Value));
            set => Row["invisibleFlag07"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag8
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag08"].Value));
            set => Row["invisibleFlag08"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag9
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag09"].Value));
            set => Row["invisibleFlag09"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (collar)
        /// </summary>
        public bool HideFlag10
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag10"].Value));
            set => Row["invisibleFlag10"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (around collar)
        /// </summary>
        public bool HideFlag11
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag11"].Value));
            set => Row["invisibleFlag11"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag12
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag12"].Value));
            set => Row["invisibleFlag12"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag13
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag13"].Value));
            set => Row["invisibleFlag13"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag14
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag14"].Value));
            set => Row["invisibleFlag14"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (hood hem)
        /// </summary>
        public bool HideFlag15
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag15"].Value));
            set => Row["invisibleFlag15"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag16
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag16"].Value));
            set => Row["invisibleFlag16"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag17
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag17"].Value));
            set => Row["invisibleFlag17"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag18
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag18"].Value));
            set => Row["invisibleFlag18"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag19
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag19"].Value));
            set => Row["invisibleFlag19"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (sleeve A)
        /// </summary>
        public bool HideFlag20
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag20"].Value));
            set => Row["invisibleFlag20"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (sleeve B)
        /// </summary>
        public bool HideFlag21
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag21"].Value));
            set => Row["invisibleFlag21"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag22
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag22"].Value));
            set => Row["invisibleFlag22"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag23
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag23"].Value));
            set => Row["invisibleFlag23"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag24
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag24"].Value));
            set => Row["invisibleFlag24"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (arm)
        /// </summary>
        public bool HideFlag25
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag25"].Value));
            set => Row["invisibleFlag25"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag26
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag26"].Value));
            set => Row["invisibleFlag26"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag27
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag27"].Value));
            set => Row["invisibleFlag27"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag28
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag28"].Value));
            set => Row["invisibleFlag28"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag29
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag29"].Value));
            set => Row["invisibleFlag29"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (belt)
        /// </summary>
        public bool HideFlag30
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag30"].Value));
            set => Row["invisibleFlag30"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag31
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag31"].Value));
            set => Row["invisibleFlag31"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag32
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag32"].Value));
            set => Row["invisibleFlag32"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag33
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag33"].Value));
            set => Row["invisibleFlag33"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag34
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag34"].Value));
            set => Row["invisibleFlag34"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag35
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag35"].Value));
            set => Row["invisibleFlag35"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag36
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag36"].Value));
            set => Row["invisibleFlag36"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag37
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag37"].Value));
            set => Row["invisibleFlag37"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag38
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag38"].Value));
            set => Row["invisibleFlag38"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag39
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag39"].Value));
            set => Row["invisibleFlag39"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag40
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag40"].Value));
            set => Row["invisibleFlag40"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag41
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag41"].Value));
            set => Row["invisibleFlag41"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag42
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag42"].Value));
            set => Row["invisibleFlag42"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag43
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag43"].Value));
            set => Row["invisibleFlag43"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag44
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag44"].Value));
            set => Row["invisibleFlag44"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag45
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag45"].Value));
            set => Row["invisibleFlag45"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag46
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag46"].Value));
            set => Row["invisibleFlag46"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Hide part of the character model: (unknown)
        /// </summary>
        public bool HideFlag47
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["invisibleFlag47"].Value));
            set => Row["invisibleFlag47"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this armor cannot be given to other players by dropping it.
        /// Always False in vanilla.
        /// </summary>
        public bool DisableMultiplayerShare
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableMultiDropShare"].Value));
            set => Row["disableMultiDropShare"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown; always set to False.
        /// </summary>
        public bool SimpleDLCModelExists
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["simpleModelForDlc"].Value));
            set => Row["simpleModelForDlc"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Sorting index for an obsolete build of the game. No effect.
        /// </summary>
        public short OldSortIndex
        {
            get => Convert.ToInt16(Row["oldSortId"].Value);
            set => Row["oldSortId"].Value = value;
        }
    }
}
