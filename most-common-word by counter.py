from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[\W ]', ' ', paragraph).lower().split() if word not in banned]
        counts = Counter(words)

        return counts.most_common(1)[0][0]


solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))