from PyQt5.QtWidgets import *
from src.raw.billing_prediction_screen import *
import sys
#   features imports
from src.features.import_files import import_file
from src.features.toggle_components import disable_components

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)
        
        # Connect functions to buttons
        self.btn_import.clicked.connect(lambda: import_file(self))
        # Disable components
        disable_components(self)
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    qt.exec_()