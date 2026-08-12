class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = list(s)
        new_t = list(t)
        for i in range(len(new_s)):
            for j in range(len(new_t)):
                if new_s[i] == new_t[j]:
                    return True
            return False
        

        
        
    
       
        