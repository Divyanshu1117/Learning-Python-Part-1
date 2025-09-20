# An empty set can be created using the below syntax
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)  # Adding a value repeatedly does not change a set

# b.add([4, 5, 6]) # Throws TypeError: unhashable type: 'list'

b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets

print(b)

## Length of the set
print(len(b))  # Prints the length of this set

## Removal of an Item
b.remove(5)  # Removes 5 from set b
# b.remove(15)  # Throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop())  # Removes & returns a random element
print(b)

print(b.clear())  # Clears the set, returns None
print(b)  # b is now empty

# Union
b = {1, 2, 3}  # Re-adding elements
print(b.union({8, 11}))  # Returns a new set with all elements
print(b)  # Original set b unchanged

# Intersection
c = {2, 3, 4, 11}  # Another set
print(b.intersection(c))  # Returns elements common to b and c
print(b)  # Original set b unchanged