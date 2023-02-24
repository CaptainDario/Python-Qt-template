# PySide2-template

A simple PySide(2) project which can be used as a template for PySide(2) projects.

## What is this?

This is a template to be used to have a quick start with developing Qt applications in python with any qt binding (pyside 2/5/6 pyqt).
The current feature set is:

* `.ui`-files (designed in QtDesigner) which are connected to python
* About page which displays the repositories README.md
* Automatically check for new versions on GitHub
* Settings which are saved to disk and loaded on start up
* Script to bundle the application with PyInstaller

and all of this can easily be extended.

## Getting started

Clone or use this repos as a template for your own qt project.
Afterwards, install the dependencies with:

``` python
pip install -r requirements.txt
```

Additionally, you need to install a qt-python binding, for example PySide6.

Now this template can be cnofigured:

* In the `about.py` some variables like: application name, version no. and repo URL need to be set for your application.
* In the `settings.py` you can define your settings which can be saved and loaded with the `IO.save_settings()` and `IO.load_settings`
* In the `.\ui` folder the UI can be modified with QtDesigner

**Caution:**
For accessing files in the file system the `IO.resource_path()` function should be used to generate the paths.
This function works both with and without PyInstaller.

## Bundling with PyInstaller

To build an executable (MacOS, Linux and Windows are supported) run:

``` bash
python build_with_pyinstaller.py
```

this script assumes that in a folder `pyside2-template/.venv` a python virtual environment exists. Then a executable will be build and stored in a folder called `build`.
