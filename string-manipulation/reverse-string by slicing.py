class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]


solution = Solution()
solution.reverseString(["h","e","l","l","o"])
solution.reverseString(["H","a","n","n","a","h"])