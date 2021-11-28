import cx_Oracle


def change_white_list():
    result = []
    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()
        request_str = 'SELECT LPN FROM car_sharing'
        c.execute(request_str)
        for row in c:
            result.append(*row)
        conn.close()

    except cx_Oracle.DatabaseError:
        result.append('База данных не доступна!')

    return result


def search_number(number_avto):
    result = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()
        request_str = "SELECT LPN FROM car_sharing WHERE LPN LIKE '%" + number_avto + "%'"
        c.execute(request_str)
        for row in c:
            result.append(*row)
        conn.close()
        if not result:
            result.append('Данного номера нет в списке!')
    except cx_Oracle.DatabaseError:
        result.append('База данных не доступна!')

    return result


def convert_number(number_avto):
    new_number = []
    convert_rus_big = 'АВЕКМНОРСТУХ'
    convert_rus_lit = 'авекмнорстух'
    convert_eng = 'ABEKMHOPCTYX'
    digit = '0123456789'
    for number in number_avto:
        if number in convert_eng:
            new_number.append(number)
        elif number in convert_rus_big:
            for i in range(len(convert_rus_big)):
                if number == convert_rus_big[i]:
                    new_number.append(convert_eng[i])
        elif number in convert_rus_lit:
            for i in range(len(convert_rus_lit)):
                if number == convert_rus_lit[i]:
                    new_number.append(convert_eng[i])
        elif number in digit:
            for i in range(len(digit)):
                if number == digit[i]:
                    new_number.append(digit[i])
        else:
            pass

    new_number_str = ''.join(new_number)

    return new_number_str


def update_number(number, new_number):
    result = []

    try:
        dsn = cx_Oracle.makedsn('192.168.24.2', '1521', service_name='orcl')
        conn = cx_Oracle.connect(user='db', password='db', dsn=dsn)
        c = conn.cursor()
        request_str = "UPDATE car_sharing set LPN = '" + new_number + "' where LPN = '" + number + "'"
        c.execute(request_str)
        conn.commit()
        result.append('Номер успешно записан!')
        conn.close()
    except cx_Oracle.DatabaseError:
        result.append('Не удалось подключится к базе данных!')

    return result


if __name__ == '__menu__':
    menu()

