#-------------------------------------------------------------------------------
# treeset.py
#
#
# Copyright (C) 2016, Ryosuke Fukatani
# License: Apache 2.0
#-------------------------------------------------------------------------------

import bisect


class TreeSet(object):
    """
    Binary-tree set like java Treeset.
    Duplicate elements will not be added.
    When added new element, TreeSet will be sorted automatically.
    """
    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self._treeset: continue
            self.add(element)

    def add(self, element):
        bisect.insort(self._treeset, element)

    def ceiling(self, e):
        self._treeset[bisect.bisect_right(self._treeset, e)]

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        """
        Delete all elements in TreeSet.
        """
        self._treeset = []

    def clone(self):
        """
        Return shallow copy of self.
        """
        return TreeSet([], self.key)

    def remove(self, element):
        """
        Remove element if element in TreeSet.
        """
        try:
            self._treeset.remove(element)
        except KeyError:
            return False
        return True

    def __iter__(self):
        """
        Do ascending iteration for TreeSet
        """
        for element in self._treeset:
            yield element

    def pop(self, index):
        return self._treeset.pop(index)

    def __str__(self):
        return str(self._treeset)

if __name__ == '__main__':
    ts = TreeSet([3,7,2,7,1,3])
    print(ts)
