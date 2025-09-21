# Is:-
# a = None
# if (a is None):
#     print("Yes")
# else:
#     print("No")

# In:-
# a1 = [45, 56, 6]
# print(45 in a)

# List of students with special access
vip_students = ["Aarav", "Ananya", "Rohan"]
sports_club = ["Priya", "Karan", "Sneha"]

# Input from user
name = input("Enter your name: ")
special_pass = ["Aarav"]  # list containing a single special pass object

# Check access
if name in vip_students or name in sports_club:
    print(f"{name}, you have access to the school event.")
else:
    print(f"{name}, you do NOT have access.")

# Identity check
# Check if user has the exact same special pass object
user_pass = ["Aarav"]  # a new list object with same content
if user_pass is special_pass:
    print("User has the original special pass object.")
else:
    print("User does NOT have the original special pass object.")