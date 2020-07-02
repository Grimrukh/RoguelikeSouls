using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RoguelikeSouls.Utils
{
    static class WordWrapper
    {
		static readonly char[] Whitespace = { ' ', '\r', '\n', '\t' };
		static readonly char[] Separators = { ' ', ',', '.', '?', '!', ':', ';', '-', '\n', '\r', '\t' };
		public static List<string> WordWrap(string text, int maxLineLength)
		{
			var list = new List<string>();

			int currentIndex;
			var lastWrap = 0;
			do
			{
				currentIndex = lastWrap + maxLineLength > text.Length ? text.Length : (text.LastIndexOfAny(Separators, Math.Min(text.Length - 1, lastWrap + maxLineLength)) + 1);
				if (currentIndex <= lastWrap)
				{
					currentIndex = Math.Min(lastWrap + maxLineLength, text.Length);
				}
				list.Add(text.Substring(lastWrap, currentIndex - lastWrap).Trim(Whitespace));
				lastWrap = currentIndex;
			} while (currentIndex < text.Length);

			return list;
		}
	}
}
	