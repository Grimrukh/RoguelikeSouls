using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class Behavior : RowWrapper
    {
        public Behavior() { }
        public Behavior(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// </summary>
        public int VariationID
        {
            get => Convert.ToInt32(Row["variationId"].Value);
            set => Row["variationId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// This is the ID specified by TAE events that trigger behaviors.
        /// </summary>
        public int BehaviorSubID
        {
            get => Convert.ToInt32(Row["behaviorJudgeId"].Value);
            set => Row["behaviorJudgeId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Unused remnant from Demon's Souls.
        /// </summary>
        public byte EzstateBehaviorType
        {
            get => Convert.ToByte(Row["ezStateBehaviorType_old"].Value);
            set => Row["ezStateBehaviorType_old"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Is the reference ID below an Attack or Bullet ID?
        /// </summary>
        public byte ReferenceType
        {
            get => Convert.ToByte(Row["refType"].Value);
            set => Row["refType"].Value = value;
        }
        // TODO: MULTI_TYPE_FIELD
        /// <summary>
        /// TODO
        // </summary>
        public int RefID
        {
            get => Convert.ToInt32(Row["refId"].Value);
            set => Row["refId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect ID.
        /// </summary>
        public int FXVariationID
        {
            get => Convert.ToInt32(Row["sfxVariationId"].Value);
            set => Row["sfxVariationId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Stamina cost of behavior.
        /// </summary>
        public int StaminaCost
        {
            get => Convert.ToInt32(Row["stamina"].Value);
            set => Row["stamina"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Weapon/shield durability cost of behavior.
        /// </summary>
        public int DurabilityCost
        {
            get => Convert.ToInt32(Row["mp"].Value);
            set => Row["mp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines compatibility with special effects that affect certain
        /// types of attacks. Set to 'Basic' for thrown goods and 'No Category'
        /// otherwise.
        /// </summary>
        public byte Category
        {
            get => Convert.ToByte(Row["category"].Value);
            set => Row["category"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Humanity cost of behavior. Never used.
        /// </summary>
        public byte HumanityCost
        {
            get => Convert.ToByte(Row["heroPoint"].Value);
            set => Row["heroPoint"].Value = value;
        }

    }
}
