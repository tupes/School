
from string import ascii_uppercase

from utilities import getInBothCount


english_letter_freq = { 'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I':
	6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C':
	2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P':
	1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z':
	0.07 }

sorted_letters = ''.join(sorted(english_letter_freq.keys(), 
	key=lambda x: english_letter_freq[x], reverse=True))

LETTERS = ascii_uppercase


class FrequencyAnalyzer:

	def __init__(self, cipher, key_symbols, most_freq_symbols_cutoff=4):
		self.cipher = cipher
		self.key_symbols = key_symbols
		self.freq_rank_cutoff = most_freq_symbols_cutoff

		self.message = None
		self.key_length = 0		

	# ////////////////////////
	# PUBLIC
	# ////////////////////////

	def getFreqScores(self, message, key_length):
		self.message = message
		self.key_length = key_length

		all_freq_scores = []
		for nth in range(1, self.key_length + 1):
			subkey_message = self.getNthSubkeyMessage(nth)
			subkey_scores = self.getSubkeyFreqScores(subkey_message)
			all_freq_scores.append(subkey_scores[:self.freq_rank_cutoff])
		return all_freq_scores

	# ////////////////////////
	# PRIVATE
	# ////////////////////////

	def getNthSubkeyMessage(self, n):
		return [self.message[i] for i in range(n - 1, len(self.message), self.key_length)]

	def getSubkeyFreqScores(self, subkey_message):
		freq_scores = []
		for possible_key in self.key_symbols:
			decrypted_text = self.cipher.decrypt(subkey_message, possible_key)
			freq_scores.append((possible_key, englishFreqMatchScore(decrypted_text)))
		return sorted(freq_scores, key=lambda x: x[1], reverse=True)


def englishFreqMatchScore(message):
	freq_order = getFreqOrder(message)
	return getInBothCount(sorted_letters[:6], freq_order[:6]) + getInBothCount(sorted_letters[-6:], freq_order[-6:])

def getFreqOrder(message):
	letter_counts = getLetterCounts(message)
	letters_by_count = getLettersByCount(letter_counts)
	sorted_letters = sortLettersByNormalFreq(letters_by_count)
	sorted_counts = sortByCount(sorted_letters)
	return sorted_counts

def getLetterCounts(message):
	message = message.upper()
	return {letter: message.count(letter) for letter in LETTERS}

def getLettersByCount(letter_counts):
	return {count: [letter for letter, value in letter_counts.items() if value == count] 
		for count in letter_counts.values()}

def sortLettersByNormalFreq(letters_by_count):
	return {count: ''.join(sorted(letters_by_count[count], 
		key=sorted_letters.find, reverse=True)) for count in letters_by_count}

def sortByCount(letters_by_count):
	return ''.join([letter for count, letter in 
		sorted(letters_by_count.items(), key=lambda x: x[0], reverse=True)])



