def get_sum_of_matrices(first_matrix, second_matrix):
    matrix_size1 = []
    matrix_size1.append(len(first_matrix[1]))
    matrix_size1.append(len(first_matrix[0]))
    matrix_size2 = []
    matrix_size2.append(len(second_matrix[1]))
    matrix_size2.append(len(second_matrix[0]))
    if matrix_size1 != matrix_size2:
        return 'Матрицы разных размеров'
    result = [[] for i in range(matrix_size1[0])]
    for i in range(matrix_size1[0]):
        for j in range(matrix_size1[1]):
            result[i].append(first_matrix[i][j] + second_matrix[i][j])
    return result

def get_difference_of_matrices(first_matrix, second_matrix):
    matrix_size1 = []
    matrix_size1.append(len(first_matrix[1]))
    matrix_size1.append(len(first_matrix[0]))
    matrix_size2 = []
    matrix_size2.append(len(second_matrix[1]))
    matrix_size2.append(len(second_matrix[0]))
    if matrix_size1 != matrix_size2:
        return 'Матрицы разных размеров'
    result = [[] for i in range(matrix_size1[0])]
    for i in range(matrix_size1[0]):
        for j in range(matrix_size1[1]):
            result[i].append(first_matrix[i][j] - second_matrix[i][j])
    return result
