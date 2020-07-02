using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class QwcJudge : RowWrapper
    {
		public QwcJudge() { }
		public QwcJudge(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		public short PcJudgeUnderWB
		{
			get => Convert.ToInt16(Row["pcJudgeUnderWB"].Value);
			set => Row["pcJudgeUnderWB"].Value = value;
		}
		public short PcJudgeTopWB
		{
			get => Convert.ToInt16(Row["pcJudgeTopWB"].Value);
			set => Row["pcJudgeTopWB"].Value = value;
		}
		public short PcJudgeUnderLR
		{
			get => Convert.ToInt16(Row["pcJudgeUnderLR"].Value);
			set => Row["pcJudgeUnderLR"].Value = value;
		}
		public short PcJudgeTopLR
		{
			get => Convert.ToInt16(Row["pcJudgeTopLR"].Value);
			set => Row["pcJudgeTopLR"].Value = value;
		}
		public short AreaJudgeUnderWB
		{
			get => Convert.ToInt16(Row["areaJudgeUnderWB"].Value);
			set => Row["areaJudgeUnderWB"].Value = value;
		}
		public short AreaJudgeTopWB
		{
			get => Convert.ToInt16(Row["areaJudgeTopWB"].Value);
			set => Row["areaJudgeTopWB"].Value = value;
		}
		public short AreaJudgeUnderLR
		{
			get => Convert.ToInt16(Row["areaJudgeUnderLR"].Value);
			set => Row["areaJudgeUnderLR"].Value = value;
		}
		public short AreaJudgeTopLR
		{
			get => Convert.ToInt16(Row["areaJudgeTopLR"].Value);
			set => Row["areaJudgeTopLR"].Value = value;
		}
	}
}