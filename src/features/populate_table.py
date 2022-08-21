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
    
    # List comprehension to separate all data into a matrix
    rows = [testing_df.iloc[x].to_list() for x in range(len(testing_df.index))]
    for x, row in enumerate(rows):
        print(f'\nx => {x}')
        for y, column in enumerate(row):
            print(f'    y => {y} result => {column}')


if __name__ == '__main__':
    testing()