# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 400)
        MainWindow.setMaximumSize(QtCore.QSize(580, 400))
        MainWindow.setStyleSheet("background-color: rgb(225, 232, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -40, 640, 505))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setProperty("123", "")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(250, 60, 81, 23))
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 60, 81, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_12.setGeometry(QtCore.QRect(250, 90, 81, 23))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"")
        self.pushButton_12.setObjectName("pushButton_12")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 60, 211, 51))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 90, 81, 23))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(164, 42, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(360, 40, 191, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(170, 112, 71, 16))
        self.label_15.setObjectName("label_15")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_13.setGeometry(QtCore.QRect(480, 370, 81, 23))
        self.pushButton_13.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 101, 321))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 30, 81, 23))
        self.pushButton_15.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(40, 10, 491, 331))
        self.commandLinkButton.setStyleSheet("border-image: url(:/newPrefix/2222.png);")
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(280, 265, 71, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(200, 350, 211, 31))
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/brend.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 150, 81, 111))
        self.label.setStyleSheet("border-image: url(:/newPrefix/22.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(80, 400, 51, 61))
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/2.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 210, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 70, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 370, 81, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 180, 74, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 290, 74, 22))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 180, 81, 23))
        self.pushButton_4.setStyleSheet("\n"
"background-color: rgb(0, 170, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 210, 81, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 320, 81, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 350, 70, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 30, 171, 23))
        self.pushButton_8.setStyleSheet("\n"
"background-color: rgb(241, 255, 82);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 31, 21))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 80, 31, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(80, 110, 91, 21))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(180, 110, 91, 21))
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(100, 58, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(135, 60, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(100, 140, 71, 20))
        self.label_17.setObjectName("label_17")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 140, 91, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 80, 91, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(185, 60, 81, 13))
        self.label_11.setObjectName("label_11")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(300, 60, 271, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 91, 111))
        self.label_10.setStyleSheet("border-image: url(:/newPrefix/barrier.png);\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setGeometry(QtCore.QRect(310, 300, 81, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 270, 81, 23))
        self.pushButton_10.setStyleSheet("\n"
"background-color: rgb(241, 255, 82);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(310, 320, 221, 51))
        self.label_5.setStyleSheet("border-image: url(:/newPrefix/brend.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 290, 81, 23))
        self.pushButton_14.setStyleSheet("\n"
"background-color: rgb(255, 221, 117);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(320, 370, 131, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setGeometry(QtCore.QRect(490, 270, 81, 23))
        self.pushButton_16.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(0, 30, 91, 51))
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/tb.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setGeometry(QtCore.QRect(0, 80, 90, 16))
        self.pushButton_17.setStyleSheet("\n"
"background-color: rgb(255, 221, 117);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(42, 46, 47, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 30, 71, 22))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(500, 30, 71, 23))
        self.pushButton_18.setStyleSheet("\n"
"background-color: rgb(241, 255, 82);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setGeometry(QtCore.QRect(420, 30, 71, 23))
        self.pushButton_19.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(300, 30, 31, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setGeometry(QtCore.QRect(100, 240, 75, 23))
        self.pushButton_20.setStyleSheet("\n"
"background-color: rgb(241, 255, 82);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setGeometry(QtCore.QRect(190, 350, 81, 23))
        self.pushButton_21.setStyleSheet("\n"
"background-color: rgb(241, 255, 82);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit_2.setGeometry(QtCore.QRect(400, 300, 81, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 270, 81, 23))
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parking_Manager ver 3.5"))
        self.pushButton_9.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_12.setText(_translate("MainWindow", "Замена номера"))
        self.label_12.setText(_translate("MainWindow", "Введите номер"))
        self.label_14.setText(_translate("MainWindow", "Отчет о выполненных операциях"))
        self.label_15.setText(_translate("MainWindow", "Новый номер"))
        self.pushButton_13.setText(_translate("MainWindow", "ВЫХОД"))
        self.pushButton_15.setText(_translate("MainWindow", "Поиск номеров"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.pushButton.setText(_translate("MainWindow", "Перезапуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Перезапуск"))
        self.pushButton_3.setText(_translate("MainWindow", "ВЫХОД"))
        self.pushButton_4.setText(_translate("MainWindow", "Тест Сети"))
        self.pushButton_5.setText(_translate("MainWindow", "Обновление"))
        self.pushButton_6.setText(_translate("MainWindow", "Тест Сети"))
        self.pushButton_7.setText(_translate("MainWindow", "Обновление"))
        self.pushButton_8.setText(_translate("MainWindow", "Расчет нечитаемого билета"))
        self.label_8.setText(_translate("MainWindow", " 2 часа бесплатно "))
        self.label_7.setText(_translate("MainWindow", "Часы"))
        self.label_9.setText(_translate("MainWindow", "Минуты"))
        self.label_17.setText(_translate("MainWindow", " 50 руб час"))
        self.label_11.setText(_translate("MainWindow", "Время стоянки"))
        self.pushButton_10.setText(_translate("MainWindow", "Отчёт СРНЗ"))
        self.pushButton_14.setText(_translate("MainWindow", "Видео"))
        self.pushButton_16.setText(_translate("MainWindow", "Фин. отчет"))
        self.pushButton_17.setText(_translate("MainWindow", "обновить"))
        self.pushButton_18.setText(_translate("MainWindow", "По клиенту"))
        self.pushButton_19.setText(_translate("MainWindow", "По номеру"))
        self.label_13.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_20.setText(_translate("MainWindow", "Платежи"))
        self.pushButton_21.setText(_translate("MainWindow", "Руч.Открытия"))
        self.pushButton_11.setText(_translate("MainWindow", "Таблица СРНЗ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

