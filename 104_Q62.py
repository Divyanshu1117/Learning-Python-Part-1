import os

oldname = "104_text.txt"
newname = "104_text_new.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)
os.remove(oldname)