class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    return "Age is valid"

try:
    print(check_age(16))
except InvalidAgeError as e:
    print("Error:", e)
