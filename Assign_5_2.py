# Prompts user to input a series of numbers, displays error message if input is not an integer, 
# and reports back the biggest and smallest number in the series when user types "done".
largest = None
smallest = None
while True :
    num = input('Enter a number: ')
    if num == 'done' :
        break

    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

# print('All Done!')
print('Maximum is', largest)
print('Minimum is', smallest)
