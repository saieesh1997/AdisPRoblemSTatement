
# functions

# function for additon
def add(x, y):
    return x + y


# function for subtraction
def sub(x,y):
    return x-y

# function for multiplication
def mul(x,y):
    return x*y

# function for division
def div(x,y):
    if(y==0):
        print("number cannot be divided by zero")
    else:
        return x/y

def sqr(x):
    return x * x


print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Square")

while True:
    # getting the input from users
    choice = input("Enter choice(1/2/3/4): ")

    # choice to check 4 options
    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Addition of two numbers", "=", add(num1, num2))

        if choice == '2':
            print("subtraction of two numbers", "=", sub(num1, num2))

        if choice == '3':
            print("Multiplication of two numbers","=",mul(num1,num2))

        if choice == '4':
            print("Division of two numbers", "=",div(num1,num2))

        if choice == '5':
            print("Square of the number",sqr(num1))


    else:
        print("invalid input")


