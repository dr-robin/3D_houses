def get_address():
    return nb + ', ' + street + ', ' + city + ', ' + pc

address = get_address(nb, street, city, pc)
print('Your address is {}'.format(address))
