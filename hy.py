# take input from user month and day

date = int(input("ENTER THE DAY : "))

month = int(input("ENTER THE MONTH : "))

if month < 1 and month > 12:

    print("WRONG INPUT")

elif month >= 3 and month <= 4:

    if month == 3 and date >= 3:

        print(date, "/", month, " is SPRING SEASON")

    elif month == 3 and date < 3:

        print(date, "/", month, " is WINTER SEASON")

    else:

        print(date, "/", month, " is SPRING SEASON")



elif month <= 2 and month >= 11:

    print(date, "/", month, " is WINTER SEASON")

elif month >= 5 and month <= 8:

    if month == 5 and date >= 5:

        print(date, "/", month, " is SUMMER SEASON")

    elif month == 5 and date < 5:

        print(date, "/", month, " is SPRING SEASON")

    else:

        print(date, "/", month, " is SUMMER SEASON")

elif month >= 9 and month <= 10:

    if month == 9 and date >= 5:

        print(date, "/", month, " is RAINY SEASON")

    elif month == 9 and date < 5:

        print(date, "/", month, " is SUMMER SEASON")

    else:

        print(date, "/", month, " is RAINY SEASON")