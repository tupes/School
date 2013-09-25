

(defun interp (E P)
	(print E)
	(if 
		(atom E) E   ; this includes the case where expr is nil
		; else
		(let ( (f (car E))  (arg (cdr E)) )
			;(print arg)
			(cond 
				; handle built-in functions
				((eq f 'first) (car (interp arg P)))
				((eq f 'rest) (cdr (interp arg P)))
				((eq f 'null) (null (interp arg P)))
				((eq f 'atom) (atom (interp arg P)))
				((eq f 'number) (numberp (interp arg P)))
				((eq f 'eq) (eq (interp arg P)))
				((eq f 'equal) (equal (interp arg P)))
				((eq f '+) (+ (interp (car arg) P) (interp (cdr arg) P)))
				((eq f '-) (- (interp (car arg) P) (interp (cdr arg) P)))
				((eq f '*) (* (interp (car arg) P) (interp (cdr arg) P)))
				((eq f '>) (> (interp (car arg) P) (interp (cdr arg) P)))
				((eq f '<) (< (interp (car arg) P) (interp (cdr arg) P)))
				((eq f '=) (= (interp (car arg) P) (interp (cdr arg) P)))
				

				; if f is a user-defined function,
				;    then evaluate the arguments 
				;         and apply f to the evaluated arguments 
				;             (applicative order reduction) 


				; otherwise f is undefined; in this case,
				; E is returned as if it is quoted in lisp
				(t
					(if (not (atom f))
						(car E)
						E
					)
				)
			)
		)
	)
)

;(print (cdr '(1 2 (3))))

;(print (interp '(rest (1 2 (3))) nil))
;(print (interp '(first (1 2 (3))) nil))
;(print (interp '(rest (p 1 2 (3))) nil))
;(print (interp '(first (p 1 2 (3))) nil))
;(print (interp '(first (rest (1 (2 3)))) nil))
;(print (interp '(+ 3 4) nil))
(print (interp '(first (rest (1 (2 3)))) nil))