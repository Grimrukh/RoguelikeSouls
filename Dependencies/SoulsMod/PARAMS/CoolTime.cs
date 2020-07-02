using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class CoolTime : RowWrapper
    {
        public CoolTime() { }
        public CoolTime(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public float LimitationTime_0
        {
            get => Convert.ToSingle(Row["limitationTime_0"].Value);
            set => Row["limitationTime_0"].Value = value;
        }
        public float ObservationTime_0
        {
            get => Convert.ToSingle(Row["observationTime_0"].Value);
            set => Row["observationTime_0"].Value = value;
        }
        public float LimitationTime_1
        {
            get => Convert.ToSingle(Row["limitationTime_1"].Value);
            set => Row["limitationTime_1"].Value = value;
        }
        public float ObservationTime_1
        {
            get => Convert.ToSingle(Row["observationTime_1"].Value);
            set => Row["observationTime_1"].Value = value;
        }
        public float LimitationTime_2
        {
            get => Convert.ToSingle(Row["limitationTime_2"].Value);
            set => Row["limitationTime_2"].Value = value;
        }
        public float ObservationTime_2
        {
            get => Convert.ToSingle(Row["observationTime_2"].Value);
            set => Row["observationTime_2"].Value = value;
        }
        public float LimitationTime_3
        {
            get => Convert.ToSingle(Row["limitationTime_3"].Value);
            set => Row["limitationTime_3"].Value = value;
        }
        public float ObservationTime_3
        {
            get => Convert.ToSingle(Row["observationTime_3"].Value);
            set => Row["observationTime_3"].Value = value;
        }
    }
}
