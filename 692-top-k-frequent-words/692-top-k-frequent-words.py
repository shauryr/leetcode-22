class Solution:
    
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        # get the count of the words
        count_word_map, maxheap, result = Counter(words), [], []
        
        # reverse the map and push to heap
        for key, value in count_word_map.items():
            heappush(maxheap, (-value, key))
            
        # pop k times and store the words
        for i in range(k):
            result.append(heappop(maxheap)[1])
        return result