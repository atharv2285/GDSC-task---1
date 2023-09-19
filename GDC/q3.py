
def matrix(matrix1, matrix2):
    n = len(matrix1)
 
    result = [[0] * n for _ in range(n)]
    trace = 0
    
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                if i == j:
                    trace += result[i][j]
    
    return result, trace


n = int(input("Enter size "))

print("Enter elements of the first matrix:")
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter elements of the second matrix:")
matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)


result_matrix, trace_value = matrix(matrix1, matrix2)


print("Resultant Matrix:")
for row in result_matrix:
    print(" ".join(map(str, row)))


print("Trace of the Resultant Matrix:", trace_value)
