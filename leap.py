num=int(input("enter a year"));
if (num%4==0):
    if(num%100==0):
        if(num%400==0):
            print("number is leap year")
        else:
            print("number is not a leap year")
    else:
            print("number is not a leap year")
else:
            print("number is not a leap year")
