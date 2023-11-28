def display_menu():
    print('Convert USD to any currency by selecting number below: ')
    print('1. Convert USD to Euro(EUR)')
    print('2. Convert USD to British Pound Sterling(GBP)')
    print('3. Convert USD to Japanese Yen(JPY)')
    print('4. Convert USD to Canadian Dollar(CAD)')
    print('5. Exit')

#Create four functions that convert currencies accept a value through an argument and return the converted value on the console
def USD_to_EU(value):
    return value*0.91
def USD_to_GBP(value):
    return value*0.79
def USD_to_JPY(value):
    return value*148
def USD_to_CAD(value):
    return value*1.36
while True:
    display_menu()
    choice = int(input())
    if choice == 5:
        print('Bye!')
        break
    else:
        amount = float(input('Enter an amount in US Dollars: '))
        if choice == 1:
            print(amount,'USD is equivalent to ',USD_to_EU(amount),'Euro')
        elif choice == 2:
            print(amount,'USD is equivalent to ',USD_to_GBP(amount),'GPB')
        elif choice == 3:
            print(amount,'USD is equivalent to ',USD_to_JPY(amount),'JPY')
        elif choice == 4:
            print(amount,'USD is equivalent to ',USD_to_CAD(amount),'CAD')