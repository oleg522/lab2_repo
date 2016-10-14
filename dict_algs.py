ivan = {
    'name': 'ivan',
    'age': 34,
    'children': [{
        'name': 'vasja',
        'age': 12,
    }, {
        'name': 'petja',
        'age': 10,
    }],
}

darja = {
    'name': 'darja',
    'age': 41,
    'children': [{
        'name': 'kirill',
        'age': 21,
    }, {
        'name': 'pavel',
        'age': 15,
    }],
}

emps = [ivan, darja]


def hasAdultChildren (x):
    n = []
    for person in x:
            for childen in person['children']:
                if childen['age'] >= 18:
                    n.append(person['name'])
    return n

print (hasAdultChildren(emps))