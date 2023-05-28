def read_employees_from_file(path):
    with open(path, 'r') as f:
        employees = f.readlines()
        f.close()
    return [employee.strip() for employee in employees]