#ADD
def add(a, b):
    return a + b
#SUBTRACT
def subtract(a, b):
    return a - b
#MULTIPLY
def multiply(a, b):
    return a * b
#DIVIDE
def divide(a, b):
    return a / b
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
next_calculation= "yes"
while next_calculation !="no" and next_calculation !="n":

    # this is where the user decides which function to use
    choice = input("Enter your choice(1/2/3/4): ")

    # this will divide into two input options after they decide on the function
    # use the float incase they add a decimal number
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # if the answer is no the exercise finishes
        next_calculation = input("Would you like to do another equation? (yes/no): ")
