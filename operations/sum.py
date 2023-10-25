def matrices_for_sum_is_correct(first_matrix, second_matrix):
    if not (len(first_matrix) == len(second_matrix) and len(first_matrix[0]) == len(second_matrix[0])):
        print("чтобы сложить матрицы они должи быть одного размера")
        return False
    
    return True


def get_sum_of_matrices(first_matrix, second_matrix):
    res = []
    for row_index in range(len(first_matrix)):
        row = []
        for element_index in range(len(first_matrix[row_index])):
            new_element = first_matrix[row_index][element_index] + second_matrix[row_index][element_index]
            row.append(new_element)

        res.append(row)
    
    return res