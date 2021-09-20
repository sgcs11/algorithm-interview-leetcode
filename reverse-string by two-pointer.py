class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


solution = Solution()
solution.reverseString(["h","e","l","l","o"])
solution.reverseString(["H","a","n","n","a","h"])