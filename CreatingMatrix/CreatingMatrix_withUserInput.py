matrix1 = [[0 for x in range(3)]for y in range(3)] #creating a 3x3 Zero matrix
for i in range(3): #creating rows of matrix
    for j in range(3): #creating columns of matrix
        matrix1[i][j] = int(input(str(i+1) + ". row " + str(j+1) + ". column element of first matrix : ")) #input elements from user
    
for i in range(3): 
    for j in range(3):
        print("%5d" % (matrix1[i][j]), end='')
    print() 


