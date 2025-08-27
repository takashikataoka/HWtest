#!/usr/bin/env python3
import sys
import argparse

def multiply(a, b, c):
    return a * b * c

def main():
    parser = argparse.ArgumentParser(description='Multiply three numbers')
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('num2', type=float, help='Second number')
    parser.add_argument('num3', type=float, help='Third number')
    
    args = parser.parse_args()
    
    result = multiply(args.num1, args.num2, args.num3)
    print(f"{args.num1} × {args.num2} × {args.num3} = {result}")

if __name__ == "__main__":
    main()