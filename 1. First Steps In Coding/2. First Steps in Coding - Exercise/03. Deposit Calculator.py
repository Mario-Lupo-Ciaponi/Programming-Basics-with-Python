deposited_sum = float(input())
term_of_deposit = int(input())
annual_interest_percent = float(input())

accrued_interest = deposited_sum * (annual_interest_percent / 100)
interest_for_one_month = accrued_interest / 12
total_sum = deposited_sum + term_of_deposit * interest_for_one_month

print(total_sum)