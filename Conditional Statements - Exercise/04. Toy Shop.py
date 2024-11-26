needed_money = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

total_money = (count_puzzles * 2.6
               + count_dolls * 3
               + count_bears * 4.1
               + count_minions * 8.2
               + count_trucks * 2)

total_count_of_toys = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

if total_count_of_toys >= 50:
    total_money -= total_money * 0.25
total_money -= total_money * 0.1
diff = abs(needed_money - total_money)

if total_money >= needed_money:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")