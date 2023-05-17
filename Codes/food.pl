% Facts
breakfast(idly).
breakfast(dosa).
dinner(chappathi).
lunch(briyani).
food(idly).
food(dosa).
food(chappathi).
food(briyani).

% Rule
meal(X) :- food(X).
meal(X) :- food(X), !.

% Queries
% i) Is Pizza a food?
?- food(pizza).

% ii) Is Idly a food?
?- food(idly).

% iii) Which food is meal and lunch?
?- food(X), meal(X), lunch(X).

% iv) Is Dosa a dinner?
?- dinner(dosa).

% v) Is Idly a breakfast?
?- breakfast(idly).

/*
First -> Make and Compile 

?- food(pizza).
?- food(idly).
?- food(X), meal(X), lunch(X).
?- dinner(dosa).
?- breakfast(idly).

*/