#default
import os
import tempfile

#PySide
from PySide2.QtWidgets import QPushButton, QMainWindow
from PySide2.QtGui import QIcon, QPixmap, QImage






class main_ui(object):
    """The main-UI of the IP-time-lapse-toll.

    Attributes:
        kanji_preview             (QLabel) : The window which previews the IP camera stream.
    """
    
    pushButton_test_button = None


    def __init__(self, window : QMainWindow):

        self.window = window

        #window.setWindowIcon(QIcon(IO.resource_path("img/icon.ico")))
        
        # init ui
        self.get_ui_elements()
        self.init_ui_elements()
        self.connect_ui()


    def get_ui_elements(self):
        '''
        Set the references to the ui elements read from the .ui file
        '''

        self.pushButton_test_button = self.window.findChild(QPushButton, "pushButton_test_button")


    def init_ui_elements(self):
        
        pass

    def connect_ui(self):
        '''
        Connect the ui-elements with their functions
        '''

        self.pushButton_test_button.pressed.connect(lambda : print("test"))

