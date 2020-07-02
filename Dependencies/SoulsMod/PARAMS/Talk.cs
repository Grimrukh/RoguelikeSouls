using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Talk : RowWrapper
    {
        public Talk() { }
        public Talk(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <Text:Conversations>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Text ID for dialogue subtitle.
        /// </summary>
		public int MsgId
		{
			get => Convert.ToInt32(Row["msgId"].Value);
			set => Row["msgId"].Value = value;
		}
        // LINK_STRING: <Sound:Voice>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sound ID (voice) for dialogue.
        /// </summary>
		public int VoiceId
		{
			get => Convert.ToInt32(Row["voiceId"].Value);
			set => Row["voiceId"].Value = value;
		}
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation used for talking (-1 for default, or no animation). Usually
        /// 7000 (e.g. Fair Lady) or 7001 (e.g. Andre) when used.
        /// </summary>
		public int MotionId
		{
			get => Convert.ToInt32(Row["motionId"].Value);
			set => Row["motionId"].Value = value;
		}
        // LINK_STRING: <Params:Conversations>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Conversation ID to use instead if the player has 'returned' to this
        /// conversation. Used exactly once for one line by the Crestfallen
        /// Warrior, so presumably works, but probably not useful.
        /// </summary>
		public int ReturnPos
		{
			get => Convert.ToInt32(Row["returnPos"].Value);
			set => Row["returnPos"].Value = value;
		}
        // LINK_STRING: <Params:Conversations>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Conversation ID to use as 'reaction'. Always -1.
        /// </summary>
		public int ReactionId
		{
			get => Convert.ToInt32(Row["reactionId"].Value);
			set => Row["reactionId"].Value = value;
		}
        // LINK_STRING: <Flag>
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Flag that is enabled when conversation plays (I assume). Used exactly
        /// once, for the same Crestfallen Warrior line that uses the
        /// ReturnConversation field.
        /// </summary>
		public int EventId
		{
			get => Convert.ToInt32(Row["eventId"].Value);
			set => Row["eventId"].Value = value;
		}
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, specified TalkingAnimation will loop while dialogue is being
        /// spoken. Always True for any entry that has a non-zero
        /// TalkingAnimation.
        /// </summary>
		public byte IsMotionLoop
		{
			get => Convert.ToByte(Row["isMotionLoop"].Value);
			set => Row["isMotionLoop"].Value = value;
		}
	}
}
