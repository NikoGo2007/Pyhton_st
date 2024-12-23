from pickle_p import Pickle
from csv_p import Csv
from table import Table

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": ["30", "25", "35"],
    "Salary": ["1333313", "50000", "80000"]
}

csv = Csv(data, "output.csv", "output.csv", "output.txt")
csv.save_table()
print(csv.load_table())
csv.save_table_as_text()

pickle = Pickle(data, "output.pkl", "output.pkl", "output.txt")
pickle.save_table()
print(pickle.load_table())
pickle.save_table_as_text()

table = Table(csv.load_table())
table.print_table()
