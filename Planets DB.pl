planet('Mercury', 58, 0).
planet('Venus', 108, 0).
planet('Earth', 150, 1).
planet('Mars', 228, 2).
planet('Jupiter', 778, 79).
planet('Saturn', 1430, 83).
planet('Uranus', 2870, 27).
planet('Neptune', 4500, 14).
find_distance(PlanetName, Distance) :-
    planet(PlanetName, Distance, _).
find_moons(PlanetName, Moons) :-
    planet(PlanetName, _, Moons).
find_planet_by_moons(Moons, PlanetName) :-
    planet(PlanetName, _, Moons).

find_planet_by_distance(DistanceLimit, PlanetName) :-
    planet(PlanetName, Distance, _),
    Distance =< DistanceLimit.
