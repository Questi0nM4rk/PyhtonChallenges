salmple_dict = {
    "name": "Adi",
    "age": 16,
    "salary": 21000,
    "city": "Mumbai"
}

keys_to_del = ["name", "salary"]

for key in keys_to_del:
    salmple_dict.pop(key, None)

print(salmple_dict)
# output: {'age': 16, 'city': 'Mumbai'}