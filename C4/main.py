import time
delayBetweenExercises = 5

# 1.
"""
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
"""


# 2.
if 2**30 > 10**9:
    print(True)
    print("2**30 = " + str(2**30))
    print("10**9 = " + str(10**9))
else:
    print(False)
    print("2**30 = " + str(2**30))
    print("10**9 = " + str(10**9))


time.sleep(delayBetweenExercises)
# 3.
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))

sum = first + second + third
product = first * second * third

print("The sum of the three integers is:", sum)
print("The product of the three integers is:", product)


time.sleep(delayBetweenExercises)
# 4.
for i in range(7, 28, 4):
    print(i)


time.sleep(delayBetweenExercises)
# 5.
for i in range(1000, -1, -1):
    if (i % 3 == 0 or i % 5 == 0) and i % 15 != 0:
        print(i)


time.sleep(delayBetweenExercises)
# 6.
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if len(word1) > len(word2):
    print(word1 + " is longer than " + word2)
elif len(word1) < len(word2):
    print(word2 + " is longer than " + word1)
else:
    print("Both words are of equal length")
