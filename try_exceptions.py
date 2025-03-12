class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
    def get_details(self):
        return f"Invalid age: {self.age}. Details: {self.message}"

# Define the validation function
def validate_age(age):
    if (age < 0):
        raise InvalidAgeError(age, "Age cannot be negative!")
    if  (age >= 120):
         raise InvalidAgeError(age, "Age cannot be greater than 120")
    # if (0<= age<=120):
    return (age)                        #this is a typically useful when using validated age to calculate new age:: eg: validated_age = validate(age)
                                        #this is a design choice and comes in handy when the validated age need to be used further in the program

# Usage
try:
    validate_age(-10)
except InvalidAgeError as e:
    print(e.get_details())  # Output: Invalid age: -10. Details: Age cannot be negative!
else:
    print("The age is valid")


# More examples
try:
    validate_age(150)  # Too high
except InvalidAgeError as e:
    print(e.get_details())
else:
    print("The age is valid")

try:
    validate_age(25)  # This will work fine
except InvalidAgeError as e:
    print(e.get_details())
else:
    print("The age is valid")