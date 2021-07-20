import os
import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QTextStream

import qtmodern.styles
import qtmodern.windows

import IO
import about
from main_ui import main_ui
from settings import Settings
from mode import Mode



if __name__ == "__main__":

    # load settings
    IO.create_data_file()
    settings = IO.load_settings()

    app = QApplication(sys.argv)

    #load the ui from file
    window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "main.ui"))) 
    window.setWindowTitle(about.full_id)
    
    # set the theme
    if(settings.mode == Mode.DARK):
        qtmodern.styles.dark(app)
    else:
        qtmodern.styles.light(app)

    # show the ui
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    ui = main_ui(mw, settings)

    sys.exit(app.exec_())
