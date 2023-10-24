from checking_for_correctionss import matrix_name_is_correct
from matrices_dict import matrices_dict

def del_matrices():
    flag = True
    while flag:
        try:
            names_arr = input("введите имена матриц которую вы хотите удалить, all - если хоитите удалить все\n").split()
            flag = False
        except:
            continue
        
        if names_arr[0] == "all" and len(names_arr) == 1:
            names_arr = list(matrices_dict.keys())

        index = 0
        while index < len(names_arr):
            name = names_arr[index]
            if not matrix_name_is_correct(name):
                continue

            del matrices_dict[name]
            index += 1

                
