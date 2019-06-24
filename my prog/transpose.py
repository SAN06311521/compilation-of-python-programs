r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
matrix = []
print("Enter the elements of matrix row-wise: ")


for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

print("The entered matrix is: ")

for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = ' ')
    print()

transpose_matrix = []

for i in range(r):
    b = []
    for j in range(c):
        b.append(matrix[j][i])
    transpose_matrix.append(b)

print("Transpose of the given matrix is: ")

for i in range(r):
    for j in range(c):
        print(transpose_matrix[i][j], end = ' ')
    print()
