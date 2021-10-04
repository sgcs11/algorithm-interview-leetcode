class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(cur, route):
            if cur == len(digits):
                res.append(route)
                return

            for char in dic[digits[cur]]:
                dfs(cur + 1, route + char)

        if len(digits) == 0:
            return []
        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        dfs(0, "")

        return res