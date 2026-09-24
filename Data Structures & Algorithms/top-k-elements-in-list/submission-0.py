class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #using a hashmap, the key is k and the values will be -> nums[i]
        frequency = {}
        for x in nums:
            frequency[x] = frequency.get(x, 0) + 1
        return sorted(frequency, key=frequency.get, reverse=True)[:k]        