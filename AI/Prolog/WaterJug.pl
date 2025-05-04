% jug(X, Y) means X liters in Jug1 and Y liters in Jug2
goal(jug(2, _)).  % we want 2 liters in Jug1

move(jug(X, Y), jug(4, Y)) :- X < 4.        % Fill Jug1
move(jug(X, Y), jug(X, 3)) :- Y < 3.        % Fill Jug2
move(jug(X, Y), jug(0, Y)) :- X > 0.        % Empty Jug1
move(jug(X, Y), jug(X, 0)) :- Y > 0.        % Empty Jug2

% Pour Jug1 to Jug2
move(jug(X, Y), jug(X1, Y1)) :- 
    X > 0, Y < 3,
    T is min(X, 3 - Y),
    X1 is X - T, Y1 is Y + T.

% Pour Jug2 to Jug1
move(jug(X, Y), jug(X1, Y1)) :- 
    Y > 0, X < 4,
    T is min(Y, 4 - X),
    X1 is X + T, Y1 is Y - T.

% Path-finding
path(State, _, []) :- goal(State).
path(State, Visited, [Move|Rest]) :-
    move(State, Move),
    \+ member(Move, Visited),
    path(Move, [Move|Visited], Rest).

% ?- path(jug(0, 0), [jug(0, 0)], Moves).
