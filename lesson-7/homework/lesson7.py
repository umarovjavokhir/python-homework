# 1. is_prime(n) 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. digit_sum(k) 
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# 3. powers of two
def powers_of_two(n):
    result = []
    i = 1
    while i <= n:
        result.append(i)
        i *= 2
    return result

