# multiline strings
email = '''
Hi John,

This is our first email to you.

Thank you,
The support team
'''
print(email)

# Careful about symbols in strings (' '), (" ")
course = "Python's Course for beginners"
print(course)

course = 'python course for "beginners"'
print(course)

# Accessing characters of a string
print(course[0])  # first character
print(course[-2])  # second character from the end

# substrings
text = "Python programming"
substring = text[0:3]  # from 0 to 2
print(substring)  # Python

substring = text[0: ] # from 0 to end
substring = text[2: ] # from 2 to end
print(substring)  # thon programming

substring = text[ :3] # from start to 2
print(substring)  # Pyt

