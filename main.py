from PyQt5 import Qt, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5.QtGui import QPixmap, QIcon
import design
import mainform
from easygui import msgbox
import vk_api
import psycopg2
import requests
import os
from time import sleep

list_friends = []
domains = []
messages = []


class Loginform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.setWindowTitle("Povistochka")
        self.setWindowIcon(QIcon("photos/logo.png"))
        self.lineEdit.returnPressed.connect(self.login)

    def login(self):
        global vk
        try:
            if (int(self.textEdit.toPlainText().__len__()) == 0) or (int(self.lineEdit.text().__len__()) == 0):
                msgbox(msg="Введите данные", title="Login", ok_button="fuck go back")
            else:
                vk_session = vk_api.VkApi(self.textEdit.toPlainText(), self.lineEdit.text())
                vk_session.auth()
                vk = vk_session.get_api()

                self.mainform = Mainform()
                self.mainform.show()
                self.hide()
                # if self.checkBox.isChecked():
                #     f = open("sign.txt", "w")
                #     f.write(self.textEdit.toPlainText() + "\n" + self.lineEdit.text().__len__())
                #     f.close()
                # else:
                #     os.remove("vk_config.v2.json")
                #     os.remove("sign.txt")
        except vk_api.exceptions.BadPassword:
            msgbox(msg="Введён неверный логин или пароль", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')
        except requests.exceptions.ConnectionError:
            msgbox(msg="Отсутствует интернет соединение", title="Login", ok_button="fuck go back")
            self.lineEdit.setText('')


class Mainform(QtWidgets.QMainWindow, mainform.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Povistochka')
        self.pushButton.clicked.connect(self.send)
        self.setWindowIcon(QIcon('photos/logo.png'))
        self.lineEdit.returnPressed.connect(self.key_press)
        self.load()

    def load(self):

        info = vk.account.getProfileInfo()
        name = info['first_name']
        surname = info['last_name']
        domain = info['screen_name']

        conn = psycopg2.connect(
            "dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM users")
        row = cur.fetchone()
        print(row)
        for entry in cur:
            print(entry)
        res = cur.execute("SELECT * FROM users WHERE DOMAIN = '" + domain + "' ")
        row = cur.fetchone()
        if not row:
            res = cur.execute("INSERT INTO users(domain, name, surname) VALUES (%s,%s,%s)",
                              (domain, name, surname))  # Добавление информации
            conn.commit()

        res = cur.execute("SELECT name, surname FROM users")
        row = cur.fetchone()
        self.check = QRadioButton(str(row))
        self.verticalLayout.addWidget(self.check)

        for entry in cur:
            self.check = QRadioButton(str(entry))
            self.verticalLayout.addWidget(self.check)

        # friends = vk.friends.get(fields='domain', count=20)
        # i = 0
        # while i < len(friends["items"]):
        #     self.check = QRadioButton(friends['items'][i]['first_name'] + ' ' + friends['items'][i]['last_name'])
        #     list_friends.append(self.check)
        #     domains.append(friends['items'][i]['domain'])
        #     self.verticalLayout.addWidget(self.check)
        #     i += 1

    def send(self):
        i = 0
        choose_friends = 0
        text = ''
        for check in list_friends:
            if check.isChecked():
                choose_friends = 1
                if self.lineEdit.text() != '':
                    vk.messages.send(message=self.lineEdit.text(), domain=domains[i])
                    messages.append(self.lineEdit.text())
                    self.lineEdit.setText('')
                    for mess in messages:
                        text += mess + "\n"
                    self.plainTextEdit.setPlainText(text)
                else:
                    msgbox(msg="Enter a message", title="ERROR")
            i += 1
        if choose_friends == 0:
            msgbox(msg="Choose a friend", title="ERROR")

    def key_press(self):
        i = 0
        choose_friends = 0
        text = ''
        for check in list_friends:
            if check.isChecked():
                choose_friends = 1
                if self.lineEdit.text() != '':
                    vk.messages.send(message=self.lineEdit.text(), domain=domains[i])
                    messages.append(self.lineEdit.text())
                    self.lineEdit.setText('')
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
