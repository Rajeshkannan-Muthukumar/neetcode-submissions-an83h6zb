class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<=j and i<len(s) and j>=0:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].isalnum() and s[j].isalnum():
                if s[i].lower() ==s[j].lower():
                    i+=1
                    j-=1
                else: 
                    return False
                # i+=1
                # j-=1
        return True
        