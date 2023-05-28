def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()

    matching_names = [line.split()[0] for line in lines if profession in line]

    result = ' '.join(matching_names)
    return result


# result = get_employees_by_profession('employees.txt', 'cook')
# print(result)
