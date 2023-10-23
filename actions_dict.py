from operations.sum import get_sum_of_matrices
from operations.product import get_product_of_matrices
from operations.transposition import get_transposed_matrix
from interface.add import add_matrices
from interface.print_matrices_list import print_matrices_list

actions_dict = {
    "--add": {
        "func": add_matrices,
        "arg_count": 0,
        "about": "Если вы хотите добавить матрицы введите: --add"
    },
    "--list": {
        "func": print_matrices_list,
        "arg_count": 0,
        "about": "Если вы хотите вывести все матрицы: --list"
    }, 
    "sum": {
        "func": get_sum_of_matrices,
        "arg_count": 2,
        "about": "Если вы хотите сложить матрицы введите строку вида: sum 'имя первой матрицы' 'имя второй матрицы' 'имя под которым сохранить результат'"
    }, 
    "product": {
        "func": get_product_of_matrices,
        "arg_count": 2,
        "about": "Если вы хотите умножить матрицы введите строку вида: product 'имя первой матрицы' 'имя второй матрицы' 'имя под которым сохранить результат'"
    }, 
    "transpose": {
        "func": get_transposed_matrix,
        "arg_count": 1,
        "about": "Если вы хотите добавить матрицу введите строку вида: transpose 'имя матрицы' 'имя под которым сохранить результат'"
    }, 
}