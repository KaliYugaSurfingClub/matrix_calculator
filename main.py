from actions_dict import actions_dict
from matrices_dict import matrices_dict
from checking_for_correctionss import matrix_name_is_correct
from interface.print_matrices_list import print_matrix

def user_text_for_action_is_correct(action, matrices_for_action, new_matrix_name):
    if action not in actions_dict.keys():
        print("нет такой команды")
        return False
            
    if len(matrices_for_action) != actions_dict[action]["arg_count"]:
        print("не верное кол-во аргументов для указанной операции")
        return False

    if matrices_dict.__contains__(new_matrix_name):
        print("имя уже занято")
        return False
    
    flag = False
    for name in matrices_for_action:
        if not matrix_name_is_correct(name):
            print("имя матрицы - одна латинская буква")
            flag = True
            continue
        if not matrices_dict.__contains__(name):
            print(f"матрица {name} - не определена")
            flag = True
            continue

    if flag:
        return False
    
    return True     


def main():
<<<<<<< HEAD
    while True:
        for action in actions_dict:
            print(actions_dict[action]["about"])

        try:
            text = input().split()
            action = text[0]
        except:
            continue

        if action[:2] == "--":
            if not user_text_for_action_is_correct(action, [], "#"):
                continue

            actions_dict[action]["func"]()
            
        else:
            new_matrix_name = text[-1]
            names_matrices_for_action = text[1:-1]

            if not user_text_for_action_is_correct(action, names_matrices_for_action, new_matrix_name):
                continue
            
            matrices_for_action = [matrices_dict[name] for name in names_matrices_for_action]
            if not actions_dict[action]["checking_for_correctness_func"](*matrices_for_action):
                continue

            matrices_dict[new_matrix_name] = actions_dict[action]["func"](*matrices_for_action)
            print_matrix(new_matrix_name)
        print("\n")

=======
    print("work")
    
>>>>>>> sum
main()