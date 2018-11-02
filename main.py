from PyQt5 import Qt, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
import design
import mainform
from easygui import msgbox


class Loginform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.mainform = Mainform()

    def login(self):
        try:
            # vk_session = vk_api.VkApi(self.textEdit.toPlainText(), self.lineEdit.text())
            # vk_session.auth()
            # vk = vk_session.get_api()
            self.mainform.show()
            self.hide()
        except:
            msgbox(msg="Введён неверный логин или пароль", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')


class Mainform(QtWidgets.QMainWindow, mainform.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Main')
        pixmap = QPixmap('photos/1.png')
        self.label.setPixmap(pixmap)
        Icon: QIcon = QtGui.QIcon("photos/2.png")
        self.pushButton_2.setIcon(Icon)


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
