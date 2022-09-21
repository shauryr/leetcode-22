class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        # n log k
        # find count of all the numbers
        # create a max heap of size n
        # add all elements
        # pop the heap n times to return element
        dict_counts = Counter(nums)
        
        tups = []
        heap = []
        for value, count in dict_counts.items():
            tups.append((count, value))
            
        for pair in tups:
            if len(heap) < k:
                heappush(heap, pair)
            elif heap[0][0]< pair[0]:
                heapreplace(heap, pair)
        
        result = []
        for i in range(k):
            result.append(heappop(heap)[1])
        
        return result