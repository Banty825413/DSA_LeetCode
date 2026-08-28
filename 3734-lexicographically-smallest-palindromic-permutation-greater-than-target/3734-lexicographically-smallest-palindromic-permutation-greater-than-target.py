class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        
        cnt =[0]*26
        for c in s :
            cnt[ord(c)-ord('a')] +=1
        
        # can be palindrome or not
        odd = 0
        for i in range(len(cnt)):
            if cnt[i] % 2 ==1:
                odd +=1 

        if odd > 1:
            return ""

        # Finding the middle if nums of character are odd 
        middle =""
        if len(s) %2 == 1:
            for i in range(len(cnt)):
                if cnt[i] % 2==1:
                    middle= chr(i+ord('a'))
                    break
        
        # we need half of palindrome 
        half_cnt = [i//2 for i in cnt]
        half_len = len(s)//2
        
        # Lets build the left half

        prefix = []

        def isgreater():
            left = "".join(prefix)

            for i in range (25,-1,-1):
                left += chr(i+ord("a")) * half_cnt[i] 
            
            palindrome = left + middle + left[::-1]

            return palindrome > target

        for _ in range (half_len):

            picked = False

            for i in range (26):
                
                if half_cnt[i] ==0:
                    continue
                half_cnt[i] -= 1
                prefix.append(chr(i +ord('a')))

                if isgreater():
                    picked = True
                    break
                
                half_cnt[i] += 1
                prefix.pop()
            
            if not picked: 
                # if none of charcter is greater or not choosen to make palindrome or make it lexico greater
                return ""
            
        left = "".join(prefix)
        result = left + middle + left[::-1]

        if result > target:
            return result
        return ""