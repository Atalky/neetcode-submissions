class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter is a built-in dict subclass designed for exactly this:
        # it builds a {character: count} dictionary from an iterable in
        # one call, instead of you writing the counting loop by hand.
        # Comparing two Counters with == checks that every key and its
        # count match on both sides — which is exactly "same letters,
        # same frequencies", the same logic as your hand-rolled hashmap
        # version, just built for you under the hood.

        return Counter(s) == Counter(t)
        
        
        # If two strings are anagrams, they contain the exact same
        # characters — just in a different order. Sorting both strings
        # puts their characters into the same canonical order, so if
        # they're anagrams, the sorted results will be identical.
        # sorted() returns a list, and Python compares lists element by
        # element, so this is really checking "same characters, same
        # counts, once ordering is removed" in one line.
        # Also handles a length mismatch for free: different-length
        # strings produce different-length sorted lists, which can never
        # be equal — no separate len() check needed.

        return sorted(s) == sorted(t)


        # Two strings can only be anagrams if they have the same number of
        # characters overall — cheap check, so do it first and bail early.
        if len(s) != len(t):
            return False

        # Two separate hashmaps: one counts characters in s, the other in t.
        # Using dicts (not lists) means checking/updating a count is O(1)
        # average, instead of scanning for the character every time.
        countS, countT = {}, {}

        # Single pass over both strings at once (they're the same length,
        # so one index i works for both). For each position, bump that
        # character's running count in its own dictionary.
        for i in range(len(s)):
            # .get(key, 0) returns the current count, or 0 if this is the
            # first time we've seen this character — avoids a KeyError.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Now compare the two frequency counts. Looping over countS's keys
        # (the distinct characters seen in s) and checking each one against
        # countT is enough — if a character's counts don't match, or a
        # character in s never appears in t at all (countT.get(c, 0) = 0),
        # the strings aren't anagrams.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        # Every character count matched — same letters, same frequencies.
        return True