class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        pow=2**31
        while  n!=0:
            res=res+(n&1)*pow
            n=n>>1
            pow=pow/2
        return int(res)
        