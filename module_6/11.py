def get_credentials_users(path):
    with open(path, 'rb') as f:
        lines = [line.decode().strip() for line in f]
    return lines