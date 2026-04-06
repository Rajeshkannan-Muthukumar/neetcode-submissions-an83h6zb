class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot_fuel=sum(gas)
        flag=False
        tot_cost=sum(cost)
        bal=0
        if tot_cost>tot_fuel:
            return -1
        for i in range(len(gas)):
            curr=gas[i]-cost[i]
            bal+=curr
            if curr>=0 and not flag:
                pos=i
                flag=True
            elif bal<0 and flag :
                flag=False
        return pos