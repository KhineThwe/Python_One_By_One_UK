def return_day(num):
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wednesday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")

if __name__ == '__main__':
    num = int(input("Enter num: "))
    return_day(num)