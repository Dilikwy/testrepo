# Password Generator

import random

name = "Okwy"
number = "12345"
special_char = "!@#$%^&"

all_char = name + number + special_char

question = "yes"

#While loop
while question == "yes":
 password_length = 8
 password_count = 1

#For loop

for num in range(password_count):
 password= "".join(random.sample(all_char, password_length))
print(password)
