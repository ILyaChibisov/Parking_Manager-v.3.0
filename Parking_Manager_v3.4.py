import sys
import os
import time
import keyboard
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import *
import xres_rs
from menu import *
from datetime import datetime
import math
import request_srnz
import Change_white_list as cwl
import finance as fin
import avto_in_park as ap
import searh_card as sc
import device_log as dl
import xlwt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Инициализируем QSystemTrayIcon иконку в трей со своим дизайном

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.ico'))
        '''
            Объявим и добавим действия для работы с иконкой системного трея
            show - показать окно
            hide - свернуть окно
            exit - выход из программы
        '''
        show_action = QAction("Показать", self)
        quit_action = QAction("Выход", self)
        hide_action = QAction("Свернуть", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Прописываем элементы интерфейса

        self.ui.commandLinkButton.clicked.connect(self.get_password)
        self.ui.pushButton_3.clicked.connect(self.ex_to_main)
        self.ui.pushButton.clicked.connect(self.terminal_device)
        self.ui.pushButton_2.clicked.connect(self.barrier_device)
        self.ui.pushButton_4.clicked.connect(self.network_test_terminal)
        self.ui.pushButton_6.clicked.connect(self.network_test_barrier)
        self.ui.pushButton_7.clicked.connect(self.bios_barrier)
        self.ui.pushButton_5.clicked.connect(self.bios_terminal)
        self.ui.pushButton_8.clicked.connect(self.tariff_validation)
        self.ui.pushButton_14.clicked.connect(self.video)
        self.ui.pushButton_10.clicked.connect(self.srnz)
        self.ui.pushButton_13.clicked.connect(self.ex_to_main)
        self.ui.pushButton_15.clicked.connect(self.create_white_list)
        self.ui.pushButton_9.clicked.connect(self.search_number)
        self.ui.pushButton_12.clicked.connect(self.update_number)
        self.ui.pushButton_16.clicked.connect(self.fin_table)
        self.ui.pushButton_17.clicked.connect(self.avto_in)
        self.ui.pushButton_18.clicked.connect(self.search_client)
        self.ui.pushButton_19.clicked.connect(self.number_tr)
        self.ui.pushButton_20.clicked.connect(self.terminal_pay)
        self.ui.pushButton_21.clicked.connect(self.device_open)
        self.ui.pushButton_11.clicked.connect(self.srnz_interval)
        # валидация на ввод текста

        int_validator = QIntValidator()
        int_validator.setRange(0, 999)
        self.ui.lineEdit_4.setMaxLength(9)
        self.ui.lineEdit_7.setMaxLength(9)
        self.ui.lineEdit.setValidator(int_validator)
        self.ui.lineEdit.setMaxLength(6)

        # Ставим любой IP камеры по умолчанию

        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.browser.load(QUrl("http://192.168.24.121"))
        self.ui.gridLayout.addWidget(self.browser)


        # Прописываем номера устройств в comboBox

        number_terminal = range(601, 630, 1)

        for i in number_terminal:
            self.ui.comboBox.addItem("%s" % i)
            i += 1

        number_barrier = range(201, 213, 1)
        number_barrier_2 = range(101, 114, 1)

        for e in number_barrier:
            self.ui.comboBox_2.addItem("%s" % e)
            e += 1
        for e in number_barrier_2:
            self.ui.comboBox_2.addItem("%s" % e)
            e += 1

        # Установка даты в виджите выбора времени по умолчанию на текущую

        current_date = str(datetime.now().date())
        date_list = current_date.split('-')
        date = self.ui.dateEdit
        date_2 = self.ui.dateEdit_2
        d = QDate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        date.setDate(d)
        date_2.setDate(d)

    @staticmethod
    def close_window():
        """
        Закрытие окна командной строки
        """
        keyboard.send("alt+space")
        time.sleep(0.2)
        key_step = 0
        while key_step != 5:
            keyboard.send("Down")
            key_step += 1
        keyboard.send("enter")

    @staticmethod
    def device_out(dev_id):
        """
        Процесс авторизации устройства через telnet
        """
        os.startfile(r"C:\Windows\System32\\cmd.exe")
        time.sleep(1.5)
        keyboard.write("telnet 192.168.24.%s" % dev_id)
        keyboard.send("enter")
        time.sleep(0.3)
        keyboard.write("root")
        keyboard.send("enter")
        time.sleep(0.3)
        keyboard.write("root")
        keyboard.send("enter")
        time.sleep(0.3)

        # Чистим от других виджетов...

    def clear_layout(self):
        for i in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(i).widget().deleteLater()

    def video(self):
        """
        Видео данного устройства
        """

        d = self.ui.comboBox_2.currentText()
        d = int(d) + 20
        time.sleep(0.2)
        self.browser.close()
        self.clear_layout()
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.browser.load(QUrl("http://192.168.24.%s" % d))
        self.ui.gridLayout.addWidget(self.browser)

    def tariff_validation(self):
        """
        Расчет тарифов буднего и выходного дня по времени въезда, исключаем неправильный ввод данных...
        """
        now = datetime.now()
        time_h = int(now.strftime("%H"))
        time_m = int(now.strftime("%M"))

        try:
            hour = int(self.ui.lineEdit_2.text())
            minutes = int(self.ui.lineEdit_3.text())
            if (0 <= hour <= 23) and (0 <= minutes <= 59) \
                    and (hour <= time_h) or (hour == time_h and minutes <= time_m):
                time_park2free = math.ceil(((time_h * 60 + time_m) - (hour * 60 + minutes + 120)) / 60) * 50
                if time_park2free < 0:
                    time_park2free = 0
                time_park = math.ceil(((time_h * 60 + time_m) - (hour * 60 + minutes)) / 60) * 50
                if math.ceil((time_h * 60 + time_m) - (hour * 60 + minutes)) <= 20:
                    time_park = 0
                a = self.ui.textEdit.setText(str(time_park2free) + ' руб')
                b = self.ui.textEdit_2.setText(str(time_park) + ' руб')
                c = self.ui.textEdit_3.setText(
                    str(math.ceil(((time_h * 60 + time_m) - (hour * 60 + minutes))) // 60) + 'ч '
                    + str(math.ceil(((time_h * 60 + time_m) - (hour * 60 + minutes))) % 60) + 'мин')
            else:
                a = self.ui.textEdit.setText("Ошибка")
                b = self.ui.textEdit_2.setText("Ошибка")
        except ValueError:
            a = self.ui.textEdit.setText("Ошибка")
            b = self.ui.textEdit_2.setText("Ошибка")

    def get_password(self):
        """
        Вводим пароль,после кликаем по картинке(ссылке) и переходим на
        вторую страницу tabWidget в основное меню программы.
        Если пароль неправильный открывается окно с ошибкой ввода пароля
        """

        c = self.ui.lineEdit.text()
        if c == '777':
            self.ui.tabWidget.setCurrentIndex(2)
        elif c == '740':
            self.ui.tabWidget.setCurrentIndex(0)
        elif c != 777 and c != 740:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Неверный пароль")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def ex_to_main(self):
        """
        Выход в окно ввода пароля
        """
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.lineEdit.setText("")

    def terminal_device(self):
        """
        Выбор терминала (кассы) для перезапуска в comboBox и преобразование его
        в нужный IP адресс, далее через командную строку переходи в telnet
        и перезапускаем устройство с помощью автоматического ввода пароля
        логина и команды перезагрузки в Cmd
        """
        d = self.ui.comboBox.currentText()
        d = int(d)
        d = d % 100 + 60
        self.device_out(d)
        keyboard.write("reboot")
        time.sleep(1)
        keyboard.send("enter")
        time.sleep(1)
        self.close_window()

    def barrier_device(self):
        """
        Выбор терминала (стойки) для перезапуска в comboBox и преобразование его
        в нужный IP адресс, далее через командную строку переходи в telnet
        и перезапускаем устройство с помощью автоматического ввода пароля
        логина и команды перезагрузки в Cmd
        """
        d = self.ui.comboBox_2.currentText()
        d = int(d)
        self.device_out(d)
        keyboard.write("reboot")
        time.sleep(1)
        keyboard.send("enter")
        time.sleep(1)
        self.close_window()

    def network_test_terminal(self):
        """
        Пинг тест данного устройства
        """
        d = self.ui.comboBox.currentText()
        d = int(d)
        d = d % 100 + 60
        os.startfile(r"C:\Windows\System32\\cmd.exe")
        time.sleep(1.5)
        keyboard.write("ping 192.168.24.%s -t" % d)
        keyboard.send("enter")
        time.sleep(3)
        self.close_window()


    def network_test_barrier(self):
        """
        Пинг тест данного устройства
        """
        d = self.ui.comboBox_2.currentText()
        d = int(d)
        os.startfile(r"C:\Windows\System32\\cmd.exe")
        time.sleep(1.5)
        keyboard.write("ping 192.168.24.%s -t" % d)
        keyboard.send("enter")
        time.sleep(3)
        self.close_window()

    def bios_terminal(self):
        """
        Выход в биос меню конфигурации устройства
        """
        d = self.ui.comboBox.currentText()
        d = int(d)
        d = d % 100 + 60
        self.device_out(d)
        keyboard.write("sh -c /usr/srvmode")
        keyboard.send("enter")

    def bios_barrier(self):
        """
        Выход в биос меню конфигурации устройства
        """
        d = self.ui.comboBox_2.currentText()
        d = int(d)
        self.device_out(d)
        keyboard.write("sh -c /usr/srvmode")
        keyboard.send("enter")

    def srnz(self):

        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        my_srnz_nolpn, my_srnz_good = request_srnz.request_srnz(value)
        if value <= str(datetime.now().date()):

            # создаём таблицу для вывода на экран данных

            table = QTableWidget(self)  # Создаём таблицу
            table.setColumnCount(4)  # Устанавливаем три колонки
            table.setRowCount(24)  # 24 строки в таблице

            # Устанавливаем заголовки таблицы

            table.setHorizontalHeaderLabels(["Уст-во", "Проезды", "Не Расп.", " % Не Расп."])
            table.verticalHeader().setVisible(False)

            # Устанавливаем выравнивание на заголовки

            table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
            table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
            table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)

            # заполняем строки

            for i in range(len(request_srnz.device)):
                table.setItem(i, 0, QTableWidgetItem(str(request_srnz.device[i])))
                if i <= len(my_srnz_good) - 1:
                    table.setItem(i, 1, QTableWidgetItem(str(my_srnz_good[i])))
                    table.setItem(i, 2, QTableWidgetItem(str(my_srnz_nolpn[i])))
                    if my_srnz_good[i] == 0:
                        my_srnz_good[i] = 1    # избегаем деления на ноль
                    present_nolpn = round(my_srnz_nolpn[i] / (my_srnz_good[i] / 100), 2)
                    table.setItem(i, 3, QTableWidgetItem(str(present_nolpn)))
                else:
                    pass

            # делаем ресайз колонок по содержимому

            table.resizeColumnsToContents()
            table.updateGeometry()

            # масштабируем таблицу
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу

            return my_srnz_nolpn, my_srnz_good, value
            # сохраняем в ХML

        def file_saver(*args, file_name):
                df = {}
                for arg in args:
                    df = {arg: [*arg]}
                print()





    def create_white_list(self):

        numbers = cwl.change_white_list()
        table = QTableWidget(self)
        table.setColumnCount(1)
        table.setRowCount(len(numbers))

        # Устанавливаем заголовки таблицы

        table.setHorizontalHeaderLabels(["Номера авто"])
        table.verticalHeader().setVisible(False)

        # Устанавливаем выравнивание на заголовки

        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)

        # заполняем строки

        if len(numbers) < 2:
            self.ui.lineEdit_6.setText(f'   {numbers[0]}')
        else:
            for i in range(len(numbers)):
                table.setItem(i, 0, QTableWidgetItem(numbers[i]))

        # делаем ресайз колонок по содержимому

        table.resizeColumnsToContents()
        table.updateGeometry()

        # масштабируем таблицу
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.gridLayout_2.addWidget(table, 0, 0)  # Добавляем таблицу

    def search_number(self):

        number = self.ui.lineEdit_4.text()
        convert_number = cwl.convert_number(number)
        number_info = cwl.search_number(convert_number)
        self.ui.lineEdit_6.setText( '  '.join(number_info))

    def update_number(self):
        number_1 = self.ui.lineEdit_4.text()
        changed_number = cwl.convert_number(number_1)
        number_2 = self.ui.lineEdit_7.text()
        new_number = cwl.convert_number(number_2)
        result = cwl.update_number(changed_number, new_number)
        self.ui.lineEdit_6.setText('  '.join(result))

    def fin_table(self):

        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        pay_bank, pay_money = fin.finance(value)

        if value <= str(datetime.now().date()):

            device = range(601, 630)
            # создаём таблицу для вывода на экран данных

            table = QTableWidget(self)  # Создаём таблицу
            table.setColumnCount(4)  # Устанавливаем четыре колонки
            table.setRowCount(30)  # 30 строк в таблице

            # Устанавливаем заголовки таблицы

            table.setHorizontalHeaderLabels(["Касса", "Безнал", "Налич", "Итого:"])
            table.verticalHeader().setVisible(False)

            # Выравниваем влево название столбцов

            for i in range(4):
                table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)

            # заполняем строки

            for i in range(29):
                table.setItem(i, 0, QTableWidgetItem(str(device[i])))
                table.setItem(i, 1, QTableWidgetItem(str(int(pay_bank[i] / 100))))
                table.setItem(i, 2, QTableWidgetItem(str(int(pay_money[i] / 100))))
                sum_finance = int((pay_bank[i] + pay_money[i]) / 100)
                table.setItem(i, 3, QTableWidgetItem(str(sum_finance)))
            table.setItem(29, 0, QTableWidgetItem(('Итого:')))
            table.setItem(29, 1, QTableWidgetItem(str(int(sum(pay_bank) / 100))))
            table.setItem(29, 2, QTableWidgetItem(str(int(sum(pay_money) / 100))))
            table.setItem(29, 3, QTableWidgetItem(str(int(sum(pay_bank) / 100 + sum(pay_money) / 100))))

            # делаем ресайз колонок по содержимому

            table.resizeColumnsToContents()
            table.updateGeometry()

            # масштабируем таблицу
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу


    def avto_in(self):

        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        avto_in = ap.avto_in_park(value)
        if value <= str(datetime.now().date()):
                self.ui.lineEdit_5.setText(str(avto_in))

    def search_client(self):
        result = []
        search = self.ui.lineEdit_8.text()
        result = sc.name(search)

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(5)  # Устанавливаем  колонки
        table.setRowCount(len(result))  #  строк в таблице

        # Устанавливаем заголовки таблицы

        table.setHorizontalHeaderLabels(["Карта", "Компания", "ФИО", "Авто", " Срок Действия"])
        table.verticalHeader().setVisible(False)

        # Выравниваем влево название столбцов

        # for i in range(5):
        #     table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)

        # заполняем строки

        for i in range(len(result)):
            table.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            table.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            table.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            table.setItem(i, 3, QTableWidgetItem(str(result[i][3])))
            table.setItem(i, 4, QTableWidgetItem(str(result[i][4])))

        # делаем ресайз колонок по содержимому

        table.resizeColumnsToContents()
        table.updateGeometry()

        # масштабируем таблицу
        # table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу



    def number_tr(self):
        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        search = self.ui.lineEdit_8.text()

        if value <= str(datetime.now().date()):
            result = sc.number_tr(value, search)

            table = QTableWidget(self)  # Создаём таблицу
            table.setColumnCount(3)  # Устанавливаем  колонки
            table.setRowCount(len(result))  #  строки в таблице

            # Устанавливаем заголовки таблицы

            table.setHorizontalHeaderLabels(["Время", "Уст-во", "Номер"])
            table.verticalHeader().setVisible(False)

            # Выравниваем влево название столбцов

            for i in range(3):
                table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)

            # заполняем строки

            for i in range(len(result)):
                table.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
                table.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
                table.setItem(i, 2, QTableWidgetItem(str(result[i][2])))


            # делаем ресайз колонок по содержимому

            table.resizeColumnsToContents()
            table.updateGeometry()

            # масштабируем таблицу
            # table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу

    def terminal_pay(self):
        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        d = self.ui.comboBox.currentText()
        time_create, pay, type_pay = fin.terminal_pay(value, str(d))

        if value <= str(datetime.now().date()):

            len_table = int(len(time_create) / 2)
            # создаём таблицу для вывода на экран данных

            table = QTableWidget(self)  # Создаём таблицу
            table.setColumnCount(3)  # Устанавливаем 2 колонки
            table.setRowCount(len(time_create))  # строки в таблице

            # Устанавливаем заголовки таблицы

            table.setHorizontalHeaderLabels(["Время", "Итог", "Тип"])
            table.verticalHeader().setVisible(False)

            # Выравниваем влево название столбцов

            for i in range(3):
                table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)

            # заполняем строки

            for i in range(len(time_create)):
                table.setItem(i, 0, QTableWidgetItem(str(time_create[i])))
                table.setItem(i, 1, QTableWidgetItem(str(pay[i])))
                table.setItem(i, 2, QTableWidgetItem(str(type_pay[i])))

            # делаем ресайз колонок по содержимому

            table.resizeColumnsToContents()
            table.updateGeometry()

            # масштабируем таблицу
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу

    def device_open(self):
        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        result = dl.open_bar(value)

        if value <= str(datetime.now().date()):

            # создаём таблицу для вывода на экран данных

            table = QTableWidget(self)  # Создаём таблицу
            table.setColumnCount(2)  # Устанавливаем 2 колонки
            table.setRowCount(len(result))  # строки в таблице

            # Устанавливаем заголовки таблицы

            table.setHorizontalHeaderLabels(["Время", "Устройство"])
            table.verticalHeader().setVisible(True)

            # Выравниваем влево название столбцов

            for i in range(2):
                table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)

            # заполняем строки

            for i in range(len(result)):
                table.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
                table.setItem(i, 1, QTableWidgetItem(str(result[i][1])))

            # делаем ресайз колонок по содержимому

            table.resizeColumnsToContents()
            table.updateGeometry()

            # масштабируем таблицу
            # table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.gridLayout.addWidget(table, 0, 0)  # Добавляем таблицу

    def srnz_interval(self):
        value = self.ui.dateEdit.dateTime().toString("yyyy-MM-dd")
        value_2 = self.ui.dateEdit_2.dateTime().toString("yyyy-MM-dd")
        request_srnz.mounth_srnz(value, value_2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
