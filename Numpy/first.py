#Numpy is a pythoon library
#Numpy is used for working with arrays
#Numpy is short for Numerical python

#Creating a Numpy array
import numpy as np

array=np.array([1,2,3,4,5])
print(array)
print(type(array))


#Use a tuple to create a Numpy array
import numpy as np
arr=np.array((1,2,3,4,5))
print(arr)

#0-D arrays or 0-Scalars are the elements in an array.each value in an array is a 0-D array.
#Create a 0-D array with value 42
import numpy as np
arr=np.array(42)
print(arr)


#create a 1-D array containing the values 1,2,3,4,5
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

#create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#create a 3-D with two 2-D arrays both containing two arrays with the values 1,2,3 and 4,5,6
import numpy as np

arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print (arr)

#check dimensions
import numpy as np

a=np.array(42)
b=np.array([1,2,3,4,5])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher Dimensional Arrays
#When the array is created you can defined the number of dimensions by using ndim argument
"""
create an array with 5 dimensions and verify that it has 5 dimensions
"""
import numpy as np
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print("Number of dimensions:", arr.ndim)

#Access Array Elements
import numpy as np
arr=np.array([1,2,3,4])
print(arr[0])

#get third and fourth elements from array and add them
import numpy as np
arr=np.array([1,2,3,4])
print(arr[2]+arr[3])

#Access the element on the first row ,second column
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("2nd element on 1st row :",arr[0,1])

#Access the third element of the second array of the first array
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2])

#Numpy Array Slicing
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])


#Slice elements from index 4 to the end of the array
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[4:])

#Slice elements from the begining to index 4
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[:4])

#Slice from the index 3 from the end to index 1 from the end
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])#use the inus operator to refers to an index from the end

#use the step value to determine the step of the Slicing
import numpy as np
arr=np.array([a,2,3,4,5,6,7])
print(arr[1:5:2])

#Return every other eleemnt from the entire array
import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[::2])

#Slicing 2_D arrays
#From the second element,Slice elements from index 1 to index 4
import numpy as np
arr=np.array([1,2,3,4,5],[6,7,8,9,10])
print(arr[1,1:4])

#From numpy as np
#From both elements return index 2
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
slice_col = arr[0:2, 2]
print("The Slice_col is:",slice_col)