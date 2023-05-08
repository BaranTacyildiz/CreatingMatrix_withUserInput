import MatrixOperationsModule
import random

matrix1 = input("Name of the matrix = ")
x = int(input("\nHow do you create your matrix? \n1) Create with user input \n2) Create random \nChoose 1 or 2 => "))

if x == 1:
    matrix1 = [[0 for x in range(3)]for y in range(3)] #creating a 3x3 Zero matrix
    for i in range(3): #creating rows of matrix
        for j in range(3): #creating columns of matrix
            matrix1[i][j] = int(input(str(i+1) + ". row " + str(j+1) + ". column element of first matrix : ")) #input elements from user
        
    for i in range(3): 
        for j in range(3):
            print("%5d" % (matrix1[i][j]), end='')
        print() 

if x == 2:
    
    while True:
        minvalue = int(input("What is the minimum value of the matrix? => "))
        maxvalue = int(input("What is the maximum value of the matrix? => "))
        if minvalue>maxvalue:
            print("\n!!! Input Error. You can't choose minimum value bigger than maximum value. Try Again.\n")
        else:
            break
            


    matrix1 = [[0 for x in range(3)]for y in range(3)] #creating a 3x3 Zero matrix
    for i in range(3): #creating rows of matrix
        for j in range(3): #creating columns of matrix
            matrix1[i][j] = random.randint(minvalue,maxvalue)
        
    for i in range(3): 
        for j in range(3):
            print("%5d" % (matrix1[i][j]), end='')
        print() 


cEmatrix = matrix1
y= int(input("Which Row = "))-1
x= int(input("Which Column = "))-1
print(str(y+1)+". row",str(x+1)+". column element =>" ,MatrixOperationsModule.chooseElement(cEmatrix,y,x))  #printing the choosed element


