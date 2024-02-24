person(john, date(1990, 5, 15),day(2)).
person(susan, date(1985, 8, 23),day(5)).
person(mike, date(1995, 2, 10),day(6)).
person(alice, date(1980, 11, 5),day(7)).
get_dob(Name, DOB,DAY) :- person(Name, DOB,DAY).
