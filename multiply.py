#!/usr/bin/env python3
import sys
import argparse

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def main():
    parser = argparse.ArgumentParser(description='Multiply any number of numbers')
    parser.add_argument('numbers', type=float, nargs='+', help='Numbers to multiply')
    
    args = parser.parse_args()
    
    result = multiply(*args.numbers)
    multiplication_string = ' × '.join(str(num) for num in args.numbers)
    print(f"{multiplication_string} = {result}")

if __name__ == "__main__":
    main()