

(defun interp (E P)
  (cond 
	((atom E) E)   ;this includes the case where expr is nil
        (t
           (let ( (f (car E))  (arg (cdr E)) )
	      (cond 
                ; handle built-in functions
                ((eq f 'first)  (car (interp arg P)))
		(t (car E)))))))


(print (interp '(first (1 2 (3))) nil))