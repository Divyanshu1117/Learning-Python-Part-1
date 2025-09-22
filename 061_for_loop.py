# fruits = ["Banana", "Watermelon", "Grapes", "Mango"]
# for item in fruits:
#     print(item)

word = input("Enter a word: ")
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is NOT a palindrome")