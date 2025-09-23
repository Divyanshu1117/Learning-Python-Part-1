# n = 3
# for i in range(n):
#     print("*" * (n - i)) # Prints * n - i times
3
def print_pattern(n):
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter number of lines: "))
print_pattern(n)