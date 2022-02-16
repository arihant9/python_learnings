"""
Question_3. Temperature of a city in Fahrenheit is input through the keyboard. Write a program to convert this temperature into centigrade degree.

"""



tempF = float(input("Enter the temperature in Farenheit "))

tempC= (tempF - 32) * 5 / 9

print("Temperature in Centi-grades ", tempC)
