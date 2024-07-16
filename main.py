# Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

from PyQt5.QtWidgets import QWidget

def main():
    pass
if __name__ == '__main__':
    main()


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()    
        
        #Load and show the UI
        uic.loadUi("exFile.ui", self)
        self.show()

#Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()
