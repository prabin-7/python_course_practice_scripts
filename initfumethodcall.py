class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        # Forgot to call super().__init__()
        # super().__init__(self.message)                #only by writing this proper initialization of base exception occurs, behaves expectedly while raisin or printing

try:
    raise InvalidAgeError(25, "Invalid age!")
except InvalidAgeError as e:
    print(e)  # Output: InvalidAgeError (no message displayed)