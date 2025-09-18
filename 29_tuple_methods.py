# Creating a tuple using ()
t = (1, 2, 4, 5, 4, 1, 2, 1, 1)

# Tuple methods
print(t.count(1))  # Returns how many times 1 appears -> 4
print(t.index(5))  # Returns the index of first occurrence of 5 -> 3

# Built-in functions with tuples
print(len(t))  # Returns the length of tuple -> 9
print(max(t))  # Returns the maximum element -> 5
print(min(t))  # Returns the minimum element -> 1
print(sum(t))  # Returns the sum of all elements -> 22
print(sorted(t))  # Returns a sorted list -> [1, 1, 1, 1, 2, 2, 4, 4, 5]

# Boolean checks
print(any(t))  # Returns True if any element is non-zero -> True
print(all(t))  # Returns True if all elements are non-zero -> True