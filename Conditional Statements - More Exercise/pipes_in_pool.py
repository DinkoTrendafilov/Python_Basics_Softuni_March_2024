pool_capacity_v = int(input())
pipe_p1 = int(input())
pipe_p2 = int(input())
hours_h = float(input())

overflow_per_hour_p1 = pipe_p1 * hours_h
overflow_per_hour_p2 = pipe_p2 * hours_h

filled_capacity = overflow_per_hour_p1 + overflow_per_hour_p2

filled_capacity_percentage = ((filled_capacity / pool_capacity_v) * 100)

pipe1 = (overflow_per_hour_p1 / filled_capacity) * 100
pipe2 = (overflow_per_hour_p2 / filled_capacity) * 100

if filled_capacity_percentage <= 100:
    print(f"The pool is {filled_capacity_percentage:.2f}% full. Pipe 1: {pipe1:.2f}%. "
          f"Pipe 2: {pipe2:.2f}% ")

elif filled_capacity_percentage > 100:
    liters_overflow = (overflow_per_hour_p1 + overflow_per_hour_p2) - pool_capacity_v
    print(f"For {hours_h} hours the pool overflows with {liters_overflow:.2f} liters")
