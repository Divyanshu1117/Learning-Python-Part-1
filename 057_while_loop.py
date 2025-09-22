# i = 0
# while (i < 10):
#     print("Yes " + str(i))
#     i = i + 1
# print("Done")

num = int(input("Enter a number: "))
i = 1

print(f"Multiplication table of {num}:")
while (i <= 10):
    print(f"{num} x {i} = {num*i}")
    i += 1