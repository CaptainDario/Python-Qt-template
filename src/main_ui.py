import os
import webbrowser

from PySide2.QtWidgets import QAction, QLineEdit, QPushButton, QMainWindow, QMessageBox, QTextEdit
from PySide2.QtGui import QIcon

import requests

from settings import Settings
from mode import Mode
import IO
import about



class main_ui(object):
    """The main-UI of the IP-time-lapse-toll.

    Attributes:
        pushButton_test_button (QPus) : The window which previews the IP camera stream.
    """
    
    # settings menu
    action_light = None
    action_dark  = None
    action_about = None

    #extra windows
    about_window = None

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

        # check if updates are available
        self.check_for_updates()


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

        self.action_light.triggered.connect(lambda : self.set_mode(Mode.LIGHT))
        self.action_dark.triggered.connect(lambda : self.set_mode(Mode.DARK))
        self.action_about.triggered.connect(self.show_about_window)

        self.pushButton_test_button.pressed.connect(lambda : print("test"))

    def set_mode(self, mode : Mode):
        """ Sets the theme of the ui and saves it to file.

        Args;
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
                release = r.json()["tag_name"][1:]

                if(release > about.version + about.release_suffix):
                    print("there is a new version available on GitHub")

                    msgb = QMessageBox(QMessageBox.Information,
                        "New Version Available!",
                        "There is a new version of " + about.name + " available at GitHub!",
                        buttons=QMessageBox.Open | QMessageBox.Close
                    )
                    #msgb.setWindowIcon(QIcon(IO.resource_path("img/icon.ico")))
                    result = msgb.exec()

                    if (result == QMessageBox.Open):
                        webbrowser.open_new_tab(about.latest_release_url)

        except:
            print("Could not connect to GitHub at:", about.latest_release_api)

    def show_about_window(self):
        """ Open the about window which shows the repos README.md.
        """

        #load the ui from file
        self.about_window = IO.load_ui_file(IO.resource_path(os.path.join("ui", "about.ui"))) 
        self.about_window.setWindowTitle(about.full_id)
        
        path = IO.resource_path(os.path.join(os.getcwd(), "README.md"))
        with open(path, mode="r") as f:
            self.about_window.findChild(QTextEdit, "textEdit_about").setMarkdown(f.read())
        self.about_window.show()
        


