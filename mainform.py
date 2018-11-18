# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(1122, 863)
        Dialog.setStyleSheet("background-color: rgb(14, 22, 33);\n"
"")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1050, 810, 71, 51))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 33, 43);")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(330, 500, 791, 311))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setMouseTracking(False)
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(14, 22, 33);")
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setOverwriteMode(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 810, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(23, 33, 43);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 38, 37))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/photos/menu.png);\n"
"border-color: rgb(23, 33, 43);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(-262, 0, 261, 171))
        self.listView_2.setStyleSheet("background-color: rgb(39, 104, 153);\n"
"border-color: rgb(39, 104, 153);")
        self.listView_2.setSelectionRectVisible(False)
        self.listView_2.setObjectName("listView_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-262, 90, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(39, 104, 153);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-200, 10, 61, 61))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/photos/users.png);\n"
"background-color: rgb(39, 104, 153);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(-1000, 0, 861, 861))
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/photos/prozrach.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(-262, 170, 261, 701))
        self.listView.setStyleSheet("background-color: rgb(23, 33, 43);\n"
"border-color: rgb(23, 33, 43);")
        self.listView.setObjectName("listView")
        self.listView_3 = QtWidgets.QListView(Dialog)
        self.listView_3.setGeometry(QtCore.QRect(0, 0, 331, 871))
        self.listView_3.setStyleSheet("background-color: rgb(23, 33, 43);\n"
"")
        self.listView_3.setObjectName("listView_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 760, 259, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 33, 43);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(-250, 200, 35, 35))
        self.label_4.setStyleSheet("background-color: rgb(23, 33, 43);\n"
"background-image: url(:/newPrefix/photos/settings.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(-250, 200, 171, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(23, 33, 43);")
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(60, 7, 251, 27))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-color: rgb(36, 47, 61);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 47, 61);\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(620, 410, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-color: rgb(30, 44, 58);\n"
"color: rgb(240, 240, 240);\n"
"background-color: rgb(30, 44, 58);")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.listView.raise_()
        self.plainTextEdit.raise_()
        self.listView_3.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.textEdit.raise_()
        self.listView_2.raise_()
        self.label_2.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Отправить"))
        self.label_5.setText(_translate("Dialog", "Настройки"))
        self.label_6.setText(_translate("Dialog", "Выберите кому хотите написать"))

import main_form_rc
