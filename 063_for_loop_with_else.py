# for i in range(10):
#     print(i)
# else:
#     print("This is inside else of for")

num = int(input("Enter a number: "))

for i in range(2, num):
    if (num % i == 0):
        print(num, "is NOT a prime number (divisible by", i, ")")
        break
else:
    print(num, "is a prime number")