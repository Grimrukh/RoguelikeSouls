using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class WeaponUpgrade : RowWrapper
    {
		public WeaponUpgrade() { }
		public WeaponUpgrade(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		// DEFAULT_VISIBLE: True
		/// <summary>
		/// Multiplier applied to outgoing physical damage (of any type).
		/// </summary>
		public float PhysicsAtkRate
		{
			get => Convert.ToSingle(Row["physicsAtkRate"].Value);
			set => Row["physicsAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing magic damage.
        /// </summary>
		public float MagicAtkRate
		{
			get => Convert.ToSingle(Row["magicAtkRate"].Value);
			set => Row["magicAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing fire damage.
        /// </summary>
		public float FireAtkRate
		{
			get => Convert.ToSingle(Row["fireAtkRate"].Value);
			set => Row["fireAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to outgoing lightning damage.
        /// </summary>
		public float ThunderAtkRate
		{
			get => Convert.ToSingle(Row["thunderAtkRate"].Value);
			set => Row["thunderAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the amount of damage dealt to targets' stamina.
        /// </summary>
		public float StaminaAtkRate
		{
			get => Convert.ToSingle(Row["staminaAtkRate"].Value);
			set => Row["staminaAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the amount of damage dealt to targets' poise.
        /// Never used.
        /// </summary>
		public float SaWeaponAtkRate
		{
			get => Convert.ToSingle(Row["saWeaponAtkRate"].Value);
			set => Row["saWeaponAtkRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to wielder's poise while using (attacking/blocking
        /// with?) weapon. Never used.
        /// </summary>
		public float SaDurabilityRate
		{
			get => Convert.ToSingle(Row["saDurabilityRate"].Value);
			set => Row["saDurabilityRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to strength scaling of this weapon.
        /// </summary>
		public float CorrectStrengthRate
		{
			get => Convert.ToSingle(Row["correctStrengthRate"].Value);
			set => Row["correctStrengthRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to dexterity scaling of this weapon.
        /// </summary>
		public float CorrectAgilityRate
		{
			get => Convert.ToSingle(Row["correctAgilityRate"].Value);
			set => Row["correctAgilityRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to intelligence scaling of this weapon.
        /// </summary>
		public float CorrectMagicRate
		{
			get => Convert.ToSingle(Row["correctMagicRate"].Value);
			set => Row["correctMagicRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to faith scaling of this weapon.
        /// </summary>
		public float CorrectFaithRate
		{
			get => Convert.ToSingle(Row["correctFaithRate"].Value);
			set => Row["correctFaithRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of physical damage blocked by
        /// this weapon/shield.
        /// </summary>
		public float PhysicsGuardCutRate
		{
			get => Convert.ToSingle(Row["physicsGuardCutRate"].Value);
			set => Row["physicsGuardCutRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of magic damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float MagicGuardCutRate
		{
			get => Convert.ToSingle(Row["magicGuardCutRate"].Value);
			set => Row["magicGuardCutRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of fire damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float FireGuardCutRate
		{
			get => Convert.ToSingle(Row["fireGuardCutRate"].Value);
			set => Row["fireGuardCutRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of lightning damage blocked by
        /// this weapon/shield.
        /// </summary>
		public float ThunderGuardCutRate
		{
			get => Convert.ToSingle(Row["thunderGuardCutRate"].Value);
			set => Row["thunderGuardCutRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of poison damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float PoisonGuardResistRate
		{
			get => Convert.ToSingle(Row["poisonGuardResistRate"].Value);
			set => Row["poisonGuardResistRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of toxic damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float DiseaseGuardResistRate
		{
			get => Convert.ToSingle(Row["diseaseGuardResistRate"].Value);
			set => Row["diseaseGuardResistRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of bleed damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float BloodGuardResistRate
		{
			get => Convert.ToSingle(Row["bloodGuardResistRate"].Value);
			set => Row["bloodGuardResistRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of curse damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float CurseGuardResistRate
		{
			get => Convert.ToSingle(Row["curseGuardResistRate"].Value);
			set => Row["curseGuardResistRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier applied to the percentage of stamina damage blocked by this
        /// weapon/shield.
        /// </summary>
		public float StaminaGuardDefRate
		{
			get => Convert.ToSingle(Row["staminaGuardDefRate"].Value);
			set => Row["staminaGuardDefRate"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 0). Overrides slot 0 of
        /// base weapon parameters.
        /// </summary>
		public byte SpEffectId1
		{
			get => Convert.ToByte(Row["spEffectId1"].Value);
			set => Row["spEffectId1"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 1). Overrides slot 1 of
        /// base weapon parameters.
        /// </summary>
		public byte SpEffectId2
		{
			get => Convert.ToByte(Row["spEffectId2"].Value);
			set => Row["spEffectId2"].Value = value;
		}

        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to struck target (slot 2). Overrides slot 2 of
        /// base weapon parameters.
        /// </summary>
		public byte SpEffectId3
		{
			get => Convert.ToByte(Row["spEffectId3"].Value);
			set => Row["spEffectId3"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 0).
        /// Overrides slot 0 of base weapon parameters.
        /// </summary>
		public byte ResidentSpEffectId1
		{
			get => Convert.ToByte(Row["residentSpEffectId1"].Value);
			set => Row["residentSpEffectId1"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 1).
        /// Overrides slot 1 of base weapon parameters.
        /// </summary>
		public byte ResidentSpEffectId2
		{
			get => Convert.ToByte(Row["residentSpEffectId2"].Value);
			set => Row["residentSpEffectId2"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to character with weapon equipped (slot 2).
        /// Overrides slot 2 of base weapon parameters.
        /// </summary>
		public byte ResidentSpEffectId3
		{
			get => Convert.ToByte(Row["residentSpEffectId3"].Value);
			set => Row["residentSpEffectId3"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value to be added to Upgrade Materials field in base weapon
        /// parameters.
        /// </summary>
		public byte MaterialSetId
		{
			get => Convert.ToByte(Row["materialSetId"].Value);
			set => Row["materialSetId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// <DSR> Reinforcement level. Not sure where this is used; it could be
        /// used to calculate the final weapon ID (e.g. 100005 for Dagger+5).
        /// </summary>
		public byte ReinforcementLevel
		{
			get => Convert.ToByte(Row["reinforcementLevel"].Value);
			set => Row["reinforcementLevel"].Value = value;
		}
	}
}