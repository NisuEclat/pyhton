#A simple recursion function that counts down from 5
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)
countdown(5)  

#base case :A condition that stops the recursion
# A recursive case: the function calling itself with a modified argument

def factorial(n):
    #Base case
    if n==0 or n==1:
        return 1
    #Recursive case
    else:
        return n*factorial(n-1)
print(factorial(5))              

#Fibonacci Series
def fibonacci(n):
    if n<=1 :
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))    