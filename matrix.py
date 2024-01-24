#This is a matrix solver


p = [[1,2,4],[5,6,9]]
def matrix_reducer(matrix):
    #rref
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = []

    for i in range(row):
        new_row = []
        for j in range(col):
            new_row.append(matrix[i][j]/matrix[i][0])
        new_matrix.append(new_row)
    return new_matrix

#print(matrix_solver(p))
def matrix_combiner(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = []
    new_matrix.append(matrix[0])
    for i in range(1,row):
        new_row = []
        for j in range(col):
            new_row.append(matrix[i][j]-matrix[0][j])
        new_matrix.append(new_row)
    return new_matrix

#print(matrix_combiner(matrix_reducer(p)))
def matrix_final(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = []
    new_matrix.append(matrix[0])
    for i in range(row-1,0, -1):
        new_row = []
        for j in range(col):
            new_row.append(matrix[i][j] / matrix[i][1])
        new_matrix.append(new_row)

    return new_matrix

c = matrix_combiner(matrix_reducer(p))
d = (matrix_final(c))

def combinf(matrix):
    row = len(matrix)
    col = len(matrix[0])
    new_matrix = []
    counter = 2 -1
    #new_matrix.append(matrix[0])
    for i in range(row):
        if i == counter:
            continue
        else:
            new_row = []
            for j in range(col):
                print(i,j)
                print(matrix[i][counter])
                new_row.append(matrix[i][j]-(matrix[i][counter])*(matrix[counter][j]))
            new_matrix.append(new_row)
        new_matrix.append(matrix[counter])
    return new_matrix

print(combinf(d))

#cramer rules
def deter(m):
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    return a*d-b*c
    my_dict = {}
    for row in m:
        for col in row:
            my_dict[str(col)+str(row)] = col
    return my_dict


def deter1(m):
    a = m[0][2]
    b = m[0][1]
    c = m[1][2]
    d = m[1][1]
    return a*d-b*c
print(1/(deter(p)/deter1(p)))

