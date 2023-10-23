def get_product_of_matrices(first_matrix, second_matrix):
    # Количество строк/колонн первой матрицы
    first_rows = len(first_matrix)
    first_columns = len(first_matrix[0])

    # Количество строк/колонн второй матрицы
    second_rows = len(second_matrix)
    second_columns = len(second_matrix[0])

    # Результат произведения
    result = []

    # Проходим по каждой строке первой матрицы
    for i in range(first_rows):
        # Добавляем строку к результату
        result.append([])
        # Проходим по каждой колонне второй матрицы
        for j in range(second_columns):
            # Скалярное произведение компонентовы
            s = 0
            for k in range(first_columns):
                s += first_matrix[i][k] * second_matrix[k][j]
            # Добавляем результат к указанной строке
            result[i].append(s)

    # Возвращаем результат
    return result