"""working with classes"""


class Car:
    """defines a car"""

    # top_speed = 100

    def __init__(self, start_top_speed=100) -> None:
        self.top_speed = start_top_speed
        self.warnings = []

    def drive(self):
        """drives a car"""
        print(f"I am driving below {self.top_speed}")


car1 = Car()
car1.drive()

car1.warnings.append("New warning")

car2 = Car(300)
car2.drive()

print(car2.warnings)
