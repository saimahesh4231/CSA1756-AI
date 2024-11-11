person('John Doe', '1990-01-15').
person('Alice Smith', '1985-03-22').
person('Bob Johnson', '1978-11-30').
person('Emily Davis', '2000-07-10').
person('Michael Brown', '1995-05-05').

find_dob(Name, DOB) :- person(Name, DOB).

find_name(DOB, Name) :- person(Name, DOB).
