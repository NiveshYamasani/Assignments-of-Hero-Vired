import pandas as pd
x = open('answer4.txt','a')                             # Opening files in append mode
A = [int(input('Enter number :')) for _ in range(5)]    # input of the Five numbers 
B=[]
for i in A:
    b= i**2                                             # Power of the five numbers
    B.append(b)
df = pd.Series(B,index=A)                               # Taking the input and power value into the Series
print(df)
print(df,file=x)                                        # output into the file
x.close()                                               # closing the file