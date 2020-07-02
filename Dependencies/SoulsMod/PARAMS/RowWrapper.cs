using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SoulsFormats;

namespace SoulsFormatsMod.PARAMS
{
    public abstract class RowWrapper
    {
        internal GameParamHandler GPARAM { get; }
        internal TextHandler Text { get; }

        public PARAM.Row Row { get; set; }

        public string Name
        {
            get => Row.Name;
            set => Row.Name = value;
        }

        public long ID => Row.ID;

        public static implicit operator long(RowWrapper r) => r.ID;

        public static implicit operator int(RowWrapper r) => (int) r.ID;

        public RowWrapper() { }

        public RowWrapper(PARAM.Row r, GameParamHandler gParam, TextHandler text)
        {
            GPARAM = gParam;
            Text = text;
            Row = r;
        }

        public void CopyField(RowWrapper otherRow, string fieldName)
        {
            Row[fieldName].Value = otherRow.Row[fieldName].Value;
        }
    }

    public static class MiscUtil
    {
        public static bool AsBoolean(byte b) => b == 1;
    }
}
