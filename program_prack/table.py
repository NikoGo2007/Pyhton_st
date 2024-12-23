class Table:
    def __init__(self, data):
        #Инициализация таблицы с данными.
        self.data = data  # Внутреннее представление таблицы
        self.column_types = {key: str for key in data.keys()}  # По умолчанию все столбцы типа str

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        #Получение строк по номеру.
        if stop is None:
            stop = start + 1
        rows = {key: values[start:stop] for key, values in self.data.items()}
        return Table(rows) if copy_table else rows

    def get_rows_by_index(self, *vals, copy_table=False):
        #Получение строк по значению в первом столбце.
        first_col = list(self.data.keys())[0]
        filtered_data = {key: [] for key in self.data.keys()}

        for index in range(len(self.data[first_col])):
            if self.data[first_col][index] in vals:
                for key in self.data.keys():
                    filtered_data[key].append(self.data[key][index])

        return Table(filtered_data) if copy_table else filtered_data

    def get_column_types(self, by_number=True):
        #Получение типов столбцов.
        if by_number:
            return {i: self.column_types[key] for i, key in enumerate(self.data.keys())}
        return self.column_types

    def set_column_types(self, types_dict, by_number=True):
        #Задание типов столбцов.
        keys = list(self.data.keys())
        if by_number:
            for index, type_value in types_dict.items():
                self.column_types[keys[index]] = type_value
        else:
            for key, type_value in types_dict.items():
                if key in self.column_types:
                    self.column_types[key] = type_value

    def get_values(self, column=0):
        #Получение значений из столбца.
        if isinstance(column, int):
            column_name = list(self.data.keys())[column]
        else:
            column_name = column

        values = self.data[column_name]
        return [self._cast_value(value, self.column_types[column_name]) for value in values]

    def get_value(self, column=0):
        #Получение одного значения из столбца.
        values = self.get_values(column)
        return values[0] if values else None

    def set_values(self, values, column=0):
        #Задание значений для столбца.
        if isinstance(column, int):
            column_name = list(self.data.keys())[column]
        else:
            column_name = column

        for i in range(len(values)):
            self.data[column_name][i] = self._cast_value(values[i], self.column_types[column_name])

    def set_value(self, value, column=0):
        #Задание одного значения для столбца.
        values = [value]
        self.set_values(values, column)

    def print_table(self):
        #Вывод таблицы на печать.
        headers = list(self.data.keys())
        print("\t".join(headers))

        rows_count = len(next(iter(self.data.values())))

        for i in range(rows_count):
            row = [str(self.data[header][i]) for header in headers]
            print("\t".join(row))

