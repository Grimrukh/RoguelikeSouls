using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class ArmorUpgrade : RowWrapper
    {
		public ArmorUpgrade() { }
		public ArmorUpgrade(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
		// DEFAULT_VISIBLE: True
		/// <summary>
		/// Multiplier for physical defense at this upgrade level.
		/// </summary>
		public float PhysicalDefenseMultiplier
		{
			get => Convert.ToSingle(Row["physicsDefRate"].Value);
			set => Row["physicsDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for magic defense at this upgrade level.
        /// </summary>
		public float MagicDefenseMultiplier
		{
			get => Convert.ToSingle(Row["magicDefRate"].Value);
			set => Row["magicDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for fire defense at this upgrade level.
        /// </summary>
		public float FireDefenseMultiplier
		{
			get => Convert.ToSingle(Row["fireDefRate"].Value);
			set => Row["fireDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for lightning defense at this upgrade level.
        /// </summary>
		public float LightningDefenseMultiplier
		{
			get => Convert.ToSingle(Row["thunderDefRate"].Value);
			set => Row["thunderDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for slash defense at this upgrade level.
        /// </summary>
		public float SlashDefRate
		{
			get => Convert.ToSingle(Row["slashDefRate"].Value);
			set => Row["slashDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for strike defense at this upgrade level.
        /// </summary>
		public float BlowDefRate
		{
			get => Convert.ToSingle(Row["blowDefRate"].Value);
			set => Row["blowDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for thrust defense at this upgrade level.
        /// </summary>
		public float ThrustDefRate
		{
			get => Convert.ToSingle(Row["thrustDefRate"].Value);
			set => Row["thrustDefRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for poison resistance at this upgrade level.
        /// </summary>
		public float PoisonResistanceMultiplier
		{
			get => Convert.ToSingle(Row["resistPoisonRate"].Value);
			set => Row["resistPoisonRate"].Value = value;
		}

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for toxic resistance at this upgrade level.
        /// </summary>
		public float ToxicResistanceMultiplier
		{
			get => Convert.ToSingle(Row["resistDiseaseRate"].Value);
			set => Row["resistDiseaseRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for bleed resistance at this upgrade level.
        /// </summary>
		public float BleedResistanceMultiplier
		{
			get => Convert.ToSingle(Row["resistBloodRate"].Value);
			set => Row["resistBloodRate"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for curse resistance at this upgrade level.
        /// </summary>
		public float CurseResistanceMultiplier
		{
			get => Convert.ToSingle(Row["resistCurseRate"].Value);
			set => Row["resistCurseRate"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (first of three).
        /// </summary>
		public byte ResidentSpEffectId1
		{
			get => Convert.ToByte(Row["residentSpEffectId1"].Value);
			set => Row["residentSpEffectId1"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (second of three).
        /// </summary>
		public byte ResidentSpEffectId2
		{
			get => Convert.ToByte(Row["residentSpEffectId2"].Value);
			set => Row["residentSpEffectId2"].Value = value;
		}
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect granted to wearer (third of three).
        /// </summary>
		public byte ResidentSpEffectId3
		{
			get => Convert.ToByte(Row["residentSpEffectId3"].Value);
			set => Row["residentSpEffectId3"].Value = value;
		}
        // LINK_STRING: <Params:UpgradeMaterials>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Upgrade material set for reinforcement.
        /// </summary>
		public byte MaterialSetId
		{
			get => Convert.ToByte(Row["materialSetId"].Value);
			set => Row["materialSetId"].Value = value;
		}
	}
}