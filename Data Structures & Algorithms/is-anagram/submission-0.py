class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0]*26
        for i in s:
            res[ord(i) - ord("a")] +=1
        for j in t:
            res[ord(j) -ord("a")] -=1
        for k in res:
            if k !=0:
                return False
        return True        