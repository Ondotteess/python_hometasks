class LRUCache:
    def __init__(self, capacity = 16):
        self._capacity = capacity
        self._history = []
        self._cache = {}

    def put(self, key, value):
        if key not in self._cache.keys() and len(self._cache.keys()) < self._capacity:
            self._cache[key] = value
            self._history += [key]

        elif key not in self._cache.keys() and len(self._cache.keys()) == self._capacity:
            self._cache.pop(self._history.pop())
            self._cache[key] = value
            self._history += [key]

    def get(self, key):
        if key in self._cache.keys():
            self._history.remove(key)
            key += self._history
            return key, self._cache[key]

        return None

    def display_info(self):
        for key, val in self._cache.items():
            print(f"key: {key}\tval: {val}")


    def display_history(self):
        print(self._history)


cache = LRUCache(capacity=2)

cache.put('first', 1)
cache.put('second', 2)

cache.display_info()
cache.display_history()

print()

cache.put('third', 3)

cache.display_info()
cache.display_history()
print('----------------------')

cache = LRUCache(capacity=3)

cache.put('first', 1)
cache.put('second', 2)

cache.display_info()
cache.display_history()

print()

cache.put('third', 3)

cache.display_info()
cache.display_history()


'''
key: first	val: 1
key: second	val: 2
['first', 'second']

key: first	val: 1
key: third	val: 3
['first', 'third']
----------------------
key: first	val: 1
key: second	val: 2
['first', 'second']

key: first	val: 1
key: second	val: 2
key: third	val: 3
['first', 'second', 'third']
'''
