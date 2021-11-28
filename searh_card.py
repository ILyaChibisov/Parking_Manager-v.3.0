import cx_Oracle
import datetime



def name(name):
    result = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()

        request_str = "select ccardno,linvcaddrref,clastname,clicenceno,xvalendtimest FROM pt_pta_h where " \
                      "(clastname like '%" + name +"%' or ccardno like '%" + name +"%' or clicenceno like '%" + name +"%')" \
                      " ORDER BY lastchangedate DESC "


        c.execute(request_str)

        i = 0
        for row in c:
            i += 1
            if i < 2:
                result.append(row)
            else:
                break

        for i in range(len(result)):
            result[i] = list(result[i])

        conn.close()

    except cx_Oracle.DatabaseError:
        print('База данных не доступна!')

    return result


def number_tr(date, name):

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

        request_str = "SELECT  tactiontime, sdevice, clicenseplate " \
                      "FROM udbidentdata_" + year + "M" + month + " WHERE (clicenseplate like '%" + name + "%') ORDER BY tactiontime DESC"

        c.execute(request_str)


        for row in c:
                result.append(row)

        for i in range(len(result)):
            result[i] = list(result[i])

        conn.close()
        return result

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')


if __name__ == '__menu__':
    menu()

