class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        max_length=0
        while i<len(s) and j <len(s):
            if len(s[i:j+1])==len(set(s[i:j+1])):
                
                max_length=max(max_length,j-i+1)
                j+=1
            else:
                i+=1
                j=i
        return max_length
        