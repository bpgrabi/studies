import time
stime = time.time()
tab = [2]*50
for i in tab:
    print(i, ": ", time.time() - stime)
print("time iter for: ", time.time() - stime)
stime = time.time()
for i in range(0, 50):
    print(i + 1, ": ", time.time() - stime)
print("time c++ for: ", time.time() - stime)
print("pętla iterowana jest szybsza, a wartość 'i' jest zależna od zawartości obiektu"
      "iterowanego, podczas gdy w pętli z ranege i jest 'licznikiem' kroków")
