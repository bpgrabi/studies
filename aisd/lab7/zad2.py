def horizontal(size, pattern, d, q):
    file = open("./patterns/patterns/" + str(size) + "_pattern.txt", "r")
    txt = file.read().splitlines()
    n = len(txt)
    m = len(pattern)
    h = d ** (m-1) % q
    result = set()
    for y in range(0, n-2):
        p = 0
        t = 0
        for i in range(0, m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(txt[y][i])) % q

        for x in range(0, n-m+1):
            if p == t:
                count = 0
                for i in range(0, m):
                    if (txt[y][x + i] != pattern[i]):
                        count = 1
                        break
                if count == 0:
                    result.add((y, x))
            if x < n - m:
                t = ((t - h*ord(txt[y][x]))*d + ord(txt[y][x+m])) % q
    return result


def vertical(size, pattern, d, q, result):
    file = open("./patterns/patterns/" + str(size) + "_pattern.txt", "r")
    txt = file.read().splitlines()
    n = len(txt)
    m = len(pattern)
    h = d ** (m-1) % q
    final_result = set()
    for x in range(0, n - 2):
        p = 0
        t = 0
        for i in range(0, m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(txt[i][x])) % q

        for y in range(0, n-m+1):
            if p == t:
                found = True
                for i in range(m):
                    if (txt[y+i][x] != pattern[i]):
                        found = False
                        break
                if found and (y, x) in result:
                    final_result.add((y, x))
            if y < n - m:
                t = (d*(t - h*ord(txt[y][x])) + ord(txt[y+m][x])) % q
    return final_result


def rabin(size, parr, number, mod):
    horizont = horizontal(size, parr, number,  mod )
    hits = vertical(size, parr, number,  mod, horizont)
    #print("number of patterns:", str(len(hits)))
    #print(hits)
    return hits


if __name__ == "__main__":
    tab = ["A", "B", "C"]
    bol = 0
    results = None
    while bol == 0:
        #try:
            size = int(input("write witch txt u want check (1000, 2000, 3000, 4000, 5000, or 8000) "))
            results = rabin(size, tab, 16, 6353)
            bol = 1
        #except:
            print("wrong number")
    print("number of patterns:", str(len(results)))
    print(results)
