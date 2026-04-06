class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ascii=[0]*26
        for i in range(len(s)):
            ascii[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            ascii[ord(t[i])-ord('a')]-=1
        for k in ascii:
            if k !=0:
                return False
        return True      