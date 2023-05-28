def save_credentials_users(path, users_info):
    with open(path, 'wb') as f:
        for username, password in users_info.items():
            line = f"{username}:{password}\n".encode('utf-8')
            f.write(line)