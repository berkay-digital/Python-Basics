import time

# If you don't want to install pyfiglet (ASCII text), comment out the following lines or just delete them
from pyfiglet import Figlet
def print_cool(text):
    cool_text = Figlet(font='slant')
    return str(cool_text.renderText(text))

# And uncomment the following line
#def print_cool(text):
#  return text

# Example 1
print(print_cool('Example 1'))
def sum_of_three(a, b, c):
    return a + b + c, a, b, c


print(sum_of_three(1, 2, 3))
print(sum_of_three(1, 55, 3))
print(sum_of_three(1, 2, 333))
time.sleep(3)
# Example 2
print(print_cool('Example 2'))
def abs_num(num):
    abs_num = 0
    if num >= 0:
        abs_num = num
    elif num < 0:
        abs_num = -num
    return abs_num


def max_abs(a, b, c, d):
    max_num = a
    for num in [b, c, d]:
        if abs_num(num) > abs_num(max_num):
            max_num = num
    return max_num


print(max_abs(1, 2, 3, 4))
print(max_abs(1, 22, -3, 4))
print(max_abs(1, 2, 3, -4))
time.sleep(3)
# Example 3
print(print_cool('Example 3'))
def biggest_power_of_2(num):
    if not type(num) == int and not type(num) == float:
        return "Parameter is not a number."
    if num <= 0:
        return "Parameter is not a positive number."
    power = 0
    while 2 ** power <= num:
        power += 1
    return 2 ** (power - 1)


print(biggest_power_of_2(10))
print(biggest_power_of_2(1024))
print(biggest_power_of_2(-5))
print(biggest_power_of_2("abc"))
time.sleep(3)
# Example 4
print(print_cool('Example 4'))
def return_first_b_digits(a, b):
    while a >= 10**b:
        a = a // 10
    return a


print(return_first_b_digits(123456, 3))
print(return_first_b_digits(123456, 5))
print(return_first_b_digits(123456, 6))
time.sleep(3)
# Example 5
print(print_cool('Example 5'))
def digit_multiplication(a):
    result = 1
    for digit in str(a):
        result = result * int(digit)
    return result


print(digit_multiplication(123))    
print(digit_multiplication(12345))
print(digit_multiplication(123456))