def is_leap_year(year):
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return False
    if (year % 4 == 0):
        return True
    return False

yr = int(input("Enter the year you want to check for leap year: "))
print(is_leap_year(yr))
