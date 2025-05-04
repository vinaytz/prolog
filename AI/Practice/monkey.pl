% state(MonkeyLocation, MonkeyPosition, BoxLocation, HasBanana)
% MonkeyPosition: onfloor or onbox
% HasBanana: no or has

% Entry point: wrapper that starts with empty visited list
can_get(State, Moves) :-
    can_get(State, [], Moves).

% Base case: goal state reached
can_get(state(_, _, _, has), _, []).

% Recursive case with visited states tracking
can_get(State1, Visited, [Move | Moves]) :-
    move(State1, Move, State2),
    \+ member(State2, Visited),        % prevent cycles
    can_get(State2, [State2 | Visited], Moves).



can_get(state(door, onfloor, window, no), Moves).


% Monkey walks (from one location to another)
move(state(X, onfloor, Box, no), walk(X, Y), state(Y, onfloor, Box, no)).

% Monkey pushes box (if both are at same location and monkey is on floor)
move(state(X, onfloor, X, no), push(X, Y), state(Y, onfloor, Y, no)).

% Monkey climbs box
move(state(X, onfloor, X, no), climb, state(X, onbox, X, no)).

% Monkey grasps banana
move(state(X, onbox, X, no), grasp, state(X, onbox, X, has)).


% state = monkey_cd, monkey_po, box_cd, hasbanana? 