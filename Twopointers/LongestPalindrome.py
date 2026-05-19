# Name: Longest Palindrome String
# Ref: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        txt = ""
        str_len = 0

        if not s or len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for k in range(len(s)):

            # odd variant
            i,j=k,k
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > str_len:
                    txt = s[i:j+1]
                    str_len = j-i+1

                i-=1
                j+=1

            # even variant
            i,j=k,k+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > str_len:
                    txt = s[i:j+1]
                    str_len = j-i+1

                i-=1
                j+=1

        return txt

# IGNORE, test
sol = Solution()
assert sol.longestPalindrome("babad") in ['bab', 'aba']
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("ss") == "ss"
assert sol.longestPalindrome("a") == "a"
assert sol.longestPalindrome("") == ""
