using SoulsFormats;
using SoulsFormatsMod.Extensions;
using SoulsFormatsMod.PARAMS;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using static SoulsFormats.TAE;

namespace SoulsFormatsMod
{
    public class PlayerMoveset
    {
        SoulsMod SM;

        /// <summary>
        /// Right-hand attacks.
        /// </summary>
        public HandSet RightHand { get; }
        /// <summary>
        /// Two-hand attacks.
        /// </summary>
        public HandSet TwoHand { get; }
        /// <summary>
        /// Left-hand attacks.
        /// </summary>
        public HandSet LeftHand { get; }

        public byte ID { get; }

        bool MakeNew { get; }

        public byte SourceID { get; }

        public static implicit operator int(PlayerMoveset m) => m.ID;
        public static implicit operator long(PlayerMoveset m) => m.ID;

        internal TAE AnimFile => SM.Player.GetTAE(ID);

        public int Variation { get; set; }

        public Action<Animation> DefaultAtkAction
        {
            get => SM.Player.TaeAttackOveride[ID];
            set => SM.Player.TaeAttackOveride[ID] = value;
        }

        public void EditInBulk(Action<Animation> act)
        {
            foreach (Animation animation in AnimFile.Animations)
            {
                act(animation);
            }
        }

        public PlayerMoveset(int id, SoulsMod s, int variation, bool makeNew = true, byte? newId = null)
        {
            SM = s;
            Variation = variation;
            MakeNew = makeNew;
            if (MakeNew)
            {
                TAE source = SM.Player.GetTAE(id);
                BinderFile sourceBinder = SM.Player.GetBinderFile(id);
                SourceID = (byte)id;
                ID = newId ?? Convert.ToByte(SM.Player.TAEs.Keys.Where(k => k < 200).Max() + 1);
                string uri = Path.GetDirectoryName(sourceBinder.Name) + $@"\a{ID.ToString("00")}.tae";
                TAE tae = TAE.Read(sourceBinder.Bytes);
                tae.ID = ID;

                foreach (var tgtAnim in tae.Animations)
                {
                    long srcId = SourceID * 10000 + tgtAnim.ID;
                    Animation srcAnim = SM.Player.GetAnimation((int) srcId);
                    while (srcAnim.MiniHeader.Type == Animation.MiniHeaderType.ImportOtherAnim)
                    {
                        srcId = (srcAnim.MiniHeader as Animation.AnimMiniHeader.ImportOtherAnim).ImportFromAnimID;
                        srcAnim = SM.Player.GetAnimation((int)srcId);
                    }
                    tgtAnim.CloneReference(srcAnim, srcId);
                }

                BinderFile newBinder = new BinderFile(sourceBinder.Flags, tae.Write())
                {
                    Name = uri,
                    ID = 5000000 + ID
                };

                SM.Player.ChrFile.Files.Add(newBinder);
                SM.Player.ChrFile.Files.Sort((x, y) => x.ID.CompareTo(y.ID));
                SM.Player.TAEs[ID] = (newBinder, tae);
            }
            else
            {
                ID = (byte)id;
            }

            RightHand = new HandSet(this, HandNum.Right);
            TwoHand = new HandSet(this, HandNum.Two);
            LeftHand = new HandSet(this, HandNum.Left);
        }

        public AnimHandler Anim(long id)
        {
            if (!AnimFile.Animations.Exists(a => a.ID == id))
            {
                Animation anim = new Animation(id, new Animation.AnimMiniHeader.Standard(), "anim" + id);
                AnimFile.Animations.Add(anim);
                AnimFile.Animations.Sort((a, b) => a.ID.CompareTo(b.ID));
                if (MakeNew)
                {
                    long srcId = SourceID * 10000 + anim.ID;
                    Animation srcAnim = SM.Player.GetAnimation((int) srcId);
                    if (srcAnim != null)
                    {
                        if (srcAnim.MiniHeader.Type == Animation.MiniHeaderType.ImportOtherAnim)
                        {
                            srcId = (srcAnim.MiniHeader as Animation.AnimMiniHeader.ImportOtherAnim).ImportFromAnimID;
                            srcAnim = SM.Player.GetAnimation((int) srcId);
                        }
                        anim.CloneReference(srcAnim, srcId);
                    }
                }
            }
            return new AnimHandler(SM, this, AnimFile.Animations.First(a => a.ID == id));
        }

    }

    public class HandSet
    {
        PlayerMoveset moveset;  

        int hand;

        public HandSet(PlayerMoveset m, int h)
        {
            moveset = m;
            hand = h;
        }

        public void SetAllMainActions(Action<Animation> action)
        {
            AnimHandler[] handlers = { QuickAtkA, QuickAtkB, QuickAtkARepeat, QuickAtkC, QuickAtkD,
            StrongAtkA, StrongAtkB, StrongAtkFromQuick, RunAtk, RollAtk };
            foreach (AnimHandler handler in handlers)
            {
                handler.Action = action;
            }
        }

        AnimHandler Anim(int atkNum) => moveset.Anim(hand + atkNum);
        public AnimHandler QuickAtkA => Anim(AttackNum.QuickAtkA);
        public AnimHandler QuickAtkB => Anim(AttackNum.QuickAtkB);
        public AnimHandler QuickAtkARepeat => Anim(AttackNum.QuickAtkA1);
        public AnimHandler QuickAtkC => Anim(AttackNum.QuickAtkC);
        public AnimHandler QuickAtkD => Anim(AttackNum.QuickAtkD);
        public AnimHandler TooHeavy => Anim(AttackNum.TooHeavy);
        public AnimHandler Kick => Anim(AttackNum.Kick);
        public AnimHandler StrongAtkA => Anim(AttackNum.StrongAtkA);
        public AnimHandler StrongAtkB => Anim(AttackNum.StrongAtkB);
        public AnimHandler StrongAtkFromQuick => Anim(AttackNum.StrongAtkFromQuick);
        public AnimHandler RunAtk => Anim(AttackNum.RunAtk);
        public AnimHandler JumpAtk => Anim(AttackNum.JumpAtk);
        public AnimHandler DropAtkStart => Anim(AttackNum.DropAtkStart);
        public AnimHandler DropAtkMiddle => Anim(AttackNum.DropAtkMiddle);
        public AnimHandler DropAtkEnd => Anim(AttackNum.DropAtkEnd);
        public AnimHandler DropAtkCustomA => Anim(AttackNum.DropAtkCustomA);
        public AnimHandler DropAtkCustomB => Anim(AttackNum.DropAtkCustomB);
        public AnimHandler DropAtkCustomC => Anim(AttackNum.DropAtkCustomC);
        public AnimHandler RollAtk => Anim(AttackNum.RollAtk);
        public AnimHandler RollAtkWhiff => Anim(AttackNum.RollAtkWhiff);
        public AnimHandler Special => moveset.Anim(3950);
    }

    public class AnimHandler
    {
        SoulsMod SM { get; set; }
        PlayerMoveset Moves { get; set; }
        public Animation Anim { get; set; }

        public Attack Attack => Attacks(Moves.Variation).First();

        public Behavior Behavior => AtkBehaviors(Moves.Variation).First();

        public IEnumerable<Behavior> AtkBehaviors(int? variation = null)
        {
            if (!variation.HasValue) variation = Moves.Variation;
            IEnumerable<Event> evtList = Anim.Events.Where(evt => evt.Type == 1 || evt.Type == 307);
            IEnumerable<Behavior> behList = evtList.Select(e =>
            {
                int attackId = 1000 * variation.Value + (int)e.Parameters["BehaviorSubId"];
                int behaviorId = 100000000 + attackId;
                if (SM.GPARAM.BehaviorsPC[behaviorId] == null)
                {
                    var beh = SM.GPARAM.BehaviorsPC.AddRow(behaviorId);
                    beh.BehaviorSubID = (int)e.Parameters["BehaviorSubID"];
                    beh.RefID = attackId;
                    if (SM.GPARAM.AttacksPC[attackId] == null)
                    {
                        var atk = SM.GPARAM.AttacksPC.AddRow(attackId);
                        atk.Hitbox0StartModelPoint = 100;
                    }
                }
                return SM.GPARAM.BehaviorsPC[behaviorId];
            });
            return behList;
        }

        public IEnumerable<Attack> Attacks(int? variation) => AtkBehaviors(variation).Select(b => SM.GPARAM.AttacksPC[b.RefID]);

        public AnimHandler(SoulsMod sm, PlayerMoveset m, Animation a)
        {
            SM = sm;
            Moves = m;
            Anim = a;
        }

        public long FullAnimId => Moves.ID * 10000 + Anim.ID;
        public static implicit operator long(AnimHandler h) => h.FullAnimId;
        public static implicit operator int(AnimHandler h) => (int)h.FullAnimId;

        public void FullReference(long refId) => Anim.SetReference((int) refId);

        public void CloneReference(int refId) => Anim.CloneReference(SM.Player.GetAnimation(refId), refId);
        public int FindUnusedJudge(int variation)
        {
            var behs = SM.GPARAM.BehaviorsPC.Values.Where(b => b.VariationID == variation);
            for (int i = 0; i <= 999; i++)
            {
                if (!behs.Any(a => a.BehaviorSubID == i))
                    return i;
            }
            throw new Exception("Variation " + variation + " has no open judge IDs.");

        }
        public void FireBullet(int variation, int bullet, int dmy, float? time = null, float? offset = null, int? stamina = null)
        {
            int judge = FindUnusedJudge(variation);
            Behavior beh = SM.GPARAM.BehaviorsPC.AddRow(int.Parse($"10{variation:0000}{judge:000}"));
            
            beh.ReferenceType = 1;
            beh.RefID = bullet;
            beh.VariationID = variation;
            beh.BehaviorSubID = judge;
            beh.StaminaCost = stamina ?? 20;
            beh.EzstateBehaviorType = 1;

            if (!time.HasValue)
            {
                Event atkEvt = Anim.RemoveEvent(1) ?? Anim.RemoveEvent(307);
                time = atkEvt != null ? atkEvt.StartTime : 0.4f;
                if (offset.HasValue)
                    time += offset;
            }

            Anim.NewEvent(002, time.Value, time.Value + 0.3f, "DummyPolyID", dmy, "BehaviorSubID", judge, "Enable", true);
            Anim.NewEvent(225, 0, time.Value + 0.3f, "RegenRatePercent", 0);
        }

        public Action<Animation> Action
        {
            get
            {
                int animId = (int)FullAnimId % 10000;
                int taeId = (int)Math.Floor((float)FullAnimId / 10000);
                return SM.Player.Override[taeId * 10000 + animId];
            }
            set => SM.Player.Override[FullAnimId] = value;
        }
    }

    static class HandNum
    {
        public static int Right = 3000;
        public static int Two = 4000;
        public static int Left = 5000;
    }

    static class AttackNum
    {
        public static int QuickAtkA = 0;
        public static int QuickAtkB = 1;
        public static int QuickAtkA1 = 2;
        public static int QuickAtkC = 3;
        public static int QuickAtkD = 4;
        public static int TooHeavy = 30;
        public static int Kick = 100;
        public static int StrongAtkA = 300;
        public static int StrongAtkFromQuick = 301;
        public static int StrongAtkB = 310;
        public static int RunAtk = 500;
        public static int JumpAtk = 600;
        public static int DropAtkStart = 800;
        public static int DropAtkMiddle = 801;
        public static int DropAtkEnd = 810;
        public static int DropAtkCustomA = 822;
        public static int DropAtkCustomB = 824;
        public static int DropAtkCustomC = 826;
        public static int RollAtk = 900;
        public static int RollAtkWhiff = 940;
    }
}
