annual_fee_for_basketball_training = int(input())

price_of_basketball_trainers = annual_fee_for_basketball_training - annual_fee_for_basketball_training * 0.4
price_of_basketball_tracksuit = price_of_basketball_trainers - price_of_basketball_trainers * 0.2
price_of_ball = price_of_basketball_tracksuit / 4
price_of_basketball_accesories = price_of_ball / 5

total_price = (annual_fee_for_basketball_training + price_of_basketball_trainers + price_of_basketball_tracksuit +
               price_of_ball + price_of_basketball_accesories)

print(f'{total_price:.2f}')
