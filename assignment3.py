"""Assignment 3

1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person.
Fill in any data you want.

2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

3) Use a list comprehension to check whether all persons are older than 20.

4) Copy the person list such that you can safely edit the name of the first person
(without changing the original list).

5) Unpack the persons of the original list into different variables and output these variables.
"""

import copy

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person.
# Fill in any data you want.

person1 = {
    "name": "John",
    "age": 22,
    "hobbies": ["table tennis", "running", "calculus"],
}
person2 = {
    "name": "Mary",
    "age": 21,
    "hobbies": ["knitting", "existentialist philosophy", "plotting revolution"],
}
person3 = {
    "name": "Luke",
    "age": 25,
    "hobbies": ["pilotting", "sword-fighting", "horse riding"],
}
list_of_persons = [person1, person2, person3]
print(list_of_persons)

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

list_of_names = [person["name"] for person in list_of_persons]
print(list_of_names)

# 3) Use a list comprehension to check whether all persons are older than 20.

are_all_persons_older_than_20 = all(person["age"] > 20 for person in list_of_persons)
COMPLEMENT_TO_PRINT = "" if are_all_persons_older_than_20 else "not "
print("All people are " + COMPLEMENT_TO_PRINT + "older than 20")

# 4) Copy the person list such that you can safely edit the name of the first person
# (without changing the original list).

copied_list_of_persons = copy.deepcopy(list_of_persons)
copied_list_of_persons[0]["name"] = "Jack"
print(list_of_persons)
print(copied_list_of_persons)

# 5) Unpack the persons of the original list into different variables and output these variables.
p1, p2, p3 = list_of_persons
print(p1, p2, p3)
