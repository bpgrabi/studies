import numpy as np

with open('./towns/TSP.txt') as txt:
    towns = [line.split() for line in txt]

leng = len(towns)

neighbours = np.array(np.zeros([leng, leng]))
for x in range(leng):
    for y in range(leng):
        neighbours[x][y] = ((float(towns[x][1]) - float(towns[y][1])) ** 2 + (float(towns[x][2]) - float(towns[y][2])) ** 2) ** (1/2)

vertex = 0
edges = []
mst = []
visited = []
minway = [None, None, float('inf')]
while len(mst) != leng - 1:
    visited.append(vertex)
    for i in range(0, leng):
        if (neighbours[vertex][i]):
            edges.append([vertex, i, neighbours[vertex][i]])
    for i in range(0, len(edges)):
        if (edges[i][2] < minway[2] and edges[i][1] not in visited):
            minway = edges[i]
    edges.remove(minway)
    mst.append(minway)
    vertex = minway[1]
    minway = [None, None, float('inf')]

path = [0]
length = 0

for connection in mst:
    path.append(connection[1])
    length += neighbours[path[-2]][connection[1]]

path.append(0)
length += neighbours[int(mst[-1][2])][0]

print(path)
print("length:", length)
