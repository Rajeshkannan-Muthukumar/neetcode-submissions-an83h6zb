class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        if len(intervals)==0:
            return []
        res=[intervals[0]]
        for i in range(len(intervals)):
            if res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
        return res
