hey = "Hello World"
print(f"Hey: {hey}")


my_input = input("Enter smthng")
print(f"Your input: {my_input}")

'''
file = open("test.txt", "w")
file.write("Hello World")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

file = open("test.txt", "a")
file.write("\nHello World")
file.close()
'''

try:
    print("This happens no matter what")

except:
    print("This happens if error")

else:
    print("This happens if no error")

finally:
    print("This happens no matter what")
