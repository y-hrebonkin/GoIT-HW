import os
import shutil
import zipfile
import tarfile
import gzip

# Розширення файлів для кожного типу
extensions = {
    'images': ('.JPEG', '.PNG', '.JPG', '.SVG'),
    'videos': ('.AVI', '.MP4', '.MOV', '.MKV'),
    'documents': ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX', '.CSV'),
    'torrents': ('.TORRENT'),
    'audio': ('.MP3', '.OGG', '.WAV', '.AMR', '.FLAC', '.M4A'),
    'executables': ('.EXE'),
    'ssh-keys': ('.KEY'),
    'archives': ('.ZIP', '.GZ', '.TAR')
}

def normalize(filename):
    # Транслітерація кирилічних символів
    translit = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'i', 'і': 'i',
        'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'YE', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'І': 'I',
        'Ї': 'YI', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
        'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ь': '', 'Ю': 'YU', 'Я': 'YA'
    }
    
    normalized = ''
    for char in filename:
        if char.isalpha():
            if char in translit:
                normalized += translit[char]
            else:
                normalized += char
        elif char.isdigit():
            normalized += char
        else:
            normalized += '_'
    
    return normalized.replace(' ', '_')


def process_folder(folder_path):
    files = os.listdir(folder_path)
    known_extensions = {}
    unknown_extensions = set()

    for file in files:
        item_path = os.path.join(folder_path, file)
        if os.path.isdir(item_path):
            # Ігноруємо папки archives, videos, audio, documents, images, torrents, ssh-keys, executables
            if file.lower() not in ['archives', 'videos', 'audio', 'documents', 'images', 'torrents', 'ssh-keys', 'executables']:
                known, unknown = process_folder(item_path)
                for ext, count in known.items():
                    known_extensions[ext] = known_extensions.get(ext, 0) + count
                unknown_extensions.update(unknown)
                normalized_item = normalize(file)
                new_folder_path = os.path.join(folder_path, normalized_item)
                shutil.move(item_path, new_folder_path)
                if not os.listdir(new_folder_path):
                    os.rmdir(new_folder_path)
        else:
            _, item_extension = os.path.splitext(file)
            item_extension = item_extension.upper()

            known_category = False
            for category, exts in extensions.items():
                if item_extension in exts:
                    known_category = True
                    known_extensions[item_extension] = known_extensions.get(item_extension, 0) + 1
                    target_folder = os.path.join(folder_path, category)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    new_file_name = normalize(file[:file.rfind('.')]) + item_extension
                    new_file_path = os.path.join(target_folder, new_file_name)
                    shutil.move(item_path, new_file_path)
                    break

            if not known_category:
                unknown_extensions.add(item_extension)

            # Перенесення розпакованого вмісту архіву до папки archives
            if item_extension == '.ZIP':
                archive_folder_name = os.path.splitext(file)[0]
                archive_folder_name_normalized = normalize(archive_folder_name)
                archive_folder_path = os.path.join(folder_path, 'archives', archive_folder_name_normalized)
                if not os.path.exists(archive_folder_path):
                    os.makedirs(archive_folder_path)
                with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                    zip_ref.extractall(archive_folder_path)
                os.remove(new_file_path)
            elif item_extension == '.GZ':
                archive_folder_name = os.path.splitext(file)[0]
                archive_folder_name_normalized = normalize(archive_folder_name)
                archive_folder_path = os.path.join(folder_path, 'archives', archive_folder_name_normalized)
                if not os.path.exists(archive_folder_path):
                    os.makedirs(archive_folder_path)
                with gzip.open(new_file_path, 'rb') as gz_ref:
                    with open(os.path.join(archive_folder_path, archive_folder_name_normalized), 'wb') as output_file:
                        shutil.copyfileobj(gz_ref, output_file)
                os.remove(new_file_path)
            elif item_extension == '.TAR':
                archive_folder_name = os.path.splitext(file)[0]
                archive_folder_name_normalized = normalize(archive_folder_name)
                archive_folder_path = os.path.join(folder_path, 'archives', archive_folder_name_normalized)
                if not os.path.exists(archive_folder_path):
                    os.makedirs(archive_folder_path)
                with tarfile.open(new_file_path, 'r') as tar_ref:
                    tar_ref.extractall(archive_folder_path)
                os.remove(new_file_path)

    return known_extensions, unknown_extensions

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: python script.py folder_path')
    else:
        folder_path = sys.argv[1]
        known_extensions, unknown_extensions = process_folder(folder_path)
        print('Known Extensions:')
        for ext, count in known_extensions.items():
            print(f'{ext}: {count}')
        print('Unknown Extensions:')
        for ext in unknown_extensions:
            print(ext)
