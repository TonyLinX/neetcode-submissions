class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1

        item = list(freq.items())
        item.sort(key=lambda t: t[1], reverse=True)

        result = []
        for t in item[:k]:
            result.append(t[0])

        return result
        