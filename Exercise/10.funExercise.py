#switch case statement
#in python match statement
def return_day(num):
    match num:#num == 1
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")


if __name__ == '__main__':
    num = int(input("Enter num: "))
    return_day(num)