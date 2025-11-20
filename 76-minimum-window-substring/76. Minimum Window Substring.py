class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is longer than s, no solution
        if len(t) > len(s):
            return ""

        from collections import Counter

        # Count of required characters
        required = Counter(t)
        required_unique = len(required)  # how many unique chars we actually need

        # Variables for sliding window
        left = 0
        formed = 0  # how many unique chars currently satisfy their required counts
        window_counts = {}

        # Result tracking: (window_length, left_index, right_index)
        best = (float('inf'), 0, 0)

        # Expand the window with right pointer
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If this char's freq now matches the required freq, we "formed" one requirement
            if char in required and window_counts[char] == required[char]:
                formed += 1

            # When we satisfy all required characters, try shrinking from the left
            while left <= right and formed == required_unique:
                window_size = right - left + 1
                if window_size < best[0]:
                    best = (window_size, left, right)

                # Try to shrink the window from the left
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If shrinking breaks a requirement, reduce formed count
                if left_char in required and window_counts[left_char] < required[left_char]:
                    formed -= 1
                
                left += 1  # move left pointer forward

        # If best was updated, return substring; otherwise return empty
        if best[0] == float('inf'):
            return ""
        _, start, end = best
        return s[start:end+1]
