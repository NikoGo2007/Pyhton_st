import re


def i_22(x):
    pattern = r'\b[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ]\w*'
    return re.findall(pattern, x)


#print(i_22(input("Строка:")))


def text(file):
    f = open(file,"r")
    pattern = r'(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})'
    k = []
    for i in f:
        k.append(re.findall(pattern,i.rstrip()))
    return k

print(text("22.txt"))