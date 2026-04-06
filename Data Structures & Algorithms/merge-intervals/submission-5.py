class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        # if len(intervals)==1:
        #     return intervals
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=res[-1][1]:
                temp=[res[-1][0],max(intervals[i][1],res[-1][1])]
                res.pop()
                res.append(temp)
            else:
                res.append(intervals[i])
        return res            