
from unittest import TestCase, main

from vigenere import VigenereCipher
from vigenere_cracking import VigenereCracker


class TestVigenere(TestCase):

	def setUp(self):
		self.key = 'EDMONTON'
		self.plaintext = 'UNIVERSITY OF ALBERTA'
		self.ciphertext = 'YQUJRKGVXB AT NEPRVWM'

	def test_vigenere_encryption(self):
		ciphertext = VigenereCipher().encrypt(self.plaintext, self.key)
		self.assertEqual(ciphertext, self.ciphertext)

	def test_vigenere_decryption(self):
		plaintext = VigenereCipher().decrypt(self.ciphertext, self.key)
		self.assertEqual(plaintext, self.plaintext)

	def test_crack_vigenere(self):
		with open('data/book_cipherbytes', 'rb') as ciphertext_file, open('data/book_plaintext.txt') as plaintext_file:
			message, key = VigenereCracker(VigenereCipher()).crack(ciphertext_file.read())
			self.assertEqual(message, plaintext_file.read().replace('\n', ' '))
			self.assertEqual(key, 'ASIMOV')



if __name__ == '__main__':
	main()