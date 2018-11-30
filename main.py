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
import rsa
from threading import Thread
from PyQt5.QtCore import QThread, pyqtSignal
import pickle

list_friends_buttons = []
list_friends_surnames = []
list_domain = []
domains = []
messages = []


def login_with_sql():
    global conn, cur
    try:
        conn = psycopg2.connect(
            "dbname='dbkwmnvo' user='dbkwmnvo' host='stampy.db.elephantsql.com' password='Svlw7QnOgENeOI6XnC2obr5GY8ojNINR'")
        cur = conn.cursor()
    except psycopg2.OperationalError:
        msgbox(msg="Отсутствует интернет соединение", title="Login", ok_button="fuck go back")


class MyThread(QThread):
    progress = pyqtSignal(str)  # сигнал который мы будем передавать прогрессбару

    def __init__(self, k):
        super().__init__()
        self.k = k

    def run(self):
        info_for_messages = vk.messages.getLongPollServer(need_pts=1)
        while True:
            updates = vk.messages.getLongPollHistory(ts=info_for_messages['ts'], pts=info_for_messages['pts'],
                                                     fields='domain')
            if len(updates['messages']['items']) > 0:
                for msg in range(len(updates['messages']['items'])):
                    domain_vk = updates['profiles'][0]['domain']
                    for domain in list_domain:
                        if domain == domain_vk:
                            # vk.messages.markAsRead(peer_id=updates['messages']['items'][msg]['peer_id'])
                            if len(updates['profiles']) == 1:
                                print(updates['profiles'][0]['first_name'] + " " + updates['profiles'][0][
                                    'last_name'] + ":")
                                messages.append(updates['profiles'][0]['first_name'] + " " + updates['profiles'][0][
                                    'last_name'] + ":")
                                ex = updates['messages']['items'][msg]['text']
                                self.progress.emit(ex)
                            elif len(updates['profiles']) == 2:
                                print(updates['profiles'][1]['first_name'] + " " + updates['profiles'][1][
                                    'last_name'] + ":")
                                print(updates['messages']['items'][msg]['text'])
                info_for_messages = vk.messages.getLongPollServer(need_pts=1)


class Loginform(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)
        self.setWindowTitle("Povistochka")
        self.setWindowIcon(QIcon("photos/logo.png"))
        self.lineEdit.returnPressed.connect(self.login)
        self.load_form()

    def load_form(self):
        if os.path.isfile("sign.txt"):
            f = open("sign.txt")
            telephone = f.read()
            f.close()
            self.textEdit.setText(telephone)
            self.lineEdit.setText("11111111111")
            self.checkBox.setChecked(True)

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
                if self.checkBox.isChecked():
                    f = open("sign.txt", "w")
                    f.write(str(self.textEdit.toPlainText()))
                    f.close()
                else:
                    os.remove("vk_config.v2.json")
                    if os.path.isfile("sign.txt"):
                        os.remove("sign.txt")
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
        self.pushButton_2.clicked.connect(self.click)
        self.pushButton_3.clicked.connect(self.hide_button)
        self.setWindowIcon(QIcon('photos/logo.png'))
        self.lineEdit.returnPressed.connect(self.send)
        self.load()
        self.design()

    def click(self):
        info = vk.account.getProfileInfo()
        name = info['first_name']
        surname = info['last_name']
        self.listView_2.move(0, 0)
        self.label.move(0, 100)
        self.label_2.move(100, 20)
        self.label.setText(name + ' ' + surname)
        for btn in list_friends_buttons:
            btn.hide()
        self.pushButton_3.move(260, 0)
        self.listView.move(0, 170)
        self.label_3.move(10, 760)
        self.label_7.move(10, 810)
        self.label_4.move(30, 200)
        self.label_5.move(80, 200)

    def design(self):
        self.pushButton_2.setStyleSheet(
            'border-style: solid; border-width: 1px; border-color: black; '
            'background-image: url(:/newPrefix/photos/menu.png);')

    def hide_button(self):
        self.listView_2.move(- 265, 0)
        self.label.move(- 500, 0)
        self.label_2.move(-500, 0)
        self.pushButton_3.move(-1000, 0)
        self.listView.move(-265, 170)
        self.label_3.move(-300, 760)
        self.label_7.move(-300, 810)
        for btn in list_friends_buttons:
            btn.show()
        self.label_4.move(-500, 200)
        self.label_5.move(-500, 200)

    def load(self):
        info = vk.account.getProfileInfo()
        name = info['first_name']
        surname = info['last_name']
        domain = info['screen_name']

        cur.execute("SELECT * FROM users WHERE DOMAIN = '" + domain + "' ")
        row = cur.fetchone()

        if not row:
            cur.execute("INSERT INTO users(domain, name, surname) VALUES (%s,%s,%s)",
                        (domain, name, surname))  # Добавление информации
            conn.commit()

        cur.execute("SELECT * FROM users WHERE DOMAIN != '" + domain + "' ")
        row = cur.fetchone()
        name_button = str(row[2])
        surname_button = str(row[3])
        check = QRadioButton(name_button + ' ' + surname_button, self)
        list_friends_surnames.append(name_button + ' ' + surname_button)
        check.resize(260, 20)
        check.move(10, 70)
        check.clicked.connect(self.choosen_dialog)
        check.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        check.setStyleSheet('QRadioButton {background-color: #17212b; color: white;}')
        list_friends_buttons.append(check)
        i = 100

        for entry in cur:
            name_button = str(entry[2])
            surname_button = str(entry[3])
            check = QRadioButton(name_button + ' ' + surname_button, self)
            list_friends_surnames.append(name_button + ' ' + surname_button)
            check.resize(260, 20)
            check.move(10, i)
            check.clicked.connect(self.choosen_dialog)
            check.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
            check.setStyleSheet('QRadioButton {background-color: #17212b; color: white;}')
            list_friends_buttons.append(check)
            i += 30
        cur.execute("SELECT * FROM users WHERE DOMAIN != '" + domain + "' ")
        row = cur.fetchone()
        list_domain.append(row[1])
        for entry in cur:
            list_domain.append(entry[1])
        self.listView_3.setStyleSheet(
            'border-style: solid; border-width: 1px; border-color: #000000; background-color :#17212b;')
        self.textEdit.setStyleSheet(
            'border-style: solid; border-width: 0px; border-color: #242F3D; background-color :#242F3D;'
            ' border-radius: 3px;')
        self.pushButton.setStyleSheet(
            'border-style: solid; border-width: 1px; border-top-color: #000000; background-color :#17212b;')
        self.plainTextEdit.setStyleSheet(
            'border-style: solid; border-width: 0px; border-color: #0E1621; background-color :#0E1621; color :#ffffff')
        self.lineEdit.setStyleSheet(
            'border-style: solid; border-width: 1px; border-color: #000000; background-color :#17212b; color :#ffffff')
        self.listView.setStyleSheet('border-style: solid; border-width: 1px; border-color: #17212b')
        self.listView_2.setStyleSheet(
            'border-style: solid; border-width: 1px; border-color: #276899; background-color: #276899')
        self.thread1 = MyThread(1)
        self.thread1.progress.connect(self.add_message)
        self.thread1.start()

    def choosen_dialog(self):
        self.label_6.setVisible(False)
        self.plainTextEdit.move(330, 40)
        self.lineEdit.move(330, 810)
        self.pushButton.move(1050, 810)
        self.label_8.move(330, 0)
        self.choosen_friend()

    def choosen_friend(self):
        i = 0
        text = ''
        for check in list_friends_buttons:
            if check.isChecked():
                friend = list_friends_surnames[i]
                self.label_8.setText(friend)
                self.plainTextEdit.clear()
                messages.clear()
                break
            i += 1
        if len(messages) != 0:
            for mess in messages:
                text += mess + "\n"
            self.plainTextEdit.setPlainText(text)

    def add_message(self, value):
        messages.append(value)
        text = ''
        for mess in messages:
            text += mess + "\n"
        self.plainTextEdit.setPlainText(text)

    def send(self):
        info = vk.account.getProfileInfo()
        domain = info['screen_name']
        cur.execute("SELECT * FROM persons WHERE DOMAIN = '" + domain + "' ")
        row = cur.fetchone()
        if not row:
            (pubkey, privkey) = rsa.newkeys(512)
            print(type(pubkey))
            cur.execute("INSERT INTO persons (domain, key ) VALUES (%s,%s)", (domain, pickle.dumps(pubkey)))
            conn.commit()
        i = 0
        choose_friends = 0
        text = ''
        for check in list_friends_buttons:
            if check.isChecked():
                choose_friends = i
                if self.lineEdit.text() != '':
                    cur.execute("SELECT * FROM persons")
                    row = cur.fetchone()
                    vk.messages.send(message=self.lineEdit.text(), domain=list_domain[i])
                    messages.append("Я:")
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
    thread = Thread(target=login_with_sql)
    thread.start()
    app = Qt.QApplication([])
    si = Loginform()
    si.show()
    app.exec()
