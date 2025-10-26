#Arguments
"""
>Infiirmation can passed into functions as arguments
>arguments are specified after the function name,
inside the parentheses.you can add as many arguments 
as you want,just separate
them with a comma.
"""
#A function with one argument
def my_function(fname):
    print(fname + "Refsnes")
    
my_function("Email")
my_function("Tabias")
my_function("Linus")   



 

#Parameter vs arguments
"""
A parameter is the variable listed 
inside the parentheses in the function definition.
Aargument is the actual value that is sent 
to the function when it is called 
"""
def my_function(name):#name is a parameter
    print("Hello",name)
my_function("Emil")#Emil is an argument   

 


#Number of argument
def my_function(fname,lname):
    print(fname +" "+lname)
my_function("Email","Refsnes")    


#Dafault parameter values

"""
If the function is called without an 
argument,it uses the default value
"""

def my_function(name="friend"):
    print("hello",name)
    
my_function("Emil")
my_function("Tobias") 
my_function()
my_function("Linus")

#Sending a list as an argument
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits=["apple","banana","cherry"]   
my_function(my_fruits)     

#return values
def my_function(x,y):
    return x+y
result=my_function(5,3)
print(result)               

#Returnning DIfferent data types
def my_function():
    return["apple","banana","cherry"]

fruits=my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])