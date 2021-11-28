import cx_Oracle
import datetime
import xlwt


device = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 201, 202, 203, 204, 205, 206, 207, 208, 209,
          210, 211, 212]




def request_srnz(date):
    date_list = date.split('-')
    today = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    tomorrow = str(today + datetime.timedelta(days=1))
    year = date_list[0]
    month = date_list[1]
    my_srnz_nolpn = []
    my_srnz_good = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()
        for i in range(len(device)):
            request_str = "SELECT count(*) FROM udbidentdata_" + year + "M" + month + " WHERE (sdevice = " + str(
                device[i]) + \
                          " and clicenseplate is not null and tactiontime < TO_DATE('" + tomorrow + \
                          "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD') )"
            request_str_2 = "SELECT count(*) FROM udbidentdata_" + year + "M" + month + " WHERE (sdevice = " + str(
                device[i]) + \
                          " and clicenseplate = '#NOLPN' and tactiontime < TO_DATE('" + tomorrow + \
                          "', 'YYYY/MM/DD') and tactiontime > TO_DATE('" + date + "', 'YYYY/MM/DD') )"

            c.execute(request_str)
            for row in c:
                my_srnz_good.append(*row)

            c.execute(request_str_2)
            for row in c:
                my_srnz_nolpn.append(*row)
        conn.close()



    except cx_Oracle.DatabaseError:
        print('Не удалось подключится к базе данных!')
        if len(my_srnz_nolpn) == 0 and len(my_srnz_good) == 0:
            for i in range(len(device)):
                my_srnz_nolpn.append(1)  # так как делить на ноль нельзя
                my_srnz_good.append(1)

    # сортируем данные на нераспознанные номера и общее количество проездов

    return my_srnz_nolpn, my_srnz_good


def mounth_srnz(date1,date2):
    date_list1 = date1.split('-')
    date3 = datetime.date(int(date_list1[0]), int(date_list1[1]), int(date_list1[2]))
    date_list2 = date2.split('-')
    date4 = datetime.date(int(date_list2[0]), int(date_list2[1]), int(date_list2[2]))
    date5 = (date4 + datetime.timedelta(days=1))
    result = {}
    result_2 = {}
    result['Проезд'] = device
    result_2['Проезд'] = device
    while date3 < date5:
        proc_nolp = []
        nolp, good = request_srnz(str(date3))
        cdate = str(date3)
        cdate_2 = cdate[5] + cdate[6] + '.' + cdate[8] + cdate[9]

        result['All ' + cdate_2] = good
        result['No ' + cdate_2] = nolp
        for i in range(len(device)):
            if good[i] == 0:
                proc_nolp.append(0)
            elif nolp[i] == 0:
                proc_nolp.append(100)
            else:
                proc_nolp.append(round(nolp[i] / (good[i] / 100), 2))
        result['% ' + cdate_2] = proc_nolp
        result_2['% ' + cdate_2] = proc_nolp

        date3 = (date3 + datetime.timedelta(days=1))

    # делаем таблицу
    file = "СРНЗ c " + str(date1) + " до " + str(date2) + ".xls"
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Процент')
    ws_1 = wb.add_sheet('Статистика')
    for colIdx, headerCaption in enumerate(result_2):
        ws.write(0, colIdx, headerCaption)
        for rowIdx, itemVal in enumerate(result_2[headerCaption]):
            ws.write(rowIdx + 1, colIdx, itemVal)
    for colIdx, headerCaption in enumerate(result):
        ws_1.write(0, colIdx, headerCaption)
        for rowIdx, itemVal in enumerate(result[headerCaption]):
            ws_1.write(rowIdx + 1, colIdx, itemVal)
    wb.save(file)


    return result





if __name__ == '__menu__':
    menu()
