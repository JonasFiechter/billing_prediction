from PyQt5.QtWidgets import *
# Features imports
from src.features.populate_table import populate_table
# Compontens imports
from src.components.translate_path import translate

def import_file(self):
        # Open file dialog!
        # The function returns a tuple so let's grab the first index wich is the one we need
        complete_file_path = QFileDialog.getOpenFileName(self, "Open File", r"", "CSV files (*.csv)")[0]
        file_name = translate(complete_file_path)[0]
        file_path = translate(complete_file_path)[1]

        # Update self values
        self.file_name = file_name
        self.file_path = file_path
        self.complete_file_path = complete_file_path

        # Update screen label with file_name
        self.lb_file_description.setText(self.file_name)

        # Update tableWidget
        populate_table(self)