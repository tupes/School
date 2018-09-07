
from unittest import TestCase, main
from string import ascii_uppercase, ascii_letters, digits

from vigenere333 import Vigenere333Cipher
from vigenere333_cracking import Vigenere333Cracker


class TestVigenere333(TestCase):

	def setUp(self):
		self.key = 'k'
		self.plaintext = 'h'
		self.ciphertext = ['0xB5']

	def test_modified_vigenere_encryption(self):
		ciphertext = Vigenere333Cipher().encrypt(self.plaintext, self.key)
		self.assertEqual(ciphertext[0], self.ciphertext[0])

	def test_modified_vigenere_decryption(self):
		plaintext = ''.join(Vigenere333Cipher().decrypt(
				[int(h, 16) for h in self.ciphertext], self.key))
		self.assertEqual(plaintext, self.plaintext)


	def test_crack_book(self):
		with open('data/test_cipherbytes', 'rb') as ciphertext_file, open('data/book_plaintext.txt') as plaintext_file:
			cracker = Vigenere333Cracker(Vigenere333Cipher(), ascii_uppercase)
			message, key = cracker.crack(ciphertext_file.read())
			self.assertEqual(message, plaintext_file.read().replace('\n', ' '))
			self.assertEqual(key, 'ASIMOV')

	def test_crack_cipher1(self):
		with open('data/ciphertext1', 'rb') as ciphertext_file, open('data/ciphertext1_plaintext.txt') as plaintext_file:
			cracker = Vigenere333Cracker(Vigenere333Cipher(), ascii_letters + digits)
			message, key = cracker.crack(ciphertext_file.read())
			self.assertEqual(message, plaintext_file.read())
			self.assertEqual(key, '4fathers')


if __name__ == '__main__':
	main()