with open('data.txt','r') as file:
    content = file.readline()
    while content:
        print(content)
        content = file.readline()