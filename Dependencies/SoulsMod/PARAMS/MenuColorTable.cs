using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class MenuColorTable : RowWrapper
    {
        public MenuColorTable() { }
        public MenuColorTable(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Red value of RGBA color (0-255).
        /// </summary>
        public byte RedChannel
        {
            get => Convert.ToByte(Row["r"].Value);
            set => Row["r"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Green value of RGBA color (0-255).
        /// </summary>
        public byte GreenChannel
        {
            get => Convert.ToByte(Row["g"].Value);
            set => Row["g"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Blue value of RGBA color (0-255).
        /// </summary>
        public byte BlueChannel
        {
            get => Convert.ToByte(Row["b"].Value);
            set => Row["b"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Alpha value of RGBA color (0-255). Higher means less transparent.
        /// </summary>
        public byte AlphaChannel
        {
            get => Convert.ToByte(Row["a"].Value);
            set => Row["a"].Value = value;
        }
    }
}