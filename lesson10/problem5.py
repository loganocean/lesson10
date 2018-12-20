print('-'*65)
print('Booze Bot')
print()
print("I'm a vending machine that dispenses different kinds of alcohol. You should no be drinking in the first play but, please answer the following question: ")
print()

age = input('How old are you? ')
age = int(age)

if age >= 21: 
	order = input('What would you like to to drink? ')
	print('Gimme your money. Pick up your ' + order + ' from the slot below.')

else: 
	years = 21 - age
	years = str(years)
	print("You are a little too young, if my vending machine boss was not her i would have gotten you, sorry. Come back in " + years + " years to order.")
print('-'*65)