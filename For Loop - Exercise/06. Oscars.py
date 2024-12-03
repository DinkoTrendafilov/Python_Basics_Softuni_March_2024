MIN_POINTS = 1250.5

actor_name = input()
points = float(input())
judges_count = int(input())

for _ in range (judges_count):
    judge_name = input()
    judge_points = float(input())
    points += (len(judge_name) * (judge_points / 2))

    if points >= MIN_POINTS:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break

else:
    needed_points = MIN_POINTS - points
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')