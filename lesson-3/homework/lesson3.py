# 1. Create and Access List Elements
def create_and_access_list():
    fruits = ['Apple', 'Banana', 'Cherry', 'Mango', 'Pineapple']
    print(f"Third fruit: {fruits[2]}")

# 2. Concatenate Two Lists
def concatenate_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_list = list1 + list2
    print(f"Concatenated list: {concatenated_list}")

# 3. Extract Elements from a List
def extract_elements_from_list():
    numbers = [10, 20, 30, 40, 50]
    first = numbers[0]
    middle = numbers[len(numbers) // 2]
    last = numbers[-1]
    new_list = [first, middle, last]
    print(f"Extracted elements: {new_list}")

# 4. Convert List to Tuple
def convert_list_to_tuple():
    movies = ['Inception', 'Interstellar', 'The Dark Knight', 'Dunkirk', 'Memento']
    movies_tuple = tuple(movies)
    print(f"Movies tuple: {movies_tuple}")

# 5. Check Element in a List
def check_element_in_list():
    cities = ['New York', 'Paris', 'London', 'Tokyo', 'Berlin']
    is_paris_in_list = 'Paris' in cities
    print(f"Is Paris in the list? {is_paris_in_list}")

# 6. Duplicate a List Without Using Loops
def duplicate_list():
    numbers = [1, 2, 3, 4, 5]
    duplicated_list = numbers * 2
    print(f"Duplicated list: {duplicated_list}")

# 7. Swap First and Last Elements of a List
def swap_first_and_last():
    numbers = [10, 20, 30, 40, 50]
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    print(f"List after swapping first and last elements: {numbers}")

# 8. Slice a Tuple
def slice_tuple():
    numbers_tuple = tuple(range(1, 11))
    sliced_tuple = numbers_tuple[3:8]
    print(f"Sliced tuple (index 3 to 7): {sliced_tuple}")

# 9. Count Occurrences in a List
def count_occurrences():
    colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
    blue_count = colors.count('blue')
    print(f"Occurrences of 'blue': {blue_count}")

# 10. Find the Index of an Element in a Tuple
def find_index_in_tuple():
    animals = ('dog', 'cat', 'lion', 'tiger', 'elephant')
    lion_index = animals.index('lion')
    print(f"Index of 'lion': {lion_index}")

# 11. Merge Two Tuples
def merge_tuples():
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    merged_tuple = tuple1 + tuple2
    print(f"Merged tuple: {merged_tuple}")

# 12. Find the Length of a List and Tuple
def find_length():
    sample_list = [1, 2, 3, 4]
    sample_tuple = (1, 2, 3, 4)
    list_length = len(sample_list)
    tuple_length = len(sample_tuple)
    print(f"Length of list: {list_length}, Length of tuple: {tuple_length}")

# 13. Convert Tuple to List
def convert_tuple_to_list():
    sample_tuple = (1, 2, 3, 4, 5)
    sample_list = list(sample_tuple)
    print(f"Converted list: {sample_list}")

# 14. Find Maximum and Minimum in a Tuple
def find_max_min_in_tuple():
    numbers_tuple = (10, 20, 30, 40, 50)
    max_value = max(numbers_tuple)
    min_value = min(numbers_tuple)
    print(f"Max value: {max_value}, Min value: {min_value}")

# 15. Reverse a Tuple
def reverse_tuple():
    words_tuple = ('apple', 'banana', 'cherry', 'date')
    reversed_tuple = words_tuple[::-1]
    print(f"Reversed tuple: {reversed_tuple}")



