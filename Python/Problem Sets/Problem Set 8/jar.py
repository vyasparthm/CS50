class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity<0:
            raise ValueError("Capacity must be non negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeds Capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies in the jar!")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size