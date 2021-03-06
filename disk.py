def parse_inventory_item(keys):
    number, name, stock, replacement_fee, rental_fee = keys.split(',')
    return [number, name, int(stock), int(replacement_fee), int(rental_fee)]


def parse_history_item(keys):
    time, days_rented, deposit, profit = keys.split(',')
    return [time, days_rented, deposit, profit]


def open_file(file_name):
    with open(file_name) as file:
        keys = file.read()
        inventory = {}
        lines = keys.split('\n')[1:]
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
        keys = file.read()
        lines = keys.split('\n')[1:]
        st = ''
        for line in lines:
            st += '{}\n'.format(line)
        return st.lstrip()


def inventory_to_string(inventory):
    st = ''
    for key in inventory:
        item = inventory[key]
        st += '\n{},{},{},{},{}\n'.format(key, item['Name'], item['Stock'],
                                          item['Replacement_fee'],
                                          item['Daily_fee'])

    return st.rstrip()


def history_to_string(history):
    return '\n{},{},{},{}'.format(history['time'], history['days_rented'],
                                  history['deposit'], history['profit'])


def write_to_file_inv(inventory):
    with open('inventory.txt', 'w') as file:
        file.write(
            f'number,name,stock,replacement_fee,daily_fee{inventory_to_string(inventory)}'
        )


def write_to_file_history(history):
    with open('history.txt', 'a') as file:
        file.write(f'{history_to_string(history)}')
