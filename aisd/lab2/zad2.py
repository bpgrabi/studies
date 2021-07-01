import time
stime = time.time()
#### 1. wczytanie pliku
file = open("zadanie2.csv", "r")
txt = file.read()
#print(txt)

#### 2. usunięcie pustych linii
l_count = sum(1 for line in open('zadanie2.csv'))
print(l_count)
tab = txt.splitlines()
newtxt = tab[0]
for i in range(1, l_count):
    a = tab[i].split(",", 1)
    if a[1] != "":
        newtxt = newtxt + "\n" + tab[i]
#print(newtxt)

#### 3. sortowanie po id
tab = newtxt.splitlines()
t_count = len(tab)
for i in range(1, t_count):
    for j in range(i+1, t_count):
        a = int(tab[i].split(",")[0])
        b = int(tab[j].split(",")[0])
        if a > b:
            x, y = tab[i], tab[j]
            tab[j], tab[i] = x, y

#### 4. rozwiązanie problemu z powatrzaniem się id
for i in range(1, t_count):
    for k in range(65, 91): #### 5. zmiana dużych liter na małe
        tab[i] = tab[i].replace(str(chr(k)), str(chr(k + 32)))
    for j in range(i + 1, t_count):
        a = int(tab[i].split(",")[0])
        b = int(tab[j].split(",")[0])
        if a == b:
            tab[j] = tab[j].replace(str(b), str(b+1))
    tab[i] = tab[i].replace(",", ", ")

#### 6. usunięcie słów o prefiksach z sąsiadujących liter
for i in range(1, t_count):
    remove = tab[i].split(" ")[1:]
    tab[i] = tab[i].split(" ")[0]
    for word in remove:
        try:
            if ord(word[0]) == ord(word[1]) + 1 or ord(word[0]) == ord(word[1]) - 1:
                word = ""
        except:
            a = 1
        tab[i] = tab[i] + " " + word

for i in range(1, t_count):
    print(tab[i])
etime = time.time()
print(etime-stime)

#### kod niestety jest napisany strasznie nieefektywnie, u mnie wykonywał się w 60-90s
#### niestety nie miałem innego pomysłu, żeby zrobić to wszystko np w jednej pętli, tak by spęłnione były warunki zadań