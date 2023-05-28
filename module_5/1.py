def real_len(text):
    control_chars = ['\n', '\f', '\r', '\t', '\v']
    return len([char for char in text if char not in control_chars])