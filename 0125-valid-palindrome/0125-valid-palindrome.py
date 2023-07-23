class Solution:
    def isPalindrome(self, s: str) -> bool:
        sf=""
        new_len=0
        
        for ele in s:
            if ele.isalpha() or ele.isdigit():
                new_len+=1
                
                sf+=ele.lower()
            if ele in string.punctuation:
                new_len+=1
        print(sf)   
        if len(sf)==0 :
            return True
        if len(sf)==1 and len(s)==new_len:
            return True
        if len(sf)==1 :
                return False
        r=len(sf)-1
        for l in range(len(sf)):
            print(sf[l])
            print(sf[r])
            if l==r:
                return True
            if l>r:
                return True
            if sf[l]==sf[r]:
                r-=1
                continue
        
            else:
                return False
            r-=1

            
        