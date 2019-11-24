import pandas as pd

cars = pd.read_csv('cars.csv')
a =  cars.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]

print(a)

b= cars[:1]

print(' ')
print(' ')
print('Mazda RX4:')
print(b)
c = cars.loc[[23],['Model','cyl']]

print(' ')
print(' ')
print('Number of cylinders of Camaro Z28:')
print(c)

d = cars.loc[[1,28,18],['Model','cyl','gear']]

print(' ')
print(' ')
print('Number of cylinders and Type of gears of the given models:')
print(d)


