class Stream:
    def __init__(self, data: list):
        self._data = data
        self._index = 0
    def next(self) -> str:
        assert self._index <= len(self._data) - 1
        item = self._data[self._index]
        self._index += 1
        return item
    def peek(self) -> str:
        assert self._index <= len(self._data) - 1
        return self._data[self._index]