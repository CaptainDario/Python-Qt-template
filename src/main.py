import os
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QTextStream

import qtmodern.styles
import qtmodern.windows

import IO
import about
from main_ui import main_ui



if __name__ == "__main__":

	IO.create_data_file()

	app = QApplication(sys.argv)

	#load the ui from file
	window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "main.ui"))) 
	window.setWindowTitle(about.full_id)
	
	qtmodern.styles.dark(app)
	mw = qtmodern.windows.ModernWindow(window)
	mw.show()
	ui = main_ui(mw)

	sys.exit(app.exec_())