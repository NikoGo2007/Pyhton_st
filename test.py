# f = [open('numbers_in_words.txt', 'r').read()]
# print(f)
from num2words import num2words

with open("numbers_in_words.txt", "w", encoding="utf-8") as f:
    for num in range(0, 10001):
        num_words = num2words(num, lang='ru')
        f.write(f"{num_words}\n")