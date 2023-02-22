"""
The algorithm for determining leap years is:
If the year is divisible by 4, it could be a leap year.
If the year is divisible by 100, it is not a leap year, unless it is also divisible by 400.
If the year is divisible by 400, it is a leap year.

"""

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")