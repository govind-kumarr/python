# Tuple

subjects: tuple[str, str, str] = ("Maths", "Science", "History")


print(f"No. of Subjects: {len(subjects)}")


for subject in subjects:
    print(f"Louis is signing in for{subject}")


print(subjects[1])

addl_subjects = ("English", "Python", "Java")

total_subjects = subjects + addl_subjects

print(total_subjects)


if "Python" in total_subjects:
    print(f"Louis is learning Python")
else:
    print(f"Louins is not learning Python")
