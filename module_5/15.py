import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"https?://(?:[_a-zA-Z]+\.)+[_a-zA-Z]+", text)
    for match in iterator:
        result.append(match.group())
    return result