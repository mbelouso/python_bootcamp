# Program to use assess large numbers for primality testing
# and also figure out the largest prime factor for an inputed number

# This script can be run from the command line with a number as an argument
# Example: python3 prime_test.py 13195

import sys
from PrimeFunctions import is_prime, largest_prime_factor

# Main function to handle user input and output results

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 PrimalityTest.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        largest_factor = largest_prime_factor(number)
        if largest_factor is not None:
            print(f"The largest prime factor of {number} is {largest_factor}.")
        else:
            print("No prime factors found.")

if __name__ == "__main__":
    main()



