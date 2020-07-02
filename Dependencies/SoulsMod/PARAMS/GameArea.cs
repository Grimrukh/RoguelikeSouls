using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
	public class GameArea : RowWrapper
	{
		public GameArea() { }
		public GameArea(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		// DEFAULT_VISIBLE: True
		/// <summary>
		/// Souls awarded (after delay) when boss is defeated with no summons.
		/// </summary>
		public uint BonusSoul_single
		{
			get => Convert.ToUInt32(Row["bonusSoul_single"].Value);
			set => Row["bonusSoul_single"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Souls awarded to each player (after delay) when boss is defeated with
        /// summons.
        /// </summary>
		public uint BonusSoul_multi
		{
			get => Convert.ToUInt32(Row["bonusSoul_multi"].Value);
			set => Row["bonusSoul_multi"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// First flag for recording number of humanity drops awarded in boss's
        /// area.
        /// </summary>
		public int HumanityPointCountFlagIdTop
		{
			get => Convert.ToInt32(Row["humanityPointCountFlagIdTop"].Value);
			set => Row["humanityPointCountFlagIdTop"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// first Humanity.
        /// </summary>
		public ushort HumanityDropPoint1
		{
			get => Convert.ToUInt16(Row["humanityDropPoint1"].Value);
			set => Row["humanityDropPoint1"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// second Humanity.
        /// </summary>
		public ushort HumanityDropPoint2
		{
			get => Convert.ToUInt16(Row["humanityDropPoint2"].Value);
			set => Row["humanityDropPoint2"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// third Humanity.
        /// </summary>
		public ushort HumanityDropPoint3
		{
			get => Convert.ToUInt16(Row["humanityDropPoint3"].Value);
			set => Row["humanityDropPoint3"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// fourth Humanity.
        /// </summary>
		public ushort HumanityDropPoint4
		{
			get => Convert.ToUInt16(Row["humanityDropPoint4"].Value);
			set => Row["humanityDropPoint4"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// fifth Humanity.
        /// </summary>
		public ushort HumanityDropPoint5
		{
			get => Convert.ToUInt16(Row["humanityDropPoint5"].Value);
			set => Row["humanityDropPoint5"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// sixth Humanity.
        /// </summary>
		public ushort HumanityDropPoint6
		{
			get => Convert.ToUInt16(Row["humanityDropPoint6"].Value);
			set => Row["humanityDropPoint6"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// seventh Humanity.
        /// </summary>
		public ushort HumanityDropPoint7
		{
			get => Convert.ToUInt16(Row["humanityDropPoint7"].Value);
			set => Row["humanityDropPoint7"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// eighth Humanity.
        /// </summary>
		public ushort HumanityDropPoint8
		{
			get => Convert.ToUInt16(Row["humanityDropPoint8"].Value);
			set => Row["humanityDropPoint8"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// ninth Humanity.
        /// </summary>
		public ushort HumanityDropPoint9
		{
			get => Convert.ToUInt16(Row["humanityDropPoint9"].Value);
			set => Row["humanityDropPoint9"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of 'points' needed from killing enemies in the boss area for
        /// final Humanity.
        /// </summary>
		public ushort HumanityDropPoint10
		{
			get => Convert.ToUInt16(Row["humanityDropPoint10"].Value);
			set => Row["humanityDropPoint10"].Value = value;
		}
	}
}
