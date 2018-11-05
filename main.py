from PyQt5 import Qt, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QIcon
import design
import mainform
from easygui import msgbox
import vk_api


class Loginform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.mainform = Mainform()

    def login(self):
        global vk
        try:
            if (int(self.textEdit.toPlainText().__len__()) == 0) or (int(self.lineEdit.text().__len__()) == 0):
                msgbox(msg="Введите данные", title="Login", ok_button="fuck go back")
            else:
                vk_session = vk_api.VkApi(self.textEdit.toPlainText(), self.lineEdit.text())
                vk_session.auth()
                vk = vk_session.get_api()
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
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.clicked.connect(self.load)

    def load(self):
        list_friends = []
        friends = vk.friends.get(fields='domain', count=20)
        # i = 0
        # while i < len(friends["items"]):
        #     self.button = QPushButton(friends['items'][i]['first_name'] + ' ' + friends['items'][i]['last_name'])
        #     self.button.clicked.connect(lambda: self.button.setEnabled(False))
        #     list_friends.append(self.button)
        #     self.verticalLayout.addWidget(self.button)
        #     i += 1

    def send(self):
        if self.textEdit.toPlainText() != '':
            vk.messages.send(message=self.textEdit.toPlainText(), domain='genek_orlov')
            self.textEdit.setText('')


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
