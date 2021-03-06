

(defun interp (expr P)
	(if (atom expr) expr
		(let ( (head (car expr)) )
			(cond
				( (member head '(first rest null atom number not)) 
						(funcall head (interp (second expr) P)) )
				( (member head '(eq cons equal + - * > < =)) 
						(funcall head (interp (second expr) P) (interp (third expr) P)) )
				( (member head '(and or))
						(cond
							( (and (eq head 'and) (not (interp (second expr) P))) nil )
							( (and (eq head 'or) (interp (second expr) P)) t )
							(t (eq t (interp (third expr) P)))
						))
				( (eq head 'if)
					(if (interp (second expr) P)
						(interp (third expr) P)
						(interp (fourth expr) P)
					))
				(t expr)
			)
		)
	)
)

(defun first (seq) (car seq))
(defun second (seq) (cadr seq))
(defun third (seq) (caddr seq))
(defun fourth (seq) (cadddr seq))
(defun rest (seq) (cdr seq))
(defun number (item) (numberp item))
;(print (second '(1 2 3)))
;(print (third '(1 2 3)))
;(print (fourth '(1 2 3 4)))

(print (interp '(+ 3 4) nil))
(print (interp '(rest (1 2 (3))) nil))
(print (interp '(rest (p 1 2 (3))) nil))
(print (interp '(first (rest (1 (2 3)))) nil))
(print (interp '(eq (< 3 4) (eq (+ 3 4) (- 2 3))) nil))
(print (interp '(if (> 1 0) (+ 1 2) (+ 2 3)) nil))
(print (interp '(if (> 1 0) (if (eq 1 2) 3 4) 5)  nil))
(print (interp '(cons (first (1 2 3))  (cons a nil)) nil))
(print (interp '(and (or t nil) (> 3 4)) nil))
(print (interp '(eq (1 2 3) (1 2 3)) nil))
(print (interp '(equal (1 2 3) (1 2 3)) nil))
