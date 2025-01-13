#Using Variables in strings

# Variables declaration
car_make ="BMW"
car_model = "5er 2014"

# car F-string declarations
car= f"{car_make} {car_model}" #f strings F= format

# using car F-string variables in another F-string
my_message =f"Typhon drives a {car.upper()}"
my_bigger_message =f"{my_message} and he crashed it."

print (my_bigger_message)