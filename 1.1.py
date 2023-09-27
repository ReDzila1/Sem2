n =[0, 1, 0, 1, 1, 1, 0, 1, 1, 0]
a = 0
b = 0
for i in n:
    if i == 1:
        a += 1;
    else:
        b += 1;

print(min(a, b));
