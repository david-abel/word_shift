'''
Author: David Abel

Summary: Computes the words that satisfy the "word shift" criteria.
'''

import operator
from collections import defaultdict

def shift_word(word):
	return word[-1] + word[0:-1]

def load_words_to_dict(file_name="words.txt"):
	'''
	Returns:
		(defaultdict(int)): Loads all words in @file_name into a word dict with:
			Key-->word
			Val-->1
	'''
	word_dict = defaultdict(int)
	for word in file(file_name, "r").readlines():
		word_dict[word.strip()] = 1
	return word_dict

def check_word_rotations(word, word_dict):
	'''
	Returns:
		(bool): True iff every rotation of the word is a word.
	'''
	next_shift = shift_word(word)
	for i in range(len(word) - 1):
		if word_dict[next_shift] != 1:
			return False
		next_shift = shift_word(next_shift)
	return True

def main():
	# Load the dictionary of words.
	word_dict = load_words_to_dict()
	success_words = {}

	# Check every word.
	for word in word_dict.keys():
		if check_word_rotations(word, word_dict):
			success_words[word] = len(word)

	# Sort by word length.
	sorted_success_words = sorted(success_words.items(), key=operator.itemgetter(1))
	sorted_success_words.reverse()

	print sorted_success_words

if __name__ == "__main__":
	main()
