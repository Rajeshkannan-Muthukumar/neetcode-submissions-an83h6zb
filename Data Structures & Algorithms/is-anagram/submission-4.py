class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag=[0]*26
        if len(s)!=len(t):
            return False
        for i in s:
            anag[ord(i)-ord('a')]+=1
        for j in t:
            if anag[ord(j)-ord('a')]==0:
                return False
            anag[ord(j)-ord('a')]-=1
        for an in anag:
            if an >0:
                return False
        return True