using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Move : RowWrapper
    {
        public Move() { }
        public Move(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int StayId
		{
			get => Convert.ToInt32(Row["stayId"].Value);
			set => Row["stayId"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int WalkF
		{
			get => Convert.ToInt32(Row["walkF"].Value);
			set => Row["walkF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int WalkB
		{
			get => Convert.ToInt32(Row["walkB"].Value);
			set => Row["walkB"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int WalkL
		{
			get => Convert.ToInt32(Row["walkL"].Value);
			set => Row["walkL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int WalkR
		{
			get => Convert.ToInt32(Row["walkR"].Value);
			set => Row["walkR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int DashF
		{
			get => Convert.ToInt32(Row["dashF"].Value);
			set => Row["dashF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int DashB
		{
			get => Convert.ToInt32(Row["dashB"].Value);
			set => Row["dashB"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int DashL
		{
			get => Convert.ToInt32(Row["dashL"].Value);
			set => Row["dashL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int DashR
		{
			get => Convert.ToInt32(Row["dashR"].Value);
			set => Row["dashR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int SuperDash
		{
			get => Convert.ToInt32(Row["superDash"].Value);
			set => Row["superDash"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int EscapeF
		{
			get => Convert.ToInt32(Row["escapeF"].Value);
			set => Row["escapeF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int EscapeB
		{
			get => Convert.ToInt32(Row["escapeB"].Value);
			set => Row["escapeB"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int EscapeL
		{
			get => Convert.ToInt32(Row["escapeL"].Value);
			set => Row["escapeL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int EscapeR
		{
			get => Convert.ToInt32(Row["escapeR"].Value);
			set => Row["escapeR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int TurnL
		{
			get => Convert.ToInt32(Row["turnL"].Value);
			set => Row["turnL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int TrunR
		{
			get => Convert.ToInt32(Row["trunR"].Value);
			set => Row["trunR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int LargeTurnL
		{
			get => Convert.ToInt32(Row["largeTurnL"].Value);
			set => Row["largeTurnL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int LargeTurnR
		{
			get => Convert.ToInt32(Row["largeTurnR"].Value);
			set => Row["largeTurnR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int StepMove
		{
			get => Convert.ToInt32(Row["stepMove"].Value);
			set => Row["stepMove"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyStay
		{
			get => Convert.ToInt32(Row["flyStay"].Value);
			set => Row["flyStay"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyWalkF
		{
			get => Convert.ToInt32(Row["flyWalkF"].Value);
			set => Row["flyWalkF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyWalkFL
		{
			get => Convert.ToInt32(Row["flyWalkFL"].Value);
			set => Row["flyWalkFL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyWalkFR
		{
			get => Convert.ToInt32(Row["flyWalkFR"].Value);
			set => Row["flyWalkFR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyWalkFL2
		{
			get => Convert.ToInt32(Row["flyWalkFL2"].Value);
			set => Row["flyWalkFL2"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyWalkFR2
		{
			get => Convert.ToInt32(Row["flyWalkFR2"].Value);
			set => Row["flyWalkFR2"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyDashF
		{
			get => Convert.ToInt32(Row["flyDashF"].Value);
			set => Row["flyDashF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyDashFL
		{
			get => Convert.ToInt32(Row["flyDashFL"].Value);
			set => Row["flyDashFL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyDashFR
		{
			get => Convert.ToInt32(Row["flyDashFR"].Value);
			set => Row["flyDashFR"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyDashFL2
		{
			get => Convert.ToInt32(Row["flyDashFL2"].Value);
			set => Row["flyDashFL2"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int FlyDashFR2
		{
			get => Convert.ToInt32(Row["flyDashFR2"].Value);
			set => Row["flyDashFR2"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID.
        /// </summary>
		public int DashEscapeF
		{
			get => Convert.ToInt32(Row["dashEscapeF"].Value);
			set => Row["dashEscapeF"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID. (Never used.)
        /// </summary>
		public int DashEscapeB
		{
			get => Convert.ToInt32(Row["dashEscapeB"].Value);
			set => Row["dashEscapeB"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID. (Never used.)
        /// </summary>
		public int DashEscapeL
		{
			get => Convert.ToInt32(Row["dashEscapeL"].Value);
			set => Row["dashEscapeL"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation ID. (Never used.)
        /// </summary>
		public int DashEscapeR
		{
			get => Convert.ToInt32(Row["dashEscapeR"].Value);
			set => Row["dashEscapeR"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Movement settings for analog stick version of movement. (Unknown
        /// enum.)
        /// </summary>
		public int AnalogMoveParamId
		{
			get => Convert.ToInt32(Row["analogMoveParamId"].Value);
			set => Row["analogMoveParamId"].Value = value;
		}
	}
}