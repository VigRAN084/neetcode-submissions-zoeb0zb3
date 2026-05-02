class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    '''
    Called in strictly increasing order
    '''
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.kv[key]
        l = 0
        r = len(values) - 1
        res = -1
        # need to "prefer" the left half b/c we want the most recent value of key
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = m # best soln so far
                l = m + 1
            else: 
                r = m - 1
        if res < 0: 
            return ''
        return values[res][0]

        
