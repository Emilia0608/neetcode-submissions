# 문자열을 하나씩 돌면서 알파벳을 확인한다
## 알파벳 소문자 ASCII 코드는 97~122사이 값을 가져야한다.
## 숫자 0~9값은 48~57값을 가진다.
# 중간 인덱스까지 탐색하며 반대 인덱스 알파벳과 다를 때 false를 출력한다.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char=""
        for i in s:
            if (ord(i.lower())<=122 and ord(i.lower())>=97) or (ord(i.lower())<=57 and ord(i.lower())>=48):
                char+=i.lower()


        check_bool=True
        if len(char)==1:
            return check_bool
        elif len(char)==2:
            if char[0]==char[1]:
                return check_bool
            else:
                return False
        else:
            end_index = len(char)//2

        for i in range(0, end_index):
            left_index=i
            right_index=len(char)-i-1

            if char[left_index]!=char[right_index]:
                check_bool=False
                break # 다 돌지 않고 중단

        return check_bool



