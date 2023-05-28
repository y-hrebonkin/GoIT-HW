grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    result = []
    for i, (name, grade) in enumerate(students.items(), start=1):
        result.append(f"{i:>{4}}|{name:<{10}}|{grade:^{5}}|{grades[grade]:^{5}}")
    return result