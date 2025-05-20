inp = input('Enter the temperature (e.g., 45C or 102F): ')

if len(inp) < 2:
    print('Invalid input: too short')
else:
    degree_part = inp[:-1]
    unit = inp[-1].upper()

    if degree_part.isdigit():
        degree = int(degree_part)

        if unit == 'C':
            converted = (degree * 9/5) + 32
            print('Temperature in Fahrenheit:', converted, 'F')
        elif unit == 'F':
            converted = (degree - 32) * 5/9
            print('Temperature in Celsius:', converted, 'C')
        else:
            print('Invalid input: unknown unit (use C or F)')
    else:
        print('Invalid input: degree must be a number')
