

(defun compile-prog (P)
	(if (null P) nil
		(cons (compile-func (car P)) (compile-prog (cdr P)))))

(defun compile-func (func)
	(let ( (func-name (car func)) (params (get-params (cdr func))) (body (get-body (cdr func))) )
		;(print func-name)
		;(print params)
		;(print body)
		(function (defun func-name 'params 'body))
	)
)

(defun get-params (text)
	(if (eq (car text) '=) nil
		(cons (car text) (get-params (cdr text)))))

(defun get-body (text)
	(if (eq (car text) '=) (cdr text) 
		(get-body (cdr text))))


(print
(compile-prog
	'(
		 (count L =   (if  (null L)
							 0
							 (+ 1 (count (rest L)))))
		
		(reverse X =  (if (null X) 
                            nil
                            (append (reverse (rest X)) 
                                    (cons (first X) nil))))

        (append X Y = (if (null X) 
                            Y
                            (cons (first X) (append (rest X) Y))))
	)
)
)