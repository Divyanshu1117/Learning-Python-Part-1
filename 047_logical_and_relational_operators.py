# # And Operator:-
# age = int(input("Enter your age: "))

# if (age > 34 and age < 56):
#     print("You can work with us")
# else:
#     print("You cannot work with us")

# Or Operator:-
# age = int(input("Enter your age: "))

# if (age >= 18 or age >= 16):
#     if (age >= 18):
#         print("You can vote and drive a bike.")
#     else:
#         print("You can drive a bike but cannot vote yet.")
# else:
#     print("You are too young to vote or drive.")

# Not Operator:-
num = int(input("Enter a number: "))
if (num > 0):
    print("The number is positive.")
elif not (num > 0):
    if (num == 0):
        print("The number is zero.")
    else:
        print("The number is negative.")