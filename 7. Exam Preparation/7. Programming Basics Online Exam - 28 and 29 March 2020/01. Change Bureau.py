number_of_bitcoins = int(input())
number_of_chinese_yoans = float(input())
commission = float(input())

bitcoin_levas = number_of_bitcoins * 1168

chinese_yoans_dollars = number_of_chinese_yoans * 0.15
chinese_yoans_levas = chinese_yoans_dollars * 1.76

total_money_in_levas = bitcoin_levas + chinese_yoans_levas
total_money_in_euros = total_money_in_levas / 1.95

commission_percent = commission / 100
total_money_with_commission = total_money_in_euros - total_money_in_euros * commission_percent

print(f"{total_money_with_commission:.2f}")
