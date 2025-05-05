import re
import time
from datetime import datetime, timedelta
import pytz

# 1. Age Calculator
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Calculate months and days
    months = today.month - birthdate.month if today.month >= birthdate.month else today.month - birthdate.month + 12
    days = (today - birthdate.replace(year=today.year, month=today.month)).days
    return age, months, days

# 2. Days Until Next Birthday
def days_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

# 3. Meeting Scheduler
def meeting_end_time(current_time_str, duration_hours, duration_minutes):
    current_time = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M')
    end_time = current_time + timedelta(hours=duration_hours, minutes=duration_minutes)
    return end_time

# 4. Timezone Converter
def convert_timezone(date_str, time_str, current_tz_str, target_tz_str):
    current_tz = pytz.timezone(current_tz_str)
    target_tz = pytz.timezone(target_tz_str)
    
    local_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
    local_time = current_tz.localize(local_time)
    target_time = local_time.astimezone(target_tz)
    
    return target_time

# 5. Countdown Timer
def countdown_timer(future_date_str):
    future_date = datetime.strptime(future_date_str, '%Y-%m-%d %H:%M')
    while True:
        now = datetime.now()
        remaining_time = future_date - now
        if remaining_time.total_seconds() <= 0:
            print("Countdown finished!")
            break
        print(f"Time remaining: {remaining_time}", end="\r")
        time.sleep(1)

# 6. Email Validator
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False

# 7. Phone Number Formatter
def format_phone_number(phone_number):
    return f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

# 8. Password Strength Checker
def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True

# 9. Word Finder
def find_word_occurrences(text, word):
    word_list = text.split()
    occurrences = [i for i, w in enumerate(word_list) if w.lower() == word.lower()]
    return occurrences

# 10. Date Extractor
def extract_dates(text):
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    return re.findall(pattern, text)

# Main Menu
def main():
    while True:
        print("\nSelect a task:")
        print("1. Age Calculator")
        print("2. Days Until Next Birthday")
        print("3. Meeting Scheduler")
        print("4. Timezone Converter")
        print("5. Countdown Timer")
        print("6. Email Validator")
        print("7. Phone Number Formatter")
        print("8. Password Strength Checker")
        print("9. Word Finder")
        print("10. Date Extractor")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
            age, months, days = calculate_age(birthdate)
            print(f"Age: {age} years, {months} months, {days} days")
        
        elif choice == '2':
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
            days_left = days_until_birthday(birthdate)
            print(f"Days until next birthday: {days_left}")
        
        elif choice == '3':
            current_time = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
            duration_hours = int(input("Enter meeting duration (hours): "))
            duration_minutes = int(input("Enter meeting duration (minutes): "))
            end_time = meeting_end_time(current_time, duration_hours, duration_minutes)
            print(f"The meeting will end at: {end_time}")
        
        elif choice == '4':
            date_str = input("Enter date (YYYY-MM-DD): ")
            time_str = input("Enter time (HH:MM): ")
            current_tz_str = input("Enter your timezone (e.g., 'US/Eastern'): ")
            target_tz_str = input("Enter target timezone (e.g., 'Europe/London'): ")
            converted_time = convert_timezone(date_str, time_str, current_tz_str, target_tz_str)
            print(f"Converted time: {converted_time}")
        
        elif choice == '5':
            future_date_str = input("Enter future date and time (YYYY-MM-DD HH:MM): ")
            countdown_timer(future_date_str)
        
        elif choice == '6':
            email = input("Enter an email address: ")
            if validate_email(email):
                print("Valid email address")
            else:
                print("Invalid email address")
        
        elif choice == '7':
            phone_number = input("Enter phone number (digits only): ")
            formatted_phone = format_phone_number(phone_number)
            print(f"Formatted phone number: {formatted_phone}")
        
        elif choice == '8':
            password = input("Enter a password: ")
            if check_password_strength(password):
                print("Password is strong")
            else:
                print("Password is weak")
        
        elif choice == '9':
            text = input("Enter a text: ")
            word = input("Enter a word to find: ")
            occurrences = find_word_occurrences(text, word)
            print(f"Occurrences of the word '{word}': {occurrences}")
        
        elif choice == '10':
            text = input("Enter a text: ")
            dates = extract_dates(text)
            print(f"Dates found: {dates}")
        
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
