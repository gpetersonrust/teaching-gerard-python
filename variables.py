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
