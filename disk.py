def parse_inventory_item(string):
    number, name, stock, replacement_fee, rental_fee = string.split(',')
    return [number, name, int(stock), int(replacement_fee), int(rental_fee)]


def parse_history_item(string):
    time, days_rented, deposit, profit = string.split(',')
    return [time, days_rented, deposit, profit]


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
                    'Name': d[1],
                    'Stock': d[2],
                    'Replacement_fee': d[3],
                    'Daily_fee': d[4]
                }
        return inventory


def open_file_history():
    with open('history.txt') as file:
        string = file.read()
        lines = string.split('\n')[1:]
        history = {}
        for line in lines:
            if line:
                d = parse_history_item(line)
                history[d[0]] = {
                    'Days Rented': d[1],
                    'Deposit': d[2],
                    'Profit': d[3]
                }
        return history


def inventory_to_string(inventory):
    st = ''
    for key in inventory:
        item = inventory[key]
        st += '\n{},{},{},{},{}\n'.format(key, item['Name'], item['Stock'],
                                          item['Replacement_fee'],
                                          item['Daily_fee'])

    return st.rstrip()


def history_to_string(history):
    st = ''
    for key in history:
        st += '\n{},{},{},{}\n'.format(key, history['Days Rented'],
                                       history['Deposit'], history['Profit'])
    return st.rstrip()


def write_to_file_inv(inventory):
    with open('inventory.txt', 'w') as file:
        file.write(
            f'number,name,stock,replacement_fee,daily_fee{inventory_to_string(inventory)}'
        )


def write_to_file_history(history):
    with open('history.txt', 'a') as file:
        file.write(f'{history_to_string(history)}')
