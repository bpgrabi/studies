##prawdopodobnie mam trochę inną ścieżkę względną, a nie dało się wysłać plików razem z kodem, bo były za duże

def find(size = 1000):
    count = 0
    file = open("./patterns/patterns/" + str(size) + "_pattern.txt", "r")
    txt = file.read()
    lines = txt.splitlines()
    for i in range(0, len(lines)-2):
        letters = lines[i]
        for j in range(0, len(letters)-2):
            if (str(letters[j]) == str("A") and str(letters[j+1]) == str("B") and str(letters[j+2]) == str("C")
            and str(lines[i+1][j]) == str("B") and str(lines[i+2][j]) == str("C")):
                print(i, j)
                count += 1
    print("number of patterns:", count)


if __name__ == "__main__":
    bol = 0
    while bol == 0:
        try:
            size = int(input("write witch txt u want check (1000, 2000, 3000, 4000, 5000, or 8000) "))
            find(size)
            bol = 1
        except:
            print("wrong number")
