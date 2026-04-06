from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1
        freq_sorted = sorted(freq.items(), key=lambda f: f[1], reverse=True)
        for i in range(k):
            res.append(freq_sorted[i][0])
                
        return res
            
        