import random
import string

# 1. Age Calculator
def age_calculator():
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))
    current_year = 2025
    age = current_year - year_of_birth
    print(f"{name}, you are {age} years old.")

# 2. Extract Car Names from 'LMaasleitbtui'
def extract_car_names_1():
    txt = 'LMaasleitbtui'

    odd_chars = ''.join([txt[i] for i in range(len(txt)) if i % 2 == 0])  
    even_chars = ''.join([txt[i] for i in range(len(txt)) if i % 2 != 0])  
    
    print(f"Extracted characters from odd positions: {odd_chars}")
    print(f"Extracted characters from even positions: {even_chars}")

extract_car_names_1()


# 3. Extract Car Names from 'MsaatmiazD'
def extract_car_names_2():
    txt = 'MsaatmiazD'
    odd_chars = ''.join([txt[i] for i in range(len(txt)) if i % 2 == 0])  
    even_chars = ''.join([txt[i] for i in range(len(txt)) if i % 2 != 0])  
    
    print(f"Extracted characters from odd positions: {odd_chars}")
    print(f"Extracted characters from even positions: {even_chars}")


# 4. Extract Residence Area from "I'am John. I am from London"
def extract_residence_area():
    txt = "I'am John. I am from London"
    area = txt.split("from")[-1].strip()
    print(f"Extracted residence area: {area}")

# 5. Reverse String
def reverse_string():
    user_input = input("Enter a string to reverse: ")
    reversed_str = user_input[::-1]
    print(f"Reversed string: {reversed_str}")

# 6. Count Vowels
def count_vowels():
    text = input("Enter a string to count vowels: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    print(f"Number of vowels in the string: {count}")

# 7. Find Maximum Value
def find_max_value():
    numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    max_value = max(numbers)
    print(f"Maximum value in the list: {max_value}")

# 8. Check Palindrome
def check_palindrome():
    word = input("Enter a word to check if it is a palindrome: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome.")

# 9. Extract Email Domain
def extract_email_domain():
    email = input("Enter an email address: ")
    domain = email.split('@')[-1]
    print(f"Domain extracted from the email: {domain}")

# 10. Generate Random Password
def generate_random_password():
    password_length = int(input("Enter the desired password length: "))
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(password_length))
    print(f"Generated random password: {password}")

# Calling all functions one by one
age_calculator()
extract_car_names_1()
extract_car_names_2()
extract_residence_area()
reverse_string()
count_vowels()
find_max_value()
check_palindrome()
extract_email_domain()
generate_random_password()

