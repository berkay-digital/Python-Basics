from datetime import datetime


name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old.")
print("Your age in binary is: {:b}".format(age))


try:
    sum_of_numbers = 0
    with open("example1.txt", "r") as f:
        file = f.read()
        print(file)
        lines = file.split("\n")
        number_list = []
        for i in range(3):
            number_list.append(int(lines[i]))
        sum_of_numbers = sum(number_list)
    print(sum_of_numbers)
    with open("example1.txt", "a") as f:
        f.write("\n")
        f.write(str(sum_of_numbers))
except ValueError:
    print("File contains non-numeric data.")
except FileNotFoundError:
    print("File not found.")
except:
    print("An error occurred.")


with open("example1.txt", "r") as f:
    file = f.read()
    line_count = len(file.split("\n"))
    print(f"Number of lines: {line_count}")
    three_char = file[:3]
    print(f"First three characters: {three_char}")
    try:
        with open("example2.txt", "x") as f:
            f.write(str(line_count))
            f.write("\n")
            f.write(three_char)
    except:
        print("File already exists.")


current_date = datetime.now()
current_time = current_date.strftime("%H:%M:%S")
print(f"Current Month: {current_date.month}")
print(f"Current Month Name: {current_date.strftime('%B')}")
print(f"Current Day: {current_date.day}")


def example_func():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        division = num1 / num2
        print(f"{num1} divided by {num2} is {division}.")
    except ValueError:
        print("Invalid input.")
        example_func()
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        example_func()


example_func()


def password_check():
    try:
        password = input("Enter a password: ")
        if len(password) < 8:
            raise Exception("Password must be at least 8 characters.")
        elif len(password) > 12:
            raise Exception("Password must be less than 12 characters.")
        elif not any(char.isupper() for char in password):
            raise Exception("Password must contain at least one uppercase letter.")
        print("Password is valid.")
    except Exception as e:
        print(e)
        password_check()


password_check()
