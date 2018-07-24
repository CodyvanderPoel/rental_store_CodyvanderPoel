def parse_inventory_item(string):
    name, stock, replacement_fee, rental_fee = string.split(',')
    return [name, int(stock), int(replacement_fee), int(rental_fee)]


def open_file(file_name):
    # with open(file_name) as file:
    #     contents = {file.readlines()}
    #     print(contents)
    #     return contents
    with open(file_name) as file:
        string = file.read()
        inventory = {}
        lines = string.split('\n')[1:]
        for line in lines:
            if line:
                d = parse_inventory_item(line)
                inventory[d[0]] = {
                    'Stock': d[1],
                    'Replacement Fee': d[2],
                    'Rental Fee': d[3]
                }
        return inventory


def which_file_to_open(choice):
    if choice == "U":
        inventory = open_file('inventory.txt')
        return inventory
    else:
        history = open_file('history.txt')
        stock = open_file('inventory.txt')
        return history, stock


def reduce_value(inventory):
    pass
