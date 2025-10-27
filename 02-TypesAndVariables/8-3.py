###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# ...
# ...
# ...

celsius = float(input('Enter temperature in Celsius: '))
kelvin = celsius + 273.15
fahrenheit = (celsius * 1.8) + 32

print(f'Temperature in Kelvin:{kelvin: .2f}')
print(f'Temperature in Fahrenheit:{fahrenheit: .2f}')