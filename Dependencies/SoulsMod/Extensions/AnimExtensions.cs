using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using SoulsFormats;
using SoulsFormatsMod.PARAMS;
using static SoulsFormats.TAE.Animation;
using static SoulsFormats.TAE;

namespace SoulsFormatsMod.Extensions
{
    public static class AnimExtensions
    {
        #region Utility Methods

        public static Template DS1 = Template.ReadXMLFile("RES\\TAE.Template.DS1.xml");

        public static Event NewEvent(this Animation anim, long id, float start = 0, float end = 0, params dynamic[] args)
        {
            if (end == 0) end = anim.LatestEventEndTime();
            Event evt = new Event(start, end, (int)id, 0, false, DS1[0][(int) id]);
            evt.ApplyTemplateWithDefaultValues(false, DS1[0][(int)id]);
            for (int i = 0; i < args.Length; i += 2)
            {
                dynamic field = args[i];
                dynamic val = args[i + 1];
                evt.Parameters[field] = val;
            }
            anim.Events.Add(evt);
            return evt;
        }

        public static Event NewJumpTable(this Animation anim, int id, float start, float end) => anim.NewEvent(0, start, end, "JumpTableID", id);

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
            var list = anim.Events.Where(e => e.Type == type && Convert.ToInt32(e.Parameters["JumpTableID"]) == id);
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
        /// Returns an enumerable containing all distinct FFX IDs referenced in the TAE.
        /// </summary>
        public static IEnumerable<int> GetAllFFXIDs(this TAE tae, int variation, GameParamHandler gParam)
        {
            List<int> FFX = new List<int>();
            foreach (Animation anim in tae.Animations)
            {
                foreach (Event evt in anim.Events)
                {
                    if (evt.Type >= 96 && evt.Type <= 121 && evt.Type != 116 && evt.Type != 120)
                    {
                        FFX.Add(Convert.ToInt32(evt.Parameters["FFXID"]));
                    }
                    else if (evt.Type == 2)
                    {
                        int subID = Convert.ToInt32(evt.Parameters["BehaviorSubID"]);
                        int behID = 200000000 + (variation * 1000) + subID;
                        if (!gParam.BehaviorsNPC.ContainsKey(behID))
                            continue;
                        Behavior beh = gParam.BehaviorsNPC[behID];
                        if (beh.ReferenceType != 1) 
                            continue;
                        if (!gParam.Bullets.ContainsKey(beh.RefID)) 
                            continue;
                        Bullet bullet = gParam.Bullets[beh.RefID];
                        FFX.Add(bullet.FlickFX);
                        FFX.Add(bullet.ImpactFX);
                        FFX.Add(bullet.ProjectileFX);
                        while (bullet.BulletOnHit != -1)
                        {
                            if (!gParam.Bullets.ContainsKey(bullet.BulletOnHit))
                                break;  // missing child bullet
                            bullet = gParam.Bullets[bullet.BulletOnHit];
                            FFX.Add(bullet.FlickFX);
                            FFX.Add(bullet.ImpactFX);
                            FFX.Add(bullet.ProjectileFX);
                        }
                    }
                }
            }
            return FFX.Distinct().Where(i => i > -1);
        }

        /// <summary>
        /// Imports all events and motion data from a different animation.
        /// </summary>
        public static void SetReference(this Animation anim, long fullAnimId) => anim.MiniHeader = new AnimMiniHeader.ImportOtherAnim() { ImportFromAnimID = (int)fullAnimId };

        /// <summary>
        /// Copies all events and motion data from another animation into this one.
        /// </summary>
        public static void CloneReference(this Animation anim, Animation src, long fullSrcId, bool shouldReferenceAnimFile = true)
        {
            if (shouldReferenceAnimFile)
            {
                anim.MiniHeader = new AnimMiniHeader.Standard()
                {
                    ImportFromAnimID = (int)fullSrcId,
                    ImportsHKX = true,
                    ImportsEvents = false
                };
            }
            else
            {
                anim.MiniHeader = new AnimMiniHeader.Standard()
                {
                    ImportFromAnimID = -1,
                    ImportsHKX = false,
                    ImportsEvents = false
                };
            }

            anim.Events.Clear();
            foreach (var srcEvt in src.Events)
            {
                if (!DS1[0].ContainsKey(srcEvt.Type)) continue;
                srcEvt.ApplyTemplate(false, DS1[0][srcEvt.Type]);
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

        public static void ApplyEffect(this Animation anim, long SpEffectId, float startTime = 0, float endTime = 0, bool use302 = false)
        {
            if (endTime == 0) endTime = anim.LatestEventEndTime();
            Event evt = new Event(startTime, endTime, use302 ? 302 : 66, 0, false, DS1[0][66]);
            evt.Parameters["SpEffectID"] = SpEffectId;
            anim.Events.Add(evt);
        }

        public static void ApplyEffectFr(this Animation anim, long SpEffectId, int startFrame = 0, int endFrame = 0)
        {
            float startTime = (float) ((double) startFrame / 30);
            float endTime = (float) ((double) endFrame / 30);
            ApplyEffect(anim, SpEffectId, startTime, endTime);
        }
        #endregion
    }
}
