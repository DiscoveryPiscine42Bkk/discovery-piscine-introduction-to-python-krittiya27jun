#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]  # ไม่เอา index 0 เพราะมันคือชื่อไฟล์
    if not args:
        print("none")
    else:
        print(f"parameters: {len(args)}")
        for arg in args:
            print(f"{arg}: {len(arg)}")

if __name__ == "__main__":
    main()
