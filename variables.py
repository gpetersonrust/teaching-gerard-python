# String
# Global variable
name = "Alice"
# Integer
age = 20
# Float
height = 1.75
# Boolean
is_student = True
is_teacher = False
# List
subjects = ["Math", "Science", "English"]
# Tuple
grades = (90, 85, 95)

# Dictionary
person = {
    "name": "Gino",
    "age": 20,
    "height": 1.75,
    "is_student": True,
    "is_teacher": False,
    "subjects": ["Math", "Science", "English"],
    "grades": (90, 85, 95),
}


def print_variables(local_name):
    # This local_name is a local variable
    print(local_name)


print_variables("Bob")
print(name)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input(
                "Do you want to perform another calculation? (yes/no): "
            )
            if next_calculation.lower() != "yes":
                break
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    calculator()
