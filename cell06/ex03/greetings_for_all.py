#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# เรียกใช้งานตามตัวอย่าง
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
