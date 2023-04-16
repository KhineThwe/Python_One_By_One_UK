username = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
print("Welcome from {subject}".format(subject="Python"))#keyword argument

print("Welcome, {}".format(username))
print("Age: {0} , Gender: {1}".format(age,gender))
print(f"Bye Bye {username}")