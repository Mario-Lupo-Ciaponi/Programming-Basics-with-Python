food = input()
type_of_food = ''

if food == 'banana' or food == 'apple' or food == 'kiwi' or food == 'cherry' or food == 'lemon' or food == 'grapes':
    type_of_food = 'fruit'
elif food == 'tomato' or food == 'cucumber' or food == 'pepper' or food == 'carrot':
    type_of_food = 'vegetable'
else:
    type_of_food = 'unknown'

print(type_of_food)
