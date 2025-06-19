#!/usr/bin/env python3

def add_one(param):
    param += 1  # เพิ่มค่าที่รับเข้ามา
    return param

# ส่วนของโปรแกรมหลัก
number = 5
print("Before:", number)

add_one(number)

print("After:", number)
