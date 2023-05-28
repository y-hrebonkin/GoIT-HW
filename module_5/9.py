def formatted_numbers():
    formatted = []

    formatted.append("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))

    for i in range(16):
        num_i = '{0:d}'.format(i)
        num_x = '{0:x}'.format(i)
        num_b = '{0:b}'.format(i)
        el = "|{:<10}|{:^10}|{:>10}|".format(num_i, num_x, num_b)
        # print(el)
        formatted.append(el)

    return formatted

for el in formatted_numbers():
    print(el)
