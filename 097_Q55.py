with open("097_sample.txt") as f:
    content = f.read()
content = content.replace("donkey", "$%^@$^#")
with open("097_sample.txt", "w") as f:
    f.write(content)