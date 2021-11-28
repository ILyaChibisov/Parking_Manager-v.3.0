import cx_Oracle
import datetime



def open_bar(date):
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    tomorrow = str(today + datetime.timedelta(days=1))
    year = date_list[0]
    month = date_list[1]
    result = []


    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()


        request_str = "SELECT tstoretimest, wdeviceid FROM ev_bas_logg WHERE " \
                      "(leventref = 42250 and tstoretimest < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tstoretimest > TO_DATE('" + date + "', 'YYYY/MM/DD')) ORDER BY tstoretimest DESC"
        c.execute(request_str)

        for row in c:
            result.append(row)

        for i in range(len(result)):
            result[i] = list(result[i])

        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')

    for i in range(len(result)):
        result[i] = list(result[i])

    return result


def open_bar_del(date, interval_1, interval_2):
    date_1 = date + ' ' + interval_1
    date_2 = date + ' ' + interval_2
    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()

        request_str = "DELETE FROM ev_bas_logg WHERE " \
                      "(leventref = 42250 and tstoretimest < TO_DATE('" + date_2 + \
                      "', 'YYYY/MM/DD HH24:MI') and tstoretimest > TO_DATE('" + date_1 + "', 'YYYY/MM/DD HH24:MI'))"
        c.execute(request_str)
        conn.commit()
        conn.close()

    except cx_Oracle.DatabaseError:
        print('Не удалось подключится к базе данных!')





if __name__ == '__menu__':
    menu()