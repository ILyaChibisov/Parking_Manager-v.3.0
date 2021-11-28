import cx_Oracle
import datetime

from PyQt5.QtWidgets import *

def finance(date):
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    tomorrow = str(today + datetime.timedelta(days=1))
    year = date_list[0]
    month = date_list[1]
    result = []
    result_2 = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()
        for item in range(601, 630, 1):

            request_str = "SELECT SUM(lamount) FROM udbmovement_" + year + "M" + month + " WHERE sdevice = " + str(
                item) + \
                          " and WCREDITCLASS <> 0 and  CTEXT = 'Оплата парковки' and tactiontime < TO_DATE('" + tomorrow + \
                          "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD')"

            request_str_2 = "SELECT sum(lamount) FROM udbmovement_" + year + "M" + month + " WHERE sdevice = " + str(
                item) + \
                            " and WCREDITCLASS = 0 and  CTEXT = 'Оплата парковки' and tactiontime < TO_DATE('" + tomorrow + \
                            "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD')"

            # Вставить еще один фрагмент данных

            c.execute(request_str)
            for row in c:
                if row[0] == None:
                    result.append(0)
                else:
                    result.append(*row)

            c.execute(request_str_2)
            for row in c:
                if row[0] == None:
                    result_2.append(0)
                else:
                    result_2.append(*row)

        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')

    return result, result_2


def terminal_pay(date, terminal):
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    tomorrow = str(today + datetime.timedelta(days=1))
    year = date_list[0]
    month = date_list[1]
    result = []
    result_2 = []
    result_3 = []


    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()

        request_str = "SELECT tactiontime  FROM udbmovement_" + year + "M" + month + " WHERE sdevice = " + str(
            terminal) + \
                      "  and  CTEXT = 'Оплата парковки' and tactiontime < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD')" \
                                                                              "ORDER BY tactiontime DESC "

        request_str_2 = "SELECT lamount  FROM udbmovement_" + year + "M" + month + " WHERE sdevice = " + str(
            terminal) + \
                      " and  CTEXT = 'Оплата парковки' and tactiontime < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD') ORDER BY tactiontime DESC"

        request_str_3 = "SELECT spaymentmask  FROM udbmovement_" + year + "M" + month + " WHERE sdevice = " + str(
            terminal) + \
                      " and  CTEXT = 'Оплата парковки' and tactiontime < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD') ORDER BY tactiontime DESC"


        c.execute(request_str)
        for row in c:
                result.append(*row)
        for i in range(len(result)):

            result[i] = datetime.datetime.strptime(str(result[i]), "%Y-%m-%d %H:%M:%S").strftime('%H:%M:%S')

        c.execute(request_str_2)
        for row in c:
            result_2.append(*row)

        for i in range(len(result_2)):
                result_2[i] = str(int(result_2[i] / 100)) + 'руб'

        c.execute(request_str_3)
        for row in c:
            result_3.append(*row)

        for i in range(len(result_3)):
            if result_3[i] == 52:
                result_3[i] = 'безнал'
            else:
                result_3[i] = 'налич'

        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')

    return result, result_2, result_3




if __name__ == '__menu__':
    menu()





