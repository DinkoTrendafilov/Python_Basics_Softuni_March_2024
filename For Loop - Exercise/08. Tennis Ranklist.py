import math

number_of_tournaments = int(input())
initial_points = int(input())
total_points = initial_points
win_tourneys = 0

for tour in range(number_of_tournaments):
    stage_of_tournament = input()

    if stage_of_tournament =='W':
        total_points += 2000
        win_tourneys += 1
    elif stage_of_tournament == 'F':
        total_points += 1200
    elif stage_of_tournament == 'SF':
        total_points += 720

earned_points = total_points - initial_points
print(f"Final points: {total_points}")
print(f"Average points: {int(earned_points / number_of_tournaments)}")
print(f"{win_tourneys / number_of_tournaments * 100:.2f}%")
