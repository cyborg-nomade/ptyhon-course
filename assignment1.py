"""Script solving the first assigment of the course
    """

MY_NAME = "Uriel Fiori"
MY_AGE = 32


def print_my_data():
    """Prints my data as one string
    """
    print("Name: "+MY_NAME + "\n Age: " + str(MY_AGE))


def print_args_as_single_string(arg1, arg2):
    """Prints any 2 arguments as single string

    Args:
        arg1 (any type): first argument
        arg2 (any type): second argument
    """
    result = str(arg1) + str(arg2)
    print(result)


def calculate_decades_lived_from_age(age: int) -> int:
    """Returns the number of decades lived from the given age

    Args:
        age (int): age to calculate

    Returns:
        INT: decades lived
    """
    return age // 10


print_my_data()
print_args_as_single_string(MY_NAME, MY_AGE)
DECADES_I_LIVED = calculate_decades_lived_from_age(MY_AGE)
print(DECADES_I_LIVED)
