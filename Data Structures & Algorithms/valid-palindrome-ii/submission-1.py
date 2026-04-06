class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(s,i,j):
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        k=0
        z=len(s)-1
        while k<z:
            if s[k]==s[z]:
                k+=1
                z-=1
            else:
                return palindrome(s,k+1,z) or palindrome(s,k,z-1)
        return True