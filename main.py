from PyQt5 import Qt, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5.QtGui import QPixmap, QIcon
import design
import mainform
from easygui import msgbox
import vk_api
import psycopg2

list_friends = []
domains = []
messages = []


class Loginform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.mainform = Mainform()
        self.setWindowTitle("Povistochka")
        self.setWindowIcon(QIcon("photos/logo.png"))

    def login(self):
        global vk
        try:
            if (int(self.textEdit.toPlainText().__len__()) == 0) or (int(self.lineEdit.text().__len__()) == 0):
                msgbox(msg="Введите данные", title="Login", ok_button="fuck go back")
            else:
                vk_session = vk_api.VkApi(self.textEdit.toPlainText(), self.lineEdit.text())
                vk_session.auth()
                vk = vk_session.get_api()

                info = vk.account.getProfileInfo()
                name = info['first_name']
                surname = info['last_name']
                domain = info['screen_name']

                conn = psycopg2.connect(
                    "dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
                cur = conn.cursor()
                res = cur.execute("SELECT * FROM users")
                row = cur.fetchone()
                res = cur.execute("SELECT * FROM users WHERE DOMAIN = '"+domain+"' ")
                row = cur.fetchone()
                if not row:
                    res = cur.execute("INSERT INTO users(domain, name, surname) VALUES (%s,%s,%s)",
                                      (domain, name, surname))  # Добавление информации

                self.mainform.show()
                self.hide()
        except:
            msgbox(msg="Введён неверный логин или пароль", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')


class Mainform(QtWidgets.QMainWindow, mainform.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Povistochka')
        Icon: QIcon = QtGui.QIcon("photos/2.png")
        self.pushButton_2.setIcon(Icon)
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.clicked.connect(self.load)
        self.setWindowIcon(QIcon('photos/logo.png'))

    def load(self):
        friends = vk.friends.get(fields='domain', count=20)
        i = 0
        while i < len(friends["items"]):
            self.check = QRadioButton(friends['items'][i]['first_name'] + ' ' + friends['items'][i]['last_name'])
            list_friends.append(self.check)
            domains.append(friends['items'][i]['domain'])
            self.verticalLayout.addWidget(self.check)
            i += 1

    def send(self):
        i = 0
        choose_friends = 0
        text = ''
        for check in list_friends:
            if check.isChecked():
                choose_friends = 1
                if self.textEdit.toPlainText() != '':
                    vk.messages.send(message=self.textEdit.toPlainText(), domain=domains[i])
                    messages.append(self.textEdit.toPlainText())
                    self.textEdit.setText('')
                    for mess in messages:
                        text += mess + "\n"
                    self.plainTextEdit.setPlainText(text)
                else:
                    msgbox(msg="Enter a message", title="ERROR")
            i += 1
        if choose_friends == 0:
            msgbox(msg="Choose a friend", title="ERROR")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Enter:
            i = 0
            choose_friends = 0
            text = ''
            for check in list_friends:
                if check.isChecked():
                    choose_friends = 1
                    if self.textEdit.toPlainText() != '':
                        vk.messages.send(message=self.textEdit.toPlainText(), domain=domains[i])
                        messages.append(self.textEdit.toPlainText())
                        self.textEdit.setText('')
                        for mess in messages:
                            text += mess + "\n"
                        self.plainTextEdit.setPlainText(text)
                    else:
                        msgbox(msg="Enter a message", title="ERROR")
                i += 1
            if choose_friends == 0:
                msgbox(msg="Choose a friend", title="ERROR")


if __name__ == '__main__':
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
