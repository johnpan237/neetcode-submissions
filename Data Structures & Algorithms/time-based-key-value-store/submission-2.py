class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ""

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            middle_timestamp = values[m][1]

            if middle_timestamp <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
