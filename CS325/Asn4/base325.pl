/*
  map names to and from variables using an association list

  When we have nodes 0,1,2,..., each node is represented by a variable 
  whose value determines whether the corresponding node is in D or not,
  we need to associate the name of a node with its representing variable

  E.g., ?- map([0,1,2],Vars, MapV)
        MapV = [(0,_A),(1,_B),(2,_C)],
        Vars = [_A,_B,_C] 

        If lableing assigns variables in Vars as [1,0,1], we know that
        nodes 1 and 3 are selected to form the subset.

  Try:  ?- map([0,1,2],Vars, MapV), map(2,V,MapV).
        MapV = [(0,_A),(1,_B),(2,V)],
        Vars = [_A,_B,V] ?

        V is precisely the varaible in Vars that corresponds to node 3.

  In general, names do not have to be numbers, try this:

       ?- map([aa,bb,cc],I,MapV).
        I = [_A,_B,_C],
        MapV = [(aa,_A),(bb,_B),(cc,_C)] ?
 
*/

map(X,Y,Map):-var(Map),!,
    map_build(X,Y,Map).
map(X,Y,Map):-
    map_get(X,Y,Map).

map_build([],[],[]).
map_build([A|As],[B|Bs],[(A,B)|Map]):-
    map_build(As,Bs,Map).

map_get([],[],_):-!.
map_get([A|As],[B|Bs],Map):-!,
    map_get(A,B,Map),
    map_get(As,Bs,Map).
map_get(A,B,Map):-
    member((A,B),Map),!.

%print a dominating set as required
output(L) :- output1(1,L).
output1(_,[]) :- !. 
output1(N,[1|R]) :- !,
   Term =.. [in,N], 
   write(Term), write(' '), 
   N1 is N+1,
   output1(N1,R).

output1(N,[0|R]) :-
   N1 is N+1,
   output1(N1,R).

% Timing the used cpu time
comp_statistics :- 
   statistics(runtime,[_,X]), 
   T is X/1000,
   nl,                     
   write('run time: '),
   write(T), write(' sec.'), nl.


