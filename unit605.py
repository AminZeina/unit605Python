# Created by Amin Zeina
# Created on Mar 2018

day = input('Enter the day of the week: ')
age = int(input('Enter your age: '))

if day == 'Saturday' or day == 'Sunday':
	print('Time to relax for the weekend!')
elif age > 18:
	print('Time to go to work!')
else:
	print('Time to go to school!')

input('Program end.')