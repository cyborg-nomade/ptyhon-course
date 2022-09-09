""" Assignment 5

1) Import the random function and generate both a random number between 0 and 1
as well as a random number between 1 and 10.

2) Use the datetime library together with the random number to generate a random, unique value.
"""

# 1) Import the random function and generate both a random number between 0 and 1
# as well as a random number between 1 and 10.
import random
import datetime

random_number_between_0_and_1 = random.random()
random_number_between_1_and_10 = random.randint(1, 10)
print(random_number_between_0_and_1, random_number_between_1_and_10)

# 2) Use the datetime library together with the random number to generate a random, unique value.
random_ordinal = random.randint(
    datetime.date.min.toordinal(), datetime.date.max.toordinal()
)
random_date = datetime.date.fromordinal(random_ordinal)
print(random_date)
