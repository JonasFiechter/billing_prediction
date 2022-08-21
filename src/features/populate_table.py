import pandas as pd

def load_table(self):
    self.table = pd.read_csv(self.complete_file_path)
    self.table.iloc()

def populate_table(self):
    load_table(self)

    print(self.table.iloc[1])

    # for x in range(len(self.table.index)):
    #     print(self.table.iloc[x][:][:])
    # self.tableWidget.setItem()

def testing():
    testing_path = r'C:\Users\USER\Documents\GitHub\billing_prediction\src\services\mock\df.csv'
    testing_df = pd.read_csv(testing_path)
    print(testing_df.iloc[1].tolist())


if __name__ == '__main__':
    testing()