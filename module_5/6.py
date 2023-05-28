def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    for word in spam_words:
        if space_around:
            if f' {word} ' in f' {text} ' or f' {word}.' in f' {text} ':
                return True
        else:
            if word in text:
                return True
    return False

print(is_spam_words('Молох бог ужасен.', ['лох']))       