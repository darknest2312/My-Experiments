n = int(input("n: "))


def input_calc(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Fucntion To Print the Prime Numbers


def print_prime(n):
    for i in range(2, n):
        if input_calc(i):
            print(i)


print_prime(n)
