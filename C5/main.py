def sum_of_three(a, b, c):
    return a + b + c

print(sum_of_three(1, 2, 3))


def sum_of_digits(number):
    return sum([int(i) for i in str(number)])

print(sum_of_digits(10200003))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


def if_in_range(number, min, max):
    return number > min and number < max

print(if_in_range(5, 1, 10))