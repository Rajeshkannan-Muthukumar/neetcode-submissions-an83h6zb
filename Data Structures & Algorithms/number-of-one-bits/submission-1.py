class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n:
            cnt += n & 1   # get last bit (0 or 1)
            n >>= 1
        return cnt