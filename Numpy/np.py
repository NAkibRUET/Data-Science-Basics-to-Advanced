import numpy as np

#Making an array of 10 zeros
x = np.zeros(10)
print('\nMaking an array of 10 zeros\n',x)

#Making an array of 10 ones
x = np.ones(10)
print('\nMaking an array of 10 ones\n',x)

#Making an array of 10 fives
x = np.ones(10)*5  #np.fives() won't work
print('\nMaking an array of 10 fives\n',x)

#Create an array from 10 to 50
x = np.arange(10,51)
print('\nCreate an array from 10 to 50\n',x)

#Create an array of even numbers from 10 to 50
x = np.arange(10,51,2) #Here the 3rd parameter is like "i+=2" in for loop
print('\nCreate an array of even numbers from 10 to 50\n',x)


#Create a Matrix of 3x3
x = np.arange(0,9).reshape(3,3) 
print('\nCreate a Matrix of 3x3\n',x)


#Create a Matrix of 3x4
x = np.arange(0,12).reshape(3,4) 
print('\nCreate a Matrix of 3x4\n',x)


#Create a Matrix of 4x4 with even numbers
x = np.arange(0,31,2).reshape(4,4) 
print('\nCreate a Matrix of 4x4 with even numbers\n',x)

#Create an identity Matrix of 4x4
x = np.eye(4,4) 
print('\nCreate an identity Matrix of 4x4\n',x)

#Generating 5 Random from 0 to 1
x = np.random.rand(5) 
print('\nGenerating 5 Random from 0 to 1\n',x)

#Generating 20 Random integers from 5 to 10
x = np.random.randint(5,10,20) 
print('\n#Generating 20 Random integers from 5 to 10\n',x)

#create an array of 10 linearly spaced points between 0 to 5
x = np.linspace(0,5,20) #Double check the spelling. it's not lin'e'space
print('\n#create an array of 10 linearly spaced points between 0 to 5\n',x)

#Specifying row number and column number of a matrix
x = np.arange(0,16).reshape(4,4) 
print('\n#Specifying row number and column number of a matrix\n')
print('\nFrom row 0 and col 0\n',x[0:,0:])
print('\nFrom row 1 and col 1\n',x[1:,1:])
print('\nFrom row 1 and col 2\n',x[1:,2:])
print('\nFrom row 1 to 3 and col 1 to 3\n',x[1:3,1:3])
print('\nValue row 2 and col 1\n',x[2,1])

#Standard Deviation of matrix values
x = np.arange(0,25).reshape(5,5) 
print('\n#Standard Deviation of matrix values\n',x.std())

#Sum of the matrix elements
x = np.arange(0,25).reshape(5,5) 
print('\n#Sum of the matrix elements\n',x.sum())

#Sum of the matrix elements by columns
x = np.arange(1,26).reshape(5,5) 
print('\n#Sum of the matrix elements by columns\n',x.sum(axis=0))

#Sum of the matrix elements by rows
print('\n#Sum of the matrix elements by rows\n',x.sum(axis=1).reshape(5,1))

#Sum, multiplication, subtruction, division operation between two matrices
y = np.arange(2,51,2).reshape(5,5) 
print('\n#Matrix x\n',x)
print('\n#Matrix y\n',y)
print('\n#Sum of two matrix\n',x+y)
print('\n#Subtruction of two matrix\n',y-x)
print('\n#Division of two matrix\n',y/x)
print('\n#Multiplication of two matrix\n',y*x)

