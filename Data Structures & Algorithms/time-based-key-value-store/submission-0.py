class TimeMap:

    def __init__(self):
        self.TimeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        if value == "":
            self.TimeMap[key].append(("",timestamp))
        else:
            self.TimeMap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        arr = self.TimeMap[key]

        l,r = 0, len(arr)-1

        if arr[0][1] > timestamp:
            return ""

        while l<r:
            mid = l +(r-l+1) // 2

            if arr[mid][1] <= timestamp:
                l = mid
            else:
                r = mid -1
        return arr[l][0]