class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for key,val in hashmap.items():
            if val >1:
                return True
        return False
         