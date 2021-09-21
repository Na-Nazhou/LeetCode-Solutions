class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = 30 * (hour + minutes / 60)
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)