import re


def find_word(text, word):
    pattern = re.compile(word)
    match = pattern.search(text)
    if match:
        return {
            'result': True,
            'first_index': match.start(),
            'last_index': match.end(),
            'search_string': match.group(),
            'string': text
        }
    else:
        return {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }
    
print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))