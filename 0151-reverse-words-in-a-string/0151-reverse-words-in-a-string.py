class Solution:
    def reverseWords(self, s: str) -> str:
        if s=="":
            return ""
        s=s.rstrip()
        s_words=s.split()
        print(s_words)
        return " ".join(s_words[::-1])