# https://neetcode.io/problems/meeting-schedule
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start) #sorting based on start value
        for i in range(1,len(intervals)): #starting from the 1st index 
            i1=intervals[i-1]#comparing the current index with the previous index
            i2=intervals[i]

            if i1.end>i2.start:
                return False
        return True

