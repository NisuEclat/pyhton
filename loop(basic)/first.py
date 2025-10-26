#Print i as long as i less than 6
i = 1
while i< 6 :
    print (i)
    i+=1
#The break Statement
#with the break statement we can stop the loop even if the while condition is true
i=1
while i< 6 :
    print(i)
    if i== 3:
        break
    i+=1
#Continue to the next iteration it it is 3
#With the continue statment we can stop the current iteration and continue with the next
i=0
while i < 6:
    i+=1
    if i == 3:
        continue  
print(i)  

#The Else Statement
#With the Else statement ,we can run a block of code once when the condition no longer is true:
i=1
while i< 6 :
    print(i)
    i+=1
else :
    print("i is no longer less than 6") 
    
    
    
#Python for loops
fruits=["Apple","Banana","Cherry"]
for x in fruits :
    print(x)
#The break statement
fruits=["apple","Banana","Cherry"]
for x in fruits :
    print(x)
    if x == "banana":
        break
    
#Exit the loop when x is banana but this time the break comes before the print
fruits=["apple","banana","cherry"]
for x in fruits:
    if x== "banana":
        break
    print(x)        
    
#The continue statement
#donot print banana
fruits=["apple","banana","Cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)  
#The Range function
for x in range(6):
    print(x)
    
"""
The range function returns a sequence of 
numbers starting ,
from 0 by default and incremented by 1
and, ends with a specified number
"""   
#using the start parameter
for x in range(2,6):
    print (x)
"""
The range function defaults to increment the sequence
by 1 ,however it is possible to specify the increment
value by adding a third parameter: range(2,30,3)
"""
#Increment the sequence the 3 (default is 1)
for x in range(2,30,3):
    print(x)
#The Else in for loop
"""
print all numbers  from 0 to 5 ,and print a 
message when the loop has ended
"""
for x in range(6):
    print(x)
else:
    print("Finally finished") 
""" 
The else block will NOT be executed
if the loop is stopped by a break statement
"""  
#Break the loop when x =3 and see what happens with the else balock
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("Finally finished")    
#Nested loops
""""
print each adjective for every loop
"""
adj =["red","big","tasty"]
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
            