# Markov
C# implementation of a text generator based on Markov chains

Usage: Markov.exe infile outfile wordlimit size [exact]
- infile is the input text file
- outfile is the output text file (will be created or overwritten)
- wordlimit specifies how many words to generate
- size is the unit size: 1 is one word, 2 is two words etc. A bigger unit size will generate more coherent text,
but the random nature of the algorithm will be diminished; 2 and 3 are good values, 1 may be too random,
values above 3 may generate uninteresting results
- exact is an optional flag; if it's present the output text will be exactly *wordlimit* words long, otherwise
the generator will terminate at a full stop. Note that for this flag to be true it merely needs to exist,
so if you call the program like "Markov.exe in.txt out.txt 1000 2 false" the *exact* flag will not be false,
in fact you can write anything as the fifth argument and it will be interpreted as true. If you don't want
an exact length text, simply omit this command-line parameter.

**Please note** that a *size* of 0 wasn't tested and may result in a infinite loop. Also, the input text **must**
contain at least one Capitalized word, or the program may get stuck in an infinite loop. If the *exact* flag is
not set, the input text **must** also contain at least a word ending with a full stop, ar the program may get stuck
in an infinite loop.
