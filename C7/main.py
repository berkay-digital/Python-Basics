word = "House12!"
word = word.replace("o", "0")
print(type(word))
print(len(word))
print(word[0])
print(type(word[0]))
print(word[0:5])
for letter in range(len(word)):
    print(word[letter])

for letter in word:
    print(letter)


