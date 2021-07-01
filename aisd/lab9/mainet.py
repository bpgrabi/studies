class backpack():
    def __init__(self, size):
        self.arr = [[0 for x in range(size)] for y in range(size)]
        self.size = size
        self.mass = 0

    def add(self, item):
        if item[0] == 1 or item[0] > item[1]:
            x, y, mass = item[0], item[1], item[2]
        else:
            y, x, mass = item[0], item[1], item[2]
        tool = 0
        pointx, pointy = 0, 0
        while tool != 2:
            tool = 0
            if pointy + y < self.size:
                if pointx + x < self.size:
                    for j in range(pointy, pointy + y):
                        for i in range(pointx, pointx + x):
                            if self.arr[j][i] != 0:
                                tool = 1
                                if pointx + 1 < self.size:
                                    pointx += 1
                                elif pointy + 1 < self.size:
                                    pointy += 1
                                else:
                                    print("backpack if full")
                                    tool = 2
                                break
                        if tool == 1 or tool == 2:
                            break
                    if tool == 0:
                        self.mass += mass
                        for j in range(pointy, pointy + y):
                            for i in range(pointx, pointx + x):
                                self.arr[j][i] = mass
                                tool = 2
                else:
                    pointy += 1
                    pointx = 0
            else:
                tool = 2
        #self.print()
        #if pointx + x >= self.size or pointy + y >= self.size or tool == 1:
        #    print("u cant add item", str(x) + "x" + str(y), "at", str(pointx) + "," + str(pointy))

    def print(self):
        for i in range(0, self.size):
            print(self.arr[i])
        print(self.mass)


def item(height, width, mass):
    density = mass / (height*width)
    stats = [height, width, mass, density]
    return stats


def sort(A):
    for i in range(1, len(A)):
        x = A[i]
        key = A[i][3]
        j = i - 1
        while j >= 0 and A[j][3] < key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = x


if __name__ == "__main__":
    back = backpack(50)
    its1 = item(3, 5, 10)
    back.add(its1)
    back.print()
