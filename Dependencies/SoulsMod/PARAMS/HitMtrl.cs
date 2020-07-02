using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class HitMtrl : RowWrapper
    {
        public HitMtrl() { }
        public HitMtrl(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Multiplier for foot sound effect radius on this terrain.
        /// </summary>
        public float SoundRadiusMultiplier
        {
            get => Convert.ToSingle(Row["aiVolumeRate"].Value);
            set => Row["aiVolumeRate"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to character walking on terrain (first of two).
        /// </summary>
        public int SpecialEffect1
        {
            get => Convert.ToInt32(Row["spEffectIdOnHit0"].Value);
            set => Row["spEffectIdOnHit0"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to character walking on terrain (second of
        /// two).
        /// </summary>
        public int SpecialEffect2
        {
            get => Convert.ToInt32(Row["spEffectIdOnHit1"].Value);
            set => Row["spEffectIdOnHit1"].Value = value;
        }
        public byte FootEffectHeightType
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the height at which foot impact effects are generated.
        /// </summary>
        {

            get => Convert.ToByte(Row["footEffectHeightType:2"].Value);
            set => Row["footEffectHeightType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines the direction of foot impact effects.
        /// </summary>
        public byte FootEffectDirectionType
        {
            get => Convert.ToByte(Row["footEffectDirType:2"].Value);
            set => Row["footEffectDirType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines distance from floor collision at which effects are applied.
        /// </summary>
        public byte TerrainHeightType
        {
            get => Convert.ToByte(Row["floorHeightType:2"].Value);
            set => Row["floorHeightType"].Value = value;
        }
    }
}
