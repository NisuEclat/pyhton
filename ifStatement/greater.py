a=33
b=200
if b > a :
    print("b is greater than a")
    
# A number is positive
number =15
if number > 0:
    print("The number is positive")    
    
    
#Nested if statements 
x=41
if x > 10 :
    print("Above ten")
    if x > 20 :
        print("and also above 20 !")
    else :
        print("but not above 20")       
        
#Checking multiple conditions with nesting

age= 25 
has_License = True

if age >=18 :
    if has_License :
        print ("You can drive")
    else:
        print("You need a License")
else :
    print("You are too young to drive")     
 
 #Three level of nesting

score = 65
attendance = 90
submitted = True

if score >= 60 :
    if attendance >= 90 :
        if submitted :
            print("Pass with good standing")
        else:
            print("pass but missing assignment")
    else:
        print("pass but low attendance")
else:
    print("Fail")        
            
#Nested if vs Logical operators
#using nested first
temperature = 25
is_sunny = True

if temperature > 20 :
    if is_sunny :
        print("Perfect beach weather!")    

 #using and operator
temperature =25
is_sunny = True 
 
if temperature > 20 and is_sunny :
     print("Perfect beach weather!")        
#Ligin validation with nested checks
username="Email"
password="python123"
is_active =True

if username :
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")                    
#Grade calculation with nested logic
score = 92
extra_credit = 5

if score >=90:
    if extra_credit > 0:
        print("A + Grade")
    else:
        print("A Grade")
elif score >= 80 :
    print("B Grade")
else:
    print ("C Grade")
#The python match Statement
day = 4
match day :
    case 1 :
        print("Mnday")
    case 2 :
        print("Tuesday")
    case 3 :
        print("Wednesday")
    case 4 :
        print("Thursday")
    case 5 :
        print("Friday")
    case 6 :
        print("Saturday")
    case 7 :
        print("Sunday")                        
                   
#Default value
day = 4
match day :
    case 6:
        print("Today is Saturday")
    case 7 :
        print("Today is Sunday")
    case _:
        print("Looking forward to the weekend")
                        
#combining the values
day =4
match day :
    case 1|2|3|4|5 :
        print("Today is a weekday")
    case 6 | 7 :
        print("I love weekends")
                                      
#If statement as Guards
month = 5
day = 4
match day:
    case 1|2|3|4|5 if month ==4:
        print("A weekday in April")
    case 1|2|3|4|5 if month == 5:
        print("A weekday in may")
    case _:
        print("No match")        
                                      