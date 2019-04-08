class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def set_size(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


def _main():
    r = Rectangle(4, 5)
    print(r.get_area())
    r.set_size(2, 6)
    print(r.get_area())


if __name__ == "__main__":
    _main()
