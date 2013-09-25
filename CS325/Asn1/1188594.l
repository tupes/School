#| 
************************
Mark Tupala
1188594
CMPUT 325
Section 
Assignment 1
************************
|#

#| ************************
 QUESTION 1
This function takes a list with an even number of elements as an argument,
and returns a list of lists, where each list contains a pair of elements from the
argument, in the original order.
test case:
(form-pair '(4 6 9 4 2 5)) => ((4 6) (9 4) (2 5))
|#

(defun form-pair (L)
	(if (not L) nil ; recursive base case
		(cons ; 
			(list ; create a list from the next two elements, and cons it with the recurse
				(car L) 
				(cadr L))
			(form-pair (cddr L))))) ; recurse with everything after the first two



#| ************************
 QUESTION 2
This function takes a list of lists as an argument, where each list contains
a pair of elements. It returns the original list unmodified, except where the
first element of the pair is greater than the second element, in which case it
doubles both the first and second elements.
test case:
(increase '((4 5) (8 3) (2 8) (0 4) (7 6))) => ((4 5) (16 6) (2 8) (0 4) (14 12))
|#

(defun increase (L)
	(if (not L) nil ; recursive base case
		; the sequential let is simply to make it easier to read
		(let* ((pair (car L))
				(first (car pair))
				(second (cadr pair))
				(rest (cdr L)))
			; test whether the first element is greater than the second
			(if (<= first second) ; either way, recurse with the rest of the pairs
					(cons ; if it's not greater, keep the values the same
						(list 
							first 
							second) 
						(increase rest))
					(cons ; if it is greater, double both values
						(list 
							(* first 2) 
							(* second 2)) 
						(increase rest))))))



#| ************************
 QUESTION 3
This function takes a list as an argument, and returns the unique elements
of the list in their original order (duplicate values will overwrite earlier instances).
test case:
(remove-duplicate '(4 6 8 3 9 8 4 8 3 2 1 6)) => (9 4 8 3 2 1 6)
|#

(defun remove-duplicate (x)
	(cond
		((not x) nil) ; recursive base case
		; test whether the next element is found again in the rest of the list
		((contains? (cdr x) (car x)) 
			(remove-duplicate (cdr x))) ; if it is, recurse without including it in the result
		; if it's not found again, cons it with the recurse
		(t 
			(cons 
				(car x) 
				(remove-duplicate (cdr x))))))


#| ************************
 QUESTION 4
This function takes a list as an argument, and returns the number of unique
elements found in the list.
test case:
(my-count '(4 6 8 3 9 8 4 8 3 2 1 6)) => 7
|#

(defun my-count (L)
	(cond
		((not L) 0) ; recursive base case
		; test whether the next element is found again in the rest of the list
		((contains? (cdr L) (car L)) 
			(my-count (cdr L))) ; if it is, recurse without adding 1
		; if it's not found again, add 1 to the recurse
		(t 
			(+ 1 (my-count (cdr L))))))


#| ************************
 QUESTION 6 (Part 1)
This function takes a target value and a list of lists as arguments, where the lists contain pairs
of elements, and returns a list of the values that are linked to the target value.
test cases:
(reached 'a '((a b) (b c) (b e) (p b))) => (b c e)
(reached 'a '((e p) (b c) (a b) (c a) (c b))) => (b c)
(reached 'a '((a a))) => nil
|#

(defun reached (target pairs)
	(rchd target pairs pairs (cons target ())))

; accumulator function
(defun rchd (target whole-list part-list results)
	(if (not part-list) nil ; recursive base case
		; sequential let to make things easier to read
		(let* ((pair (car part-list))
			   (first (car pair))
			   (second (cadr pair))
			   (rest-list (cdr part-list)))
			(cond
				((and (equal target first) (not (equal first second)) (not (contains? results second)))
					; if passes cond, add it to the result
					(let ((new-results (cons second results)))
						(cons 
							second 
							(append 
								(rchd target whole-list rest-list new-results) 
								(rchd second whole-list whole-list new-results)))))
				
				(t 
					(rchd target whole-list rest-list results))))))


; HELPER FUNCTION
; boolean function that returns true when the item is found in the list L, otherwise
; returns false

(defun contains? (L item)
	(cond 
		((not L) nil)
		((equal item (car L)) t)
		((contains? (cdr L) item))))


(print (form-pair '(4 6 9 4 2 5)))
(print (increase '((4 5) (8 3) (2 8) (0 4) (7 6))))
(print (remove-duplicate '(4 6 8 3 9 8 4 8 3 2 1 6)))
(print (my-count '(4 6 8 3 9 8 4 8 3 2 1 6)))
(print (reached 'a '((a b) (b c) (b e) (p b))))
(print (reached 'a '((e p) (b c) (a b) (c a) (c b))))
(print (reached 'a '((a a))))