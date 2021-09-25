from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = Counter(S)
        count = 0

        for char in J:
            if char in freqs:
                count += freqs[char]

        return count