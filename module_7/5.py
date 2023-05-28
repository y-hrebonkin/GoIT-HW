def capital_text(s):
    result = ""
    capitalize_next = True
    for char in s:
        if capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        else:
            result += char
            if char in ['.', '!', '?']:
                capitalize_next = True
    return result
    