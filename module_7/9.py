def all_sub_lists(data):
    sub_lists = []
    for i in range(len(data) + 1):
        for j in range(i + 1, len(data) + 1):
            sub = data[i:j]
            sub_lists.append(sub)
    sub_lists.sort(key=len)
    return [[]] + sub_lists