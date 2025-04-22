name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)


birth_year = input('What is your birth year? ')
print(type(birth_year))             # This will be a string
age = 2025 - int(birth_year)
print(type(age))                    # This will be an integer
print(name + ' is ' + str(age) + ' years old.')