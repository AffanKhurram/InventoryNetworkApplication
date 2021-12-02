import pickle

def sorted(sort_by):
    with open('inventory.txt', 'r') as f:
        lines = f.read().split('\n')
        items = [tuple(line.split(',')) for line in lines]
        items.sort(key=lambda x: x[sort_by])
        return items

# items = sorted(0)
# items = [','.join(x) for x in items]
# print(pickle.loads(pickle.dumps(items)))