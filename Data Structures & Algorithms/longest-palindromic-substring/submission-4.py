# 문자열 하나씩 지나가면서 palindrome인거 기록
## 기록할 때 max 길이인 것만 남기기
## start_index에서 end_index까지 end_index를 옮기면서 체크

# palindrome인지 확인하는 법
## 
def is_palindrome(s):    
    return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_lenth = 1 # 초기값 설정
        max_palin = s[0]

        for start_index in range(len(s)):
            for end_index in range(start_index+1, len(s)+1):
                if is_palindrome(s[start_index:end_index]) and max_lenth < len(s[start_index:end_index]):
                    max_lenth = len(s[start_index:end_index])
                    max_palin = s[start_index:end_index]

        return max_palin



        