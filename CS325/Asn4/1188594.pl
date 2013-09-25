:- use_module(library(lists)).
:- use_module(library(clpfd)).

l :- consult('paperAssign1.pl').

/*
Question 2
q2(+N, -S)
determines whether there exists two numbers such that 
the sum of their squares equals N
*/
    
q2(N, S) :-
	S = [X, Y],
	domain(S, 0, N),
	N #= (X * X) + (Y * Y),
	labeling([], S).

% ****************************************************
/* Question 3
assign(-W1, -W2)
given a set of papers and reviewers, assign two reviewers to
each paper while satisfying all of the constraints
*/

assign(W1,W2) :-
      % output two lists of reviewers, the indices of positions in the lists
      % represent paper IDs
    findall([R,A1,A2], reviewer(R,A1,A2), AllR),
      % need info on areas of expertise of reviewers
    length(AllR,N), 
    relate(N,AllR,Name2Num), % Store in Name2Num name-number pairs
    findall(P,paper(P,_,_,_),Papers),
    length(Papers,NumP),
    length(VarsR1,NumP), % list of papers each assigned to 1st reviewer
    length(VarsR2,NumP),    % list of papers each assigned to 2nd reviewer
    append(VarsR1,VarsR2,Vars),  % put into one list to be labeled below
    workLoadAtMost(K),       
    !,                      % none of the above needs redone.

    domain(VarsR1,1,N),
    domain(VarsR2,1,N),

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
    rmReviewer(AllR,Area,Remaining),
           %remove all qualified and Remaining is the resulting list
    xconvert(Remaining,NotQualified,Name2Num),
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
	!,
	rmReviewer(Rest, Area, Remaining).
rmReviewer([[Person, _, Area] | Rest], Area, Remaining) :-
	!,
	rmReviewer(Rest, Area, Remaining).
rmReviewer([[Person, _, _] | Rest], Area, [Person | Remaining]) :-
	!,
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

atMost(_, 0, _).
atMost(People, N, K) :-
	nth(N, Person, People),
	limitReviews(Person, People, K),
	N1 is N - 1,
	atMost(People, N1, K).
	
limitReviews(Person, People, K) :- 
   occur(Person, People, K).   % I occurs in Vars N times

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
