#!/usr/bin/env python3

def famous_births(people_dict):
    # แปลง dict เป็น list แล้ว sort ตาม date_of_birth
    sorted_people = sorted(people_dict.values(), key=lambda p: int(p["date_of_birth"]))
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# ตัวอย่างข้อมูล
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
