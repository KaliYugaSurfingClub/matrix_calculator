from matrices_dict import matrices_dict
from checking_for_correctionss import matrix_name_is_correct


def num_is_correct(string):
    return string.isdigit() and string != "0"


def matrix_inf_is_correct(inf):
    if len(inf) != 3:
        print("введены неполные данные")
        return False
    
    name, n, m = inf

    if not matrix_name_is_correct(name):
        print("имя матрицы - одна латинская буква")
        return False
    if matrices_dict.__contains__(name):
        print("имя уже занято ")
        return False
    if not num_is_correct(n):
        print("кол-во строк - число(не может начинаться с нуля и не может быть дробным или нулем)")
        return False
    if not num_is_correct(m):
        print("кол-во столбцов - число(не может начинаться с нуля и не может быть дробным или нулем)")
     
    return True


def row_is_correct(row, length):
    if len(row) != length:
        print("длинна не соответсвует указанной")
        return False
    
    for index in range(len(row)):
        if not row[index].isdigit():
            print(f"{index + 1} эл-т в строке не являеться числом")
            return False

    return True


def add_matrices():
    # flag = True
    # while flag:
    #     count = input("сколько матриц вы хотите добавить?\n")

    #     if count == "":
    #         return

    #     if not (num_is_correct(count) and int(count) > 0):
    #         print("кол-во матриц - число")
    #         continue
        
    #     count = int(count)
    #     break

    flag = True

    while flag:
        inf = input("введите: имя матрицы(одна латинская буква), кол-во строк, кол-во столбцов, через пробел (чтобы выйти из режима добавления - enter)\n").split()
        if inf == []:
            return

        if not matrix_inf_is_correct(inf):
            continue
        
        name, n, m = inf
        n = int(n)
        m = int(m)
        matrix = []

        index = 0
        while m > 0:
            row = input(f"введите элементы {index + 1} строки через пробел\n").split()
            if not row_is_correct(row, n):
                continue

            matrix.append([int(s) for s in row])
            m -= 1
            index += 1

        matrices_dict[name] = matrix