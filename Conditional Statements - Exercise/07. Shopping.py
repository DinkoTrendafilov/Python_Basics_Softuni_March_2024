budget = float(input())
count_of_videocards = int(input())
count_of_cpu = int(input())
count_of_ram = int(input())

videocards_price = 250
cpu_price = (videocards_price * count_of_videocards) * 0.35
ram_price = (videocards_price * count_of_videocards) * 0.1

total_price = (count_of_videocards * videocards_price)\
              +(count_of_cpu * cpu_price)\
              + (count_of_ram * ram_price)

if count_of_videocards > count_of_cpu:
    total_price -= total_price * 0.15

diff = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")