from clean_folder.clean import process_folder

def main():
    import sys

    if len(sys.argv) != 2:
        print('Usage: clean-folder folder_path')
    else:
        folder_path = sys.argv[1]
        known_extensions, unknown_extensions = process_folder(folder_path)
        print('Known Extensions:')
        for ext, count in known_extensions.items():
            print(f'{ext}: {count}')
        print('Unknown Extensions:')
        for ext in unknown_extensions:
            print(ext)

if __name__ == '__main__':
    main()
