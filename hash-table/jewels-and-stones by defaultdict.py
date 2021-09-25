from collections import defaultdict


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = defaultdict(int)
        count = 0

        for char in S:
            freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]

        return count