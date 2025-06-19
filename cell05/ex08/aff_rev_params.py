#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]  # ตัดชื่อไฟล์ออก
    if len(args) < 2:
        print("none")
    else:
        for param in reversed(args):
            print(param)

if __name__ == "__main__":
    main()
