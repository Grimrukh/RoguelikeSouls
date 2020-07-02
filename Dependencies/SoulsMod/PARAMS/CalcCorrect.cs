using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class CalcCorrect : RowWrapper
    {
        public CalcCorrect() { }
        public CalcCorrect(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        public float StageMaxVal0
        {
            get => Convert.ToSingle(Row["stageMaxVal0"].Value);
            set => Row["stageMaxVal0"].Value = value;
        }
        public float StageMaxVal1
        {
            get => Convert.ToSingle(Row["stageMaxVal1"].Value);
            set => Row["stageMaxVal1"].Value = value;
        }
        public float StageMaxVal2
        {
            get => Convert.ToSingle(Row["stageMaxVal2"].Value);
            set => Row["stageMaxVal2"].Value = value;
        }
        public float StageMaxVal3
        {
            get => Convert.ToSingle(Row["stageMaxVal3"].Value);
            set => Row["stageMaxVal3"].Value = value;
        }
        public float StageMaxVal4
        {
            get => Convert.ToSingle(Row["stageMaxVal4"].Value);
            set => Row["stageMaxVal4"].Value = value;
        }
        public float StageMaxGrowVal0
        {
            get => Convert.ToSingle(Row["stageMaxGrowVal0"].Value);
            set => Row["stageMaxGrowVal0"].Value = value;
        }
        public float StageMaxGrowVal1
        {
            get => Convert.ToSingle(Row["stageMaxGrowVal1"].Value);
            set => Row["stageMaxGrowVal1"].Value = value;
        }
        public float StageMaxGrowVal2
        {
            get => Convert.ToSingle(Row["stageMaxGrowVal2"].Value);
            set => Row["stageMaxGrowVal2"].Value = value;
        }
        public float StageMaxGrowVal3
        {
            get => Convert.ToSingle(Row["stageMaxGrowVal3"].Value);
            set => Row["stageMaxGrowVal3"].Value = value;
        }
        public float StageMaxGrowVal4
        {
            get => Convert.ToSingle(Row["stageMaxGrowVal4"].Value);
            set => Row["stageMaxGrowVal4"].Value = value;
        }
        public float AdjPt_maxGrowVal0
        {
            get => Convert.ToSingle(Row["adjPt_maxGrowVal0"].Value);
            set => Row["adjPt_maxGrowVal0"].Value = value;
        }
        public float AdjPt_maxGrowVal1
        {
            get => Convert.ToSingle(Row["adjPt_maxGrowVal1"].Value);
            set => Row["adjPt_maxGrowVal1"].Value = value;
        }
        public float AdjPt_maxGrowVal2
        {
            get => Convert.ToSingle(Row["adjPt_maxGrowVal2"].Value);
            set => Row["adjPt_maxGrowVal2"].Value = value;
        }
        public float AdjPt_maxGrowVal3
        {
            get => Convert.ToSingle(Row["adjPt_maxGrowVal3"].Value);
            set => Row["adjPt_maxGrowVal3"].Value = value;
        }
        public float AdjPt_maxGrowVal4
        {
            get => Convert.ToSingle(Row["adjPt_maxGrowVal4"].Value);
            set => Row["adjPt_maxGrowVal4"].Value = value;
        }
        public float Init_inclination_soul
        {
            get => Convert.ToSingle(Row["init_inclination_soul"].Value);
            set => Row["init_inclination_soul"].Value = value;
        }
        public float Adjustment_value
        {
            get => Convert.ToSingle(Row["adjustment_value"].Value);
            set => Row["adjustment_value"].Value = value;
        }
        public float Boundry_inclination_soul
        {
            get => Convert.ToSingle(Row["boundry_inclination_soul"].Value);
            set => Row["boundry_inclination_soul"].Value = value;
        }
        public float Boundry_value
        {
            get => Convert.ToSingle(Row["boundry_value"].Value);
            set => Row["boundry_value"].Value = value;
        }
    }
}
