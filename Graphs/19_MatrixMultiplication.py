import matplotlib.pyplot as plt
import time

def add(X, Y):
    n = len(X)
    return [[X[i][j] + Y[i][j] for j in range(n)] for i in range(n)]

def subtract(X, Y):
    n = len(X)
    return [[X[i][j] - Y[i][j] for j in range(n)] for i in range(n)]

def matrix_multiply_D_AND_C(A, B):
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

    C11 = add(matrix_multiply_D_AND_C(A11, B11), matrix_multiply_D_AND_C(A12, B21))
    C12 = add(matrix_multiply_D_AND_C(A11, B12), matrix_multiply_D_AND_C(A12, B22))
    C21 = add(matrix_multiply_D_AND_C(A21, B11), matrix_multiply_D_AND_C(A22, B21))
    C22 = add(matrix_multiply_D_AND_C(A21, B12), matrix_multiply_D_AND_C(A22, B22))

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C


def matrix_multiply_By_Strassen(A,B):
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
    
    
    M1=matrix_multiply_By_Strassen(add(A11,A22),add(B11,B22))
    M2=matrix_multiply_By_Strassen(add(A21,A22),B11)
    M3=matrix_multiply_By_Strassen(A11,subtract(B12,B22))
    M4=matrix_multiply_By_Strassen(A22,subtract(B21,B11))
    M5=matrix_multiply_By_Strassen(add(A11,A12),B22)
    M6=matrix_multiply_By_Strassen(subtract(A21,A11),add(B11,B12))
    M7=matrix_multiply_By_Strassen(subtract(A12,A22),add(B21,B22))
    
    C11=subtract(add(add(M1,M4),M7),M5)
    C12=add(M3,M5)
    C21=add(M2,M4)
    C22=subtract(add(add(M1,M3),M6),M2)
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C

matrix_sizes = [8,16,32,64,128,256]

time_D_And_C=list()
time_Strassen=list()

for i in matrix_sizes:
    c=1
    A=list()
    for j in range(i):
        row = []
        for k in range(i):
            row.append(c)
            c+=1
        A.append(row)
    B=list()
    c-=1
    for j in range(i):
        row = []
        for k in range(i):
            row.append(c)
            c-=1
        B.append(row)
    start= time.perf_counter()
    matrix_multiply_D_AND_C(A, B)
    time_D_And_C.append(time.perf_counter()-start)
    start= time.perf_counter()
    matrix_multiply_By_Strassen(A,B)
    time_Strassen.append(time.perf_counter()-start)
    
plt.plot(matrix_sizes,time_D_And_C,'o-',label="By Divide_And_Conquer")
plt.plot(matrix_sizes,time_Strassen,'o-',label="By Strassen")

plt.xlabel("Matrix Sizes(N in Matrix(NxN))")
plt.ylabel("Time Taken By Algorithm to Solve")
plt.title("Matrix Multiplication Strategies")
plt.legend()
plt.grid(True)
plt.show()