class Solution:
    def validPalindrome(self, s: str) -> bool:
        def left(s):
            flag=True
            i=0
            j=len(s)-1
            while i<=j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    if flag:
                        i+=1
                        flag=False
                    else:
                        return False
            return True
        def right(s):
            flag=True
            i=0
            j=len(s)-1
            while i<=j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    if flag:
                        j-=1
                        flag=False
                    else:
                        return False
            return True

        return left(s) or right(s)
        

