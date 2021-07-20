#default
import os
import tempfile

#PySide
from PySide2.QtWidgets import QAction, QPushButton, QMainWindow

from settings import Settings
from mode import Mode
import IO



class main_ui(object):
    """The main-UI of the IP-time-lapse-toll.

    Attributes:
        pushButton_test_button (QPus) : The window which previews the IP camera stream.
    """
    
    # settings menu
    action_light = None
    action_dark  = None
    action_about = None

    # main ui elements
    pushButton_test_button = None


    def __init__(self, window : QMainWindow, settings : Settings):

        self.window   = window
        self.settings = settings

        #window.setWindowIcon(QIcon(IO.resource_path("img/icon.ico")))
        
        # init ui
        self.get_ui_elements()
        self.init_ui_elements()
        self.connect_ui()


    def get_ui_elements(self):
        '''
        Set the references to the ui elements read from the .ui file
        '''

        # settings menu
        self.action_light = self.window.findChild(QAction, "action_light")
        self.action_dark  = self.window.findChild(QAction, "action_dark")
        self.action_about = self.window.findChild(QAction, "action_about")

        self.pushButton_test_button = self.window.findChild(QPushButton, "pushButton_test_button")


    def init_ui_elements(self):
        """ Initializes all ui-elements.
        """
        
        pass

    def connect_ui(self):
        '''
        Connect the ui-elements with their functions
        '''

        self.pushButton_test_button.pressed.connect(lambda : print("test"))

        self.action_light.triggered.connect(lambda : self.set_mode(Mode.LIGHT))
        self.action_dark.triggered.connect(lambda : self.set_mode(Mode.DARK))


    def set_mode(self, mode : Mode):
        
        self.settings.mode = mode
        IO.save_settings(self.settings)

    def show_about(self):
        pass

    def check_for_update():
	    pass

    def show_about_windows():
        pass

