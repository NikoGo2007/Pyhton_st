import re


def i_22(x):
    pattern = r'\b[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ]\w*'
    return re.findall(pattern, x)


#print(i_22(input("Строка:")))


def text(file):
    f = open(file,"r")
    pattern = r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})'
    k,m = "",[]
    for i in f:
        for j in re.findall(pattern,i.rstrip()):
            for l in j:
                if len(k) != 12:
                    k += l
                    print(k)
                if len(k) == 12:
                    m += [k]
                    k = ""

    return m

print(text("22.txt"))