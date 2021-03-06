
%:- use_module(library(lists)).
:- use_module(library(clpfd)).

l :- consult('paperAssign1.pl').
:- include(ve).
:- include(base325).
bound(x). 
minweight(x).

n_factorial(0, 1).
n_factorial(N, F) :- N #> 0, N1 #= N - 1, F #= N * F1, n_factorial(N1, F1).

solve(N,S) :-
    S = [C0,C1,C2,N1,N2],       %Let S be bound to a list of five variables
    S ins 0..N, %domain(S,0,N),
    N #= C0 + C1*N1 + C2*N2*N2,
    labeling([],S).
    
q2(N, S) :-
	S = [X, Y],
	S ins 0..N, % domain(S, 0, N),
	N #= (X * X) + (Y * Y),
	labeling([], S).

% ****************************************************

assign(W1,W2) :-
      % output two lists of reviewers, the indices of positions in the lists
      % represent paper IDs
%   findall(R, reviewer(R,_,_), AllR),
    findall([R,A1,A2], reviewer(R,A1,A2), AllR), print(AllR), nl,
      % need info on areas of expertise of reviewers
    length(AllR,N), 
    relate(N,AllR,Name2Num), print(Name2Num), nl, % Store in Name2Num name-number pairs
    findall(P,paper(P,_,_,_),Papers), print(Papers), nl,
    length(Papers,NumP),
    length(VarsR1,NumP), %print(VarsR1), nl,   % list of papers each assigned to 1st reviewer
    length(VarsR2,NumP),    % list of papers each assigned to 2nd reviewer
    append(VarsR1,VarsR2,Vars),  % put into one list to be labeled below
    workLoadAtMost(K),       
    !,                      % none of the above needs redone.

    VarsR1 ins 1..N, % domain(VarsR1,1,N),
    VarsR2 ins 1..N, % domain(VarsR2,1,N),

    const1(1,VarsR1,Name2Num), % not review own paper starting from paper#1
    const1(1,VarsR2,Name2Num), % not review own paper 
    distinctReviewer(VarsR1,VarsR2),% each paper assigned to 2 distinct reviewers
    atMost(Vars,N,K),          % no reviewer reviews more than K papers
    qualified(NumP,VarsR1,VarsR2,AllR,Name2Num),
                               % reviewer must have the expertise
    labeling([ffc],Vars),
    num2name(VarsR1,W1,Name2Num),
    num2name(VarsR2,W2,Name2Num).

% ----------------------------------------------------------------------
% some utilities, you can run them to understand what they do
% For relate/3, e.g., run the query ?- relate(3,[a,b,c],W).

relate(0,[],[]) :- !.
relate(N,[[A,_,_]|L],[[A,N]|Sol]) :-
	N1 is N-1,
	relate(N1,L,Sol).

% convert a list of numbers to reviewer names
num2name([],[],_).
num2name([N|R],[B|L],N2M) :- 
    find(N,B,N2M),
    num2name(R,L,N2M).

%Given a number N, find name B, or given a name B, find the number N.
find(N,B,[[B,N]|_]) :- !.
find(N,B,[_|R]) :- find(N,B,R).

/* count(_, [], 0).
count(X, [X | T], N) :-
	!, count(X, T, N1),
	N is N1 + 1.
count(X, [_ | T], N) :-
	count(X, T, N). */
	
count(_, [], _).
count(X, [X | Rest], N) :-
	N1 is N + 1,
	count(X, Rest, N1).
count(X, [_ | Rest], N) :-
	count(X, Rest, N).
%--------------------------------------------------------------------------

%for each paper, find its subject area, eliminate all reviewers with 
%matching expertise and restrict the paper to be assigned to none of 
%the remaining reviewers.

%Note: The other way around, i.e., eliminating non-qualified, and 
%assigning the paper to one of the remaining reviewers seems more difficult.

qualified(0,_,_,_,_).
qualified(PaperID,VarsR1,VarsR2,AllR,Name2Num) :-
    paper(PaperID,_,_,Area),
           %find the paper's subject area
    print('Checking qualifications for '), print(Area), nl,
    rmReviewer(AllR,Area,Remaining), print(Remaining), nl,
           %remove all qualified and Remaining is the resulting list
    xconvert(Remaining,NotQualified,Name2Num), print(NotQualified), nl,
           %convert reviewers in Remaining to the corresponding numbers
           %and put then in list NotQualified
    nth(PaperID,V1,VarsR1), % get the domain variable in VarsR1 for PaperID
    nth(PaperID,V2,VarsR2), 
    noneOf(V1,NotQualified), %V1 cannot be assigned to any in NotQualified
    noneOf(V2,NotQualified),
    NewPaperID is PaperID-1,
    qualified(NewPaperID,VarsR1,VarsR2,AllR,Name2Num).

% rmReviewer(AllR,Area,Remaining): remove any reviewer in AllR
% if Area matches, and Remaining is the resulting list.
% ...... 
rmReviewer([], _, []) :- !.
rmReviewer([[Person, Area, _] | Rest], Area, Remaining) :-
	print('match1 '), print(Person), nl, !,
	rmReviewer(Rest, Area, Remaining).
rmReviewer([[Person, _, Area] | Rest], Area, Remaining) :-
	print('match2 '), print(Person), nl, !,
	rmReviewer(Rest, Area, Remaining).
rmReviewer([[Person, _, _] | Rest], Area, [Person | Remaining]) :-
	print('no match '), print(Person), nl, !,
	rmReviewer(Rest, Area, Remaining).

% xconvert/3 converts a list of reviewers to their corresponding numbers
% ...... list of names of people not qualified, Output as numbers, name-num pairs
xconvert([], [], _) :- !.
xconvert([Name | Rest], [Number | NotQualified], Name2Num) :-
	find(Number, Name, Name2Num),
	xconvert(Rest, NotQualified, Name2Num).

%nth(N,V,Lst): Given a number N, find the nth variable V in Lst
%this has been used before, e.g., for the graph coloring problem
nth(1,V,[V|_]) :- !. 
nth(N,V,[_|R]) :- 
    N1 is N -1,
    nth(N1,V,R).

%noneOf(A,Lst): the domain variable A is not equal to anyone in Lst.
% ......
noneOf(_, []) :- !.
noneOf(Num, [First | Rest]) :-
	Num #\= First,
	noneOf(Num, Rest). 


% for each paper, the reviewers have to be different
distinctReviewer([], []).
distinctReviewer([Person1 | Rest1], [Person2 | Rest2]) :-
	Person1 #\= Person2,
	distinctReviewer(Rest1, Rest2).

% each reviewer can only review at most K papers
/* atMost([], _, _).
atMost(People, N, K) :-
	[Person | Rest] = People,
	count(Person, People, Ans),
	%Ans #<= K,
	Ans in 0..K,
	atMost(Rest, N, K). */

atMost(_, 0, _).
atMost(People, N, K) :-
	nth(N, Person, People),
	limitReviews(Person, People, K), %print(Ans), nl,
	N1 is N - 1,
	atMost(People, N1, K).
	
limitReviews(Person, People, K) :- 
   %domain(Vars, 1,10),% some arbitrary domain
   occur(Person, People, K).   % I occurs in Vars N times
   %labeling([],Vars).

occur(Person, People, K) :- 
   generate_list(Person, People, Lst),
   sum(Lst, #<, K + 1).

generate_list(_,[],[]).
generate_list(I, [A | R], [1 | S]) :-
   I #= A,
   generate_list(I, R, S).
generate_list(I, [A | R], [0 | S]) :-
   I #\= A,
   generate_list(I, R, S).
   
/* generate_list(_,[],[]).
generate_list(I, [A | R], [T | S]) :-
   (I #= A #=> T#=1),
   (I #\= A #=> T#=0),
   generate_list(I, R, S). */	
	
% for each paper, no reviewer is an author of the paper
const1(_,[],_) :- !.
const1(N,[A|L],N2M) :-
    sat1(N,A,N2M),
    K is N+1,
    const1(K,L,N2M).

sat1(N,A,N2M) :- 
    paper(N,Author1,Author2,_),
    locate(N2M,Author1,Num1),
    locate(N2M,Author2,Num2),
    Num1 #\= A,
    Num2 #\= A.

locate([],_,-1) :- !.   % -1 does not match any author.
locate([[A,N]|_],A,N) :- !.
locate([_|L],B,M) :- 
     locate(L,B,M).

     
% ****************************************************

go(Vars) :-
	statistics(runtime,_),  % for timing the execution time
	findall(V,vtx(V),Vs),
	findall([V1,V2,W],edgewt(V1,V2,W),Es),
	map(Vs,Vars,MapV), print(MapV), nl,     % defined in the file base325.pl
	bound(K),
	minweight(MinW),
	length(Vars,N), print('setting domains'), nl, 
	Vars ins 0..1, %domain(Vars,0,1),
	NumOfOne in 0..N, %domain([NumOfOne],0,N),
	print('made it to sum'), nl,
	xsum(Vars,NumOfOne),
	NumOfOne #=< K,
	NumOfOne #> 0,
	hold(MapV,Es,MinW),
	labeling([],Vars),
	output(Vars),
	comp_statistics.

go(_) :-
	write('No more solution'),
	comp_statistics.

xsum([],0).
xsum([A|R],S) :- S #= A+S1, xsum(R,S1).  
 % counted if A=1, not otherwise

comp_statistics :-
	statistics(runtime,[_,X]), 
	T is X/1000,
	nl,                              % write CPU time to screen
	write('run time: '),
	write(T), write(' sec.'), nl.
 
 /*
hold(MapV,Es,MinW): For any vertex v not in D (i.e., it gets value 0), 
then  at least one of the following holds
 (1) sum { w_(i,v) | (i,v) in E, i is in D } >= w,
 (2) sum { w_(v,j) | (v,j) in E, j is in D } >= w.
*/

/*
hold(+MapV,+Es, +MinW) sets the constraints for the solver. 
hold1/4 generates the constraints necessary to ensure that 
        the conditions are satisfied.
*/

hold(MapV,Es,MinW) :- hold1(MapV,Es,MinW,MapV).
hold1([],_,_,_).
hold1([(N,V)|R],Es,MinW,MapV) :-
   V #=0,
   weightInList(N,Es,Lst1,MapV), print(Sum(Lst1)), nl,  %Get lists of incoming edge weights 
   weightOutList(N,Es,Lst2,MapV), %Get lists of outgoing edge weights
   Sum(Lst1) #> MinW,                         %Sum of weight for each vertex incoming edge
                            %Sum of weight for each vertex outgoting edge
                            %Compare sum of weight with MinW
   hold1(R,Es,MinW,MapV).

hold1([(_,V)|R],Es,MinW,MapV) :- V #= 1, hold1(R,Es,MinW,MapV).

/*
weightOutList(+Vertex, +Edges, -WeightList, + VertexMap)
*/

weightOutList(_,[],[],_).
% cons T for every member of 2nd arg
weightOutList(N,[[N,N1,W]|L],[W|R],MapV) :-
     !,

    weightOutList(N,L,R,MapV).

weightOutList(N,[_|R],L,MapV) :- weightOutList(N,R,L,MapV).

/*
Similar with weightOutList
*/

weightInList(_,[],[],_).

weightInList(N,[[N1,N,W]|L],[W|R],MapV) :-
    !,
   
    weightInList(N,L,R,MapV).

weightInList(N,[_|R],L,MapV) :- weightInList(N,R,L,MapV).
