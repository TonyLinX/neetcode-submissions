import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1

        item = list(freq.items())
        result = []

        ## 直觀排序(最慢)
        # item.sort(key=lambda t: t[1], reverse=True)
        # for t in item[:k]:
        #     result.append(t[0])
        

        ## Min-Heap (好一點)
        h = []
        for num, count in item:
            heapq.heappush(h,(count, num))
            if len(h)>k:
                heapq.heappop(h)

        for t in h:
            result.append(t[1])

        return result
        
        