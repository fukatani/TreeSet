from treeset import TreeSet


class TreeMap(dict):
    def __init__(self, seq=None, **kwargs):
        if seq is None:
            super().__init__(**kwargs)
        else:
            super().__init__(seq, **kwargs)
        self.sorted_keys = TreeSet(super().keys())

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.sorted_keys.add(key)

    def __delitem__(self, key):
        super().__delitem__(key)
        self.sorted_keys.remove(key)

    def keys(self):
        return self.sorted_keys

    def items(self):
        return [(k, self[k]) for k in self.sorted_keys]

    def __iter__(self):
        for k in self.sorted_keys:
            yield k

    def values(self):
        for k in self.sorted_keys:
            yield self[k]
