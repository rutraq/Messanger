from PyQt5 import Qt
from PyQt5 import QtCore, QtWidgets
import design
import vk_api
from easygui import msgbox


class Mainform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        try:
            vk_session = vk_api.VkApi(self.textEdit.toPlainText(), self.textEdit_2.toPlainText())
            vk_session.auth()
            vk = vk_session.get_api()
        except:
            msgbox(msg="Введён неверный логин или пароль", title="Login", ok_button="fuck go back")


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Mainform()
    si.show()
    app.exec()
