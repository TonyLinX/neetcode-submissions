class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicty = dict()

        for num in nums:
            if num not in dicty:
                dicty[num] = 1
            else:
                dicty[num] += 1
        
        h = []

        for num, count in dicty.items():
            heapq.heappush(h, (count, num))
            if len(h) > k:
                heapq.heappop(h)
        result = []
        
        for item in h:
            result.append(item[1])

        return result
