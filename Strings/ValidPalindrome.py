# Ref: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        txt = [c.lower() for c in s if c.isalnum()]
        return txt == txt[::-1]

sol = Solution()
assert sol.isPalindrome("A man, a plan, a canal: Panama")
assert not sol.isPalindrome("race a car")
assert sol.isPalindrome(" ")
print("ALLOK")
