class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            # Compare characters (ignore uppercase/lowercase)
            if s[l].lower() != s[r].lower():
                return False
                
            # Move pointers inward
            l += 1
            r -= 1

        return True