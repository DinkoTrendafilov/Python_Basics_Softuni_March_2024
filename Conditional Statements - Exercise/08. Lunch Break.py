import math

movie_name = input()
during_time_per_episode = int(input())
during_time_for_relax = int(input())

time_for_lunch = (during_time_for_relax / 8)
time_for_relax = (during_time_for_relax / 4)

rest_time = during_time_for_relax - time_for_relax - time_for_lunch
diff = abs(during_time_per_episode - rest_time)
diff = math.ceil(diff)

if rest_time >= during_time_per_episode:
    print(f"You have enough time to watch {movie_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {diff} more minutes.")



