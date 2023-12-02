import os
import sys

from qtpy.QtWidgets import QApplication
from qtpy.QtCore import QFile, QTextStream

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
    
    # set the theme
    if(settings.mode == Mode.DARK):
        qtmodern.styles.dark(app)
    else:
        qtmodern.styles.light(app)

    # show the ui
    ui = main_ui(settings)
    ui.show()

    sys.exit(app.exec_())
