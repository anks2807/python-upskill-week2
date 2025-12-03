fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}, {fruit}")

person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruit_list = []
for index, fruit in enumerate(fruits, start=1):
    if index % 2 == 0:
        fruit_list.append((index, fruit))

print(fruit_list)
