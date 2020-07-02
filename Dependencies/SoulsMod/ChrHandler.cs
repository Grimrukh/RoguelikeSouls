using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using SoulsFormats;
using SoulsFormatsMod.Extensions;
using static SoulsFormats.TAE;
using static SoulsFormatsMod.Extensions.AnimExtensions;

namespace SoulsFormatsMod
{
    public class ChrHandler
    {
        private SoulsMod SM;
        public int ID { get; set; }

        internal BND3 ChrFile;

        string FilePath;

        public Dictionary<int, (BinderFile binderFile, TAE tae)> TAEs = new Dictionary<int, (BinderFile, TAE)>();

        public TAE GetTAE(int id) => TAEs[id].tae;

        public BinderFile GetBinderFile(int id) => TAEs[id].binderFile;

        public Animation GetAnimation(int id)
        {
            int animId = id % 10000;
            int taeId = (int)Math.Floor((float)id / 10000);
            return TAEs[taeId].tae.Animations.FirstOrDefault(a => a.ID == animId);
        }

        public Dictionary<int, Action<Animation>> TaeAttackOveride = new Dictionary<int, Action<Animation>>();
        public List<int> ThrowAnimIds => new List<int>();
        public ChrHandler(int id, SoulsMod s) => Init(id, s);

        private void Init(int id, SoulsMod s)
        {
            ID = id;
            SM = s;
            FilePath = $@"{SM.GameDir}chr\c{ID:0000}.anibnd.dcx";
            
            ChrFile = BND3.Read(SM.Backup(FilePath));
            foreach (var binder in ChrFile.Files.Where(f => f.Name.EndsWith(".tae")))
            {
                string num = Path.GetFileNameWithoutExtension(binder.Name).Substring(1);
                TAE tae = TAE.Read(binder.Bytes);
                tae.ApplyTemplate(DS1);
                if (TAEs.ContainsKey(int.Parse(num)))
                {
                    //Console.WriteLine($"Skipping duplicate TAE entry in ANIBND: {binder.Name} (ID {binder.ID})");
                    continue;
                }
                else
                {
                    TAEs[int.Parse(num)] = (binder, tae);
                }
            }

            ThrowAnimIds.AddRange(SM.GPARAM.Throws.Values.Where(t => t.AttackingCharacterModel == ID).Select(t => t.AttackerAnimation).Distinct());
            ThrowAnimIds.AddRange(SM.GPARAM.Throws.Values.Where(t => t.DefendingCharacterModel == ID).Select(t => t.DefenderAnimation).Distinct());
            SM.Characters[ID] = this;
            Anim = new AnimModHandler(s.DefaultAnimMod);
        }


        public Action<Animation> this[int id]
        {
            get
            {
                int animId = id % 10000;
                int taeId = (int)Math.Floor((float)id / 10000);
                return Override[taeId * 10000 + animId];
            }
            set => Override[id] = value;
        }

        public Dictionary<long, Action<Animation>> Override = new Dictionary<long, Action<Animation>>();

        public AnimModHandler Anim { get; set; }

        public void ApplyMods()
        {
            long[] dashIds = { 680, 700, 701, 702, 703 };
            long[] blinkIds = { 697, 735, 736, 737, 738 };

            foreach (var grp in TAEs)
            {
                int taeNum = grp.Key;
                TAE tae = grp.Value.tae;
                foreach (Animation anim in tae.Animations)
                {
                    long fullAnimId = (long)taeNum * 10000 + anim.ID;

                    Event attackEvt = anim.FindEvent(1) ?? anim.FindEvent(4);
                    Event pushEvt = anim.FindEvent(307);

                    bool isDeath = anim.FindJumpTable(12) != null;
                    bool isMove = anim.InRange(200, 599);
                    bool isThrow = ThrowAnimIds.Contains((int)anim.ID);
                    bool isAttack = attackEvt != null || pushEvt != null;
                    bool isInjury = anim.InRange(2000, 2299);
                    bool isGeneric = anim.ID < 7000 && taeNum < 7;

                    bool isPlayer = ID == 0;
                    bool isJump = isAttack && isPlayer && anim.ID % 1000 == 600;
                    bool isDash = dashIds.Contains(fullAnimId);
                    bool isCustomAttack = isPlayer && TaeAttackOveride.ContainsKey(taeNum);
                    bool isBrokenCustomR2 = isPlayer && (anim.ID == 4305 || anim.ID == 3305 || anim.ID == 5005);
                    bool isCustomR2 = isPlayer && (anim.ID == 4300 || anim.ID == 3300 || anim.ID == 5005);
                    bool isBlink = isPlayer && blinkIds.Contains(fullAnimId);
                    bool isEstus = isPlayer && anim.InRange(7585, 7588);
                    bool isKick = isPlayer && anim.ID % 1000 == 100 && pushEvt != null;

                    if (!isThrow)
                    {
                        if (Override.ContainsKey(fullAnimId))
                        {
                            Override[fullAnimId](anim);
                            anim.NewEvent(32, 0, 0.1f, "SheathID", 1);
                        }
                        else if (ID > 0 && Override.ContainsKey(fullAnimId % 10000))
                            Override[fullAnimId % 10000](anim);
                        else if (isEstus)
                            Anim.HealMod(anim);
                        else if (isBrokenCustomR2)
                            anim.SetReference(fullAnimId - 5);
                        else if (isDeath)
                            Anim.DeathMod(anim);
                        else if (isInjury)
                            Anim.InjuryMod(anim);
                        else if (isDash)
                            Anim.DodgeMod(anim);
                        else if (isBlink)
                            Anim.BlinkMod(anim);
                        else if (isMove)
                            Anim.MoveMod(anim);
                        else if (isKick)
                            Anim.KickMod(anim);
                        else if (isAttack || isCustomR2)
                        {
                            if (isCustomAttack)
                                TaeAttackOveride[taeNum](anim);
                            else
                                Anim.AttackMod(anim);

                            anim.NewEvent(32, 0, 0.1f, "SheathID", 1);
                        }
                        else if (!isJump)
                            Anim.AttackMod(anim);
                        else if (isGeneric)
                            Anim.GenericMod(anim);
                    }
                }
            }
        }

        public void Export()
        {
            // ApplyMods();  // I'm applying my own mods.
            foreach (var pair in TAEs.Values)
            {
                pair.binderFile.Bytes = pair.tae.Write();
            }
            ChrFile.Write(FilePath);
        }
    }

    public class AnimModHandler
    {
        public Action<Animation> AttackMod = (Animation a) => { };
        public Action<Animation> KickMod = (Animation a) => { };
        public Action<Animation> DeathMod = (Animation a) => { };
        public Action<Animation> DodgeMod = (Animation a) => { };
        public Action<Animation> BlinkMod = (Animation a) => { };
        public Action<Animation> MoveMod = (Animation a) => { };
        public Action<Animation> InjuryMod = (Animation a) => { };
        public Action<Animation> GenericMod = (Animation a) => { };
        public Action<Animation> HealMod = (Animation a) => { };

        public AnimModHandler(AnimModHandler am)
        {
            AttackMod = am.AttackMod;
            KickMod = am.KickMod;
            DeathMod = am.DeathMod;
            DodgeMod = am.DodgeMod;
            DodgeMod = am.BlinkMod;
            MoveMod = am.MoveMod;
            InjuryMod = am.InjuryMod;
            GenericMod = am.GenericMod;
            HealMod = am.HealMod;
        }

        public AnimModHandler(bool nullMod = false)
        {
            if (nullMod)
            {
                AttackMod = null;
                KickMod = null;
                DeathMod = null;
                DodgeMod = null;
                MoveMod = null;
                HealMod = null;
                BlinkMod = null;
                InjuryMod = null;
                GenericMod = null;
            }
        }
    }
}
