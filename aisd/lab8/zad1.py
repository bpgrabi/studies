def way_lengh(town1, town2):
    x1 = float(town1.split("\t")[1])
    y1 = float(town1.split("\t")[2])
    x2 = float(town2.split("\t")[1])
    y2 = float(town2.split("\t")[2])
    return town1.split("\t")[0], town2.split("\t")[0], ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2)


def summary_lengh(town):
    count = 0
    lengh_sum = 0
    for i in range(0, len(town) - 1):
        lengh = way_lengh(town[i], town[i + 1])
        print(i + 1, lengh)
        lengh_sum += lengh[2]
        count += 1
    print(count + 1, way_lengh(town[count], town[0]))
    print(lengh_sum)


file = open("./towns/TSP.txt")
txt = file.read()
town = txt.splitlines()
summary_lengh(town)
