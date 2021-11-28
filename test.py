import pandas as pd

list_1 = ['1', '3']
list_2 = ['2', '4']



def file_saver(file_name,*args,**kwargs):

    table = {}
    for kwarg in kwargs:
        for arg in args:
            table[kwarg] = arg
    df = pd.DataFrame(table)
    print(table)
    df.to_excel(f'./{file_name}.xlsx')

file_saver( '123',list_1, list_2, column_1='нечетные', column_2='четные')

def file_saver(file_name,table):

    # table = {}
    # for kwarg in kwargs:
    #     for arg in args:
    #         table[kwarg] = arg
    df = pd.DataFrame(table)
    print(table)
    df.to_excel(f'./{file_name}.xlsx')

file_saver( '123',list_1, list_2, column_1='нечетные', column_2='четные')