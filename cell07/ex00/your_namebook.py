#!/usr/bin/env python3

def array_of_names(name_dict):
    result = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result

# ตัวอย่างทดสอบ
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
