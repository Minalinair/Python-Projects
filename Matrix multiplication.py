matrix1=[[1,2],
         [3,4]]
matrix2=[[5,6],
         [7,8]]
result=[[0,0],
        [0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for row in result:
    print(row)