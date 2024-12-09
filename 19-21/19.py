one = open('19.txt', 'r')
res = open("19_res.txt", 'w')
s = "rrrrreeeeeeeeaaaaaaaaaaddddddd"
for i in one:
    if len(i)-1 == 0:
        res.write(s + '\n')
    else:
        res.write(i)