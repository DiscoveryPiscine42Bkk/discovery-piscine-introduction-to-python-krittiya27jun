#!/usr/bin/env python3
import sys

def main():
    count = len(sys.argv) - 1  # ลบ 1 เพราะ argv[0] คือชื่อไฟล์
    print(f"Number of parameters: {count}.")

if __name__ == "__main__":
    main()
