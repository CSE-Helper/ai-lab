find_solution :-
          initial_state( Initial ),
          write( '== Starting Search ==' ), nl, 
          solution( [[Initial]], StateList ), 
          length( StateList, Len ),
          Transitions is Len -1, 
          format( '~n** FOUND SOLUTION of length ~p **', [Transitions] ), nl,
          showlist( StateList ), !.

solution( StateLists, StateList ) :-
          member( StateList, StateLists ),
          last( StateList, Last ), 
          goal_state(Last),
          report_progress( StateLists, final ).

solution( StateLists, StateList ) :- 
          report_progress( StateLists, ongoing ),
          extend( StateLists, Extensions ), !,
          solution( Extensions, StateList ), !.

solution( _, _ ) :- !,
          write( '!! Cannot extend statelist !!' ), nl,
          write( '!! FAILED: No plan reaches a goal  !!' ), nl, 
          fail, !.

extend( StateLists, ExtendedStateLists ) :- 
    setof( ExtendedStateList,
            StateList^Last^Next^( member( StateList, StateLists ),
                                  last( StateList, Last ),
                                  transition( Last, Next ), 
                                  legal_state( Next ),
                                  no_loop_or_loopcheck_off( Next, StateLists ),
                                  append( StateList, [Next], ExtendedStateList )
                                ),
             ExtendedStateLists
           ).
poss_empty_setof( X, G, S ) :- setof( X, G, S), !.
poss_empty_setof(_,_, []).
no_loop_or_loopcheck_off( _, _) :- loopcheck(off), !.
no_loop_or_loopcheck_off( Next, StateLists ) :- 
                        \+( already_reached( Next, StateLists ) ).
already_reached( State,  StateLists ) :-
           member( StateList, StateLists ),
           member( State1, StateList ),
           equivalent_states( State, State1 ). 
showlist([]).
showlist([H | T]) :- write( H ), nl, showlist( T ).
report_progress( StateLists, Status ) :-
      length( StateLists, NS ),
      StateLists = [L|_], length( L, N ),
      Nminus1 is N - 1,
      write( 'Found '), write( NS ), 
      write( ' states reachable in path length ' ), write(Nminus1), nl,
      ( Status = ongoing -> 
        (write( 'Computing extensions of length : ' ), write(N), nl) 
        ; true 
      ).

%%%  State representation will be as follows:
%%%  A state is a list:  [ how_reached, Jugstate1, Jugstate2, Jugstate3 ] 
%%%  Where each JugstateN is a lst of the form: [jugname, capcity, content]        
initial_state( [initial, [a,3,0], [b,5,0], [c,8,8]]).

%% Define goal state to accept any state where one of the
%% jugs contains 4 litres of water:
goal_state( [_, [a,_,4], [b,_,_], [c,_,_]]).
goal_state( [_, [a,_,_], [b,_,4], [c,_,_]]).
goal_state( [_, [a,_,_], [b,_,_], [c,_,4]]).

% Is it possible to get to this state?
%goal_state( [_, [a,_,_], [b,_,3], [c,_,3]]).
% Or this one?
%goal_state( [_, [a,_,_], [b,_,_], [c,_,6]]).


%%% There are six possible pour actions from one jug to another:
transition( [_, A1,B1,C], [pour_a_to_b, A2,B2,C] ) :- pour(A1,B1,A2,B2).
transition( [_, A1,B,C1], [pour_a_to_c, A2,B,C2] ) :- pour(A1,C1,A2,C2).
transition( [_, A1,B1,C], [pour_b_to_a, A2,B2,C] ) :- pour(B1,A1,B2,A2).
transition( [_, A,B1,C1], [pour_b_to_c, A,B2,C2] ) :- pour(B1,C1,B2,C2).
transition( [_, A1,B,C1], [pour_c_to_a, A2,B,C2] ) :- pour(C1,A1,C2,A2).
transition( [_, A,B1,C1], [pour_c_to_b, A,B2,C2] ) :- pour(C1,B1,C2,B2).

%%% The pour operation is defined as follows:
% Case where there is room to pour full contents of Jug1 to Jug2
% so Jug 1 ends up empty and its contents are added to Jug2.
pour( [Jug1, Capacity1, Initial1], [Jug2, Capacity2, Initial2], % initial jug states
      [Jug1 ,Capacity1, 0],   [Jug2, Capacity2, Final2]         % final jug states
    ):- 
       Initial1 =< (Capacity2 - Initial2), 
       Final2 is Initial1 + Initial2.

% Case where only some of Jug1 contents fit into Jug2
% Jug2 ends up full and some water will be left in Jug1.
pour( [Jug1, Capacity1, Initial1], [Jug2, Capacity2, Initial2], % initial jug states
      [Jug1 ,Capacity1, Final1],   [Jug2, Capacity2, Capacity2] % final jug states
    ):- 
       Initial1 > (Capacity2 - Initial2), 
       Final1 is Initial1 - (Capacity2 - Initial2).

%% Define the other helper predicates that specify how bb_planner will operate:
legal_state( _ ).               
equivalent_states( X, X ).      
loopcheck(on).                 

/*
?- find_solution.
*/