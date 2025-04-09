# Exception Handling Exercises

# 1. ZeroDivisionError Handling
def zero_division_error():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 2. ValueError Handling
def value_error():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Error: Invalid input, not a valid integer.")

# 3. FileNotFoundError Handling
def file_not_found_error():
    try:
        with open("non_existing_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found.")

# 4. TypeError Handling
def type_error():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = int(num1) + int(num2)
        print(result)
    except TypeError:
        print("Error: Inputs must be numerical.")

# 5. PermissionError Handling
def permission_error():
    try:
        with open("restricted_file.txt", "r") as file:
            content = file.read()
    except PermissionError:
        print("Error: Permission denied.")

# 6. IndexError Handling
def index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Index out of range
    except IndexError:
        print("Error: Index out of range.")

# 7. KeyboardInterrupt Handling
def keyboard_interrupt():
    try:
        number = int(input("Enter a number: "))
    except KeyboardInterrupt:
        print("\nError: Input interrupted by user.")

# 8. ArithmeticError Handling
def arithmetic_error():
    try:
        result = 1 / 0  # Arithmetic operation causing error
    except ArithmeticError:
        print("Error: Arithmetic error occurred.")

# 9. UnicodeDecodeError Handling
def unicode_decode_error():
    try:
        with open("non_utf_file.txt", "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        print("Error: Unicode decoding error.")

# 10. AttributeError Handling
def attribute_error():
    try:
        my_list = [1, 2, 3]
        my_list.add(4)  # 'add' is not a valid method for a list
    except AttributeError:
        print("Error: 'list' object has no attribute 'add'.")

# File Input/Output Exercises

# 1. Read an entire text file
def read_file():
    try:
        with open("sample.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")

# 2. Read first n lines of a file
def read_n_lines(n):
    try:
        with open("sample.txt", "r") as file:
            lines = [next(file) for _ in range(n)]
            print("".join(lines))
    except FileNotFoundError:
        print("Error: File not found.")

# 3. Append text to a file
def append_to_file():
    try:
        with open("sample.txt", "a") as file:
            file.write("This is a new line of text.\n")
        print("Text appended successfully.")
    except FileNotFoundError:
        print("Error: File not found.")

# 4. Read last n lines of a file
def read_last_n_lines(n):
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
            print("".join(lines[-n:]))
    except FileNotFoundError:
        print("Error: File not found.")

# 5. Read file line by line and store it into a list
def read_lines_into_list():
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
            print(lines)
    except FileNotFoundError:
        print("Error: File not found.")

# 6. Read file line by line and store it into a variable
def read_lines_into_variable():
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

# 7. Read file line by line and store it into an array (list)
def read_lines_into_array():
    try:
        with open("sample.txt", "r") as file:
            lines = [line.strip() for line in file]
            print(lines)
    except FileNotFoundError:
        print("Error: File not found.")

# 8. Find the longest word in the file
def longest_word():
    try:
        with open("sample.txt", "r") as file:
            words = file.read().split()
            longest = max(words, key=len)
            print(f"Longest word: {longest}")
    except FileNotFoundError:
        print("Error: File not found.")

# 9. Count the number of lines in a text file
def count_lines():
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
            print(f"Number of lines: {len(lines)}")
    except FileNotFoundError:
        print("Error: File not found.")

# 10. Count the frequency of words in a file
def word_frequency():
    try:
        with open("sample.txt", "r") as file:
            words = file.read().split()
            word_count = {word: words.count(word) for word in words}
            print(word_count)
    except FileNotFoundError:
        print("Error: File not found.")

# 11. Get the file size of a plain file
def get_file_size():
    try:
        import os
        size = os.path.getsize("sample.txt")
        print(f"File size: {size} bytes")
    except FileNotFoundError:
        print("Error: File not found.")

# 12. Write a list to a file
def write_list_to_file():
    try:
        my_list = ["Apple", "Banana", "Cherry"]
        with open("fruits.txt", "w") as file:
            for item in my_list:
                file.write(f"{item}\n")
        print("List written to file successfully.")
    except FileNotFoundError:
        print("Error: File not found.")

# 13. Copy contents of a file to another file
def copy_file_contents():
    try:
        with open("source.txt", "r") as file1:
            content = file1.read()
        with open("destination.txt", "w") as file2:
            file2.write(content)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: File not found.")

# 14. Combine each line from the first file with the corresponding line in the second file
def combine_files():
    try:
        with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            combined = [f"{l1.strip()} {l2.strip()}\n" for l1, l2 in zip(lines1, lines2)]
            with open("combined.txt", "w") as output:
                output.writelines(combined)
            print("Files combined successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")

# 15. Read a random line from a file
import random
def random_line():
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
            print(random.choice(lines))
    except FileNotFoundError:
        print("Error: File not found.")

# 16. Assess if a file is closed or not
def is_file_closed():
    try:
        with open("sample.txt", "r") as file:
            print(f"Is the file closed? {file.closed}")
    except FileNotFoundError:
        print("Error: File not found.")

# 17. Remove newline characters from a file
def remove_newlines():
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
        with open("sample_no_newlines.txt", "w") as file:
            for line in lines:
                file.write(line.strip() + " ")
        print("Newlines removed and saved to new file.")
    except FileNotFoundError:
        print("Error: File not found.")

# 18. Count the number of words in a text file
def count_words():
    try:
        with open("sample.txt", "r") as file:
            words = file.read().replace(',', '').split()
            print(f"Word count: {len(words)}")
    except FileNotFoundError:
        print("Error: File not found.")

# 19. Extract characters from various text files and put them into a list
def extract_characters():
    try:
        characters = []
        with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2:
            characters.extend(file1.read())
            characters.extend(file2.read())
        print(characters)
    except FileNotFoundError:
        print("Error: File not found.")

# 20. Generate 26 text files named A.txt, B.txt, ..., Z.txt
def generate_text_files():
    for i in range(26):
        with open(f"{chr(65+i)}.txt", "w") as file:
            file.write(f"This is file {chr(65+i)}.")
    print("Generated 26 text files.")

# 21. Create a file where all letters of the English alphabet are listed
def alphabet_file():
    with open("alphabet.txt", "w") as file:
        for i in range(65, 91):
            file.write(chr(i) + ' ')
    print("Alphabet written to file.")

