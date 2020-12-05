"""
# A Calculator for common AP Stats Problems
"""

__author__ = 'Michael Nycz'
__version__ = '1.0'


while 1:
    points = input("Enter the number of events: ")
    try:
        points = int(points)
        if points <=0:
            raise ValueError
    except ValueError:
        print("Please enter a integer number, greater than 0:")

    events_base = []

    for i in range(points):
        pass

