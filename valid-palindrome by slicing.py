import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome('A man, a "plan, a canal: Panama'))
print(solution.isPalindrome('race a car'))
