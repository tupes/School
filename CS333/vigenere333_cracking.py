
from vigenere_cracking import VigenereCracker
from frequency_analysis import FrequencyAnalyzer
from detect_english import isEnglish


class Vigenere333Cracker(VigenereCracker):

	def __init__(self, cipher, key_symbols, verbose=False):
		self.cipher = cipher
		self.verbose = verbose
		self.freq_analyzer = FrequencyAnalyzer(cipher, key_symbols)
		
		self.ciphertext = None
		self.key_length = 0

	# ////////////////////////
	# PRIVATE
	# ////////////////////////

	def tryDecrypting(self, possible_key):
		decrypted_text = self.cipher.decrypt(self.ciphertext, possible_key)

		if isEnglish(decrypted_text) and self.userAcceptance(possible_key, decrypted_text):
			return decrypted_text


class Vigenere333Part2Cracker(VigenereCracker):

	def __init__(self, cipher, key_symbols, target, verbose=False):
		self.cipher = cipher
		self.key_symbols = key_symbols
		self.target = target
		self.key_length = len(self.target)
		self.verbose = verbose
		
		self.ciphertext = None

	# ////////////////////////
	# PUBLIC
	# ////////////////////////

	def crack(self, ciphertext):
		self.ciphertext = ciphertext
		
		print('Attempting crack with key length', self.key_length)
			
		result = self.attemptCrack()
		if result:
			return result

	def attemptCrack(self):
		for i in range(self.key_length):
			for possible_key in self.key_symbols:			
				decrypted_text = self.tryDecrypting(possible_key)
				if decrypted_text:
					return decrypted_text, possible_key

	def tryDecrypting(self, possible_key):
		decrypted_text = self.cipher.decrypt(self.ciphertext, possible_key)

		if isEnglish(decrypted_text) and self.userAcceptance(possible_key, decrypted_text):
			return decrypted_text
