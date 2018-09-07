
from string import ascii_uppercase
from itertools import product

from frequency_analysis import FrequencyAnalyzer
from detect_english import isEnglish
from kasiski_examination import kasiskiExamination
from utilities import *


NUM_MOST_FREQ_LETTERS = 4


class VigenereCracker:

	def __init__(self, cipher, verbose=False):
		self.cipher = cipher
		self.verbose = verbose
		self.freq_analyzer = FrequencyAnalyzer(cipher, ascii_uppercase)
		
		self.ciphertext = None
		self.key_length = 0

	# ////////////////////////
	# PUBLIC
	# ////////////////////////

	def crack(self, ciphertext):
		self.ciphertext = ciphertext

		likely_key_lengths = kasiskiExamination(ciphertext)
		
		if self.verbose:
			print('The most likely key lengths are: ', ', '.join([str(length) for length in likely_key_lengths]))	
		
		for key_length in likely_key_lengths:
			self.key_length = key_length

			if self.verbose:
				print('Attempting crack with key length', key_length)
			
			result = self.attemptCrack()
			if result:
				return result

	# ////////////////////////
	# PRIVATE
	# ////////////////////////

	def attemptCrack(self):
		freq_scores = self.freq_analyzer.getFreqScores(self.ciphertext, self.key_length)

		if self.verbose:
			for i in range(len(freq_scores)):
				print('Possible letters for letter ' + str(i+1) + ' of the key:', 
					', '.join([key for (key, score) in freq_scores[i]]))

		return self.tryKeys(freq_scores)

	def tryKeys(self, freq_scores):
		for indexes in product(range(NUM_MOST_FREQ_LETTERS), repeat=self.key_length):
			possible_key = self.getPossibleKey(freq_scores, indexes)

			#if self.verbose:
			#	print('Attempting with key:', possible_key)			
			
			decrypted_text = self.tryDecrypting(possible_key)
			if decrypted_text:
				return decrypted_text, possible_key

	def getPossibleKey(self, freq_scores, indexes):
		return ''.join([freq_scores[i][indexes[i]][0] for i in range(self.key_length)])

	def tryDecrypting(self, possible_key):
		decrypted_text = self.cipher.decrypt(self.ciphertext.upper(), possible_key)

		if isEnglish(decrypted_text):
			decrypted_text = ''.join([decrypted_text[i].upper() if getSymbol(self.ciphertext[i]).isupper() else decrypted_text[i].lower() 
				for i in range(len(self.ciphertext))])
		
			return decrypted_text

	def userAcceptance(self, possible_key, decrypted_text):
		print('Possible encryption hack with key:', possible_key)
		print(decrypted_text[:200] + '\n') # only show first 200 characters
		print('Enter D if done:')
		return input('> ').strip().upper().startswith('D')
