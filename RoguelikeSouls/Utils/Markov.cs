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
    class MarkovProseGenerator
    {
        internal readonly Random Rand;
        internal readonly TDict graphWeights;
        public MarkovProseGenerator(string input, int unitSize, Random random = null)
        {
            Rand = random ?? new Random();
            string s = Regex.Replace(input, @"\s+", " ").TrimEnd(' ');
            graphWeights = BuildTDict(s, unitSize);
        }
        public static MarkovProseGenerator MarkovFromFileInput(string inputPath, int unitSize)
        {
            if (!File.Exists(inputPath))
            {
                Console.WriteLine("Input file doesn't exist");
                return null;
            }
            return new MarkovProseGenerator(File.ReadAllText(inputPath), unitSize);
        }
        public string Generate(int maxCount, bool exact = false)
        {
            return BuildString(maxCount, exact: exact).TrimEnd(' ');
        }

        public void PrintGraphWeights()
        {
            foreach (var keyValue in graphWeights)
            {
                Console.WriteLine(keyValue.Key);
                foreach (var keyValue2 in keyValue.Value)
                {
                    Console.WriteLine($"  {keyValue2.Key}: {keyValue2.Value}");
                }
            }
        }
        internal static TDict BuildTDict(string s, int size)
        {
            // TDict maps each node "prev" to frequency counts of all nodes "next", where
            // each node is a chunk string containing `size` words.
            TDict t = new TDict();
            string prevNode = "";
            foreach (string nextNode in Chunk(s, size) )
            {
                if (t.ContainsKey(prevNode))
                {
                    WDict w = t[prevNode];
                    if (w.ContainsKey(nextNode))
                    {
                        w[nextNode] += 1;
                    }
                    else
                    {
                        w.Add(nextNode, 1);
                    }
                }
                else
                    t.Add(prevNode, new WDict(){ {nextNode, 1} });
                prevNode = nextNode;
            }
            return t;
        }
        internal static string[] Chunk(string s, int size)
        {
            string[] ls = s.Split(' ');
            List<string> chunks = new List<string>();

            for (int i = 0; i <= ls.Length - size; ++i)
            {
                string chunk = ls.Skip(i).Take(size).Aggregate((w, k) => w + " " + k);
                chunks.Add(chunk);
            }

            return chunks.ToArray();
        }
        internal virtual string BuildString(int len, bool exact)
        {
            string last;
            StringBuilder sb = new StringBuilder();

            // Get a random capitalized word first.
            List<string> ucStr = new List<string>();
            foreach (string word in graphWeights.Keys.Skip(1))
            {
                if (char.IsUpper( word.First()))
                {
                    ucStr.Add(word);
                }
            }
            if (ucStr.Count > 0)
            {
                sb.Append(ucStr.ElementAt(Rand.Next(0, ucStr.Count)));
            }
            last = sb.ToString();
            sb.Append(" ");

            WDict w;
 
            for (uint i = 0; i < len; ++i)
            {
                if (graphWeights.ContainsKey(last))
                {
                    w = graphWeights[last];
                }
                else
                {
                    w = graphWeights[""];
                }
                last = Choose(w);
                sb.Append(last.Split(' ').Last() ).Append(" ");
            }

            if (!exact)
            {
                while (last.Last() != '.')
                {
                    if (graphWeights.ContainsKey(last))
                    {
                        w = graphWeights[last];
                    }
                    else
                    {
                        w = graphWeights[""];
                    }
                    last = Choose(w);
                    if (last.Last() == ',')  // replace comma with full stop
                        last = last.Substring(0, last.Length - 1) + ".";
                    sb.Append(last.Split(' ').Last()).Append(" ");
                }
            }
            return sb.ToString();
        }
        internal string Choose(WDict w)
        {
            // Choose a random key from dictionary, weighted by its relative value.
            long total = w.Sum(t => t.Value);
            while (true)
            {
                int i = Rand.Next(w.Count);
                double c = Rand.NextDouble();
                KeyValuePair<string, uint> k = w.ElementAt(i);
                if (c < (double)k.Value / total)
                {
                    return k.Key;
                }
            }
        }
    }

    class SmartMarkovProseGenerator : MarkovProseGenerator
    {
        // Variant of MarkovProseGenerator that uses the requested unit size when there are
        // multiple options to select, and falls back to a single-unit graph otherwise.
        readonly TDict singleGraphWeights;
        public SmartMarkovProseGenerator(string input, int unitSize = 2, Random random = null) : base(input, unitSize, random)
        {
            string s = Regex.Replace(input, @"\s+", " ").TrimEnd(' ');
            singleGraphWeights = BuildTDict(s, 1);
        }
        public static SmartMarkovProseGenerator MarkovFromFileInput(string inputPath, int unitSize, Random random = null)
        {
            if (!File.Exists(inputPath))
            {
                Console.WriteLine("Input file doesn't exist");
                return null;
            }
            return new SmartMarkovProseGenerator(File.ReadAllText(inputPath), unitSize, random);
        }
        internal override string BuildString(int len, bool exact)
        {
            // Falls back to unit size 1 graph if default unit size has only one option.
            string last;
            StringBuilder sb = new StringBuilder();

            // Get a random capitalized word first.
            List<string> ucStr = new List<string>();
            foreach (string word in graphWeights.Keys.Skip(1))
            {
                if (char.IsUpper(word.First()))
                {
                    ucStr.Add(word);
                }
            }
            if (ucStr.Count > 0)
            {
                sb.Append(ucStr.ElementAt(Rand.Next(0, ucStr.Count)));
            }
            last = sb.ToString();
            sb.Append(" ");

            WDict w;
            for (uint i = 0; i < len; ++i)
            {
                if (graphWeights.ContainsKey(last) && graphWeights[last].Count > 1)
                {
                    w = graphWeights[last];
                    last = Choose(w);
                    sb.Append(last.Split(' ').Last()).Append(" ");
                }
                else
                {
                    string singleLast = last.Split(' ').Last();
                    if (singleGraphWeights.ContainsKey(singleLast))
                    {
                        w = singleGraphWeights[singleLast];
                        string newSingleLast = Choose(w);
                        sb.Append(newSingleLast).Append(" ");
                        last = singleLast + " " + newSingleLast;  // restore to default unit size
                    }
                    else
                    {
                        w = graphWeights[""];
                        last = Choose(w);
                        sb.Append(last.Split(' ').Last()).Append(" ");
                    }
                }
            }

            if (!exact)
            {
                while (last.Last() != '.')
                {
                    if (graphWeights.ContainsKey(last) && graphWeights[last].Count > 1)
                    {
                        w = graphWeights[last];
                        last = Choose(w);
                        sb.Append(last.Split(' ').Last()).Append(" ");
                    }
                    else
                    {
                        string singleLast = last.Split(' ').Last();
                        if (singleGraphWeights.ContainsKey(singleLast))
                        {
                            w = singleGraphWeights[singleLast];
                            string newSingleLast = Choose(w);
                            sb.Append(newSingleLast).Append(" ");
                            last = singleLast + " " + newSingleLast;  // restore to default unit size
                        }
                        else
                        {
                            w = graphWeights[""];
                            last = Choose(w);
                            if (last.Last() == ',')  // replace comma with full stop
                                last = last.Substring(0, last.Length - 1) + ".";
                            sb.Append(last.Split(' ').Last()).Append(" ");
                        }
                    }
                }
            }
            return sb.ToString();
        }
    }

    class MarkovWordGenerator
    {
        private readonly Random Rand;
        private readonly TDict graphWeights;
        public MarkovWordGenerator(string input, int unitSize, Random random = null)
        {
            Rand = random ?? new Random();
            string s = Regex.Replace(input, @"[^'\w\s]", " ");  // remove punctuation (except apostrophe)
            s = Regex.Replace(s, @"\s+", " ").TrimEnd(' ');  // collapse excess whitespace
            graphWeights = BuildTDict(s, unitSize);            
        }
        public static MarkovWordGenerator MarkovFromFileInput(string inputPath, int unitSize, Random random = null)
        {
            if (!File.Exists(inputPath))
            {
                Console.WriteLine("Input file doesn't exist");
                return null;
            }
            return new MarkovWordGenerator(File.ReadAllText(inputPath), unitSize, random);
        }
        public string Generate(int maxCount, bool exact = false)
        {
            return BuildWord(graphWeights, maxCount, exact: exact).TrimEnd(' ');
        }
        
        public void PrintGraphWeights()
        {
            foreach (var keyValue in graphWeights)
            {
                Console.WriteLine(keyValue.Key);
                foreach (var keyValue2 in keyValue.Value)
                {
                    Console.WriteLine($"  {keyValue2.Key}: {keyValue2.Value}");
                }
            }
        }

        private static TDict BuildTDict(string s, int size)
        {
            // TDict maps each node "prev" to frequency counts of all nodes "next", where
            // each node is a chunk string containing `size` letters.
            TDict t = new TDict();
            string prevNode = "";
            foreach (string nextNode in ChunkChars(s, size))
            {
                if (t.ContainsKey(prevNode))
                {
                    WDict w = t[prevNode];
                    if (w.ContainsKey(nextNode))
                    {
                        w[nextNode] += 1;
                    }
                    else
                    {
                        w.Add(nextNode, 1);
                    }
                }
                else
                    t.Add(prevNode, new WDict() { { nextNode, 1 } });
                prevNode = nextNode;
            }
            return t;
        }
        private static string[] ChunkChars(string s, int size)
        {
            List<string> chunks = new List<string>();
            for (int i = 0; i <= s.Length - size; ++i)
            {
                StringBuilder sb = new StringBuilder();
                foreach (char c in s.Skip(i).Take(size))
                {
                    sb.Append(c);
                }
                chunks.Add(sb.ToString());
            }
            return chunks.ToArray();
        }
        private string BuildWord(TDict t, int len, bool exact)
        {
            string last;
            StringBuilder sb = new StringBuilder();

            // Get a random capitalized letter first.
            List<string> ucStr = new List<string>();
            foreach (string letter in t.Keys.Skip(1))
            {
                if (char.IsUpper(letter.First()))
                {
                    ucStr.Add(letter);
                }
            }
            if (ucStr.Count > 0)
            {
                sb.Append(ucStr.ElementAt(Rand.Next(0, ucStr.Count)));
            }
            last = sb.ToString();
            
            WDict w;

            for (uint i = 0; i < len; ++i)
            {
                if (t.ContainsKey(last))
                {
                    w = t[last];
                }
                else
                {
                    w = t[""];
                }
                last = Choose(w);
                sb.Append(last.Last());
            }

            if (!exact)
            {
                // Finish off current word with space.
                while (sb[sb.Length - 1] != ' ')
                {
                    if (t.ContainsKey(last))
                        w = t[last];
                    else
                        w = t[""];

                    last = Choose(w);
                    sb.Append(last.Last());
                }
            }
            List<string> words = new List<string>(sb.ToString().Split(' '));
            for (int i = 0; i < words.Count; i++)
            {
                if (words[i].Length > 0)
                {
                    words[i] = char.ToUpper(words[i].First()) + (words[i].Length > 1 ? words[i].Substring(1) : "");
                }
            }
            return string.Join(" ", words);
        }

        private string Choose(WDict w)
        {
            long total = w.Sum(t => t.Value);

            while (true)
            {
                int i = Rand.Next(0, w.Count);
                double c = Rand.NextDouble();
                KeyValuePair<string, uint> k = w.ElementAt(i);

                if (c < (double)k.Value / total)
                {
                    return k.Key;
                }
            }
        }
    }
}
