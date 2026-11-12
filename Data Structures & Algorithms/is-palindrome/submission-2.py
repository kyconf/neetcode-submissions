class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s))
        clean = clean.lower()

        print(clean)
        left = 0
        right = len(clean) - 1

        while left < right:
            if clean[left] != clean[right]: 
                return False
            
            left += 1
            right -= 1

        return True
                
        