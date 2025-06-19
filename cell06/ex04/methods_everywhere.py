#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + 'Z' * (8 - len(text)))

def main():
    args = sys.argv[1:]
    if not args:
        print("none")
        return

    for word in args:
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)

if __name__ == "__main__":
    main()
