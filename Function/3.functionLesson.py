#calculator
def add(num1,num2):#num1 = 5,num2 = 4
    result = num1 + num2
    return result

def subtract(num1,num2):
    result = num1 - num2
    return result

def multiply(num1,num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1/num2
    return result

def main():
    print("Calculator program!!!")
    total = 0
    first_no = int(input("Enter first number : "))#4
    second_no = int(input("Enter second number: "))#5
    option = int(input("Press 1 to add\nPress 2 to subtract\nPress 3 to multiply\nPress 4 to divide"))
    if option == 1:
        total = add(first_no,second_no)#add(5,4)
        # total = first_no + second_no
    elif option == 2:
        total = subtract(first_no,second_no)
        # total = first_no - second_no
    elif option == 3:
        total = multiply(first_no,second_no)
        # total = first_no * second_no
    elif option == 4:
        total = divide(first_no,second_no)
        # total = first_no/second_no
    print(f'Total number : {total}')

main()