myNumber = int(input("Enter a number to see if it's odd or even: "))
check = int(input('By what value do you want to check if your number is divisible? '))
if myNumber % 4 == 0:
    print(f'{myNumber} is divisible by 4')  
elif myNumber % 2 == 0:
    print(f'{myNumber} is Even')
else:
    print(f'{myNumber} is Odd')

if myNumber % check == 0:
    print(f'Your number "{myNumber}" is divisible by {check}.')
else:
    print(f'Your number "{myNumber}" is NOT divisible by {check}.')
    