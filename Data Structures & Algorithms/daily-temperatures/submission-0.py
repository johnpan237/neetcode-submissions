class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # each element will be in this pair format [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append([t, i])
        
        return result
