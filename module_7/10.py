def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    else:
        request = dict(zip(keys, values))
        return request