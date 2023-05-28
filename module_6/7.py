def sanitize_file(source, output):
    
    with open(source, "r") as f:
                text = f.read()
    text_without_digits = ''.join(filter(lambda x: not x.isdigit(), text))
    with open(output, "w") as f:
        f.write(text_without_digits)
    