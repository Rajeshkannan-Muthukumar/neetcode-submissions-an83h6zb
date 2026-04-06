class Solution:
        def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
                bal=0
                pos=-1
                flag=False
                for i in range(len(gas)):
                    curr=gas[i]-cost[i]
                    bal+=curr
                    if curr>=0 and not flag:
                        pos=i
                        flag=True
                    else:
                        flag=False
                if bal>=0:
                    return pos
                return -1
                # return -1