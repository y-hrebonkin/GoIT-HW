import re


def replace_spam_words(text, spam_words):
    pattern = re.compile('|'.join(spam_words), flags=re.IGNORECASE)
    result = pattern.sub(lambda match: '*' * len(match.group()), text)
    return result

print(replace_spam_words('Молох бог ужасен.', ['лох']))
    
        
    