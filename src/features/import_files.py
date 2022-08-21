from PyQt5.QtWidgets import *
# Compontens imports
from src.components.translate_path import translate

def import_file(self):
        # Open file dialog!
        # The function returns a tuple so let's grab the first index wich is the one we need
        file_path = QFileDialog.getOpenFileName(self, "Open File", r"", "CSV files (*.csv)")[0]
        file_name = translate(file_path)[0]

        # Output filename to screen
        self.lb_file_description.setText(file_name)