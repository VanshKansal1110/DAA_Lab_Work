def add(X, Y):
    n = len(X)
    return [[X[i][j] + Y[i][j] for j in range(n)] for i in range(n)]

def matrix_multiply(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    C11 = add(matrix_multiply(A11, B11), matrix_multiply(A12, B21))
    C12 = add(matrix_multiply(A11, B12), matrix_multiply(A12, B22))
    C21 = add(matrix_multiply(A21, B11), matrix_multiply(A22, B21))
    C22 = add(matrix_multiply(A21, B12), matrix_multiply(A22, B22))

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C
    
A=[[72,-45, 63,-81],[-56,94,-37,68],[89,-22,51,-74],[-93,67,-58,102]]
B=[[-84,59, -71,96],[43,-112,65,-39],[-97,54,88,-61],[76,-48,33,119]]
C=matrix_multiply(A,B)
print(C)