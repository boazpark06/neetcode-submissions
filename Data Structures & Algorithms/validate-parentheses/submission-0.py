class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        return s == "" 

# Time = O(n^2) - repeatedly checking string and replacing chars, Space = O(n)
        