with open("./patterns/patterns/8000_pattern.txt") as txt:
    lines = [line for line in txt]

counter = 0
for x in range(len(lines)-2):
    for y in range(len(lines)-2):
        if(lines[x+1][y] == 'B' and lines[x+2][y] == 'C' and
        lines[x][y+2] == 'C' and lines[x][y+1] == 'B' and lines[x][y] == 'A'):
                print(x,y)
                counter += 1

print("Found " + str(counter) + " patterns")