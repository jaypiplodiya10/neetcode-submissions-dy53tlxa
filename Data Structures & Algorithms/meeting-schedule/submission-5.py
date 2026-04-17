"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, its: List[Interval]) -> bool:
        its.sort(key=lambda x: x.start)
        for idx in range(len(its)-1):
            if its[idx].end > its[idx+1].start: return False
        
        return True