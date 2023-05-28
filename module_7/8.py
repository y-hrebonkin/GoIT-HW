def token_parser(s):
    tokens = []
    current_token = ''
    for char in s:
        if char in ['+', '-', '*', '/', '(', ')']:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char.isdigit():
            current_token += char
        elif char == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ''
        else:
            raise ValueError('Invalid character: {}'.format(char))
    if current_token:
        tokens.append(current_token)
    return tokens
    