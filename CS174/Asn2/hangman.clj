
; messages
(def intro "Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
(def options "Please enter an integer number (0<=number<10) to choose the word in the list: ")
(def hint "The length of the word is: ")
(def instruct "Please enter the letter you guess: ")
(def hit "The letter is in the word.")
(def miss "The letter is not in the word.")
(def progress "Letters matched so far: ")
(def bye "Goodbye!")

; error messages
(def empty-input "Empty input!")
(def coerce-error "Input must be an integer!")
(def range-error "Index is out of range!")
(def extra-chars "You need to input a single alphabetic character!")

; target words
(def words ["cow", "horse", "deer", "elephant", "lion", "tiger", "baboon", "donkey", "fox", "giraffe"])
(def max_value 9)
(def min_value 0)


(defn input 
	([] 
		(println "Please enter your input: ")
		(read-line)
	)
	([user-message]
		(println user-message)
		(read-line)
	)
)

(defn coerce| 
	([value]
		(try
			(Integer/parseInt value)
			(catch Exception e false)
		)
	)
	([value verbose]
		(let [attempt (coerce| value)]	
			(if
				(boolean attempt)
				attempt
				(do
					(println coerce-error)
					false
				)
			)
		)
	)
)

(defn between? 
	([x] (and (> x min_value) (< x max_value)))
	([x verbose]
		(if 
			(between? x)
			true
			(do
				(println range-error)
				false
			)
		)
	)
)
	

(defn passes? [x]
	(let [attempt (coerce| x "verbose")] 
		(cond
			(or  
				(not attempt)
				(not (between? attempt "verbose"))
			) false
			:else attempt
		)
	)	
)

(defn menu []
	(loop [choice (input options)]
		(let [attempt (passes? choice)]
			(if attempt
				attempt
				(recur (input options))
			)
		)
	)
)

(defn play-game [option]
	(seq (println "playing game"))
)


; main function
(do
	(println intro)
	(play-game (menu))
	(println bye)
)
