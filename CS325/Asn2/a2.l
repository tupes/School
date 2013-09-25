
(defvar *unary-funcs* '(car cdr))
(defvar *binary-funcs* '(+ - *))

(defun interp (expr P)
	(print expr)
	(if (atom expr) expr
		;else
		(let ( (head (car expr)) (body (cdr expr)) )
			(if (not (atom head)) (interp head P)
				;else
				(cond
					( (member head *unary-funcs*) (apply head (interp body P)) )
					;( (member head *ops*) (apply head body) )
					; check for user defined funcs
					(t expr)
					;(t (cons head (interp body P)))
				)
			)
		)
	)
)


;(print (interp '(+ 3 4) nil))

(print (interp '(cdr (1 2 (3))) nil))
;(print (interp '(rest (p 1 2 (3))) nil))
;(print (interp '(first (rest (1 (2 3)))) nil))