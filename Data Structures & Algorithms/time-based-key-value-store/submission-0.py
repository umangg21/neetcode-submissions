class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key]=[]
        self.ds[key].append((timestamp,value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        items= self.ds.get(key, [])
        if len(items) == 0:
            return ""

        left = 0
        right = len(items)-1
        res= ""
        while (left <= right):
            mid = (left+right)//2
            
            if items[mid][0] > timestamp:
                right = mid-1
            else:
                res = items[mid][1]
                left = mid+1

        return res       
            
        
        
