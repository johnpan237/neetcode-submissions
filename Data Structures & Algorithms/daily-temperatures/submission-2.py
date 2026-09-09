class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append([t, i])
        

        return result