#!/usr/bin/env python3
import sys
import argparse

def multiply(a, b):
    return a * b

def main():
    parser = argparse.ArgumentParser(description='Multiply two numbers')
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('num2', type=float, help='Second number')
    
    args = parser.parse_args()
    
    result = multiply(args.num1, args.num2)
    print(f"{args.num1} × {args.num2} = {result}")

if __name__ == "__main__":
    main()