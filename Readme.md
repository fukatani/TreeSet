### Introduction
"TreeSet" is a Binary-tree set like java TreeSet.
The TreeSet will be sorted automatically when adding/removing elements.
Duplicate elements will not be added.

"TreeMap" is a dictionary with sorted keys similar to java TreeMap.
Keys, iteration, items, values will all return values ordered by key.
Otherwise it should behave just like the builtin dict.

### Usage
Copy treeset.py and treemap.py to any directory.

```python
from treeset import TreeSet
ts = TreeSet([3,7,2,7,1,3])
print(ts)
>>> [1, 2, 3, 7]

ts.add(4)
print(ts)
>>> [1, 2, 3, 4, 7]

ts.remove(7)
print(ts)
>>> [1, 2, 3, 4]

ts.remove(5)
print(ts)
>>> [1, 2, 3, 4]

ts.addAll([3,4,5,6])
print(ts)
>>> [1, 2, 3, 4, 5, 6]

print(ts[0])
>>> 1

print(ts[-1])
>>> 6

print(1 in ts)
>>> True

print(100 in ts)
>>> False

for i in TreeSet([1,3,1]):
	print(i)
>>> 1
>>> 3
```

Usage of TreeMap is described in test_treemap.py

### Software Requirements
Python (2.7 or 3.4)

### License
Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)

### Copyright
Copyright (C) 2016, Ryosuke Fukatani
