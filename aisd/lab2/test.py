f = open('zadanie2.csv')
file = f.readlines()
f.close()

a=0
for line in file:
     if str(line.split(',',1)[1]) == '\n':
         print(len(line.split(',',1)[1]))
         a=a+1

print(a)