class Solution:
    def angleClock(self, hour, minutes):

        minHand = minutes * 6
        hourHand = (hour * 60 + minutes) * 0.5

        angle = abs(minHand - hourHand)

        return min(angle, 360 - angle)
