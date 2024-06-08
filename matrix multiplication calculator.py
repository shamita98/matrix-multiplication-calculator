# function to input matrix
def matrix_entry(matrix_name):
    matrix_row, matrix_col = input(f"Enter the row,column of matrix {matrix_name}:").split(',')
    matrix_list = []
    i = 1
    try:
        if int(matrix_row) > 0 and int(matrix_col) > 0:
            while i >= 1:
                row = input(f'Enter entries in row {i} separated by comma: ').split(',')
                if len(row) == int(matrix_col):
                    matrix_list.append(row)
                else:
                    print('Entries is not equal to no. of columns. Enter again.')
                    continue
                i += 1
                if len(matrix_list) == int(matrix_row):
                    break
        else:
            print('\nRow and column should be an integer and greater than 0.')
            matrix_entry(matrix_name)
    except ValueError:
        print('\nRow and column should be an integer and greater than 0.')
        matrix_entry(matrix_name)

    return matrix_list


# function to check compatibility between two matrices
def matrix_compatibility(matrix_1, matrix_2):
    is_defined = False
    matrix_1_col = len(matrix_1[0])
    matrix_2_row = len(matrix_2)

    if matrix_1_col == matrix_2_row:
        is_defined = True

    return is_defined


# function to display matrix in 2D
def display_matrix(matrix_list):
    for line in matrix_list:
        row = '|'
        for entry in line:
            if line[0] == entry:
                row += '{:>4}'.format(entry)
            else:
                row += '{:>7}'.format(entry)
        row += '|'
        print(row)


# function to perform matrix multiplication
def matrix_multiplier(matrix_1, matrix_2):
    M_mat1 = len(matrix_1)
    N_mat1 = len(matrix_1[0])
    M_mat2 = len(matrix_2)
    N_mat2 = len(matrix_2[0])

    # create a blank matrix of size M_mat1 x N_mat2
    ans = []
    for i in range(M_mat1):
        row = []
        for j in range(N_mat2):
            row.append(0)
        ans.append(row)

    # perform matrix multiplication
    for i in range(N_mat2):  # access columns of mat2
        for j in range(M_mat1):  # access rows of mat1
            sum = 0
            for k in range(N_mat1):  # access columns of mat1
                sum += int(matrix_1[j][k]) * int(matrix_2[k][i])
            ans[j][i] = sum

    return ans


matrix_A = matrix_entry('A')
print('\n')
matrix_B = matrix_entry('B')
is_defined = matrix_compatibility(matrix_A, matrix_B)
if is_defined:
    try:
        product = matrix_multiplier(matrix_A, matrix_B)
        print('\nProduct of the two matrices is: \n')
        display_matrix(product)
    except ValueError:
        print('\nEnter integers or decimals for the entries in the matrices')
else:
    print('\nMatrix dimensions are not compatible.')




