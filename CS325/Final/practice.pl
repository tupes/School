
test([],L,L).
test(L,[],L).
test([A|X],[A|Y],R) :- !, test(X,Y,R).
test([_|X],[B|Y],R) :- test(X,[B|Y],R).


a(X) :- b(X), !, c1(X), c2(X,Y).
b(X) :- d(X).
d(f(_)).
d(g(1)).
d(g(2)).
c1(f(1)).
c1(f(2)).
c1(g(1)).
c2(X,1).
c2(X,2).


generate(0, R) :- !, print(R).
generate(N, R) :- var(R), N1 is N - 1,
	generate(N1, [N]).
generate(N, R) :- N1 is N - 1,
	generate(N1, [N | R]).


count([], A, 0).
count([A | B], A, N) :- count(B, A, N1), N is N1 + 1.
count([C | B], A, N) :- atomic(C), count(B, A, N).
count([L | B], A, N) :- count(L, A, N1), !,
	count(B, A, N2), !, 
	N is N1 + N2.


courses_taken([], Name, []).
courses_taken([[Course, Names] | Rest], Name, [Course | Courses]) :-
	member(Name, Names), print(Names), nl, !, 
	courses_taken(Rest, Name, Courses).
courses_taken([[Course, Names] | Rest], Name, Courses) :-
	courses_taken(Rest, Name, Courses).
	
