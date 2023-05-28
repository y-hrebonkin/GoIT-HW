def sanitize_phone_number(phone):
    return ''.join(filter(str.isdigit, phone.strip('()-+ ')))