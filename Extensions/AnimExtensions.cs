using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SoulsFormats;
using static SoulsFormats.TAE.Animation;
using static SoulsFormats.TAE;

namespace SoulsFormatsMod.Extensions
{
    public static class AnimExtensions
    {
        #region Utility Methods

        public static Template DS1 = Template.ReadXMLFile("RES\\TAE.Template.DS1.xml");

        /// <summary>
        /// Returns whether the animation's internal ID is within the specified range (inclusive).
        /// </summary>
        public static bool InRange(this Animation anim, int low, int high) => anim.ID >= low && anim.ID <= high;

        /// <summary>
        /// Removes and returns the nth occurance of a jumptable entry with the specified value in the animation.
        /// </summary>
        public static Event RemoveJumpTable(this Animation anim, int id, int n = 0, bool setValue = false)
        {
            TAE.Event evt = anim.FindJumpTable(id, n, setValue);
            if (evt != null) anim.Events.Remove(evt);
            return evt;
        }

        /// <summary>
        /// Returns the nth occurance of a jumptable entry with the specified value in the animation.
        /// </summary>
        public static Event FindJumpTable(this Animation anim, int id, int n = 0, bool setValue = false)
        {
            int type = setValue ? 300 : 0;
            var list = anim.Events.Where(e => e.Type == type && (int)e.Parameters["JumpTableID"] == id);
            if (n > list.Count() - 1) return null;
            return list.ElementAt(n);
        }

        /// <summary>
        /// Removes and returns the nth occurance of the specified event type in the animation.
        /// </summary>
        public static Event RemoveEvent(this Animation anim, int id, int n = 0)
        {
            TAE.Event evt = anim.FindEvent(id, n);
            if (evt != null) anim.Events.Remove(evt);
            return evt;
        }

        /// <summary>
        /// Returns the nth occurance of the specified event type in the animation.
        /// </summary>
        public static Event FindEvent(this Animation anim, int id, int n = 0)
        {
            IEnumerable<TAE.Event> list = anim.Events.Where(e => e.Type == id);
            if (n > list.Count() - 1) return null;
            return list.ElementAt(n);
        }

        /// <summary>
        /// Imports all events and motion data from a different animation.
        /// </summary>
        public static void SetReference(this Animation anim, long fullAnimId) => anim.MiniHeader = new AnimMiniHeader.ImportOtherAnim() { ImportFromAnimID = (int)fullAnimId };

        /// <summary>
        /// Copies all events and motion data from another animation into this one.
        /// </summary>
        public static void CloneReference(this Animation anim, Animation src, int fullSrcId)
        {
            anim.MiniHeader = new AnimMiniHeader.Standard()
            {
                ImportFromAnimID = fullSrcId,
                ImportsHKX = true,
                ImportsEvents = false
            };

            anim.Events.Clear();
            foreach (var srcEvt in src.Events)
            {
                Event tgtEvt = new Event(srcEvt.StartTime, srcEvt.EndTime, srcEvt.Type, srcEvt.Unk04, false, srcEvt.Template);
                tgtEvt.SetParameterBytes(false, srcEvt.GetParameterBytes(false));
                anim.Events.Add(tgtEvt);
            }
        }

        public static float LatestEventEndTime(this Animation anim)
        {
            if (anim.Events.Count == 0) return 0;
            return anim.Events.Select(a => a.EndTime).Max();
        }

        public static void ApplyEffect(this Animation anim, long SpEffectId, float startTime = 0, float endTime = 0)
        {
            if (endTime == 0) endTime = anim.LatestEventEndTime();
            Event evt = new Event(startTime, endTime, 66, 0, false, DS1[0][66]);
            evt.Parameters["SpEffectID"] = SpEffectId;
            anim.Events.Add(evt);
        }
        #endregion
    }
}
