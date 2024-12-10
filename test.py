import re


def find_consonant_words(input_string):
    # Регулярное выражение для поиска слов, начинающихся на согласную букву
    pattern = r'\b[бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ]\w*'

    # Находим все слова, соответствующие паттерну
    consonant_words = re.findall(pattern, input_string)

    return consonant_words


# Пример использования функции
input_string = "Это пример строки с несколькими словами"
result = find_consonant_words(input_string)
print(result)