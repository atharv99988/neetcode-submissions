class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Build frequency map for t
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        countS = {}
        l = 0
        min_len = float('inf')
        result = ""   # ← important: start with empty string

        def is_valid_window():
            for char in countT:
                if char not in countS or countS[char] < countT[char]:
                    return False
            return True

        for r in range(len(s)):
            # Always add the right character
            countS[s[r]] = countS.get(s[r], 0) + 1

            # Shrink from left as much as possible while window is valid
            while l <= r and is_valid_window():
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    result = s[l : r + 1]

                # Remove left character
                countS[s[l]] -= 1
                if countS[s[l]] == 0:
                    del countS[s[l]]     # optional but cleaner
                l += 1

        return result