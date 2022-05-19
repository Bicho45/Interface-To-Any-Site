from PyQt5 import QtWidgets, QtCore
from Register import Ui_Form
import sys

sys.path.insert(0, '..')
import Photos.res

class regApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(regApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = regApp()
    Form.show()
    sys.exit(app.exec_())