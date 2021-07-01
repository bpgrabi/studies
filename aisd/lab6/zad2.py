import zad1


class tree:
    def __init__(self, value = None):
        self.tab = [zad1.Node(1)] * int(value)
        for i in range(0, len(self.tab)):
            self.tab[i] = zad1.Node(i + 0.5)

    def printing(self):
        for i in range(0, len(self.tab)):
            self.tab[i].print()

    def insert(self, value):
        if len(self.tab) < value:
            for i in range(len(self.tab), int(value) + 1):
                self.tab.append(zad1.Node(i + 0.5))
        i = int(value)
        self.tab[i].insert(value)

    def search(self, value):
        if value >= len(self.tab):
            print("that value is not write in the structure")
        else:
            self.tab[int(value)].search(value)
            self.tab[int(value)].print()

    def minimum(self, value):
        if value >= len(self.tab):
            print("that value is not write in the structure")
        else:
            print("minimum in tree where is", value, " :", end=" ")
            self.tab[int(value)].mini()

    def maximum(self, value):
        if value >= len(self.tab):
            print("that value is not write in the structure")
        else:
            print("maximum in tree where is", value, " :", end=" ")
            self.tab[int(value)].max()

#example
if __name__ == "__main__":
    tabaluga = tree(5)
    tabaluga.tab[3].insert(3.99)
    tabaluga.insert(7.68)
    tabaluga.insert(19.99)
    tabaluga.printing()
    tabaluga.search(3.89)
    tabaluga.minimum(7.69)
    tabaluga.maximum(3.89)
    tabaluga.maximum(0.1)
