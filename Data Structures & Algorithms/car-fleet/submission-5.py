class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - pos) / spd for pos, spd in cars]

        fleets = 0
        current_time = 0

        for time in times:
            if time > current_time:
                fleets += 1
                current_time = time

        return fleets
