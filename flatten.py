test = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3], 'e':[{'x':1}, {'y':2}, {'x':2}], 'f': [1, 2]}

# http://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys
def flatten_dict(d, parent_key = None):
    if parent_key is None:
        parent_key = ''
    items = []
    for k, v in d.items():
        try:
            if (type(v)==type([])): 
                for l,w in enumerate(v): 
                    items.extend(flatten_dict(w, str(parent_key) + str(k) + '_' + str(l) + '_').items())
            else: 
                items.extend(flatten_dict(v).items())
        except AttributeError:
            items.append((str(parent_key) + str(k), v))
    return dict(items)

f = flatten_dict(test)
print(f)

import pandas as pd
p = pd.DataFrame(f)
print(p)
