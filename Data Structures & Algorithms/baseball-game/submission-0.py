class Solution:
    def calPoints(self, operations: List[str]) -> int:
        base=[]
        for o in operations:
            if o =='C':
                base.pop()
            elif o=='D':
                base.append(2*base[-1])
            elif o =='+':
                base.append(base[-1]+base[-2])
            else:
                base.append(int(o))
        return sum(base)