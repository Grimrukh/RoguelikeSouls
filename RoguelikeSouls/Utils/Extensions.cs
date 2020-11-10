using System;
using System.Collections.Generic;
using System.Linq;

namespace RoguelikeSouls.Extensions
{
    public static class Extensions
    {
        public static bool In<T>(this T item, params T[] values)
        {
            return values.Contains(item);
        }
        
        public static int IndexOfMinBy<T>(this IList<T> self, Func<T, double> minFunc)
        {
            if (self == null)
                throw new ArgumentNullException("self");
            if (self.Count == 0)
                throw new ArgumentException("List is empty.", "self");

            double min = minFunc(self[0]);
            int minIndex = 0;

            for (int i = 1; i < self.Count; ++i)
            {
                double candidate = minFunc(self[i]);
                if (candidate < min)
                {
                    min = candidate;
                    minIndex = i;
                }
            }
            return minIndex;
        }

        public static bool ContainsAny(this string haystack, params string[] needles)
        {
            foreach (string needle in needles)
            {
                if (haystack.Contains(needle))
                    return true;
            }
            return false;
        }

        public static bool ContainsAny(this string haystack, List<string> needles)
        {
            foreach (string needle in needles)
            {
                if (haystack.Contains(needle))
                    return true;
            }
            return false;
        }

        public static T GetRandomElement<T>(this IList<T> list, Random random)
        {
            if (!list.Any())
                throw new ArgumentException($"Cannot select random element from empty list.");
            return list[random.Next(list.Count)];
        }

        public static T PopRandomElement<T>(this IList<T> list, Random random)
        {
            if (!list.Any())
                throw new ArgumentException($"Cannot pop random element from empty list.");
            T chosen = list.GetRandomElement(random);
            list.Remove(chosen);
            return chosen;
        }

        public static T GetWeightedRandomElement<T>(this IDictionary<T, int> options, Random random)
        {
            int total = options.Sum(option => option.Value);
            int roll = random.Next(total);
            int runningTotal = 0;
            foreach (var option in options)
            {
                runningTotal += option.Value;
                if (roll < runningTotal)
                    return option.Key;
            }
            throw new Exception($"Could not get weighted random element (roll = {roll}, total = {total}).");
        }

        public static bool Roll(this Random random, double odds)
        {
            return random.NextDouble() < odds;
        }

        public static float NextAngle(this Random random)
        {
            return (float)random.NextDouble() * 360.0f - 180.0f;
        }
    }
}
