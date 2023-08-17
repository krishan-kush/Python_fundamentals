import self


class Circle:
    def __init__(self, radius):
      self.radius = radius

    def area(self):
        return  3.14 * self.radius **2
circle=Circle(3)
print("my circle area is",circle.area())
