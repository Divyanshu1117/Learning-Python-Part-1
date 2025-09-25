f = open("094_poem.txt")
t = f.read()
if "Twinkle" in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()