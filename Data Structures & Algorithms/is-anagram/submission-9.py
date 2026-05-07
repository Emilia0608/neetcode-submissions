# 문자열 -> 리스트
# 리스트 -> 정렬
# 하나씩 비교

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=[]
        t_list=[]

        for i in s:
            s_list.append(i)
        for i in t:
            t_list.append(i)

        check_anagram = True

        if len(s_list)!=len(t_list):
            check_anagram = False

        else:
            s_list.sort()
            t_list.sort()
        
            for i in range(0, len(s)):
                if s_list[i]!=t_list[i]:
                    check_anagram = False
        
        return check_anagram
