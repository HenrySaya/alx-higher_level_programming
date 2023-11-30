#!/usr/bin/python3
import imp
hidden_4 = imp.load_source('hidden_4', 'hidden_4.pyc')
names = dir(hidden_4)
filtered_names = [name for name in names if not name.startswith('__')]
sorted_names = sorted(filtered_names)
for name in sorted_names:
    print("{}".format(name))
