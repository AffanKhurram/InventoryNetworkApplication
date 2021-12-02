import pickle

def sorted(sort_by):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        items = [tuple(line.split(',')) for line in lines]
        items.sort(key=lambda x: x[sort_by])
        return items

def create_string(arr):
    s = ''
    
    for name, amount, date in arr:
        s += name + ',' + amount + ',' + date + ';'

    if len(s) > 0:
        s = s[:-1]
    return s

# items = sorted(0)
# items = [','.join(x) for x in items]
# print(pickle.loads(pickle.dumps(items)))