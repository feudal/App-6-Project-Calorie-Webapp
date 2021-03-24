
class Calorie:
    """
    Represent a amount of calories needs a person a today
    """
    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = 10*self.weight + 6.25*self.height + 5 - 10*self.temperature
        return result
