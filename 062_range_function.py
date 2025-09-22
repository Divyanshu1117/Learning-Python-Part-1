# for i in range(1, 8, 2):
#     print(i)

# 1. Simple range(start, stop)
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# 2. Range with step (odd numbers)
print("Odd numbers from 1 to 10:")
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

# 3. Reverse range (counting down)
print("Counting down from 5 to 1:")
for i in range(5, 0, -1):
    print(i, end=" ")