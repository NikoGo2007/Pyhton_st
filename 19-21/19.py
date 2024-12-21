f = open('19.txt', 'r')
s, k = input("S: "), []
for i in f:
    if len(i)-1 == 0:
        k += [s + "\n"]
    else:
        k += [i]
f = open('19.txt', 'w')
for i in k:
    f.write(i)
f.close()