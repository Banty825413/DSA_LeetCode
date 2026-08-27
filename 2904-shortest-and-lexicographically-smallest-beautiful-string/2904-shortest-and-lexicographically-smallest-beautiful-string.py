class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        
        ans= ""
        left = 0
        count_ones= 0
        
        for right in range(len(s)):
            if s[right] == "1":
                count_ones += 1
            while count_ones == k:

                if s[left] =="1" :
                    
                    current_str = s[left:right+1]
                    if not ans:
                        ans = current_str
                    elif len(current_str) < len(ans):
                        ans = current_str
                    elif len(current_str) == len(ans):
                        if current_str < ans:
                            ans = current_str
                    count_ones -= 1

                left +=1

                
                
        return ans