myDict = {
    "Fast": "In a Quick Manner",
    "Shree Ram": "The God",
    "Marks": [1, 2, 5],
    "anotherdict": {"Divyanshu": "Player"},
    1: 2,
}

# Dictionary Methods
# print(myDict.keys())
# print(type(myDict.keys()))
print(list(myDict.keys()))  # Prints the keys of the dictionary
print(list(myDict.values()))  # Prints the values of the dictionary
print(myDict.values())  # Prints the values of the dictionary
print(myDict.items())  # Prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Shubham": "Friend",
    "Divya": "Friend",
    "Karan Kumar (KK)": "A Dancer",
}
myDict.update(updateDict)  # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Karan Kumar (KK)"))  # Prints value associated with key "Karan Kumar (KK)"
print(myDict["Karan Kumar (KK)"])  # Prints value associated with key "Karan Kumar (KK)"

# The difference between .get and [] syntax in Dictionaries?
print(myDict.get("Karan Kumar (KK) 2"))  # Returns None as Karan Kumar (KK) 2 is not present in the dictionary
# print(myDict["Karan Kumar (KK) 2"])  # Throws an error as Karan Kumar (KK) 2 is not present in the dictionary