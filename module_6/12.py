import base64


def encode_data_to_base64(data):
    encoded_data = []
    for pair in data:
        username, password = pair.split(":")
        encoded_pair = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
        encoded_data.append(encoded_pair)
    return encoded_data