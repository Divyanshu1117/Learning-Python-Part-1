num = int(input("Enter your number: "))
table = [num * i for i in range(1, 11)]
print(str(table))
with open("148_1_tables.txt", "a") as f:
    f.write(str(table))
    f.write("\n")