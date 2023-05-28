articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    if not letter_case:
        key = key.lower()
    result = []
    for article in articles_dict:
        if not letter_case:
            title = article['title'].lower()
            author = article['author'].lower()
        else:
            title = article['title']
            author = article['author']
        if key in title or key in author:
            result.append(article)
    return result