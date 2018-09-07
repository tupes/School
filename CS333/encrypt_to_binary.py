
from binascii import a2b_hex, b2a_hex

from vigenere333 import Vigenere333Cipher


path = 'data/'


def encrypt_text_to_binary(source_filename, sink_filename, key):
	with open(path + source_filename) as plaintext_file:
		plaintext = plaintext_file.read().replace('\n', ' ')
	write(sink_filename, key, plaintext)

def encrypt_binary_to_binary(source_filename, sink_filename, key):
	with open(path + source_filename, 'rb') as plaintext_file:
		plaintext = plaintext_file.read()
	write(sink_filename, key, plaintext)


def write(sink_filename, key, plaintext):
	cipher = Vigenere333Cipher()
	ciphertext = cipher.encrypt(plaintext, key)
	cipherbytes = [a2b_hex(h[2:]) for h in ciphertext]

	with open(path + sink_filename, 'wb') as cipherbytes_file:
		for hx in cipherbytes:
			cipherbytes_file.write(hx)


if __name__ == '__main__':

	encrypt_text_to_binary('book_plaintext.txt', 'test_cipherbytes', 'ASIMOV')
