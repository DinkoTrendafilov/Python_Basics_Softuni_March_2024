import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_one_meter = float(input())

resistance = (distance_in_meters // 15) * 12.5
result = distance_in_meters * time_in_seconds_per_one_meter + resistance

needed_seconds = abs(record_in_seconds - result)
if record_in_seconds <= result:
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {result:.2f} seconds.")
