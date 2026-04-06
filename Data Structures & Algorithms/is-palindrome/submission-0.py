class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp ="".join(ch for ch in s if ch.isalnum()).lower()
        return temp==temp[::-1]
        