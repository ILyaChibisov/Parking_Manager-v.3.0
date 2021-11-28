import cx_Oracle
import datetime


def avto_in_park(date):
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


        request_str = "SELECT COUNT(*) FROM udbmovement_" + year + "M" + month + " WHERE (sdevice = 101 or " \
                     "sdevice = 102 or sdevice = 103 or sdevice = 104 or sdevice = 105 or sdevice = 106 " \
                     "or sdevice = 107 or sdevice = 108 or sdevice = 109 or sdevice = 110 or sdevice = 112" \
                      "or sdevice = 113) and stranstype = 2 and " \
                     "tactiontime < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD')"

        request_str_2 = "SELECT COUNT(*) FROM udbmovement_" + year + "M" + month + " WHERE (sdevice = 201 or sdevice = 202" \
                        "or sdevice = 203 or sdevice = 204 or sdevice = 205 or sdevice = 206 or sdevice = 207 or sdevice = 208" \
                        "or sdevice = 209 or sdevice = 210 or sdevice = 211 or sdevice = 212) " \
                       " and stranstype = 12 and tactiontime < TO_DATE('" + tomorrow + \
                      "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD')"

        result_count = [request_str, request_str_2]

        for count in result_count:
            c.execute(count)
            for row in c:
                if row[0] == None:
                    result.append(0)
                else:
                    result.append(*row)

        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')

    count_avto = result[0] - result[1]

    return count_avto



if __name__ == '__menu__':
    menu()