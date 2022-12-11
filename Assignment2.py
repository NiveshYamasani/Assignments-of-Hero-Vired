n = int(input('Enter the number of entries:')) #Number of entries you want to enter
Car = {}
x = open('answer2.txt','a') # Opening files in append mode
for i in range(n):
    brand_name = input('Enter the brand name of the car :')  # taking input of the brand of the car
    color = input('Enter the color of the car :') # taking input of the color of the car
    Car[brand_name] = color # Entering the brand and the color into a dictionary
print(Car)
print(Car,file=x) # entering into files
x.close() # closing the file

