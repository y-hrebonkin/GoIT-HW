def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file:
        lines = file.readlines()

    indexed_lines = [f'{i}: {line}' for i, line in enumerate(lines)]

    with open(output_file, 'w') as file:
        file.writelines(indexed_lines)