from PyQt5.QtWidgets import *
import pandas as pd

def load_table(self):
    self.table = pd.read_csv(self.complete_file_path)
    self.table.iloc() 

def populate_table(self):
    load_table(self)

    self.tableWidget.setRowCount(len(self.table.index))
    sum_billing = sum(self.table['Billing'])
    print(str(f'{sum_billing:.2f}'))
    rows_list = [self.table.iloc[row_index].tolist() for row_index in range(len(self.table.index))]

    for row_index, x in enumerate(rows_list):
        for column_index, y in enumerate(x):
            self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(y)))


# Test function
def module_test():
    testing_path = r'C:\Users\USER\Documents\GitHub\billing_prediction\src\services\mock\df.csv'
    testing_df = pd.read_csv(testing_path)
    
    # List comprehension to separate all data into a matrirow_index
    rows = [testing_df.iloc[row_index].to_list() for row_index in range(len(testing_df.index))]
    for row_index, row in enumerate(rows):
        print(f'\nrow_index => {row_index}')
        for column_index, y in enumerate(row):
            print(f'    column_index => {column_index} result => {y}')


if __name__ == '__main__':
    module_test()