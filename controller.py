from PyQt5.QtWidgets import *
from TV_Window import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.setupUi(self)
