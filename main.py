from PyQt5 import Qt
from PyQt5 import QtCore, QtWidgets
import design


class Mainform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Mainform()
    si.show()
    app.exec()
