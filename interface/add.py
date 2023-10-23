from checking_for_correctionss import *
from matrices_dict import matrices_dict

def matrix_inf_checking_for_correctness(inf):
    if len(inf) != 3:
        print("введены неполные данные")
        return False
    
    name, n, m = inf

    if not matrix_name_checking_for_correctness(name):
        print("имя матрицы - одна латинская буква")
        return False
    if matrices_dict.__contains__(name):
        print("имя уже занято ")
        return False
    if not checking_is_num(n):
        print("кол-во строк - число(не может начинаться с нуля и не может быть дробным или нулем)")
        return False
    if not checking_is_num(m):
        print("кол-во столбцов - число(не может начинаться с нуля и не может быть дробным или нулем)")
        return False
     
    return True


def row_checking_for_correctness(row, length):
    if len(row) != length:
        print("длинна не соответсвует указанной")
        return False
    
    for index in range(len(row)):
        if not row[index].isdigit():
            print(f"{index + 1} эл-т в строке не являеться числом")
            return False

    return True

def add_matrices():
    flag = True
    while flag:
        try:
            count = int(input("сколько матриц вы хотите добавить?\n"))
            flag = False
        except:
            print("кол-во матриц - число")
            continue
    
    while count > 0:
        inf = input("введите: имя матрицы(одна латинская буква), кол-во строк, кол-во столбцов, через пробел\n").split()
        if not matrix_inf_checking_for_correctness(inf):
            continue
        
        name, n, m = inf
        n = int(n)
        m = int(m)
        matrix = []

        index = 0
        while m > 0:
            row = input(f"введите элементы {index + 1} строки через пробел\n").split()
            if not row_checking_for_correctness(row, n):
                continue

            matrix.append([int(s) for s in row])
            m -= 1
            index += 1

        matrices_dict[name] = matrix
        count -= 1