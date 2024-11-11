bird('sparrow', yes).
bird('penguin', no).
bird('eagle', yes).
bird('ostrich', no).
bird('parrot', yes).
bird('kiwi', no).
can_fly(Bird) :-
    bird(Bird, yes),
    write(Bird), write(' can fly.'), nl.
cannot_fly(Bird) :-
    bird(Bird, no),
    write(Bird), write(' cannot fly.'), nl.

check_flight(Bird) :-
    (can_fly(Bbird) ; cannot_fly(Bbird)).
