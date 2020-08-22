class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        
        while True:
            if num==0:
                break
            else:
                if num%2 == 1:
                    num -= 1
                else:
                    num = int(num/2)    
                count += 1
        
        return count