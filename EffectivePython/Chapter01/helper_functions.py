my_values = {'red': ['5'], 'green': [''], 'blue': ['0']}

red = int(my_values.get('red', [''])[0] or 0)
print(red)

red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0
print(red)

green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0
print(green)


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


green = get_first_int(my_values, 'green')
print(green)
