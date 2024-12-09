bottles_count = int(input())

detergent = bottles_count * 750
counter = 0
plates_count = 0
pots_count = 0

while True:
    command = input()
    if command == 'End':
        break
    counter += 1
    vessels = int(command)

    if counter % 3 == 0:
        current_result = vessels * 15
        pots_count += vessels
    else:
        current_result = vessels * 5
        plates_count += vessels

    detergent -= current_result

    if detergent < 0:
        print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
        break

if detergent >= 0:
    print("Detergent was enough!")
    print(f"{plates_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
