with open("092_this.txt", "r") as f:
    a = f.read()
print(a)

with open("092_this.txt", "w") as f:
    a = f.write("me")
print(a)