from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = deque([char.lower() for char in s if char.isalnum()])

        while len(s) > 1:
            if s.popleft() != s.pop():
                return False

        return True


solution = Solution()
print(solution.isPalindrome('A man, a plan, a canal: __Panama'))
print(solution.isPalindrome('race a car'))
