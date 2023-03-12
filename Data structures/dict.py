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
