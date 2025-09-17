letter = """Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Lovish Kamboj
Date: <|DATE|>
"""
name = input("Enter your Name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)