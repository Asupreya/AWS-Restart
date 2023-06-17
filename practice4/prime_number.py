# pylint: disable=trailing-whitespace
''' Display all the prime numbers between 1 to 250 '''
import numpy as np

def check_is_prime(num):
    """ Check if num is prime number or not """
    if num in (0, 1):
        return False
    if num == 2:
        return True
    # Prime numbers are natural numbers that are divisible by only 1 and the number itself
    # so we exclude 1 and start at 2 and stop at half of num because numbers beyond half of num
    # are not divisible.
    for i in range(2, int(np.floor(num/2 + 1))):
        if num % i == 0:
            return False
    return True

def find_prime_number(num1, num2):
    """ find prime numbers between num1 and num2 """
    # num1 and num2 must greater than zero and num2 must greater than num1.
    if (num1 > 0 and num2 > 0) and (num2 > num1):   
        prime_list = []
        for i in range(num1, num2 + 1):
            if check_is_prime(i) is True:
                prime_list.append(i)
        print(f"Prime numbers between {num1} and {num2} are: ")
        print(prime_list)
    else:
        print("Your numbers is wrong please try again with the correct numbers")

find_prime_number(1, 500)
