marks: dict = {"Math": 80, "Science": 79, "English": 90}

print(f"Marks: {marks}")

for subject in marks.keys():
    print(f"Louis got {marks[subject]}/100 in {subject}")


for score in marks.values():
    print(f"Marks: {score}")

for subject, value in marks.items():
    print(f"{subject}: {value}")

marks["English"] = 70

print(f"English: {marks['English']}")


# marks["Geography"] = 90
print(f"Geography: {marks.get('Geography')}")

print(f"typeof {type(marks.values())}")

# for deleting
del marks["English"]

print(f"{marks}")

# !Use the get method to print the value of the "model" key of the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(car.get("model"))

# Use the pop method to remove "model" from the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.pop("model")
print(car)


# Use the clear method to empty the car dictionary.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
car.clear()
print(car)
