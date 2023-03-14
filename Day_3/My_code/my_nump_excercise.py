#%%
import numpy as np
a = np.zeros(10)
a[4]=1
print(a)
#%%
b = np.arange(10,49,1)
b[4]=1
print(b)
#%%
b = np.arange(10,49,3)
a=b[::-1]
print(b)
print(a)
#%%
#numpy excersise (d)
m=np.arange(9).reshape(3,3)
print(m)
#%%
a=np.array([0,1,2])
b=np.array([1,3,4])
a[:, np.newaxis] + b
# %%
#find indices of non-zero elements from[1,2,0,0,4,0]
x=np.array([1,2,0,0,4,0])
x
print(np.nonzero(x))
#%%
#Create a random vector of size 30 and find the mean value
b = np.array(np.random.rand(30))
print(np.mean(b))
#%%
#Create a 2d array with 1 on the border and 0 inside
a=np.array([1,1,1,1,0,1,1,1,1]).reshape(3,3)
print(a)

matrix=np.zeros((5,5))
matrix[0,:]=1
matrix[-1,:]=1
matrix[:,0]=1
matrix[:,-1]=1
print(matrix)
#%%
#Create a 8x8 matrix and fill it with a checkerboard pattern
x=np.zeros((8,8))
x[1::2,0::2] =1
x[0::2,1::2] =1
print(x)
#%%
#Create a checkerboard 8x8 matrix using the tile function
print("checkboard pattern")
checkboard=np.tile([["0","1"], ["1","0"]], (4,4))
print(checkboard)
# %%
#Given a 1D array, negate all elements which are between 3 and 8, in place
x=np.arange(11)
m=(x>3) & (x<8)
x[m] *= -1
print(x)

#%%
#Create a random vector of size 10 and sort it
a = np.random.rand((10))
print(a)
sortedlist=sorted(a)
print(sortedlist)

# %%
#Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A,B)
print(equal)

#%%
#How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
A = float(Z)
print(A.dtype)

#%%
#How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print(C)
print("select the diagonal")
D = np.diag(C)
print(D)