fruit = input()
size_of_set = input()
number_of_sets = int(input())

number_of_gels = 0
total_price = 0

if size_of_set == "small":
    number_of_gels = number_of_sets * 2

    if fruit == "Watermelon":
        total_price = number_of_gels * 56
    elif fruit == "Mango":
        total_price = number_of_gels * 36.66
    elif fruit == "Pineapple":
        total_price = number_of_gels * 42.1
    else:
        total_price = number_of_gels * 20
else:
    number_of_gels = number_of_sets * 5

    if fruit == "Watermelon":
        total_price = number_of_gels * 28.7
    elif fruit == "Mango":
        total_price = number_of_gels * 19.6
    elif fruit == "Pineapple":
        total_price = number_of_gels * 24.8
    else:
        total_price = number_of_gels * 15.2

if 400 <= total_price <= 1000:
    total_price -= total_price * 0.15
elif total_price > 1000:
    total_price -= total_price * 0.5

print(f"{total_price:.2f} lv.")
