deposit_sum = float(input())
deposit_in_months = float(input())
interest_percent = float(input())

accumulated_sum = (deposit_sum * interest_percent) / 100
interest_per_month = accumulated_sum / 12
total_sum = deposit_sum + deposit_in_months * interest_per_month

print(total_sum)
