can_get(State, Moves) :-
    can_get(State, [], Moves).

can_get(state(_, _, _, has), _, []).

can_get(State1, Visited, [Move | Moves]) :-
    move(State1, Move, State2),
    \+ member(State2, Visited),        % prevent cycles
    can_get(State2, [State2 | Visited], Moves).


move(state(X, onfloor, Box, no), walk(X, Y), state(Y, onfloor, Box, no)).
move(state(X, onfloor, X, no), push(X, Y), state(Y, onfloor, Y, no)).
move(state(X, onfloor, X, no), climb, state(X, onbox, X, no)).
move(state(X, onbox, X, no), grasp, state(X, onbox, X, has)).
