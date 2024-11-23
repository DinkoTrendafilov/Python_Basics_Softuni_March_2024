mackerel_price_per_kg = float(input())
sprinkle_price_per_kg = float(input())
bonito_quantity_in_kg = float(input())
safrid_quantity_in_kg = float(input())
mussels_quantity_in_kg = float(input())

price_mussels = 7.5
price_bonito = mackerel_price_per_kg * 1.6
price_safrid = sprinkle_price_per_kg * 1.8

total_price = (bonito_quantity_in_kg * price_bonito) + \
              (safrid_quantity_in_kg * price_safrid) + \
              (mussels_quantity_in_kg * price_mussels)

print(f'{total_price:.2f}')
