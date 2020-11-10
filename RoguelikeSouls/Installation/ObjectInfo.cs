using System.Collections.Generic;

namespace RoguelikeSouls.Installation
{
    static class Objects
    {
        public static List<short> CorpsePoses = new List<short>()
        {
            10,  // Lying on stomach, right knee slightly crooked, head turned slightly right. (add 0.25 to your Y)
            11,  // As above, but head turned more to the left. (add 0.25 to your Y)
            20,  // Lying on back with right knee raised, left hand on chest, looking right.
            21,  // Fully laid out on back.
            // 31,  // Fully bent over a thin wall (e.g. a well).
            // 35,  // Bent over a thick wall, head looking down.
            // 42,  // Hanging off edge on stomach at 90 degrees, legs dangling over. (subtract 0.1 from your Y standing on the same platform)
            50,  // Sitting with back against wall, hunched over, legs spread. (add 0.2 to your Y)
            51,  // Sitting with back against wall, hunched over, legs almost crossed. (add 0.2 to your Y)
            81,  // Foetal position, lying on right side.
            82,  // Lying on left side, not quite foetal, arms out.
            // 90,  // Arms wrapped around something (e.g. a spike statue). (hard to get working...)
            // 95,  // Floating face-down in water.
        };

        public static Dictionary<short, float> CorpsePoseYOffsets = new Dictionary<short, float>()
        {
            { 10, 0.0f },  // adding 0.25f was wrong
            { 11, 0.25f },
            { 20, 0.0f },
            { 21, 0.0f },
            { 31, 0.0f },
            { 35, 0.0f },
            { 42, -0.1f },
            { 50, 0.2f },
            { 51, 0.2f },
            { 81, 0.0f },
            { 82, 0.0f },
        };
    }
}
