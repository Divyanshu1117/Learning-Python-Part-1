text = input("Enter the text: \n")
spam = False
if ("Make A Lot Of Money" in text):
    spam = True
elif ("Buy Now" in text):
    spam = True
elif ("Click This" in text):
    spam = True
elif ("Subscribe This" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This text is spam")
else:
    print("This text is not spam")