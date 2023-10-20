apple = True
if apple:
    print("I have an apple")
else:
    print("I don't have an apple")

if(1 != 2):
    print("1 is not equal to 2")
else:
    print("1 is equal to 2")

if(2 == 4):
    print("2 is equal to 4")
elif(2 == 2):
    print("2 is equal to 2")
else:
    print("None of the above is true")

print(True if 5 > 7 else False)

pancake = 0
while pancake < 5:
    print("I need to make pancakes")
    pancake += 1
    if pancake >= 5:
        break
#else:
#    print("I have enough pancakes")

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10, 2):
    print(i)

for _ in ["a", "b", "c"]:
    print("I don't care about the variable")

for i in range(200, 655):
    if(i%13 == 0):
        print(str(i) + " is divisible by 13")
    else:
        print(str(i) + " is not divisible by 13")
