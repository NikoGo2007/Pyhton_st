def one(file):
    try:
        file = open(file, 'r')
        try:
            content = file.read()
            if not content:
                raise EOFError
            return ("Файл успешно открыт")
        finally:
            file.close()
    except FileNotFoundError:
        return ("Файл не найден")
    except EOFError:
        return "Файл пустой"

# Пример использования
print(one('23_tet.txt'))