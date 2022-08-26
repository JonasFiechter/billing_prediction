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

    def disable_components(self):
        self.btn_calculate.setDisabled(True)
        self.line_result.setDisabled(True)
        self.rb_data_segregation.setDisabled(True)
        self.rb_linear_regression.setDisabled(True)
        self.rb_mean.setDisabled(True)
        self.rb_standard_deviation.setDisabled(True)
        self.rb_time_series.setDisabled(True)
        self.rb_weighted_average.setDisabled(True)

    def enable_components(self):
        self.btn_calculate.setDisabled(False)
        self.line_result.setDisabled(False)
        self.rb_data_segregation.setDisabled(False)
        self.rb_linear_regression.setDisabled(False)
        self.rb_mean.setDisabled(False)
        self.rb_standard_deviation.setDisabled(False)
        self.rb_time_series.setDisabled(False)
        self.rb_weighted_average.setDisabled(False)
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    window = MainWindow()
    window.disable_components()
    window.show()
    qt.exec_()
