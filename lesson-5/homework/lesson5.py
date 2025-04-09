# 1
def sort_dictionary_by_value():
    my_dict = {1: 10, 2: 20, 3: 15, 4: 5}
    sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    print(f"Dictionary sorted by value (ascending): {sorted_dict_asc}")
    sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    print(f"Dictionary sorted by value (descending): {sorted_dict_desc}")

# 2
def add_key_to_dict():
    sample_dict = {0: 10, 1: 20}
    sample_dict[2] = 30
    print(f"Dictionary after adding a new key: {sample_dict}")

# 3
def concatenate_dictionaries():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    concatenated_dict = {**dic1, **dic2, **dic3}
    print(f"Concatenated dictionary: {concatenated_dict}")

# 4
def generate_square_dict(n):
    square_dict = {x: x**2 for x in range(1, n+1)}
    print(f"Dictionary with squares (1 to {n}): {square_dict}")

# 5
def dictionary_of_squares():
    square_dict = {x: x**2 for x in range(1, 16)}
    print(f"Dictionary of squares from 1 to 15: {square_dict}")

# Set Exercises

# 1
def create_set():
    my_set = {1, 2, 3, 4, 5}
    print(f"Created set: {my_set}")

# 2
def iterate_over_set():
    my_set = {1, 2, 3, 4, 5}
    print("Iterating over set:")
    for item in my_set:
        print(item, end=' ')
    print()  

# 3
def add_members_to_set():
    my_set = {1, 2, 3}
    my_set.add(4)
    my_set.update([5, 6])
    print(f"Set after adding members: {my_set}")

# 4
def remove_items_from_set():
    my_set = {1, 2, 3, 4, 5}
    my_set.discard(3)
    my_set.remove(4)
    print(f"Set after removing items: {my_set}")

# 5
def remove_item_if_present():
    my_set = {1, 2, 3, 4, 5}
    item_to_remove = 2
    if item_to_remove in my_set:
        my_set.remove(item_to_remove)
    print(f"Set after conditionally removing item: {my_set}")

