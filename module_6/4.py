def add_employee_to_file(record, path):
   with open(path, 'a') as f:
        if not record.endswith('\n'):
            record += '\n'
        f.write(record)
        f.close()