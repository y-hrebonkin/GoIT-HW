def write_employees_to_file(employee_list, path):
    with open(path, "w") as f:
        for department in employee_list:
            for employee in department:
                f.write(employee + "\n")
        f.close()