
def sorted(sort_by):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        items = [tuple(line.split(',')) for line in lines]
        if sort_by != 1:
            items.sort(key=lambda x: x[sort_by])
        else:
            # if sorting by quantity, first turn parse it into integer
            items.sort(key=lambda x: int(x[sort_by]))
        print(items)
        return items

def create_string(arr):
    s = ''
    
    for name, amount, date in arr:
        s += name + ',' + amount + ',' + date + ';'

    if len(s) > 0:
        s = s[:-1]
    return s

def updated(name, newq):
    with open('inventory.txt', 'w+') as f:
        lines = f.read().split('\n')
        for line in lines:
            print(line)

# items = sorted(0)
# items = [','.join(x) for x in items]
# print(pickle.loads(pickle.dumps(items)))