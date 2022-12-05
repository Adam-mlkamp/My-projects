shopping_list = []
prices = []

item = None
number = None
total = 0

while number != 5:
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    number = float(input('Please enter an action: '))
    if number == 1:
        print('')
        item = input('What item would you like to add? ')
        price = float(input(f"What is the price of '{item.capitalize()}': "))
        shopping_list.append(item)
        prices.append(price)
        print(f"{item.capitalize()} has been added to the cart!")
        print('')
    elif number == 2:
        print('')
        print('The contents of your shopping cart are:')
        for i in range(len(shopping_list)):
            item = shopping_list[i]
            price = prices[i]
            print(f"{i +1}. {item.capitalize()} - ${price:.2f}")
        print('')
        
    elif number == 3:
       baditem = int(input('Which item would you like to remove? '))
       correction = baditem - 1
       shopping_list.pop(correction)
       prices.pop(correction)
       print('Item Removed')

    elif number == 4:
        print('') 
        total = sum(prices)
        print(f'The total price of the items in the shopping cart is ${total:.2f}')
        print('')
    
print('Thank you. Goodbye.')