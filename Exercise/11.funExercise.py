def return_day(num):#num=2
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday"]
    #        0     , 1        ,2        ,3 ,4, 5,6,7
    if num>0 and num<8:
        return days[num-1]#days[2-1]#days[1]
    else:
        return "Invalid Number"




if __name__ == '__main__':
    num = int(input("Enter num: "))#1,2,3,---,7
    day = return_day(num)
    print("Day: ",day)