parent('John', 'Paul').
parent('John', 'Mary').
parent('Paul', 'Robert').
parent('Paul', 'Linda').
parent('Mary', 'Kevin').
parent('Mary', 'Sophia').

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

male('John').
male('Paul').
male('Robert').
male('Kevin').

female('Mary').
female('Linda').
female('Sophia').

sibling(Person1, Person2) :-
    parent(Parent, Person1),
    parent(Parent, Person2),
    Person1 \= Person2.

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

grandchild(Grandchild, Grandparent) :-
    grandparent(Grandparent, Grandchild).

uncle_or_aunt(UncleOrAunt, NieceOrNephew) :-
    sibling(UncleOrAunt, Parent),
    parent(Parent, NieceOrNephew).

cousin(Person1, Person2) :-
    parent(Parent1, Person1),
    parent(Parent2, Person2),
    sibling(Parent1, Parent2).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Person),
    ancestor(Person, Descendant).

descendant(Descendant, Ancestor) :-
    ancestor(Ancestor, Descendant).
