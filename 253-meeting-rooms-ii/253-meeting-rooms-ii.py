class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/meeting-rooms-ii/discuss/373235/Python3-Min-heap-with-explaination
        '''
        h =[]
        sort = sorted(intervals)
        for i in sort:
            # need a new meeting room
            if h == [] or h[0] >i[0]:
                heapq.heappush(h,i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h,i[1])
        return len(h)