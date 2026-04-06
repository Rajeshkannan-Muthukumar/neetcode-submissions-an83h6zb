class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        strt=0
        while strt<len(gas):
            temp=strt
            fuel=0
            k=len(gas)
            while k:
                fuel+=gas[temp]
                if fuel<cost[temp]:
                    strt+=1
                    break
                fuel-=cost[temp]
                temp+=1
                temp=temp%len(gas)
                k-=1
            if k==0:
                return strt
        return -1