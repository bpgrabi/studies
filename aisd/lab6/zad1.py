class Node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    # printing elements according to instruction
    def printer(self, counter=0, space = 0, new = 0):
        if new == 1:
            print("\n" + " " * space + "-" * counter + str(self.value), end=" ")
        else:
            print("-" * counter + str(self.value), end=" ")

        if self.left:
            self.left.printer(counter + 1, space + counter + len(str(self.value)) + 1, 0)
        if self.right:
            self.right.printer(counter + 1, space + counter + len(str(self.value)) + 1, 1)

    # add new line to separate trees
    def print(self):
        self.printer()
        print("\n", "____________")

    #insert new elements in the list
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def search(self, value):
        if self.value:
            if value < self.value:
                if self.left == None:
                    print("that value doesnt exist")
                else:
                    self.left.search(value)
            if value > self.value:
                if self.right == None:
                    print("that value doesnt exist")
                else:
                    self.right.search(value)
            if value == self.value:
                print("that value exists")
        else:
            print("hmm something is wrong, u should never see this error")

    def mini(self):
        if self.value:
            if self.left != None:
                self.left.mini()
            if self.left == None:
                # print(self.value)
                pass

    def max(self):
        if self.value:
            if self.right != None:
                self.right.max()
            if self.right == None:
                #print(self.value)
                pass


#example
if __name__ == "__main__":
    tab = [Node(1.5), Node(3.5), Node(4.5), Node(7.5), Node(9.5)]
    for i in range(0, len(tab)):
        tab[i].print()
    print("and now new tab")
    tab[0].insert(1.3), tab[0].insert(1.6)
    tab[1].insert(3.7)
    tab[2].insert(4.0), tab[2].insert(4.99)
    tab[3].insert(7.3), tab[3].insert(7.8), tab[3].insert(7.7)
    tab[3].insert(7.9), tab[3].insert(7.6)
    tab[4].insert(9.3)
    for i in range(0, len(tab)):
        tab[i].print()
