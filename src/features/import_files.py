from PyQt5.QtWidgets import *
# Features imports
from src.features.populate_table import populate_table
from src.features.toggle_components import enable_components
# Utils imports
from src.utils.translate_path import translate

def import_file(window):
    # Open file dialog!
	try:
		# The function returns a tuple so let's grab the first index wich is the one we need
		complete_file_path = QFileDialog.getOpenFileName(window, "Open File", r"", "CSV files (*.csv)")[0]
		file_name = translate(complete_file_path)[0]
		file_path = translate(complete_file_path)[1]

		# Update window values
		window.file_name = file_name
		window.file_path = file_path
		window.complete_file_path = complete_file_path

		# Update screen label with file_name
		window.lb_file_description.setText(window.file_name)

		# Update tableWidget
		populate_table(window)

		# Enable components
		window.enable_components()

	except:
			print('Import aborted!')