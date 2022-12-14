from PyQt5.QtWidgets import *
from src.raw.billing_prediction_screen import *
import sys
#   features imports
from src.features.import_files import import_file
from src.features.toggle_components import disable_components
from src.features.predictions import check_prediction

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        
        # Connect functions to buttons
        self.btn_import.clicked.connect(lambda: import_file(self))
        self.btn_calculate.clicked.connect(lambda: check_prediction(self))
        
        # Disable components
        disable_components(window=self)
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.disable_components()
    window.show()
    qt.exec_()
