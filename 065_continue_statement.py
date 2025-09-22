# for i in range(10):
#     if (i == 5):
#         continue
#     print(i)

print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if (i % 2 != 0):
        continue
    print(i, end=" ")
print("\n")

print("Odd numbers from 1 to 20:")
for i in range(1, 21):
    if (i % 2 == 0):
        continue
    print(i, end=" ")