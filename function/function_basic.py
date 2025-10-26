"""
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avioding code repetition.
"""
#Creating a function
def greet():
    print("Hello from a function")
#calling a function
def greet():
    print("Hello from a function")
greet() 
  
#Why we using a function
"""
Imagine you need to convert temperatures from farenheit 
to Celsius several times in your program.Without functions,
you would have to write the
same calculation code repeatedly
"""
#without functions -repetitive code
temp1=77
celsius1=(temp1-32)*5/9
print(celsius1)

temp2=95
celsius2=(temp2-32)*5/9
print(celsius2)

temp2=50
celsius2=(temp2-32)*5/9
print(celsius2)

#with functions-reusable code
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Return values
"""
Functions can send back to the code that calles 
then using the retuen statement
,When a functuind reaches a return statement,it stops executing
and send the result back
"""
#A function that returns a value
def get_greeting():
    return "hello from a function"
message=get_greeting()
print(message)
#Using the return value directly
def get_greeting():
    return "Hello from a function"
print(get_greeting())