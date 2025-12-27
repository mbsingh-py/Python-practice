def add():
    l = []
    t = 2
    while t > 0:
        try:
            i = int(input('Enter a number: '))
            l.append(i)
            t -= 1
        except ValueError:
            print('Wrong input')
            continue
    s = sum(l)
    return (s)
def divide():
    while True:
        try:
            x = int(input('Enter a number x: '))
            break
        except ValueError:
            print('Wrong input')
    while True:
        try:
            y = int(input('Enter a number y: '))
            if y == 0:
                print('Denominator cant be 0.')
                continue
            break
        except ValueError:
            print('Wrong input')
            continue
    d = x / y
    return d

while True:
    print(f'1. Sum \n2. Divide \n3. Exit')
    try:
        i = int(input('Enter your choice 1/2/3: '))
    except ValueError:
        print(f'Wrong input \n')
        continue
    if i == 1:
        print(f'\nAdding two numbers')
        print(f'Sum of two numbers is {add()}. \n')
    elif i == 2:
        print(f'\nDivede x by y')
        print(f'y divides x = {divide()}. \n')
    elif i == 3:
        print(f'\nPrograme closed')
        break
    else:
        print(f'Invalid choice \n')
