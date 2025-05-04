% --------------------------
% Interactive Medical Diagnosis Expert System
% --------------------------

% Ask the user about a symptom
ask(Symptom) :-
    format('Does the patient have ~w? (yes/no): ', [Symptom]),
    read(Reply),
    Reply == yes.

% Rules for diseases based on symptoms
disease(cold) :-
    ask(cough),
    ask(runny_nose),
    ask(sore_throat).

disease(flu) :-
    ask(fever),
    ask(cough),
    ask(headache),
    ask(fatigue).

disease(measles) :-
    ask(fever),
    ask(rash),
    ask(runny_nose),
    ask(cough).

% Diagnosis rule
diagnose(Disease) :-
    disease(Disease),
    format('The patient may have: ~w.~n', [Disease]),
    !.

diagnose(_) :-
    write('Sorry, the diagnosis is inconclusive based on the given symptoms.'), nl.
