import numpy as np

# 1. Convert List to 1D Array
def list_to_1d_array():
    original_list = [12.23, 13.32, 100, 36.32]
    np_array = np.array(original_list)
    print("Original List:", original_list)
    print("One-dimensional NumPy array:", np_array)

# 2. Create 3x3 Matrix (2 to 10)
def create_3x3_matrix():
    matrix = np.arange(2, 11).reshape(3, 3)
    print("3x3 Matrix with values from 2 to 10:")
    print(matrix)

# 3. Null Vector (10) & Update Sixth Value
def update_null_vector():
    null_vector = np.zeros(10)
    print("Original Null Vector:", null_vector)
    null_vector[5] = 11
    print("Updated Null Vector with sixth value updated to 11:", null_vector)

# 4. Array from 12 to 38
def array_from_12_to_38():
    array = np.arange(12, 39)
    print("Array with values ranging from 12 to 38:")
    print(array)

# 5. Convert Array to Float Type
def convert_to_float():
    original_array = np.array([1, 2, 3, 4])
    print("Original array:", original_array)
    float_array = original_array.astype(float)
    print("Converted array to float type:", float_array)

# 6. Celsius to Fahrenheit Conversion
def celsius_to_fahrenheit():
    celsius = np.array([0, 12, 45.21, 34, 99.91])
    fahrenheit = (celsius * 9/5) + 32
    print("Values in Celsius degrees:", celsius)
    print("Values in Fahrenheit degrees:", fahrenheit)

# 7. Append Values to Array
def append_values_to_array():
    original_array = np.array([10, 20, 30])
    print("Original array:", original_array)
    appended_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
    print("After appending values to the array:", appended_array)

# 8. Array Statistical Functions (Self-study)
def array_statistical_functions():
    random_array = np.random.random(10)
    mean = np.mean(random_array)
    median = np.median(random_array)
    std_dev = np.std(random_array)
    print("Random Array:", random_array)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")

# 9. Find min and max
def find_min_max():
    random_matrix = np.random.random((10, 10))
    min_value = np.min(random_matrix)
    max_value = np.max(random_matrix)
    print("10x10 Array with random values:")
    print(random_matrix)
    print(f"Minimum Value: {min_value}, Maximum Value: {max_value}")

# 10. Create 3x3x3 Array with random values
def create_3x3x3_array():
    random_3d_array = np.random.random((3, 3, 3))
    print("3x3x3 Array with random values:")
    print(random_3d_array)

# Main function to execute all tasks
def main():
    list_to_1d_array()
    create_3x3_matrix()
    update_null_vector()
    array_from_12_to_38()
    convert_to_float()
    celsius_to_fahrenheit()
    append_values_to_array()
    array_statistical_functions()
    find_min_max()
    create_3x3x3_array()

if __name__ == "__main__":
    main()

