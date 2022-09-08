"""Functions
"""


def unlimited_args(*args, **kwargs):
    """prints unlimited args"""
    for arg in args:
        print(arg)
    for k, argument in kwargs.items():
        print(k, argument)


unlimited_args(1, 2, 3, 4, name="Uriel", age=29)
