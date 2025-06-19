#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # ใช้ set เพื่อเก็บค่าใหม่ที่ไม่ซ้ำ
    new_set = set()

    for num in original_array:
        if num > 5:
            new_set.add(num + 2)

    print(original_array)
    print(new_set)

if __name__ == "__main__":
    main()
