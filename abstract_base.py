# abstract base


from abc import ABC , abstractmethod
class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class ractangle(shape):
    type = "ractangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth

rect1 = ractangle()
print(rect1.print_area())
