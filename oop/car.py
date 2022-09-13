"""working with classes"""


class Car:
    """defines a car"""

    top_speed = 100

    def drive(self):
        """drives a car"""
        print(f"I am driving below {self.top_speed}")


car1 = Car()
car1.drive()
