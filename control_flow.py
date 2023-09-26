
class info(Name):
    first_name = str(input('Enter your first name: '))
    middle_name = str(input('Enter your middle name: '))
    last_name = str(input('Enter your last name: '))
    dob = input('Enter your date of birth: ')
    age = int(input('Enter your age: '))
    gender = str(input('Enter your gender: '))
name = (first_name, middle_name, last_name)
print(name)