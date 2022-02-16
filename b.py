"""
Question_2. Distance between two cities(in km) is input through the keyboard. Write a program to convert and print this distnace in meters, feet, inches and centimeters.

"""

dist = int(input("Enter the distance "))
print('Distance in meters ', dist * 1000)
print('Distance in centi-meters ', dist * 100000)
print('Distance in feet ', dist * 100000 / 30.48)
print('Distance in inches ', dist * 100000 / 2.54)
