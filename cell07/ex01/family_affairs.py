#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # ใช้ filter เพื่อกรอง key ที่ value เป็น 'red'
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    return list(redheads)

# ตัวอย่างข้อมูล
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# เรียกใช้เมทอดแล้วแสดงผล
print(find_the_redheads(dupont_family))
