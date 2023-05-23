#largest number
def find_largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

if __name__ == '__main__':
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = int(input("Enter num3: "))
    largestNo = find_largest(num1,num2,num3)
    print("Largest No: ",largestNo)