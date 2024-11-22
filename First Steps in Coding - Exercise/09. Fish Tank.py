length_in_sm = int(input())
height_in_sm = int(input())
width_in_sm = int(input())
occupied_space_in_percent = float(input())

total_volume_in_liters = length_in_sm * height_in_sm * width_in_sm / 1000

occupied_space = occupied_space_in_percent * total_volume_in_liters / 100

needed_liters = total_volume_in_liters - occupied_space

print(needed_liters)
