def get_cats_info(path):
    cats = []
    with open(path, 'r') as f:
        for line in f:
            data = line.strip().split(',')
            cat = {'id': data[0], 'name': data[1], 'age': data[2]}
            cats.append(cat)
    return cats