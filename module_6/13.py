import shutil


def create_backup(path, file_name, employee_residence):
    # Створюємо шлях до бінарного файлу, використовуючи символ /
    file_path = f"{path}/{file_name}"
    # Відкриваємо бінарний файл з ім'ям file_name у теку path
    with open(file_path, "wb") as file:
        # Записуємо вміст словника employee_residence у бінарний файл
        for key, value in employee_residence.items():
            # Кожен рядок кодуємо методом encode та додаємо перенесення рядка '\n'
            file.write(f"{key} {value}\n".encode())
    # Архівуємо теку по шляху path у форматі zip з ім'ям 'backup_folder'
    shutil.make_archive('backup_folder', 'zip', path)
    # Повертаємо рядок шляху до архіву 'backup_folder.zip'
    return f"{path}/backup_folder.zip"
        