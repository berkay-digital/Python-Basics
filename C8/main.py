# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Modifying elements in a tuple is not allowed
# my_tuple[0] = 10  # Raises TypeError

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

# Creating a list
my_list = [1, 2, 3, 4, "Hello"]
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3

# Modifying elements in a list
my_list[0] = 10
my_list[0:2] = [10, 3]
print(my_list)  # Output: [10, 2, 3, 4, 5]

# List unpacking
a, b, c, d, e = my_list
print(a, b, c, d, e)  # Output: 10 2 3 4 5

# Looping through a list
for i in my_list:
    print(i)

# Looping through a tuple
for i in my_tuple:
    print(i)

# List methods
print(my_list[4][0])
print(my_list[0:2])
print(my_list[:])
print(my_list[1:])
print(my_list[:4])
print(my_list[::2])

# Reverse list
print(my_list[::-1])

# Append 6 to the list
my_list.append(6)
print(my_list)

# Insert 0 at index 0
my_list.insert(0, 0)
print(my_list)

# Extend list with another list
my_list.extend([7, 8, 9])
print(my_list)

# Remove element 0
my_list.remove(0)
print(my_list)

# Remove elment at index 2
my_list.pop(2)
print(my_list)

# Remove last element
my_list.pop()
print(my_list)

# Remove all elements
my_list.clear()
print(my_list)

# Delete list
del my_list
# print(my_list)  # Raises NameError

# List comprehension
my_list = [i for i in range(10)]
print(my_list)

# List comprehension with if statement
my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)

# List comprehension with if-else statement
my_list = [i if i % 2 == 0 else 0 for i in range(10)]
print(my_list)

# List comprehension with nested for loop
my_list = [(i, j) for i in range(3) for j in range(3)]
print(my_list)

# List comprehension with nested for loop and if statement
my_list = [(i, j) for i in range(3) for j in range(3) if i != j]
print(my_list)

# List comprehension with nested for loop and if-else statement
my_list = [(i, j) if i != j else 0 for i in range(3) for j in range(3)]
print(my_list)

# Looping through a list with index
for index_value in range(0, len(my_list)):
    if my_list[index_value] == 0:
        print("Found 0 at index " + str(index_value))

# Check if element is in list
print(0 in my_list)

# Check if element is not in list
print(0 not in my_list)

# Sort list
my_list = [3, 2, 1]
my_list.sort()
print(my_list)

# Sort list in reverse
my_list.sort(reverse=True)
print(my_list)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)