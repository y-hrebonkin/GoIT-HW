def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {"JP": [], "SG": [], "TW": [], "UA": []}
    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.startswith("81"):
            phone_dict["JP"].append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            phone_dict["SG"].append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            phone_dict["TW"].append(sanitized_phone)
        elif sanitized_phone.startswith("380"):
            phone_dict["UA"].append(sanitized_phone)
        else:
            phone_dict["UA"].append(sanitized_phone)
    return phone_dict