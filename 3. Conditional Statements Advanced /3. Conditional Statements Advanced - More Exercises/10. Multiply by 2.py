num = float(input())

while(True):
     if num >= 0:
        print(f'Result: {(num * 2):.2f}')
     else:
        print('Negative number!')
        break

     num = float(input())
