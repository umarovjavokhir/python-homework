import threading
import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Worker function to check primes in a given range
def check_primes(start, end, result_list, lock):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    
    # Using lock to safely append results to the shared list
    with lock:
        result_list.extend(primes)

# Function to manage threaded prime checking
def threaded_prime_checker(start, end, num_threads):
    result_list = []
    lock = threading.Lock()
    thread_list = []
    
    # Calculate the range for each thread
    range_size = (end - start) // num_threads
    for i in range(num_threads):
        thread_start = start + i * range_size
        thread_end = start + (i + 1) * range_size if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, result_list, lock))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    return result_list

# Main Program
def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    num_threads = int(input("Enter the number of threads: "))

    prime_numbers = threaded_prime_checker(start, end, num_threads)
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")

if __name__ == "__main__":
    main()

