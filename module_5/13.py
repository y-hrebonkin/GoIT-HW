import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result

print(find_all_emails('My email is e.grebionkin@gmail.com and my second email is y.hrebonkin@protonmail.com'))