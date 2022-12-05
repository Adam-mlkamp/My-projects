def windchill_in_f(temperature):
    chilledwind = 35.74 + (0.6215 * temperature) - (35.75 * (windspeed ** 0.16)) + ((0.4275 * temperature) * (windspeed ** 0.16))
    print(f'At temperature {temp}F, and wind speed {windspeed} mph, the windchill is: {chilledwind:.2f}F')

def windchill_in_c(temperature):
    temperature = (temp * (9/5)) + 32
    chilledwind = 35.74 + (0.6215 * temperature) - (35.75 * (windspeed ** 0.16)) + ((0.4275 * temperature) * (windspeed ** 0.16))
    print(f'At temperature {temperature:.1f}F, and wind speed {windspeed} mph, the windchill is: {chilledwind:.2f}F')

windspeed = 0

temp = float(input('What is the temperature? '))
unit = input('Fahrenheit or Celsius (F/C)? ')

while windspeed != 60:
    if unit.lower() == 'f':
        windspeed = windspeed + 5
        windchill_in_f(temp)
    elif unit.lower() == 'c':
        windspeed = windspeed + 5
        windchill_in_c(temp)
    else:
        print('That is not a viable unit for temperature.')
        windspeed = 60
print('Thank you for using this program.')



