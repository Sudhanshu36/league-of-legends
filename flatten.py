test = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3], 'e':[{'x':1}, {'y':2}]}

def flatten_dict(d, parent_key = None):
    if parent_key is None:
        parent_key = ''
    items = []
    for k, v in d.items():
        try:
            if (type(v)==type([])): 
                for l in v: 
                    items.extend(flatten_dict(l, '%s%s_' % (parent_key, k)).items())
            else: 
                items.extend(flatten_dict(v).items())
        except AttributeError:
            items.append(('%s%s' % (parent_key, k), v))
    return dict(items)

print(flatten_dict(test))
