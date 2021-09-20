class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''

        # odd number
        for k in range(n):
            i, j = k, k
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            temp = s[i + 1:j]
            if len(res) < len(temp):
                res = temp
        # even number
        for k in range(n - 1):
            i, j = k, k + 1
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            temp = s[i + 1:j]
            if len(res) < len(temp):
                res = temp
