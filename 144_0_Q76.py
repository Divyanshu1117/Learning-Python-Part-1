def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("144_1.txt")
readFile("144_2.txt")
readFile("144_3.txt")