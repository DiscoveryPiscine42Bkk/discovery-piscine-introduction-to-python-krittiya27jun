#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
    else:
        print("What was the parameter?")
        user_input = input()
        if user_input == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")

if __name__ == "__main__":
    main()
