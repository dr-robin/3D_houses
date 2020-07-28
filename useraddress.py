def get_address(house_number, street_name, city, postcode):
    return house_number + ', ' + street_name + ', ' + city + ', ' + postcode

house_number = str(input('Enter house number: '))
street_name = str(input('Enter street name: '))
city = str(input('Enter city: '))
postcode = str(input('Enter postcode: '))
address = get_address(house_number, street_name, city, postcode)
print('Your address is {}'.format(address))
