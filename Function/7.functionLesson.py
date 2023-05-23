#fun return from function
def square(a):#6
    return a**2#36

def cube(b):
    return b**3

def num(number):
    if number == 1:
        return square(6)
    elif number == 2:
        return cube(6)

if __name__ == '__main__':
    # num = int(input("Enter num: "))
    # result = square(num)
    # print(result)
    # sq = num(1)#sq = square()
    # result = sq(10)
    # print(result)
    #
    # cu = num(2)
    # print(cu(4))
    result = num(1)
    print(result)

    result1 = num(2)
    print(result1)


