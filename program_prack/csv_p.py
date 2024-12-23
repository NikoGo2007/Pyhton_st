import csv


class Csv:
    def __init__(self, table, file_path_r,file_path_w, file_path_w_txt):
        self.table = table
        self.file_path_r = file_path_r
        self.file_path_w = file_path_w
        self.file_path_w_txt = file_path_w_txt

    def load_table(self):
        try:
            table = {}
            with open(self.file_path_r, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for header in headers:
                    table[header] = []
                for row in reader:
                    for header, value in zip(headers, row):
                        table[header].append(value)
            return table
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_path_r} не найден.")
        except Exception:
            raise Exception(f"Ошибка при загрузке таблицы")

    def save_table(self):
        with open(self.file_path_w, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.table.keys())
            rows = zip(*self.table.values())
            writer.writerows(rows)

    def save_table_as_text(self):
        with open(self.file_path_w_txt, 'w') as file:
            headers = self.table.keys()
            file.write('\t'.join(headers) + '\n')
            rows = zip(*self.table.values())
            for row in rows:
                file.write('\t'.join(row) + '\n')


