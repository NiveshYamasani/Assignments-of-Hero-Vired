x = open('answer3.txt','a')                                 # Opening files in append mode

import pandas as pd

def Addition(a,b):                                          # Addition Function
    return(int(a+b))

def Subtraction(a,b):                                       # Subtraction Function
    return(int(a-b))

def Multiplication(a,b):                                    # Multiplication Function
    return(int(a*b))

def Division(a,b):                                          # Division Function
    return(float(a/b))

def Modulus(a,b):                                           # Modulus Function
    return(int(a%b))

num1 = int(input(' Enter the first number :'))              # Input of frist number
num2 = int(input(' Enter the second number :'))             # Input of second number
list1 = [f'{num1} + {num2}',f'{num1} - {num2}',f'{num1} * {num2}',f'{num1} / {num2}',f'{num1} % {num2}']                               # List of Arithmetic symbols
list2 = []                                                  # Empty list
list2.append(Addition(num1,num2))                           # Appending the Addition value
list2.append(Subtraction(num1,num2))                        # Appending the Subtraction vaule
list2.append(Multiplication(num1,num2))                     # Appending the Multiplication value
list2.append(Division(num1,num2))                           # Appending the Division value
list2.append(Modulus(num1,num2))                            # Appending the Modulus value

df = pd.Series(list2,index=list1)                           # Taking the values into the Series

print(df)

print(df,file=x)                                            # Output into file

x.close()                                                   # Closing the file