from PyQt5 import QtWidgets, QtCore
from Login import Ui_Form
import sys
import mysql.connector as ms

sys.path.insert(0, '..')
import Photos.res

class LogApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(LogApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def login(self):
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LogApp()
    Form.show()
    sys.exit(app.exec_())