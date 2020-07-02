using System;
using System.Collections.Generic;
using System.Linq;
using CountDict = System.Collections.Generic.Dictionary<string, int>;

namespace RoguelikeSouls.Installation
{
    abstract class LegendaryEffects
    {
        internal readonly Random Rand;
        public bool IsAbyssal { get; }

        internal virtual string ItemType { get; }

        internal virtual int LegendPoints { get; }
        public virtual CountDict EffectPoints { get; internal set; } = new CountDict();
        internal virtual CountDict MaxEffectPoints { get; } = new CountDict();
        internal virtual Dictionary<string, string> EffectDescriptions { get; } = new Dictionary<string, string>();
        
        internal virtual int AbyssalPoints { get; }
        public virtual CountDict AbyssalEffectPoints { get; internal set; } = new CountDict();
        internal virtual Dictionary<string, string> AbyssalEffectDescriptions { get; } = new Dictionary<string, string>();
        public virtual CountDict AbyssalImmunityPoints { get; internal set; } = new CountDict();
        internal virtual Dictionary<string, string> AbyssalImmunityDescriptions { get; } = new Dictionary<string, string>();

        internal LegendaryEffects(bool isAbyssal, Random random = null)
        {
            Rand = random ?? new Random();
            IsAbyssal = isAbyssal;
        }

        internal virtual string ChooseRandomEffect()
        {
            // Weighted choice of effect based on remaining open points.
            int total = EffectPoints.Sum(t => MaxEffectPoints[t.Key] - t.Value);
            int roll = Rand.Next(total);
            long weightSum = 0;
            for (int i = 0; i < EffectPoints.Count; i++)
            {
                weightSum += MaxEffectPoints.ElementAt(i).Value - EffectPoints.ElementAt(i).Value;
                if (roll < weightSum)
                {
                    return EffectPoints.ElementAt(i).Key;
                }
            }
            throw new Exception($"Failure to choose random effect (roll {roll}, weight total {total})");
        }

        internal void AddEffectPoint()
        {
            string effect;
            do
            {
                effect = ChooseRandomEffect();
            } while (!EffectAllowed(effect));
            EffectPoints[effect] += 1;
        }

        internal virtual bool EffectAllowed(string effect)
        {
            return true;
        }

        public double GetStaminaMultiplier()
        {
            if (!EffectPoints.ContainsKey("Light") || !AbyssalEffectPoints.ContainsKey("Heavy"))
                throw new KeyNotFoundException("No 'Heavy' and/or 'Light' effect in legendary effects.");
            if (AbyssalEffectPoints["Heavy"] > 0)
                return 2.0;
            if (EffectPoints["Light"] > 0)
                return 0.5;
            return 1.0;
        }

        public virtual string GetEffectDescription()
        {
            // Returns (unwrapped) sentence describing the weapon's effects.
            List<string> positiveDescs = new List<string>(EffectDescriptions.Where(kv => EffectPoints[kv.Key] > 0).Select(kv => kv.Value));
            string positive = "";
            switch (positiveDescs.Count)
            {
                case 0:
                    throw new Exception($"Found no positive effects to describe for weapon.");
                case 1:
                    positive = positiveDescs[0];
                    break;
                case 2:
                    positive = string.Join(" and ", positiveDescs);
                    break;
                default:
                    positive = string.Join(", ", positiveDescs.GetRange(0, positiveDescs.Count - 1)) + $", and {positiveDescs[positiveDescs.Count - 1]}";
                    break;
            }
            List<string> negativeDescs = new List<string>(AbyssalEffectDescriptions.Where(kv => AbyssalEffectPoints[kv.Key] > 0).Select(kv => kv.Value));
            negativeDescs.AddRange(AbyssalImmunityDescriptions.Where(kv => AbyssalImmunityPoints[kv.Key] > 0).Select(kv => kv.Value));
            string negative = "";
            switch (negativeDescs.Count)
            {
                case 0:
                    break;
                case 1:
                    negative = negativeDescs[0];
                    break;
                case 2:
                    negative = string.Join(" and ", negativeDescs);
                    break;
                default:
                    negative = string.Join(", ", negativeDescs.GetRange(0, negativeDescs.Count - 1)) + $", and {negativeDescs[negativeDescs.Count - 1]}";
                    break;
            }
            if (negative == "")
            {
                return $"This legendary {ItemType} {positive}.";
            }
            else
            {
                return $"This abyssal {ItemType} {positive}, but {negative}.";
            }
        }
    }
}
