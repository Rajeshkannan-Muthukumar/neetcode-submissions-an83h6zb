class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return 
        i=0
        j=1
        maxsub=1
        while j<len(s):
            if len(set(s[i:j+1]))==len(s[i:j+1]):
                curr=j-i+1
                maxsub=max(maxsub,curr)
            else:
                i+=1
            j+=1
        return 0 if not s else maxsub