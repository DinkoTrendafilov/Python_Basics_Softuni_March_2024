product = input()
town = input()
quantity = float(input())

price = 0

if town == 'Sofia':
    if product == 'coffee':
        price = 0.5
    elif product == 'water':
        price = 0.8
    elif product == 'beer':
        price = 1.2
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.6

elif town == 'Plovdiv':
    if product == 'coffee':
        price = 0.4
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.3
    elif product == 'peanuts':
        price = 1.5


elif town == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.1
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55

total_price = price * quantity
print(total_price)