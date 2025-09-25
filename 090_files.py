# Use open function to read the content of a file:-
f = open("090_sample.txt")  # By default the mode is r
# f = open("090_sample.txt", "r")
# data = f.read()
data = f.read(5)  # Read first 5 character from the file
print(data)
f.close()