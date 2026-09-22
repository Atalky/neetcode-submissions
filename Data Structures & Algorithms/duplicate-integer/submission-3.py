class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #comapring each number against each number gives us O(n^2). too slow we want O(n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True    
            hashset.add(n)
        return False
