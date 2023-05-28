def data_preparation(list_data):
    result = []
    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        result += sublist
    return sorted(result, reverse=True)