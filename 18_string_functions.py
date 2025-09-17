story = "once upon a time, Dumbledore dreamed of peace and light. ✨"
# print(story[0:5])

# String Functions
print(len(story))  # Return 58
print(story.endswith("notes"))  # Return Flase
print(story.startswith("notes"))  # Return False
print(story.endswith("light. ✨"))  # Return True
print(story.startswith("Once"))  # Return True
print(story.count("a"))  # Return 4
print(story.count("course"))  # Return 0
print(story.count("time"))  # Return 1
print(story.count("dr"))  # Return 1
print(story.count("ea"))  # Return 2
print(story.capitalize())  # Return Big O
print(story.find("peace"))  # Return 40
print(story.find("pece"))  # Return -1 (Unable to find that word)
print(story.replace("time", "Time"))  # Return once upon a Time, Dumbledore dreamed of peace and light. ✨