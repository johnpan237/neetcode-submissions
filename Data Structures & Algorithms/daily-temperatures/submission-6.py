class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initializing the result list with all 0's
        result = [0] * len(temperatures)
        # This stack will store indices of the temperatures array
        stack = []

        # Loop over temperatures array
        for i, current in enumerate(temperatures):
            # Check if the current temperature is higher than the temperature corresponding
            # to the index at the top of the stack
            while stack and temperatures[stack[-1]] < current:
                last_index = stack.pop()
                result[last_index] = i - last_index

            # Add current day index to the stack
            stack.append(i)

        return result
