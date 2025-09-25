with open("101_this.txt") as f:
    content = f.read()

    with open("101_copy.txt", "w") as f:
        f.write(content)