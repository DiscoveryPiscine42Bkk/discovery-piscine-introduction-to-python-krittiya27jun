#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    input_str = sys.argv[1]
    result = ""

    for char in input_str:
        if char == 'z':
            result += 'z'

    if result:
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()
