class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for x in nums:
            frequency[x] = frequency.get(x, 0) + 1   # count occurrences of each number

        return sorted(frequency, key=frequency.get, reverse=True)[:k]  # top k by frequency, descending