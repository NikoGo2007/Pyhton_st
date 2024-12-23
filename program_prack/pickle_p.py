import pickle


class Pickle:
    def __init__(self, table, file_path_r, file_path_w,file_path_w_txt):
        self.table = table
        self.file_path_r = file_path_r
        self.file_path_w = file_path_w
        self.file_path_w_txt = file_path_w_txt

    def load_table(self):
        try:
            with open(self.file_path_r, 'rb') as file:
                table = pickle.load(file)
            return table
        except FileNotFoundError:
            raise Exception(f"Файл {self.file_path_r} не найден")
        except Exception:
            raise Exception(f"Ошибка при загрузке таблицы")

    def save_table(self):
        with open(self.file_path_w, 'wb') as file:
            pickle.dump(self.table, file)

    def save_table_as_text(self):
        with open(self.file_path_w_txt, 'w') as file:
            headers = self.table.keys()
            file.write('\t'.join(headers) + '\n')
            rows = zip(*self.table.values())
            for row in rows:
                file.write('\t'.join(row) + '\n')


