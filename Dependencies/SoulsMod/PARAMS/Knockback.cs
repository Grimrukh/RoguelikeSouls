using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Knockback : RowWrapper
    {
		public Knockback() { }
		public Knockback(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
		public float Damage_Min_ContTime
		{
			get => Convert.ToSingle(Row["damage_Min_ContTime"].Value);
			set => Row["damage_Min_ContTime"].Value = value;
		}
		public float Damage_S_ContTime
		{
			get => Convert.ToSingle(Row["damage_S_ContTime"].Value);
			set => Row["damage_S_ContTime"].Value = value;
		}
		public float Damage_M_ContTime
		{
			get => Convert.ToSingle(Row["damage_M_ContTime"].Value);
			set => Row["damage_M_ContTime"].Value = value;
		}
		public float Damage_L_ContTime
		{
			get => Convert.ToSingle(Row["damage_L_ContTime"].Value);
			set => Row["damage_L_ContTime"].Value = value;
		}
		public float Damage_BlowS_ContTime
		{
			get => Convert.ToSingle(Row["damage_BlowS_ContTime"].Value);
			set => Row["damage_BlowS_ContTime"].Value = value;
		}
		public float Damage_BlowM_ContTime
		{
			get => Convert.ToSingle(Row["damage_BlowM_ContTime"].Value);
			set => Row["damage_BlowM_ContTime"].Value = value;
		}
		public float Damage_Strike_ContTime
		{
			get => Convert.ToSingle(Row["damage_Strike_ContTime"].Value);
			set => Row["damage_Strike_ContTime"].Value = value;
		}
		public float Damage_Uppercut_ContTime
		{
			get => Convert.ToSingle(Row["damage_Uppercut_ContTime"].Value);
			set => Row["damage_Uppercut_ContTime"].Value = value;
		}
		public float Damage_Push_ContTime
		{
			get => Convert.ToSingle(Row["damage_Push_ContTime"].Value);
			set => Row["damage_Push_ContTime"].Value = value;
		}
		public float Damage_Breath_ContTime
		{
			get => Convert.ToSingle(Row["damage_Breath_ContTime"].Value);
			set => Row["damage_Breath_ContTime"].Value = value;
		}
		public float Damage_HeadShot_ContTime
		{
			get => Convert.ToSingle(Row["damage_HeadShot_ContTime"].Value);
			set => Row["damage_HeadShot_ContTime"].Value = value;
		}
		public float Guard_S_ContTime
		{
			get => Convert.ToSingle(Row["guard_S_ContTime"].Value);
			set => Row["guard_S_ContTime"].Value = value;
		}
		public float Guard_L_ContTime
		{
			get => Convert.ToSingle(Row["guard_L_ContTime"].Value);
			set => Row["guard_L_ContTime"].Value = value;
		}
		public float Guard_LL_ContTime
		{
			get => Convert.ToSingle(Row["guard_LL_ContTime"].Value);
			set => Row["guard_LL_ContTime"].Value = value;
		}
		public float GuardBrake_ContTime
		{
			get => Convert.ToSingle(Row["guardBrake_ContTime"].Value);
			set => Row["guardBrake_ContTime"].Value = value;
		}
		public float Damage_Min_DecTime
		{
			get => Convert.ToSingle(Row["damage_Min_DecTime"].Value);
			set => Row["damage_Min_DecTime"].Value = value;
		}
		public float Damage_S_DecTime
		{
			get => Convert.ToSingle(Row["damage_S_DecTime"].Value);
			set => Row["damage_S_DecTime"].Value = value;
		}
		public float Damage_M_DecTime
		{
			get => Convert.ToSingle(Row["damage_M_DecTime"].Value);
			set => Row["damage_M_DecTime"].Value = value;
		}
		public float Damage_L_DecTime
		{
			get => Convert.ToSingle(Row["damage_L_DecTime"].Value);
			set => Row["damage_L_DecTime"].Value = value;
		}
		public float Damage_BlowS_DecTime
		{
			get => Convert.ToSingle(Row["damage_BlowS_DecTime"].Value);
			set => Row["damage_BlowS_DecTime"].Value = value;
		}
		public float Damage_BlowM_DecTime
		{
			get => Convert.ToSingle(Row["damage_BlowM_DecTime"].Value);
			set => Row["damage_BlowM_DecTime"].Value = value;
		}
		public float Damage_Strike_DecTime
		{
			get => Convert.ToSingle(Row["damage_Strike_DecTime"].Value);
			set => Row["damage_Strike_DecTime"].Value = value;
		}
		public float Damage_Uppercut_DecTime
		{
			get => Convert.ToSingle(Row["damage_Uppercut_DecTime"].Value);
			set => Row["damage_Uppercut_DecTime"].Value = value;
		}
		public float Damage_Push_DecTime
		{
			get => Convert.ToSingle(Row["damage_Push_DecTime"].Value);
			set => Row["damage_Push_DecTime"].Value = value;
		}
		public float Damage_Breath_DecTime
		{
			get => Convert.ToSingle(Row["damage_Breath_DecTime"].Value);
			set => Row["damage_Breath_DecTime"].Value = value;
		}
		public float Damage_HeadShot_DecTime
		{
			get => Convert.ToSingle(Row["damage_HeadShot_DecTime"].Value);
			set => Row["damage_HeadShot_DecTime"].Value = value;
		}
		public float Guard_S_DecTime
		{
			get => Convert.ToSingle(Row["guard_S_DecTime"].Value);
			set => Row["guard_S_DecTime"].Value = value;
		}
		public float Guard_L_DecTime
		{
			get => Convert.ToSingle(Row["guard_L_DecTime"].Value);
			set => Row["guard_L_DecTime"].Value = value;
		}
		public float Guard_LL_DecTime
		{
			get => Convert.ToSingle(Row["guard_LL_DecTime"].Value);
			set => Row["guard_LL_DecTime"].Value = value;
		}
		public float GuardBrake_DecTime
		{
			get => Convert.ToSingle(Row["guardBrake_DecTime"].Value);
			set => Row["guardBrake_DecTime"].Value = value;
		}

	}
}
