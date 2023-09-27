# 20, 19
S = 39
P = 380

for i in range(0, S):
    for j in range(0, S):
        if (i + j == S) and (i * j == P):
            print(i, j)