f = open("20.txt", "r")
g = open("20_res.txt", "w")
for i in f:
     if int(i) % 2 == 0:
         g.write(i)