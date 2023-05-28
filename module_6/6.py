def get_recipe(path, search_id):
    with open(path, "r") as file:
        for line in file:
            recipe = line.strip().split(",")
            if recipe[0] == search_id:
                return {
                    "id": recipe[0],
                    "name": recipe[1],
                    "ingredients": recipe[2:]
                }
            