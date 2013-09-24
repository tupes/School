

words = ['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon', 'donkey', 'fox', 'giraffe']
MAX_ERRORS = 6

class Hangman(object):
		def __init__(self):
			self.parts = [' ------------', ' |         |', ' |          O', ' |         / |', ' |          |', ' |         / |']
			self.errors = 0
		
		def update(self):
			self.errors += 1
			for part in self.parts[:self.errors]:
				print(part)

class Word(object):
		def __init__(self, word):
			self.name = word
			self.length = len(word)
			self.output = ['_'] * self.length
		
		def takeGuess(self, guess):
			if guess in self.name:
				self.update(guess)
				print("The letter is in the word.")
				return True
			else:
				print("The letter is not in the word.")
				return False
		
		def update(self, guess):
			for ii in range(self.length):
				if self.name[ii] == guess:
					self.output[ii] = guess
		
		def show(self):
			print("Letters matched so far:", ''.join(self.output))
		
		def isFound(self):
			if '_' in self.output: return False
			return True

def checkValidity(ans):
		if not ans:
			print("Empty input!")
			return False
		try: 
			ans = int(ans)
		except ValueError:
			print("Input must be an integer!")
			return False
		if not 0 <= ans < 10:
			print("Index is out of range!")
			return False
		return ans

def intro():
		print("Welcome to Hangman! Guess the mystery word with less than", str(MAX_ERRORS), "mistakes!")
		while True:
			ans = input("Please enter an integer number (0<=number<" + str(len(words)) + ") to choose the word in the list: ")
			wordIndex = checkValidity(ans)
			if not wordIndex: continue
			word = Word(words[wordIndex])
			print("The length of the word is:", str(word.length))
			return word

def play(word):
		man = Hangman()
		while True:
			guess = input("\nPlease enter the letter you guess: ")
			if not guess.isalpha() or len(guess) != 1:
				print("You need to input a single alphabetic character!")
				continue
			guess = guess.lower()
			isMatch = word.takeGuess(guess)
			word.show()
			if word.isFound():
				print("You have found the mystery word. You win!")
				return
			elif not isMatch:
				man.update()
				if man.errors == MAX_ERRORS:
					print(' |\n |')
					print("Too many incorrect guesses. You lost!")
					print("The word was:", word.name + '.')
					return


word = intro()
play(word)
print("Goodbye!")