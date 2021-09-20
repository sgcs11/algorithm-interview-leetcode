import re
from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

