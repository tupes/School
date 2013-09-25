
/*
Mark Tupala
1188594
CMPUT 325
Lec B1
Assignment 3
*/

/*
Question 1
setUnion(+S1, +S2, -S3)
Given two lists S1 and S2, setUnion returns the union of 
those two lists in S3
*/
setUnion([], S3, S3).
% if A is a member of S2, ignore it
setUnion([A | Rest], S2, S3) :- member(A, S2), setUnion(Rest, S2, S3).
% otherwise append it to the result
setUnion([A | Rest], S2, [A | S3]) :- setUnion(Rest, S2, S3).


/*
Question 2
swap(+L, -R)
Given a list L, swap takes every pair of elements and swaps their order, 
placing the new list in R
*/
swap([], []).
swap([A, B | Rest], [B, A | R]) :- swap(Rest, R).


/*
Question 3
largest(+L, -N)
Given a list L, largest finds the integer with the greatest value and 
returns it in N
*/
largest([A | Rest], N) :- largest_helper(Rest, N, A).

largest_helper([], Out, Out).
% if A is larger than Current, A becomes the new Current
largest_helper([A | Rest], Out, Current) :- 
	A > Current, largest_helper(Rest, Out, A).
% otherwise Current remains the same
largest_helper([A | Rest], Out, Current) :- 
	largest_helper(Rest, Out, Current).


/*
Question 4
countAll(+L, -N)
Given a list L, count the number of occurrences of each atom,
and return a list of [atom, count] pairs as N
*/
countAll(L, N) :- get_unique(L, [], N).

% get_unique takes a list of atoms and eliminates duplicate values,
% then passes its result to create_counter
get_unique([], Current, Out) :- create_counter(Current, Current, [], Out).
get_unique([A | Rest], Current, Out) :- 
	member(A, Current), get_unique(Rest, Current, Out).
get_unique([A | Rest], Current, Out) :- 
	get_unique(Rest, [A | Current], Out).

% create_counter takes a list of atoms with no duplicates,
% and creates a list with [atom, 0] pairs for each atom,
% and passes its result to add_tallies
create_counter(Orig, [], Current, Out) :- add_tallies(Orig, Current, [], Out).
create_counter(Orig, [A | Rest], Current, Out) :- 
	create_counter(Orig, Rest, [[A, 0] | Current], Out).

% add_tallies takes a list of [atom, count] pairs, 
% and attempts to get a count for each atom
% by using get_count
add_tallies(L, [], Out, Out).
add_tallies(L, [[Key, Value] | Pairs], Current, Out) :-  
	get_count(L, Key, Value, NewValue), 
	add_tallies(L, Pairs, [[Key, NewValue] | Current], Out).

% get_count takes a list of atoms and a key atom,
% and attempts to count the number of instances of the key
% in the list
get_count([], Key, Out, Out).
get_count([A | Rest], Key, Count, Out) :- 
	A == Key, NewCount is Count + 1, get_count(Rest, Key, NewCount, Out).
get_count([A | Rest], Key, Count, Out) :- 
	NewCount is Count, get_count(Rest, Key, NewCount, Out). 


