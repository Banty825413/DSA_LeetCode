class Solution:
    
     def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        count = Counter(s)

        curr = Counter(count)
        best_case  =-1

        for i in range(len(s)):

            if any ( curr[c] > 0 for c in string.ascii_lowercase if c > target[i] ):
                best_case = i
            
            if curr[target[i]] > 0:
                curr[target[i]] -= 1
            else:
                break
        
        if best_case == -1:
            return ""
        rem = Counter(s)

        for i in range(best_case):
            rem[target[i]] -= 1
        
        best_choice = None
        
        for c in string.ascii_lowercase:
            if c > target[best_case] and rem[c] >0 :
                best_choice = c
                break
        rem[best_choice] -= 1

        suffix = []
        for c in string.ascii_lowercase:
            suffix.append(c* rem[c])
        
        return (target[:best_case]+ best_choice + "".join(suffix))

