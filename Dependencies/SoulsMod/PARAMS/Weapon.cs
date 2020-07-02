using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Weapon : RowWrapper
    {
        public Weapon() { }
        public Weapon(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        public new string Name
        {
            get => Text.WeaponNames[ID];
            set {
                Row.Name = value;
                Text.WeaponNames[ID] = value;
            }
        }

        public string Summary
        {
            get => Text.WeaponSummaries[ID];
            set => Text.WeaponSummaries[ID] = value;
        }

        public string Description
        {
            get => Text.WeaponDescriptions[ID];
            set => Text.WeaponDescriptions[ID] = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number attached to the front of behaviors triggered from TAE.
        /// </summary>
        public int BehaviorVariationID
        {
            get => Convert.ToInt32(Row["behaviorVariationId"].Value);
            set => Row["behaviorVariationId"].Value = value;
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
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon replacement for ghosts.
        /// </summary>
        public uint GhostWeaponReplacement
        {
            get => Convert.ToUInt32(Row["wanderingEquipId"].Value);
            set => Row["wanderingEquipId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weight of weapon.
        /// </summary>
        public float Weight
        {
            get => Convert.ToSingle(Row["weight"].Value);
            set => Row["weight"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unknown effect. Value is about evenly split between 0 and 1 across
        /// weapons, with no obvious pattern.
        /// </summary>
        public float WeightRatio
        {
            get => Convert.ToSingle(Row["weaponWeightRate"].Value);
            set => Row["weaponWeightRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of souls required to repair weapon fully. Actual repair cost is
        /// this multiplied by current durability over max durability.
        /// </summary>
        public int RepairCost
        {
            get => Convert.ToInt32(Row["fixPrice"].Value);
            set => Row["fixPrice"].Value = value;
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
        /// Amount of attack power gained from strength. (I believe this is the
        /// percentage of the player's strength to add to the weapon's attack
        /// power, but it also depends on ScalingFormulaType below.)
        /// </summary>
        public float StrengthScaling
        {
            get => Convert.ToSingle(Row["correctStrength"].Value);
            set => Row["correctStrength"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of attack power gained from dexterity. (I believe this is the
        /// percentage of the player's dexterity to add to the weapon's attack
        /// power, but it also depends on ScalingFormulaType below.).
        /// </summary>
        public float DexterityScaling
        {
            get => Convert.ToSingle(Row["correctAgility"].Value);
            set => Row["correctAgility"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of attack power gained from intelligence. (I believe this is
        /// the percentage of the player's intelligence to add to the weapon's
        /// attack power, but it also depends on ScalingFormulaType below.)
        /// </summary>
        public float IntelligenceScaling
        {
            get => Convert.ToSingle(Row["correctMagic"].Value);
            set => Row["correctMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Amount of attack power gained from faith. (I believe this is the
        /// percentage of the player's faith to add to the weapon's attack power,
        /// but it also depends on ScalingFormulaType below.)
        /// </summary>
        public float FaithScaling
        {
            get => Convert.ToSingle(Row["correctFaith"].Value);
            set => Row["correctFaith"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of physical damage prevented when guarding with this
        /// weapon.
        /// </summary>
        public float PhysicalGuardPercentage
        {
            get => Convert.ToSingle(Row["physGuardCutRate"].Value);
            set => Row["physGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of magic damage prevented when guarding with this weapon.
        /// </summary>
        public float MagicGuardPercentage
        {
            get => Convert.ToSingle(Row["magGuardCutRate"].Value);
            set => Row["magGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of fire damage prevented when guarding with this weapon.
        /// </summary>
        public float FireGuardPercentage
        {
            get => Convert.ToSingle(Row["fireGuardCutRate"].Value);
            set => Row["fireGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of lightning damage prevented when guarding with this
        /// weapon.
        /// </summary>
        public float LightningGuardPercentage
        {
            get => Convert.ToSingle(Row["thunGuardCutRate"].Value);
            set => Row["thunGuardCutRate"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 0).
        /// </summary>
        public int SpecialEffectOnHit0
        {
            get => Convert.ToInt32(Row["spEffectBehaviorId0"].Value);
            set => Row["spEffectBehaviorId0"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 1).
        /// </summary>
        public int SpecialEffectOnHit1
        {
            get => Convert.ToInt32(Row["spEffectBehaviorId1"].Value);
            set => Row["spEffectBehaviorId1"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 2).
        /// </summary>
        public int SpecialEffectOnHit2
        {
            get => Convert.ToInt32(Row["spEffectBehaviorId2"].Value);
            set => Row["spEffectBehaviorId2"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 0).
        /// </summary>
        public int EquippedSpecialEffect0
        {
            get => Convert.ToInt32(Row["residentSpEffectId"].Value);
            set => Row["residentSpEffectId"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 1).
        /// </summary>
        public int EquippedSpecialEffect1
        {
            get => Convert.ToInt32(Row["residentSpEffectId1"].Value);
            set => Row["residentSpEffectId1"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 2).
        /// </summary>
        public int EquippedSpecialEffect2
        {
            get => Convert.ToInt32(Row["residentSpEffectId2"].Value);
            set => Row["residentSpEffectId2"].Value = value;
        }
        // LINK_STRING: <Params:UpgradeMaterials>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Upgrade materials required for reinforcement at each level.
        /// </summary>
        public int UpgradeMaterialsID
        {
            get => Convert.ToInt32(Row["materialSetId"].Value);
            set => Row["materialSetId"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 0 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin0
        {
            get => Convert.ToInt32(Row["originEquipWep"].Value);
            set => Row["originEquipWep"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 1 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin1
        {
            get => Convert.ToInt32(Row["originEquipWep1"].Value);
            set => Row["originEquipWep1"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 2 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin2
        {
            get => Convert.ToInt32(Row["originEquipWep2"].Value);
            set => Row["originEquipWep2"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 3 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin3
        {
            get => Convert.ToInt32(Row["originEquipWep3"].Value);
            set => Row["originEquipWep3"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 4 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin4
        {
            get => Convert.ToInt32(Row["originEquipWep4"].Value);
            set => Row["originEquipWep4"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 5 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin5
        {
            get => Convert.ToInt32(Row["originEquipWep5"].Value);
            set => Row["originEquipWep5"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 6 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin6
        {
            get => Convert.ToInt32(Row["originEquipWep6"].Value);
            set => Row["originEquipWep6"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 7 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin7
        {
            get => Convert.ToInt32(Row["originEquipWep7"].Value);
            set => Row["originEquipWep7"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 8 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin8
        {
            get => Convert.ToInt32(Row["originEquipWep8"].Value);
            set => Row["originEquipWep8"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 9 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin9
        {
            get => Convert.ToInt32(Row["originEquipWep9"].Value);
            set => Row["originEquipWep9"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 10 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin10
        {
            get => Convert.ToInt32(Row["originEquipWep10"].Value);
            set => Row["originEquipWep10"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 11 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin11
        {
            get => Convert.ToInt32(Row["originEquipWep11"].Value);
            set => Row["originEquipWep11"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 12 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin12
        {
            get => Convert.ToInt32(Row["originEquipWep12"].Value);
            set => Row["originEquipWep12"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 13 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin13
        {
            get => Convert.ToInt32(Row["originEquipWep13"].Value);
            set => Row["originEquipWep13"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 14 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin14
        {
            get => Convert.ToInt32(Row["originEquipWep14"].Value);
            set => Row["originEquipWep14"].Value = value;
        }
        // LINK_STRING: <Params:Weapons>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin armor for level 15 of this weapon (i.e. what you receive when a
        /// blacksmith removes upgrades).If -1, the weapon cannot be reverted.
        /// Otherwise, it will appear in each blacksmith's reversion menu.
        /// </summary>
        public int UpgradeOrigin15
        {
            get => Convert.ToInt32(Row["originEquipWep15"].Value);
            set => Row["originEquipWep15"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to damage dealt against demons with this weapon.
        /// </summary>
        public float DamageAgainstDemonsMultiplier
        {
            get => Convert.ToSingle(Row["antiDemonDamageRate"].Value);
            set => Row["antiDemonDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to damage dealt against enemies weak to divine
        /// (e.g. skeletons) with this weapon.
        /// </summary>
        public float WeakToDivineDamageMultiplier
        {
            get => Convert.ToSingle(Row["antSaintDamageRate"].Value);
            set => Row["antSaintDamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to damage dealt against Gods and Goddesses with
        /// this weapon.
        /// </summary>
        public float GodDamageMultiplier
        {
            get => Convert.ToSingle(Row["antWeakA_DamageRate"].Value);
            set => Row["antWeakA_DamageRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to damage dealt against enemies from the Abyss with
        /// this weapon.
        /// </summary>
        public float AbyssDamageMultiplier
        {
            get => Convert.ToSingle(Row["antWeakB_DamageRate"].Value);
            set => Row["antWeakB_DamageRate"].Value = value;
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
        // LINK_STRING: <Model>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon model ID.
        /// </summary>
        public ushort WeaponModel
        {
            get => Convert.ToUInt16(Row["equipModelId"].Value);
            set => Row["equipModelId"].Value = value;
        }
        // LINK_STRING: <Texture>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon icon texture ID.
        /// </summary>
        public ushort WeaponIcon
        {
            get => Convert.ToUInt16(Row["iconId"].Value);
            set => Row["iconId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Durability of weapon when it is obtained. Always equal to max
        /// durability in vanilla game.
        /// </summary>
        public ushort InitialDurability
        {
            get => Convert.ToUInt16(Row["durability"].Value);
            set => Row["durability"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum durability of weapon.
        /// </summary>
        public ushort MaxDurability
        {
            get => Convert.ToUInt16(Row["durabilityMax"].Value);
            set => Row["durabilityMax"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Power for escaping throws. Always 1, except for a few (and only a few)
        /// of the ghost replacement weapons.
        /// </summary>
        public ushort ThrowEscapePower
        {
            get => Convert.ToUInt16(Row["attackThrowEscape"].Value);
            set => Row["attackThrowEscape"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Maximum parry window duration (cannot exceed TAE duration). Always set
        /// to 10.
        /// </summary>
        public short MaxParryWindowDuration
        {
            get => Convert.ToInt16(Row["parryDamageLife"].Value);
            set => Row["parryDamageLife"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base physical damage of weapon attacks.
        /// </summary>
        public ushort BasePhysicalDamage
        {
            get => Convert.ToUInt16(Row["attackBasePhysics"].Value);
            set => Row["attackBasePhysics"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base magic damage of weapon attacks.
        /// </summary>
        public ushort BaseMagicDamage
        {
            get => Convert.ToUInt16(Row["attackBaseMagic"].Value);
            set => Row["attackBaseMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base fire damage of weapon attacks.
        /// </summary>
        public ushort BaseFireDamage
        {
            get => Convert.ToUInt16(Row["attackBaseFire"].Value);
            set => Row["attackBaseFire"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base lightning damage of weapon attacks.
        /// </summary>
        public ushort BaseLightningDamage
        {
            get => Convert.ToUInt16(Row["attackBaseThunder"].Value);
            set => Row["attackBaseThunder"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base stamina damage of weapon attacks.
        /// </summary>
        public ushort BaseStaminaDamage
        {
            get => Convert.ToUInt16(Row["attackBaseStamina"].Value);
            set => Row["attackBaseStamina"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Base poise damage of weapon attacks.
        /// </summary>
        public ushort BasePoiseDamage
        {
            get => Convert.ToUInt16(Row["saWeaponDamage"].Value);
            set => Row["saWeaponDamage"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Poise gained during attack animations with this weapon. Never used
        /// (probably done in TAE).
        /// </summary>
        public short AttackPoiseBonus
        {
            get => Convert.ToInt16(Row["saDurability"].Value);
            set => Row["saDurability"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Angle that can be guarded with this weapon. Never used.
        /// </summary>
        public short EffectiveGuardAngle
        {
            get => Convert.ToInt16(Row["guardAngle"].Value);
            set => Row["guardAngle"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Defense against (i.e. value subtracted from) stamina attack damage
        /// while guarding.
        /// </summary>
        public short GuardStaminaDefense
        {
            get => Convert.ToInt16(Row["staminaGuardDef"].Value);
            set => Row["staminaGuardDef"].Value = value;
        }
        // LINK_STRING: <Params:WeaponUpgrades>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon Upgrade parameter for weapon reinforcement.
        /// </summary>
        public short WeaponUpgradeID
        {
            get => Convert.ToInt16(Row["reinforceTypeId"].Value);
            set => Row["reinforceTypeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Index of weapon as it contributes to the Knight's Honor achievement.
        /// </summary>
        public short KnightHonorIndex
        {
            get => Convert.ToInt16(Row["trophySGradeId"].Value);
            set => Row["trophySGradeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Achievement unlocked when weapon is upgraded to maximum level (one per
        /// upgrade path).
        /// </summary>
        public short MaxUpgradeAchievementID
        {
            get => Convert.ToInt16(Row["trophySeqId"].Value);
            set => Row["trophySeqId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage damage increase (if positive) or decrease (if negative)
        /// during backstabs and ripostes with this weapon.
        /// </summary>
        public short ThrowDamageChangePercentage
        {
            get => Convert.ToInt16(Row["throwAtkRate"].Value);
            set => Row["throwAtkRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage range increase (if positive) or decrease (if negative) with
        /// this bow.
        /// </summary>
        public short BowRangeChangePercentage
        {
            get => Convert.ToInt16(Row["bowDistRate"].Value);
            set => Row["bowDistRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Model category for equipment. Only one option for weapons.
        /// </summary>
        public byte WeaponModelCategory
        {
            get => Convert.ToByte(Row["equipModelCategory"].Value);
            set => Row["equipModelCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Model gender variant. All weapons are genderless.
        /// </summary>
        public byte WeaponModelGender
        {
            get => Convert.ToByte(Row["equipModelGender"].Value);
            set => Row["equipModelGender"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Basic category of weapon. Many 'weapon types' you may be familiar with
        /// are merged here (e.g. whips are straight swords).
        /// </summary>
        public byte WeaponCategory
        {
            get => Convert.ToByte(Row["weaponCategory"].Value);
            set => Row["weaponCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Basic weapon attack animation type. More diverse than WeaponCategory.
        /// This number is multiplied by 10000 and used as an animation offset for
        /// all attacks, I believe.
        /// </summary>
        public byte AttackAnimationCategory
        {
            get => Convert.ToByte(Row["wepmotionCategory"].Value);
            set => Row["wepmotionCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Basic weapon/shield block animation type.
        /// </summary>
        public byte GuardAnimationCategory
        {
            get => Convert.ToByte(Row["guardmotionCategory"].Value);
            set => Row["guardmotionCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the sounds and visual effects generated when this weapon
        /// hits.
        /// </summary>
        public byte VisualSoundEffectsOnHit
        {
            get => Convert.ToByte(Row["atkMaterial"].Value);
            set => Row["atkMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the visual effects generated when this weapon blocks an
        /// attack.
        /// </summary>
        public byte VisualEffectsOnBlock
        {
            get => Convert.ToByte(Row["defMaterial"].Value);
            set => Row["defMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the sound effects generated when this weapon blocks an
        /// attack.
        /// </summary>
        public byte SoundEffectsOnBlock
        {
            get => Convert.ToByte(Row["defSfxMaterial"].Value);
            set => Row["defSfxMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines how scaling changes with attribute level.
        /// </summary>
        public byte ScalingFormulaType
        {
            get => Convert.ToByte(Row["correctType"].Value);
            set => Row["correctType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Element attached to hits with this weapon.
        /// </summary>
        public byte ElementAttribute
        {
            get => Convert.ToByte(Row["spAttribute"].Value);
            set => Row["spAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Category of special attack (R2) performed with this weapon, from 50 to
        /// 199 (or 0 for none). This number is multiplied by 10000 and used as an
        /// animation offset for R2 attacks, I believe.
        /// </summary>
        public byte SpecialAttackCategory
        {
            get => Convert.ToByte(Row["spAtkcategory"].Value);
            set => Row["spAtkcategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Category for one-handed attacks.This number is multiplied by 10000 and
        /// used as an animation offset for one-handed attacks, I believe. Not
        /// sure how it interacts with the base AttackAnimationCategory.
        /// </summary>
        public byte OneHandedAnimationCategory
        {
            get => Convert.ToByte(Row["wepmotionOneHandId"].Value);
            set => Row["wepmotionOneHandId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Category for two-handed attacks. This number is multiplied by 10000
        /// and used as an animation offset for two-handed attacks, I believe. Not
        /// sure how it interacts with the base AttackAnimationCategory.
        /// </summary>
        public byte TwoHandedAnimationCategory
        {
            get => Convert.ToByte(Row["wepmotionBothHandId"].Value);
            set => Row["wepmotionBothHandId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Required strength to wield weapon properly. (Reduced by one third if
        /// held two-handed.)
        /// </summary>
        public byte RequiredStrength
        {
            get => Convert.ToByte(Row["properStrength"].Value);
            set => Row["properStrength"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Required dexterity to wield weapon properly.
        /// </summary>
        public byte RequiredDexterity
        {
            get => Convert.ToByte(Row["properAgility"].Value);
            set => Row["properAgility"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Required intelligence to wield weapon properly.
        /// </summary>
        public byte RequiredIntelligence
        {
            get => Convert.ToByte(Row["properMagic"].Value);
            set => Row["properMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Required faith to wield weapon properly.
        /// </summary>
        public byte RequiredFaith
        {
            get => Convert.ToByte(Row["properFaith"].Value);
            set => Row["properFaith"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Always set to 99, except for arrows and bolts.
        /// </summary>
        public byte OverStrength
        {
            get => Convert.ToByte(Row["overStrength"].Value);
            set => Row["overStrength"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Never used.
        /// </summary>
        public byte AttackBaseParry
        {
            get => Convert.ToByte(Row["attackBaseParry"].Value);
            set => Row["attackBaseParry"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unknown. Never used.
        /// </summary>
        public byte DefenseBaseParry
        {
            get => Convert.ToByte(Row["defenseBaseParry"].Value);
            set => Row["defenseBaseParry"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if an enemy will be deflected when you block them with this
        /// weapon (by comparing it to their DeflectOnAttack).
        /// </summary>
        public byte DeflectOnBlock
        {
            get => Convert.ToByte(Row["guardBaseRepel"].Value);
            set => Row["guardBaseRepel"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines if this weapon will be deflected when attacking a blocking
        /// enemy (by comparing it to their DeflectOnBlock).
        /// </summary>
        public byte DeflectOnAttack
        {
            get => Convert.ToByte(Row["attackBaseRepel"].Value);
            set => Row["attackBaseRepel"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Percentage (from -100 to 100) of target's current guard rate to
        /// ignore. A value of 100 will ignore guarding completely, and a value of
        /// -100 will double their guarding effectiveness. Never used, in favor of
        /// the simple 'IgnoreGuard' boolean field.
        /// </summary>
        public sbyte IgnoreGuardPercentage
        {
            get => Convert.ToSByte(Row["guardCutCancelRate"].Value);
            set => Row["guardCutCancelRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'in which guard motion is the enemy attacked
        /// when guarded?' Exact effects are unclear, but this ranges from 0 to 4
        /// in effectiveness of blocking in a predictable way (daggers are worse
        /// than swords, which are worse than greatswords, which are worse than
        /// all shields).
        /// </summary>
        public sbyte GuardLevel
        {
            get => Convert.ToSByte(Row["guardLevel"].Value);
            set => Row["guardLevel"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public sbyte SlashDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["slashGuardCutRate"].Value);
            set => Row["slashGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public sbyte StrikeDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["blowGuardCutRate"].Value);
            set => Row["blowGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Always zero.
        /// </summary>
        public sbyte ThrustDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["thrustGuardCutRate"].Value);
            set => Row["thrustGuardCutRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of incoming poison damage ignored when guarding.
        /// </summary>
        public sbyte PoisonDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["poisonGuardResist"].Value);
            set => Row["poisonGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of incoming toxic damage ignored when guarding.
        /// </summary>
        public sbyte ToxicDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["diseaseGuardResist"].Value);
            set => Row["diseaseGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of incoming bleed damage ignored when guarding.
        /// </summary>
        public sbyte BleedDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["bloodGuardResist"].Value);
            set => Row["bloodGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage of incoming curse damage ignored when guarding.
        /// </summary>
        public sbyte CurseDamageReductionWhenGuarding
        {
            get => Convert.ToSByte(Row["curseGuardResist"].Value);
            set => Row["curseGuardResist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines an alternate animation used if the player tries to use this
        /// weapon's special attack without having enough durability to use it.
        /// Exact enumeration is unknown, but existing usages are documented.
        /// </summary>
        public byte DurabilityDivergenceCategory
        {
            get => Convert.ToByte(Row["isDurabilityDivergence"].Value);
            set => Row["isDurabilityDivergence"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be equipped in the right hand.
        /// </summary>
        public bool RightHandAllowed
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["rightHandEquipable"].Value));
            set => Row["rightHandEquipable"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be equipped in the left hand.
        /// </summary>
        public bool LeftHandAllowed
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["leftHandEquipable"].Value));
            set => Row["leftHandEquipable"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be held in two-handed mode.
        /// </summary>
        public bool BothHandsAllowed
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["bothHandEquipable"].Value));
            set => Row["bothHandEquipable"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon will use equipped arrow slot.
        /// </summary>
        public bool UsesEquippedArrows
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["arrowSlotEquipable"].Value));
            set => Row["arrowSlotEquipable"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon will use equipped bolt slot.
        /// </summary>
        public bool UsesEquippedBolts
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["boltSlotEquipable"].Value));
            set => Row["boltSlotEquipable"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the player can guard with this weapon by holding L1.
        /// </summary>
        public bool GuardEnabled
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableGuard"].Value));
            set => Row["enableGuard"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, the player can parry with htis weapon by pressing L2.
        /// </summary>
        public bool ParryEnabled
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableParry"].Value));
            set => Row["enableParry"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be used to cast sorcery magic.
        /// </summary>
        public bool CanCastSorceries
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableMagic"].Value));
            set => Row["enableMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be used to cast pyromancy.
        /// </summary>
        public bool CanCastPyromancy
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableSorcery"].Value));
            set => Row["enableSorcery"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool CanCastMiracles
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableMiracle"].Value));
            set => Row["enableMiracle"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool CanCastCovenantMagic
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableVowMagic"].Value));
            set => Row["enableVowMagic"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool DealsNeutralDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isNormalAttackType"].Value));
            set => Row["isNormalAttackType"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool DealsStrikeDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isBlowAttackType"].Value));
            set => Row["isBlowAttackType"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool DealsSlashDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isSlashAttackType"].Value));
            set => Row["isSlashAttackType"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool DealsThrustDamage
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isThrustAttackType"].Value));
            set => Row["isThrustAttackType"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool IsUpgraded
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEnhance"].Value));
            set => Row["isEnhance"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool IsAffectedByLuck
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isLuckCorrect"].Value));
            set => Row["isLuckCorrect"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool IsCustom
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isCustom"].Value));
            set => Row["isCustom"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool DisableBaseChangeReset
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableBaseChangeReset"].Value));
            set => Row["disableBaseChangeReset"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon cannot be repaired.
        /// </summary>
        public bool DisableRepairs
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableRepair"].Value));
            set => Row["disableRepair"].Value = value;
        }

        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Enabled only for the Dark Hand.
        /// </summary>
        public bool IsDarkHand
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDarkHand"].Value));
            set => Row["isDarkHand"].Value = value;
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

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool IsLantern
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["lanternWep"].Value));
            set => Row["lanternWep"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can hit ghosts without a Transient Curse active.
        /// </summary>
        public bool CanHitGhosts
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isVersusGhostWep"].Value));
            set => Row["isVersusGhostWep"].Value = value;
        }

        public byte BaseChangeCategory
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Never used. Likely Demon's Souls junk.
        /// </summary>
        {

            get => Convert.ToByte(Row["baseChangeCategory"].Value);
            set => Row["baseChangeCategory"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public bool IsDragonSlayer
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDragonSlayer"].Value));
            set => Row["isDragonSlayer"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this weapon can be stored in the Bottomless Box. Always True
        /// for rings.
        /// </summary>
        public bool CanBeStored
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isDeposit"].Value));
            set => Row["isDeposit"].Value = value;
        }

        // DEFAULT_VISIBLE: False
        /// <summary>
        /// If True, this weapon cannot be given to other players by dropping it.
        /// Always False in vanilla.
        /// </summary>
        public bool DisableMultiplayerShare
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["disableMultiDropShare"].Value));
            set => Row["disableMultiDropShare"].Value = value;
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
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Level sync correction (DSR only). Probably not useful.
        /// </summary>
        public short LevelSyncCorrection
        {
            get => Convert.ToInt16(Row["levelSyncCorrectID"].Value);
            set => Row["levelSyncCorrectID"].Value = value;
        }
    }
}
