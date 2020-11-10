using RoguelikeSouls.GameHook;
using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace GameHook
{
    // Parses output from https://defuse.ca/online-x86-assembler.htm
    // I like to keep the whole thing for quick reference to line numbers and so on
    static class DSRAssembly
    {
        private static Regex asmLineRx = new Regex(@"^[\w\d]+:\s+((?:[\w\d][\w\d] ?)+)");

        private static byte[] LoadDefuseOutput(string lines)
        {
            List<byte> bytes = new List<byte>();
            foreach (string line in Regex.Split(lines, "[\r\n]+"))
            {
                Match match = asmLineRx.Match(line);
                string hexes = match.Groups[1].Value;
                foreach (Match hex in Regex.Matches(hexes, @"\S+"))
                    bytes.Add(Byte.Parse(hex.Value, System.Globalization.NumberStyles.AllowHexSpecifier));
            }
            return bytes.ToArray();
        }

        public static byte[] BonfireWarp { get; } = LoadDefuseOutput(Resource.BonfireWarp);
        public static byte[] GetItem { get; } = LoadDefuseOutput(Resource.GetItem);
        public static byte[] LevelUp { get; } = LoadDefuseOutput(Resource.LevelUp);
    }
}
