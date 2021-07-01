import time
stime = time.time()

class xogame():
    def __init__(self):
        self.tab = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.counter = 0

    def board(self):
        for i in range(0, 3):
            print("_____________")
            print("|", self.tab[3 * i], "|", self.tab[3 * i + 1], "|", self.tab[3 * i + 2], "|")
        print("_____________")

    def move(self):
        if self.counter % 2 == 0:
            pos = int(input("Gdzie wpisać x?"))
            if 0 < pos < 10:
                self.tab[pos - 1] = "x"
            else:
                print("wrong move, pls choose from range (1, 9)")
        else:
            pos = int(input("Gdzie wpisać o?"))
            if 0 < pos < 10:
                self.tab[pos - 1] = "o"
            else:
                print("wrong move, pls choose from range (1, 9)")
        self.counter = self.counter + 1

    def check(self):
        if self.counter == 9:
            print("game ended")

game = xogame()
for i in range(1, 10):
    game.board()
    game.move()
