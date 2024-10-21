# i = [1351,144,132,1,22,33,21,36,2]
#
# i_min = i.index(min(i))
# i_max = i.index(max(i))
# i[min(i_min, i_max)+1:max(i_min,i_max)] = [0]*(max(i_min,i_max)-min(i_min,i_max)-1)
# print(i)
#
#

i =[1,2,3,4,5,6,7,8,9,-1,10,11,12,13,14,15]

k = 5

j = sorted(x for x in i if x < k)
print(j)