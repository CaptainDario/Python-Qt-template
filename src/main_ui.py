import os
import webbrowser

from qtpy.QtWidgets import QAction, QLabel, QPushButton, QMainWindow, QMessageBox, \
                            QTextEdit, QWidget, QStatusBar
from qtpy import uic

import requests
import qtmodern

from settings import Settings
from mode import Mode
import IO
import about



class main_ui(QMainWindow):
    """The main-UI of the application.

    Attributes:
        action_light   (QAction) : menubar element to select light mode
        action_dark    (QAction) : menubar element to select dark mode
        action_help    (QAction) : menubar element to open the help window
        action_about   (QAction) : menubar element to open the about window
    """
    
    def __init__(self, settings : Settings):

        QMainWindow.__init__(self)
        uic.loadUi(os.path.join("ui", "main.ui"), self)

        self.settings = settings
        
        # init ui
        self.get_ui_elements()
        self.init_ui_elements()
        self.connect_ui()

        # check if updates are available
        self.check_for_updates()


    def get_ui_elements(self):
        '''
        Set the references to the ui elements read from the .ui file
        '''

        # settings menu
        self.action_light = self.findChild(QAction, "action_light")
        self.action_dark  = self.findChild(QAction, "action_dark")
        self.action_about = self.findChild(QAction, "action_about")
        self.action_help  = self.findChild(QAction, "action_help")

        self.pushButton_test_button = self.findChild(QPushButton, "pushButton_test_button")

    def init_ui_elements(self):
        """ Initializes all ui-elements.
        """

    def connect_ui(self):
        '''
        Connect the ui-elements with their functions
        '''

        self.action_light.triggered.connect(lambda : self.set_mode(Mode.LIGHT))
        self.action_dark.triggered.connect(lambda : self.set_mode(Mode.DARK))
        self.action_about.triggered.connect(self.show_about_window)
        self.action_help.triggered.connect(self.show_help_window)

        self.pushButton_test_button.pressed.connect(lambda : print("test"))

    def set_mode(self, mode : Mode):
        """ Sets the theme of the ui and saves it to file.

        Args:
            mode : the new mode
        """
        
        self.settings.mode = mode
        IO.save_settings(self.settings)

    def check_for_updates(self):
        """ Tries to connect to GitHub and check if a new version of the software is available.

        Shows a popup window to the user if there is a newer version available at GitHub.
        This popup allows the user also to directly go to the new release.
        """

        try:
            r = requests.get(about.latest_release_api)

            if(r.status_code == 200):
                release = r.json()["tag_name"]
                if(release[0] == "v"):
                    release = release[1:]

                if(release > about.version + about.release_suffix):
                    print("there is a new version available on GitHub")

                    #load the ui from file
                    self.update_window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "update.ui")))
                    self.update_window.setWindowTitle(about.name + ": New Version Available!")
                    self.update_window.findChild(QLabel, "label_update").setText(
                        "There is a new version of " + about.name + " available at GitHub!"
                    )
                    self.update_window = qtmodern.windows.ModernWindow(self.update_window)
                    self.update_window.show()

        except:
            print("Could not connect to GitHub at:", about.latest_release_api)
    
    def show_help_window(self):
        """ Open the about window which shows the repos README.md.
        """

        #load the ui from file
        help_window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "help.ui")))
        help_window = qtmodern.windows.ModernWindow(help_window)
        help_window.setWindowTitle(about.full_id)
        
        path = IO.resource_path(os.path.join(os.getcwd(), "README.md"))
        with open(path, mode="r") as f:
            text = f.read()
        
        help_window.findChild(QTextEdit, "textEdit_help").setMarkdown(text)
        help_window.show()
    
    def show_about_window(self):
        """ Open the about window which shows the repos README.md.
        """

        #load the ui from file
        about_window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "about.ui")))
        about_window = qtmodern.windows.ModernWindow(about_window)
        about_window.setWindowTitle(about.full_id)
        
        about_window.findChild(QTextEdit, "textEdit_about").setMarkdown(about.toString())
        about_window.show()
        


