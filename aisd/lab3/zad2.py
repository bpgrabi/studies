class circle:
    def __init__(self):
        self.rad = float(input("type a radius of the circle"))

    def area(self):
        area = self.rad ** 2 * 3.14
        return "circle's area is: " + str(area)

    def circuit(self):
        circuit = self.rad * 2 * 3.14
        return "circle's circuit is: " + str(circuit)


class triangle:
    def __init__(self):
        count = 0
        while count == 0:
            a, b, c = float(input("type first edge of the triangle")), float(input("second")), float(input("and third edge"))
            if a + b > c and a + c > b and b + c > a:
                self.a = a
                self.b = b
                self.c = c
                count = 1
            else:
                print("its not a triangle")

    def area(self):
        try:
            p = (self.a + self.b + self.c) / 2
            area = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1/2)
            return "triangle's area is: " + str(area)
        except AttributeError:
            print("i say it again: its not a triangle")

    def circuit(self):
        try:
            circuit = self.a + self.b + self.c
            return "triangle's circuit is: " + str(circuit)
        except AttributeError:
            print("i say it again: its not a triangle")


class square:
    def __init__(self):
        self.a = float(input("type an edge of the square"))

    def area(self):
        area = self.a ** 2
        return "square's area is: " + str(area)

    def circuit(self):
        circuit = self.a * 4
        return "square's circuit is: " + str(circuit)
