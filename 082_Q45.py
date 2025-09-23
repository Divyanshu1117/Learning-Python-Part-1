# def farh(cel):
#     return (0 * (9 / 5)) + 32

# c = 0
# f = farh(c)
# print("Fahreheit Temperature is " + str(f))


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")