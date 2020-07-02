using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class ObjAct : RowWrapper
    {
        public ObjAct() { }
        public ObjAct(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <Text:EventText>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Message displayed in dialog box upon successful action (e.g. 'Door
        /// opened').
        /// </summary>
		public int ActionEnableMsgId
		{
			get => Convert.ToInt32(Row["actionEnableMsgId"].Value);
			set => Row["actionEnableMsgId"].Value = value;
		}
        // LINK_STRING: <Text:EventText>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Message displayed in dialog box upon failed action (e.g. 'Door
        /// locked').
        /// </summary>
		public int ActionFailedMsgId
		{
			get => Convert.ToInt32(Row["actionFailedMsgId"].Value);
			set => Row["actionFailedMsgId"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Action will always be successful if this flag is enabled.
        /// </summary>
		public int SpQualifiedPassEventFlag
		{
			get => Convert.ToInt32(Row["spQualifiedPassEventFlag"].Value);
			set => Row["spQualifiedPassEventFlag"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance from action model point at which the object action
        /// will be prompted.
        /// </summary>
		public ushort ValidDist
		{
			get => Convert.ToUInt16(Row["validDist"].Value);
			set => Row["validDist"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation played by a player character when they successfully activate
        /// the object.
        /// </summary>
		public ushort PlayerAnimId
		{
			get => Convert.ToUInt16(Row["playerAnimId"].Value);
			set => Row["playerAnimId"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation played by a non-player character when they successfully
        /// activate the object.
        /// </summary>
		public ushort ChrAnimId
		{
			get => Convert.ToUInt16(Row["chrAnimId"].Value);
			set => Row["chrAnimId"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public ushort SpQualifiedId
		{
			get => Convert.ToUInt16(Row["spQualifiedId"].Value);
			set => Row["spQualifiedId"].Value = value;
		}
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
		public ushort SpQualifiedId2
		{
			get => Convert.ToUInt16(Row["spQualifiedId2"].Value);
			set => Row["spQualifiedId2"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Model point that specifies where the action occurs on the object (for
        /// snapping the player and distance check).
        /// </summary>
		public byte ObjDummyId
		{
			get => Convert.ToByte(Row["objDummyId"].Value);
			set => Row["objDummyId"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation played by the object when it is successfully activated.
        /// </summary>
		public byte ObjAnimId
		{
			get => Convert.ToByte(Row["objAnimId"].Value);
			set => Row["objAnimId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum angle between the character's forward direction and the
        /// direction to the object action point for the action prompt to appear.
        /// </summary>
		public byte ValidPlayerAngle
		{
			get => Convert.ToByte(Row["validPlayerAngle"].Value);
			set => Row["validPlayerAngle"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of first success condition.
        /// </summary>
		public byte SpQualifiedType
		{
			get => Convert.ToByte(Row["spQualifiedType"].Value);
			set => Row["spQualifiedType"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of second success condition.
        /// </summary>
		public byte SpQualifiedType2
		{
			get => Convert.ToByte(Row["spQualifiedType2"].Value);
			set => Row["spQualifiedType2"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum angle between the object's forward direction and the direction
        /// to the player for the action prompt to appear.
        /// </summary>
		public byte ValidObjAngle
		{
			get => Convert.ToByte(Row["validObjAngle"].Value);
			set => Row["validObjAngle"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of method used to snap the character to the object before
        /// animations are played.
        /// </summary>
		public byte ChrSorbType
		{
			get => Convert.ToByte(Row["chrSorbType"].Value);
			set => Row["chrSorbType"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// I believe this is the delay between successful object activation and
        /// the outgoing 'success' trigger used by game events.
        /// </summary>
		public byte EventKickTiming
		{
			get => Convert.ToByte(Row["eventKickTiming"].Value);
			set => Row["eventKickTiming"].Value = value;
		}

	}
}