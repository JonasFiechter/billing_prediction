from PyQt5.QtWidgets import *
from src.raw.billing_prediction_screen import *
import sys

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        super().setupUi(self)

    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    qt.exec_()