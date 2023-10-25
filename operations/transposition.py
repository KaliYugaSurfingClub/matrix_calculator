def get_transposed_matrix(Matrix):
    trans_m = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            trans_m[j][i] = Matrix[i][j]
    return(trans_m)

