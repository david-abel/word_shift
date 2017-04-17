# word_shift
A quick solution to the word shift game.

_Shifting_ a word denotes moving the last character to the front and nudging all the other characters back one slot.
So the word "table", after one shift becomes "etabl", and after another, becomes "letab".

A word is said to satisfy the criteria of the game (relative to a specific dictionary) if, for each shift of the word, the resulting word appears in the dictionary. So, "no" satisfies the critieria since "on" is also a word, but "yes" does not, since "sye", and "esy" are not words.

The attached code solves the game for the given dictionary, which comes with the unix operating system (/usr/share/dict/words).