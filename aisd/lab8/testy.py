## algorytm najbliższego sąsiada
def mergesort(A, a, b):
    if a < b:
        c = int((a + b) / 2)
        mergesort(A, a, c)
        mergesort(A, c + 1, b)
        merge(A, a, c, b)


def merge(A, a, c, b):
    n1 = c - a + 1
    n2 = b - c
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[a + i]
    for i in range(0, n2):
        R[i] = A[c + 1 + i]
    i, j, k = 0, 0, a
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


## sorting from the shortest to the longest way
def sort(edges):
    old = edges
    new = []
    for i in range(0, len(old[0])-1):
        for j in range(0, len(old)-1):
            new.append(old[i][j])
    mergesort(new, 0, len(new)-1)
    end = []
    for i in range(0, len(new), 2):
        end.append(new[i])
    return end


def way_lengh(town1, town2):
    x1 = float(town1.split("\t")[1])
    y1 = float(town1.split("\t")[2])
    x2 = float(town2.split("\t")[1])
    y2 = float(town2.split("\t")[2])
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2), town1.split("\t")[0], town2.split("\t")[0]


def summary_lengh(town):
    edges = []
    for i in range(0, len(town)):
        edge = []
        for j in range(0, len(town)):
            if i == j:
                continue
            way = way_lengh(town[j], town[i]) ##lenght calculation for every way
            edge.append(way)
        edges.append(edge)
    newedges = sort(edges)
    #print(newedges)
    tree = [newedges[0][1]]
    lenght = 0
    checking(newedges, tree, newedges[0][1], 100)
    for i in range(0, len(newedges)):
        if (newedges[i][1] == tree[len(tree)-1] and newedges[i][2] == tree[0]) or (newedges[i][2] == tree[len(tree)-1] and newedges[i][1] == tree[0]):
            lenght += newedges[i][0]
            if newedges[i][1] == tree[len(tree) - 1] and newedges[i][2] == tree[0]:
                tree.append(newedges[i][2])
            elif newedges[i][2] == tree[len(tree)-1] and newedges[i][1] == tree[0]:
                tree.append(newedges[i][1])
            break
    print(tree)
    print(len(tree))
    print(conection(tree, newedges))


## MST making
def checking(edges, path, running, max):
    counter = 0
    pit = 0
    if max > 0:
        for i in range(0, len(edges)):
            co = 0
            tool = 0
            if edges[i][1] == running or edges[i][2] == running:
                if edges[i][1] == running:
                    pit = 2
                if edges[i][2] == running:
                    pit = 1
                for j in range(0, len(path)):
                    if path[j] == edges[i][pit]:
                        tool = 1
                        break
                    else:
                        co += 1
                if tool == 0:
                    path.append(edges[i][pit])
                    counter = i
                    print(edges[i][3-pit], " do ", edges[i][pit], " długość: ", edges[i][0])
                    if co > 1:
                        break
        checking(edges, path, edges[counter][pit], max - 1)


def conection(tree, graph):
    lengh = 0
    for i in range(0, len(tree)-2):
        for j in range(0, len(graph)):
            if (graph[j][1] == tree[i] and graph[j][2] == tree[i+1]) or (graph[j][2] == tree[i] and graph[j][1] == tree[i+1]):
                lengh += graph[j][0]
    return lengh



file = open("./towns/TSP.txt")
txt = file.read()
town = txt.splitlines()
summary_lengh(town)
