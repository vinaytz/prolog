move(1, Source, Destination, _):-
    write('move disk from '), write(Source), write(' to '), write(Destination), nl.

move(N, Source, Destination, Helper):-
    N > 1,
    M is N - 1, 

    move(M, Source, Helper, Destination),
    move(1, Source, Destination, _),
    move(M, Helper, Destination, Source).
