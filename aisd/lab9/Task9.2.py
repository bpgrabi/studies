# BRKGA knapsack

import random
import numpy as np
import multiprocessing
size = '20'


def check_fit(x, y, knapsack):
    for x_start in range(len(knapsack)-x+1):
        for y_start in range(len(knapsack)-y+1):
            fits = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if knapsack[x_start+x_iter][y_start+y_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return (x_start,y_start,False)

    # other orientation

    for x_start in range(len(knapsack)-x+1):
        for y_start in range(len(knapsack)-y+1):
            fits = True
            for x_iter in range(x):
                for y_iter in range(y):
                    if knapsack[y_start+y_iter][x_start+x_iter]:
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                return (x_start,y_start,True)

    return False


def eval(gene):
    if isinstance(gene[-1], int):
        return 0
    knapsack = np.zeros((int(size), int(size)), dtype=int)
    value = 0
    for item in gene:
        fit = check_fit(item[1], item[2], knapsack)
        if fit:
            if(fit[2]):
                for x in range(fit[0],item[1] + fit[0]):
                    for y in range(fit[1],item[2] + fit[1]):
                        knapsack[y][x] = 1
            else:
                for x in range(fit[0], item[1] + fit[0]):
                    for y in range(fit[1], item[2] + fit[1]):
                        knapsack[x][y] = 1
            value += item[3]
    
    return value


if __name__ == "__main__":
    with open('packages'+ size +'.txt') as txt:
        items = [line.split(",") for line in txt]
    
    # remove header
    del(items[0])
    del(items[0])
    
    # remove endlines
    for item in items:
        item[-1] = item[-1].strip()
    
    # convert to integers
    items = [[int(j) for j in i] for i in items]

    # constants
    p = 100 # population size
    pc = 0.2 # elite percentage
    pm = 0.01 # mutations
    ps = 0.05 # mutation severity

    population = []
    try:
        counter = 0
        while True:
            counter += 1
            # generate random population
            for i in range(p-len(population)):
                population.append(random.sample(items,k=len(items)))

            # multicore eval
            pool = multiprocessing.Pool()
            result = pool.map(eval, population)

            for i in range(len(population)):
                if not isinstance(population[i][-1], int):
                    population[i].append(result[i])
            
            # uncomment to get single core eval
            # # eval genes
            # for gene in population:
            #     if not isinstance(gene[-1], int):
            #         gene.append(eval(gene))

            # sort according to perceived value
            population.sort(key=lambda g: -g[-1])
            print (counter, population[0][-1])

            # breed
            for i in range(round(p - 2 * pc * p)):
                b = random.randint(0, pc * p - 1)
                c = random.randint(pc * p, p - 2)
                bc = []
                iter_b = 0
                iter_c = 0
                for j in range(len(items)):
                    # randomize gene mixing
                    mixer = random.randint(0,1)
                    if mixer:
                        while population[b][iter_b] in bc:
                            iter_b += 1

                        if iter_b <= len(items):
                            bc.append(population[b][iter_b].copy())
                        else:
                            bc.append(population[c][iter_c].copy())
                        
                    else:
                        while population[c][iter_c] in bc:
                            iter_c += 1

                        if iter_c <= len(items):
                            bc.append(population[c][iter_c].copy())
                        else:
                            bc.append(population[b][iter_b].copy())

                population.append(bc)
                # population[-1].append(eval(population[-1]))
                
            del population[round(pc * p):p]

            # mutate
            for i in range(round(pm * len(population))):
                # pick entity to mutate
                m = random.randint(0, len(population) - 1)
                for j in range(round(ps * len(items))):
                    # pick two genes to swap
                    m1 = random.randint(0, len(items) - 1)
                    m2 = random.randint(0, len(items) - 1)
                    
                    temp = population[m][m1].copy()
                    population[m][m1] = population[m][m2].copy()
                    population[m][m2] = temp
                    if isinstance(population[m][-1], int):
                        del population[m][-1]
                    # eval new genome
                    # population[m].append(eval(population[m]))
            
    except KeyboardInterrupt:
        print(population[0])
        print(len(population[0]))
        print(len(population))
