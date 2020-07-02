using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;

using WDict = System.Collections.Generic.Dictionary<string, uint>;
using TDict = System.Collections.Generic.Dictionary<string, System.Collections.Generic.Dictionary<string, uint>>;


namespace Markov
{
    public static class MarkovGenerator
    {
        public static Random Rand { get; private set; }
        public static string Generate(string input, int limit, int unitSize)
        {
            string s = Regex.Replace(input, @"\s+", " ").TrimEnd(' ');
            TDict t = BuildTDict(s, unitSize);
            return BuildString(t, limit, exact: false).TrimEnd(' ');
        }
        public static string GenerateFromFileInput(string inputPath, int limit, int unitSize)
        {
            if (!File.Exists(inputPath)) 
            { 
                Console.WriteLine("Input file doesn't exist"); 
                return ""; 
            }
            return Generate(File.ReadAllText(inputPath), limit, unitSize);
        }
        static TDict BuildTDict(string s, int size)
        {
            TDict t = new TDict();
            string prev = "";
            foreach (string word in Chunk(s, size) )
            {
                if (t.ContainsKey(prev))
                {
                    WDict w = t[prev];
                    if ( w.ContainsKey(word) )
                        w[word] += 1;
                    else
                        w.Add(word, 1);
                }
                else
                    t.Add( prev, new WDict(){{word, 1}} );

                prev = word;
            }

            return t;
        }
        static string[] Chunk(string s, int size)
        {
            string[] ls = s.Split(' ');
            List<string> chunk = new List<string>();

            for (int i = 0; i < ls.Length - size; ++i)
            {
                StringBuilder sb = new StringBuilder();
                sb.Append( ls.Skip(i).Take(size).Aggregate( (w, k) => w + " " + k) );
                chunk.Add( sb.ToString() );
            }

            return chunk.ToArray();
        }
        static string BuildString(TDict t, int len, bool exact)
        {
            string last;
            List<string> ucStr = new List<string>();
            StringBuilder sb = new StringBuilder();

            foreach ( string word in t.Keys.Skip(1) )
            {
                if ( char.IsUpper( word.First() ) )
                    ucStr.Add(word);
            }

            if (ucStr.Count > 0)
                sb.Append( ucStr.ElementAt(Rand.Next(0, ucStr.Count) ) );

            last = sb.ToString();
            sb.Append(" ");

            WDict w = new WDict();
 
            for (uint i = 0; i < len; ++i)
            {
                if (t.ContainsKey(last))
                    w = t[last];
                else
                    w = t[""];

                last = MarkovGenerator.Choose(w);
                sb.Append( last.Split(' ').Last() ).Append(" ");
            }

            if (!exact)
            {
                while (last.Last() != '.')
                {
                    if (t.ContainsKey(last))
                        w = t[last];
                    else
                        w = t[""];

                    last = MarkovGenerator.Choose(w);
                    sb.Append(last.Split(' ').Last()).Append(" ");
                }
            }

            return sb.ToString();
        }
        static private string Choose(WDict w)
        {
            long total = w.Sum(t => t.Value);

            while (true)
            {
                int i = Rand.Next(0, w.Count);
                double c = Rand.NextDouble();
                System.Collections.Generic.KeyValuePair<string, uint> k = w.ElementAt(i);

                if ( c < (double)k.Value / total )
                    return k.Key;
            }
        }
    }
}
