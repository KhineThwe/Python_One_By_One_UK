#average
#total/n
def calculate_average(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    return average
    # print("Average value: ",average)

def main():
    numbers = [1,2,3,4,5]
    a=calculate_average(numbers)
    print("Average value:",a)

if __name__ == '__main__':
    main()
