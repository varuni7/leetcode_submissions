class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter
        anagram_dict = {}
        # key : [len(word),set)word]
        # intially value will be  the first word itself 
        
        for word in strs:
            
            key = str(sorted(Counter(word).items()))
            
            if key in anagram_dict:
                
                
                
                anagram_dict[key].append(word)
            else:
                anagram_dict[key]=[word]
        
                
        return anagram_dict.values()
                
        