class Solution:
    def romanToInt(self, s: str) -> int:
        sign={"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=sign[s[-1]]
        for i in range(len(s)-1,0,-1):
            if sign[s[i]]>sign[s[i-1]]:
                res-=sign[s[i-1]]
            else:
                res+=sign[s[i-1]]
        return res