def inches_to_cm(inches):
    return inches * 2.54

inch = float(input("Enter value in inches: "))
cm = inches_to_cm(inch)

print(inch, "inches =", cm, "cm")