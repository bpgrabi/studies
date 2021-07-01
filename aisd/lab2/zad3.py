import time

#### 1. wczytanie dowolnego tekstu z klawiatury
text = ""
word = 0
while word == 0:
    text = input("write smoething")
#### 2. sprawdzenie czy wpisany tekst, jest jednym słowem, jeżeli nie, to ponawia próbę
#### tak zrozumiałem ten podpunkt
    if len(text.split(" ")) == 1:
        word = 1
        print("its one word")
    else:
        print("its not one word")

stime = time.time() # początek przyjąłem w tym miejscu, co by to jak długo użytkownik wpisywał nie wpływało na wynik końcowy

#### 3. sprowadzenie tekstu do małych liter
lengh = len(text)
newtext = ""
for i in range(0, lengh):
    letter = text[i]
    if 90 >= ord(text[i]) >= 65:
        letter = str(chr(ord(text[i]) + 32))
    newtext = newtext + letter

#### 4. sprawdzenie czy słowo jest w słowniku i wyświetlenie rezultatu
print("small letters: ", newtext)
f = open("SJP.txt", "r", encoding="utf8")
if len(text.split(" ")) == 1:
    dict = f.read()
    tf = dict.find(newtext)
    if tf != -1:
        print("its a correct word")
    else:
        print("its not a correct word")

#### 5. wyświetlenie czasu przetwarzania
etime = time.time()
print(etime - stime)