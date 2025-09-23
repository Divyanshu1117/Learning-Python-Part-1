# this = "                Divyanshu               "
# print(this)
# print(this.strip())


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Divyanshu is good    "
n = remove_and_split(this, "Divyanshu")
print(n)