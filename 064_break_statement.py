# for i in range(10):
#     print(i)
#     if (i == 5):
#         break

print("Processing numbers from 1 to 20:")

for i in range(1, 21):
    if (i % 2 != 0):
        continue
    if (i > 15):
        print("\nNumber exceeded 15, stopping the loop!")
        break
    print(i, end=" ")