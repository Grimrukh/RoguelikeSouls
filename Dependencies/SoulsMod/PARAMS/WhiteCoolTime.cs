using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class WhiteCoolTime : RowWrapper
    {
        public WhiteCoolTime() { }
        public WhiteCoolTime(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public float TimeLimit0
        {
            get => Convert.ToSingle(Row["timeLimit0"].Value);
            set => Row["timeLimit0"].Value = value;
        }
        public float TimeLimit1
        {
            get => Convert.ToSingle(Row["timeLimit1"].Value);
            set => Row["timeLimit1"].Value = value;
        }
        public float TimeLimit2
        {
            get => Convert.ToSingle(Row["timeLimit2"].Value);
            set => Row["timeLimit2"].Value = value;
        }
        public float TimeLimit3
        {
            get => Convert.ToSingle(Row["timeLimit3"].Value);
            set => Row["timeLimit3"].Value = value;
        }
    }
}
