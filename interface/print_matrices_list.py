from matrices_dict import matrices_dict

def print_matrix(name):
    matrix = matrices_dict[name]
    print(f"{name}:")
    for row in matrix:
        print(f"|{" ".join([str(num) for num in row])}|")


def print_matrices_list():
    if len(matrices_dict) == 0:
        print("Вы еще не добавили ни одной матрицы\n")
        return

    for name in matrices_dict:
        print_matrix(name)
        print("\n")