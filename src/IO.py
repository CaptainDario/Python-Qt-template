#default
import sys
import os
import tempfile

#PySide2
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice

#custom
import about





def load_ui_file(path : str):
    """
    Loads the main ".ui"-file from the "ui"-folder and returns the QMainWindow from it.
    Also initializes an instance of the "ui"-class.
    Arguments:
        path : the path to the ui file which should be loaded
    Returns:
        QWindow: The loaded Window
    """
    
    ui_file = QFile(path)

    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(path, ui_file.errorString()))
        sys.exit(-1)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    if not window:
        print(loader.errorString())
        sys.exit(-1)


    return window

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def create_data_file():
    """Creates a file to store the UI-data in the temp-dir of the OS.
    
    First checks if a temp-folder already exists.
    If this is not the case a directory will be created with a file in it.
    Otherwise checks if a "data.txt" exists in the directory and creates it
    id necessary.
    """

    tempdir   = tempfile.gettempdir()
    data_dir  = os.path.join(tempdir, about.name)

    #check if the directory does not exists and create it if necessary
    if(not os.path.exists(data_dir)):
        os.makedirs(data_dir)
    
    data_file = os.path.join(data_dir, about.data_file_name)
    
    #check if the directory does not exists and create it if necessary
    if(not os.path.exists(data_file)):
        with open(data_file, "w+"): pass