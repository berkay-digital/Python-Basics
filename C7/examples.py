
# Example 2
word = "C:ar12!"
if word[0:2] == "C:":
    word = word.upper()
print(word)


# Example 3
new_word = "Haaaay"
a_count = new_word.count("a")
new_word = new_word + str(a_count)
print(new_word)

# Example 4
def reverse(x):
  return x[::-1]
word123 = "Hello!"
if len(word123) % 3 == 0:
    word123 = reverse(word123)
    print(word123)

# Example 1
last_word = "x"
def return_last_two(last_word):
    if len(last_word) < 2:
        return " "
    else:
        last_word = last_word[0:2] + last_word[-2:]
        return last_word
print(return_last_two(last_word))
