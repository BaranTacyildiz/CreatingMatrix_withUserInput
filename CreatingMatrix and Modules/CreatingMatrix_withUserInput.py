import MatrixOperations

matrix1 = input("Name of the matrix = ")

matrix1 = [[0 for x in range(3)]for y in range(3)] #creating a 3x3 Zero matrix
for i in range(3): #creating rows of matrix
    for j in range(3): #creating columns of matrix
        matrix1[i][j] = int(input(str(i+1) + ". row " + str(j+1) + ". column element of first matrix : ")) #input elements from user
    
for i in range(3): 
    for j in range(3):
        print("%5d" % (matrix1[i][j]), end='')
    print() 

cEmatrix = matrix1
y= int(input("Which Row = "))-1
x= int(input("Which Column = "))-1
print(str(y+1)+". row",str(x+1)+". column element =>" ,MatrixOperations.chooseElement(cEmatrix,y,x))  #printing the choosed element
