using SoulsFormats;
using SoulsFormatsMod;
using SoulsFormatsMod.Extensions;
using System.Linq;
using SoulsFormatsMod.PARAMS;
using static SoulsFormatsMod.Extensions.AnimExtensions;
using RoguelikeSouls.Installation;

namespace RoguelikeSouls.Installation
{
    class PlayerGenerator
    {
        readonly SoulsMod Mod;
        public static int[] GuardHitAnimationIds { get; } =
        {
            140, 141, 142, 145, 146, 147,
            150, 151, 152,
            160, 162, 164,
        };

        public static int BackstepAnimation = 680;
        public static int BackflipAnimation = 697;
        public static int[] RollAnimationIds { get; } = { 700, 701, 702, 703 };
        public static int[] FlipAnimationIds { get; } = { 735, 736, 737, 738 };

        public PlayerGenerator(SoulsMod mod)
        {
            Mod = mod;
        }

        public void Install()
        {
            AddFadingAnimations();
            AddAnimationSpEffects();
            CleanStartingClasses();
        }

        void CleanStartingClasses()
        {
            for (int i = 0; i < 10; i++)
            {
                ChrInit startingClass = Mod.GPARAM.ChrInits[3000 + i];
                startingClass.Vitality = 14;
                startingClass.Attunement = 11;
                startingClass.Endurance = 25;
                startingClass.Strength = 12;
                startingClass.Dexterity = 12;
                startingClass.Resistance = 10;
                startingClass.Intelligence = 10;
                startingClass.Faith = 10;
                startingClass.SoulLevel = 20;
                startingClass.RightHandWeapon1 = -1;
                startingClass.RightHandWeapon2 = -1;
                startingClass.LeftHandWeapon1 = -1;
                startingClass.LeftHandWeapon2 = -1;
                startingClass.HeadArmor = 10000;
                startingClass.BodyArmor = 11000;
                startingClass.ArmsArmor = -1;
                startingClass.LegsArmor = 13000;

                ChrInit startingClassActual = Mod.GPARAM.ChrInits[2000 + i];
                startingClassActual.Vitality = 14;
                startingClassActual.Attunement = 11;
                startingClassActual.Endurance = 25;
                startingClassActual.Strength = 12;
                startingClassActual.Dexterity = 12;
                startingClassActual.Resistance = 10;
                startingClassActual.Intelligence = 10;
                startingClassActual.Faith = 10;
                startingClassActual.SoulLevel = 20;
                startingClassActual.RightHandWeapon1 = -1;
                startingClassActual.RightHandWeapon2 = -1;
                startingClassActual.LeftHandWeapon1 = -1;
                startingClassActual.LeftHandWeapon2 = -1;
                startingClassActual.HeadArmor = 10000;
                startingClassActual.BodyArmor = 11000;
                startingClassActual.ArmsArmor = -1;
                startingClassActual.LegsArmor = 13000;
                startingClass.SkillSlot1 = -1;
                // Still starts with Darksign AND Black Separation Crystal, in case I get vengeance invasions going.
                startingClass.ArrowSlot1 = -1;
                startingClass.ArrowSlot1Count = 0;

                Mod.Text.MenuOther[132020 + i] = "Hero";
                Mod.Text.MenuOther[132320 + i] = "Undead champion.\nLoyal friend.\nClarinet maestro.";
            }

            // Remove all gifts.
            for (int i = 0; i < 9; i++)
            {
                ChrInit startingGift = Mod.GPARAM.ChrInits[2400 + i];
                startingGift.GoodSlot1 = -1;
                startingGift.GoodSlot1Count = 0;
                startingGift.RingSlot1 = 0;
                Mod.Text.MenuOther[132050 + i] = "None";
            }
        }

        void AddFadingAnimations()
        {
            TAE.Animation standing = Mod.Player.TAEs[0].tae.Animations[0];

            TAE.Animation fadeIn = new TAE.Animation(10, standing.MiniHeader, standing.AnimFileName);
            fadeIn.CloneReference(standing, 0, true);
            TAE.Event fadeInEvent = new TAE.Event(0.0f, 2.0f, 193, 0, false, DS1[0][193]);
            fadeInEvent.Parameters["GhostVal1"] = 0.0f;
            fadeInEvent.Parameters["GhostVal2"] = 1.0f;
            fadeIn.Events.Add(fadeInEvent);
            Mod.Player.TAEs[0].tae.Animations.Add(fadeIn);

            TAE.Animation fadeOut = new TAE.Animation(11, standing.MiniHeader, standing.AnimFileName);
            fadeOut.CloneReference(standing, 0, true);
            TAE.Event fadeOutEvent = new TAE.Event(0.0f, 2.0f, 193, 0, false, DS1[0][193]);
            fadeOutEvent.Parameters["GhostVal1"] = 1.0f;
            fadeOutEvent.Parameters["GhostVal2"] = 0.0f;
            TAE.Event invisibleEvent = new TAE.Event(2.0f, 10.0f, 193, 0, false, DS1[0][193]);
            invisibleEvent.Parameters["GhostVal1"] = 0.0f;
            invisibleEvent.Parameters["GhostVal2"] = 0.0f;
            fadeOut.Events.Add(fadeOutEvent);
            fadeOut.Events.Add(invisibleEvent);
            Mod.Player.TAEs[0].tae.Animations.Add(fadeOut);
        }

        void AddAnimationSpEffects()
        {
            // Add triggers for rolling.
            foreach (int dodgeAnimationId in RollAnimationIds)
            {
                TAE.Animation dodgeAnimation = Mod.Player.GetAnimation(dodgeAnimationId);
                float behaviorEndTime = dodgeAnimation.FindEvent(307).EndTime;
                dodgeAnimation.ApplyEffect(SpEffectGenerator.Effects["Rolling Damage (TAE TRIGGER)"], behaviorEndTime, behaviorEndTime + (1.0f / 30.0f));
            }

            // Add triggers for taking a hit while guarding.
            foreach (var (_, playerTAE) in Mod.Player.TAEs.Values)
            {
                foreach (int guardHitAnimationId in GuardHitAnimationIds)
                {
                    TAE.Animation guardHitAnimation = playerTAE.Animations.FirstOrDefault(a => a.ID == guardHitAnimationId);
                    if (guardHitAnimation != null)
                    {
                        // Apply trigger effect for one frame at the start of the animation.
                        guardHitAnimation.ApplyEffect(SpEffectGenerator.Effects["On Guard (TAE TRIGGER)"], 0.0f, 1.0f / 30.0f);
                    }
                }
            }
        }
    }
}
