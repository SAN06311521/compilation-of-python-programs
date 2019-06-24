print("This program is used to determine weather the entered year is a leap year or not.")
yr = int(input("Enter the year to be checked: "))
if (yr%4) == 0 :
    if (yr%100) == 0 :
        if (yr%400) == 0 :
            print("{} is a leap year.".format(yr))
        else:
            print("{}  is not a leap year.".format(yr))
    else:
        print("{} is a leap year.".format(yr))
else:
    print("{} is not a leap year.".format(yr))
