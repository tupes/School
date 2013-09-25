
(defun rotate (L N)
	(if
		(= N 0) L
		(rotate
			(append (cdr L) (list (car L)))
			(- N 1))))

(defun prefix (L)
	(if
		(null L) nil
		(let ( (first (car L)) )
			