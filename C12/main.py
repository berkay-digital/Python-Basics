import time
from datetime import datetime
import numpy as np
from random import *
import os
import math

current_date = datetime.now()
current_time = current_date.strftime("%H:%M:%S")
print(f"Current Month: {current_date.month}")
print(f"Current Month Name: {current_date.strftime('%B')}")
print(f"Current Day: {current_date.day}")


def example_func():
    try:
        date = input("Enter a date. (YYYY/DD/MM)")
        date = datetime.strptime(date, "%Y/%d/%m")
        day_name_of_week = date.strftime("%A")
        print(f"Day of the week: {day_name_of_week}")
    except Exception as e:
        print(f"Error: {e}")
        example_func()


example_func()


answer = math.cos(math.degrees(32.2)) + math.log(10, 7) + uniform(3.2, 4.5)
print(answer)

answer2 = (
    math.pow(math.e, 2 * math.pi)
    + math.log(5, 2)
    + math.sin(math.degrees(abs(math.pow(2, 3) - math.pow(3, 2))))
)
print(answer2)

ans3 = math.sin(90 * math.pi / 180)
print(ans3)
