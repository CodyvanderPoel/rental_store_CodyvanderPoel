def parse_inventory_item(string):
    name, stock, replacement_fee, rental_fee = string.split(',')
    return [name, int(stock), int(replacement_fee), int(rental_fee)]


def which_file_to_open(choice):
    if choice == "U":
        inventory = open_file('inventory.txt')
        return inventory


def open_file(file_name):
    # This was my first attempt at this
    # with open(file_name) as file:
    #     contents = {file.readlines()}
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
                    'Replacement_fee': d[2],
                    'Rental_fee': d[3]
                }
        return inventory


def write_to_file():
    pass
