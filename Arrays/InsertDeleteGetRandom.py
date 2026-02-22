import random

class RandomizedSet:

    def __init__(self):
        self.items = []
        self.idxs = {}

    def is_exists(self, val: int):
        return val in self.idxs

    def insert(self, val: int) -> bool:
        if not self.is_exists(val):
            n = len(self.items)
            self.items.append(val)
            self.idxs[val] = len(self.items) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if self.is_exists(val):
            idx = self.idxs[val]
            self.items[idx] = self.items[-1] # replace the value
            self.idxs[self.items[idx]] = idx
            self.items.pop()
            del self.idxs[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.items)



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.items)
print(obj.getRandom())
print(obj.remove(1))
print(obj.items)
print(obj.insert(2))
print(obj.items)
print(obj.getRandom())
