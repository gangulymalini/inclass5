

print("Malini Ganguly - HW1")


#username = input("Enter year number: ")

def leapyeartest(username):
    if (username % 400) == 0 :
        print(username, " is a leap year")
    else:
        if (username % 100) == 0 :
            print(username, " is not a leap year")
        else:
            if (username % 4) == 0 :
                print(username, " is a leap year")
            else:
                print(username, " is not a leap year")