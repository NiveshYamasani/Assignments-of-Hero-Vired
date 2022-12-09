# Taking inputs in five Different lines
a = int(input('Enter the first Number :'))
b = int(input('Enter the second Number :'))
c = int(input('Enter the third Number :'))
d = int(input('Enter the fourth Number :'))
e = int(input('Enter the fifth Number :'))

x = open('answer1.txt','a') # Opening files in append mode

if ((a<=0)or(b<=0)or(c<=0)or(d<=0)or(e<=0)): # checking weather the numbers are positive or not
    print('The entered values are',a,b,c,d,e)
    print('The entered values are',a,b,c,d,e,file=x) # entering into files
    print('Enter Values Higher Than Zero',file=x) # entering into files
    print('Enter Values Higher Than Zero')
else:
    sum = a+b+c+d+e # adding the numbers
    print('The entered values are',a,b,c,d,e)
    print('The entered values are',a,b,c,d,e,file=x) # entering into files
    print('The TOTAL of the five entered numbers is :',sum)
    print('The TOTAL of the five entered numbers is :',sum,file=x) # entering into files

x.close() # closing the file