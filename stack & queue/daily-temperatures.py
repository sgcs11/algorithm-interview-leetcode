class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = (i - last)
            stack.append(i)

        return res
