# sorting 을 쓴 문자열을 키 값으로 딕셔너리를 만듦
# 같은 애너그램 문자열을 키 값으로 가진 리스트에 append
# 2n+~

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for str in strs:
            str_reordered = [s for s in str]
            str_reordered.sort()
            str_reordered = "".join(str_reordered) # 정렬 후 다시 합치기
            
            if str_reordered not in anagram_dict:
                anagram_dict[str_reordered]=[]

            anagram_dict[str_reordered].append(str)
        
        answer = []
        for val in anagram_dict.values():
            answer.append(val)

        return answer
