words = ["donkey", "kaddu", "mote"]

with open("098_sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    
with open("098_sample.txt", "w") as f:
    f.write(content)