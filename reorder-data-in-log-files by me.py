class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        res = []
        letters = []
        digits = []
        for log in logs:
            log = log.split()
            try:
                int(log[-1])
                digits.append(log)
            except:
                letters.append(log)
        letters.sort(key=lambda x: (x[1:], x[0]))

        return list(map(' '.join, letters)) + list(map(' '.join, digits))


solution = Solution()
print(solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
