style="font-size: 1.8em; color: var(--ic-brand-font-color-dark);"

child_meal = float(input('What is the price of a child\'s meal? '))
adult_meal = float(input('What is the price of an adult\'s meal? '))
children = int(input('How many children are there? '))
adults = int(input('How many adults are there? '))
taxrate = float(input('What is the sales tax rate? '))

subtotal = (child_meal*children) + (adult_meal*adults)
salestax = (subtotal *taxrate) / 100
total = subtotal + salestax


print('\n''Subtotal: ${0:.2f}'.format(subtotal))
print('Sales Tax: ${0:.2f}'.format(salestax))
print('Total: ${0:.2f}'.format(total))
print()

payment = float(input('What is the payment amount? '))
while True:
    tip = input('How much tip would you like to give? ')
    try:
        tip = float(tip)
        break
    except ValueError:
        print ('Numbers only')
change = (payment - total)-tip
print('Change: ${0:.2f}'.format(change))

#I added additional features.
#I asked the user an input of how much tip they want to give and it only accepts numbers. The tip then deducts the total amount.



