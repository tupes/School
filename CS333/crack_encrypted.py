
from string import ascii_uppercase, ascii_letters, digits

from vigenere333 import Vigenere333Cipher
from vigenere333_cracking import Vigenere333Cracker


path = 'data/'


def crack_encrypted(source_filename):
	cipher = Vigenere333Cipher()
	cracker = Vigenere333Cracker(cipher, ascii_letters + digits, True)

	with open(path + source_filename, 'rb') as cipherbytes_file:
		cipherbytes = cipherbytes_file.read()

	result = cracker.crack(cipherbytes)

	message, selected_key = result 
	print(message)
	print('Key:', selected_key)


if __name__ == '__main__':

	crack_encrypted('test_cipherbytes')
	
	crack_encrypted('ciphertext1')
