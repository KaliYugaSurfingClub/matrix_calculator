from checking_for_correctionss import matrix_name_is_correct
from matrices_dict import matrices_dict

def del_matrices():
        names_arr = input("введите имена матриц которую вы хотите удалить, all - если хоитите удалить все, enter - если не хотите ничего удалять\n").split()

        #на enter выходит из режима удаления
        if names_arr == [] or names_arr == ["--del"]:
             return

        if names_arr[0] == "all" and len(names_arr) == 1:
            names_arr = list(matrices_dict.keys())

        index = 0
        while index < len(names_arr):
            name = names_arr[index]
            if not matrix_name_is_correct(name):
                continue

            if not matrices_dict.__contains__(name):
                print(f"матрица {name} - не определенна")
                index += 1
                continue

            del matrices_dict[name]
            index += 1

                
