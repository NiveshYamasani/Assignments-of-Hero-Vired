x = open('answer2.txt','a')
brand_name = input('Enter the brand name of the car :')
color = input('Enter the color of the car :')
Car = {brand_name:color}
print(Car)
print(Car,file=x)
x.close()