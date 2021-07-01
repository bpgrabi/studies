string = ""
for i in range(500, 3001):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        string = string + str(i)
print(string)
count = string.count("21")
print("21 występuje: ", count, " razy")
if "21" in string:
    string = string.replace("21", "XX")
print(string)
