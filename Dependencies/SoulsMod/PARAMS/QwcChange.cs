using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
	public class QwcChange : RowWrapper
    {
		public QwcChange() { }
		public QwcChange(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

		public short PcAttrB
		{
			get => Convert.ToInt16(Row["pcAttrB"].Value);
			set => Row["pcAttrB"].Value = value;
		}
		public short PcAttrW
		{
			get => Convert.ToInt16(Row["pcAttrW"].Value);
			set => Row["pcAttrW"].Value = value;
		}
		public short PcAttrL
		{
			get => Convert.ToInt16(Row["pcAttrL"].Value);
			set => Row["pcAttrL"].Value = value;
		}
		public short PcAttrR
		{
			get => Convert.ToInt16(Row["pcAttrR"].Value);
			set => Row["pcAttrR"].Value = value;
		}
		public short AreaAttrB
		{
			get => Convert.ToInt16(Row["areaAttrB"].Value);
			set => Row["areaAttrB"].Value = value;
		}
		public short AreaAttrW
		{
			get => Convert.ToInt16(Row["areaAttrW"].Value);
			set => Row["areaAttrW"].Value = value;
		}
		public short AreaAttrL
		{
			get => Convert.ToInt16(Row["areaAttrL"].Value);
			set => Row["areaAttrL"].Value = value;
		}
		public short AreaAttrR
		{
			get => Convert.ToInt16(Row["areaAttrR"].Value);
			set => Row["areaAttrR"].Value = value;
		}
	}
}