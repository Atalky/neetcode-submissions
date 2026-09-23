class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #go through words, sort them, hash them, if they exist count them and then
        sorted_words = {}

        for word in strs:                     # loop over the words themselves, not indices
            key = "".join(sorted(word))        # sorted(word) -> list of chars, join back into a string
            if key not in sorted_words:
                sorted_words[key] = []
            sorted_words[key].append(word)

        return list(sorted_words.values())

        # second solution from video : count[a-z] using a hashmap with key letters / patterns -> and values which are the anagrams.
        result = defaultdict(list)   # count-pattern (as a tuple) -> list of anagrams

        for s in strs:
            count = [0] * 26          # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)   # once per string, after counting is done

        return list(result.values())
