# PySide2-template

A simple PySide(2) project which can be used as a template for PySide(2) projects.

## What is this?

This is a template to be used to get a quick start with developing Qt applications in python with PySide 2.
The current feature set is:

* main ui (designed in QtDesigner) which is connected to python
* About page which displays the repositories README.md
* Automatically check for new versions on GitHub
* Settings which are stored to disk
* Script to bundle the application with Pyinstaller

However all of this can easily be extended and/or changed.

## Getting started

Clone or use this repos as a template for your own PySide2 project.
Than install the dependencies with:

``` python
pip install -r requirements.txt
```

Afterwards this template should be initialized with:

* In the `about.py` some variables like: application name, version no. and repo URL need to be set for your application.
* In the `settings.py` you can define your settings which can be saved and loaded with the `IO.save_settings()` and `IO.load_settings`
* In the `.\ui` folder the UI can be modified with the QtDesigner

**Caution:**
For accessing files in the file system the `IO.resource_path()` function should be used.
This function works both with and without PyInstaller.

## Bundling with PyInstaller
