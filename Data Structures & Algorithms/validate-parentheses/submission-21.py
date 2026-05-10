# 뒤로 문자열 하나씩 빼면서 close bracket일 때 짝꿍인지 확인 -> 아님 꼭 전체보다는 그룹그룹 닫힌 모양 가능
# -> 순차적으로 확인 필요
# open bracket 을 리스트에 올리고 close를 만났을 때 가장 최근 opened가 짝꿍인지 확인
# 시간 복잡도 O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        opened = []

        for i in s:
            if i in ['(','[','{']: # open 확인
                opened.append(i)

            else:
                if len(opened)==0:
                    return False
                else:
                    if i == ')' and opened[-1]=='(':
                        opened.pop()
                    elif i == ']' and opened[-1]=='[':
                        opened.pop()
                    elif i == '}' and opened[-1]=='{':
                        opened.pop()
                    else: # 짝꿍 아닌 경우 False
                        return False

        if len(opened)==0: # 남는게 없을 때 True
            return True
        else:
            return False

        
        