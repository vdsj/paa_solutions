from collections import defaultdict, deque
from copy import deepcopy

n = 3
magic_sum = int((n * n * (n * n + 1)) / 6)

def equal_sum(dict):
    for _, v in dict.items():
        if v != magic_sum:
            return False
    return True


def smallest_sum(dict):
    for _, v in dict.items():
        if v > magic_sum:
            return False
    return True

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")

def validate_matrix(matrix):
    add_line = defaultdict(int)
    col_sum = defaultdict(int)
    diag_sum = defaultdict(int)
    left = False

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                left = True

            add_line[i] += matrix[i][j]
            col_sum[j] += matrix[i][j]

            if i == j:
                diag_sum[0] += matrix[i][j]

            if i + j == n - 1:
                diag_sum[n - 1] += matrix[i][j]
    
    if left:
        return smallest_sum(add_line) and smallest_sum(col_sum) and smallest_sum(diag_sum)
    
    return equal_sum(add_line) and equal_sum(col_sum) and equal_sum(diag_sum)

def next(Current, matrix):
    possible = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                pMatrix = deepcopy(matrix)
                pMatrix[i][j] = Current

                if validate_matrix(pMatrix):
                    possible.append(pMatrix)

    return possible

def resolver():
    matrix = [ [0 for col in range(n)] for linha in range(n) ]
    possibilities = deque([ (1, matrix )])

    while len(possibilities):
        x = possibilities.popleft()
        Current = x[0]
        matrixCurrent = x[1]

        if Current == n * n + 1:
            print_matrix(matrixCurrent)
            continue
        
        for y in next(Current, matrixCurrent):
            possibilities.append((Current + 1, y))

resolver()
