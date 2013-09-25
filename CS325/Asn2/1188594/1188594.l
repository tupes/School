
#| 
************************
Mark Tupala
1188594
CMPUT 325
Section 
Assignment 1
************************
|#

(defun interp (expr P)
	(if (atom expr) expr
		(let ( (head (car expr)) )
			(cond
				( (member head '(first rest null atom number not eq cons equal + - * > < =))
						(apply head (interp-args (cdr expr) P)) )
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
				; check for a user defined function
				( (get-func head P)
						; found the function, so reduce
						(let* ( (func (get-func head P)) (body (get-body func)) (params (get-params (cdr func))) )
							(sub body (zip params (interp-args (cdr expr) P)) )))
				
				; first element is not a function, return as data
				(t expr)
			)
		)
	)
)

(defun get-func (func-name P)
	(cond 
		( (null P) nil )
		( (eq func-name (caar P)) (car P) )
		(t (get-func func-name (cdr P)))))

(defun get-params (text)
	(if (eq (car text) '=) nil
		(cons (car text) (get-params (cdr text)))))

(defun get-body (text)
	(if (eq (car text) '=) (cdr text) 
		(get-body (cdr text))))

(defun sub (body sub-pairs)
	(cond 
		( (null body) nil )
		( (not (atom body)) (cons (sub (car body) sub-pairs) (sub (cdr body) sub-pairs)) )
		; body must be an atom. try to replace for every param-arg pair
		(t
			(cons (sub-token body sub-pairs) (sub (cdr body) sub-pairs)))))

(defun sub-token (token sub-pairs)
	(if (null sub-pairs) nil
		(cons (maybe-sub token (car sub-pairs)) (sub-token token (cdr sub-pairs)))))

(defun maybe-sub (token sub-pair)
		(let ( (param (first sub-pair)) (arg (second sub-pair)) )
			(if (eq token param)
				arg
				token)))

(defun interp-args (args P)
	(if (null args) nil
		(cons (interp (car args) P) (interp-args (cdr args) P))))

(defun zip (L1 L2)
	(if (null L1) nil
		(list (car L1) (car L2) (zip (cdr L1) (cdr L2)))))

(defun first (seq) (car seq))
(defun second (seq) (cadr seq))
(defun third (seq) (caddr seq))
(defun fourth (seq) (cadddr seq))
(defun rest (seq) (cdr seq))
(defun number (item) (numberp item))


