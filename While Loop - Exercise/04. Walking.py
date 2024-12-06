goal_steps = 10000
total_steps = 0


while total_steps < goal_steps:
    command = input()

    if command == 'Going home':
        last_steps = int(input())
        total_steps += last_steps
        break

    current_steps = int(command)
    total_steps += current_steps


is_goal_reached = total_steps >= goal_steps
diff = abs(goal_steps - total_steps)

if is_goal_reached:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    print(f'{diff} more steps to reach goal.')
