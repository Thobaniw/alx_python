multiTable = [[0]*10 for i in range(10)]
for i in range(1,10):
    for j in range(1,10):
        multiTable[i][j] = i * j
for i in range(1,10):
     for j in range(1,10):
            print(multiTable[i][j], end=",")
print()
#multiplication table