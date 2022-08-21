import pandas as pd

def load_table(self):
    self.table = pd.read_csv(self.complete_file_path)

def populate_table(self):
    load_table(self)

    print(self.table)

    # for x, column in enumerate(self.table):
    #     for y, row in enumerate(self.)
    # self.tableWidget.setItem()