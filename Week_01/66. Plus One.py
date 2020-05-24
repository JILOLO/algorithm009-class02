class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if not digits:
            return
        
        if len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
            
        if digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]