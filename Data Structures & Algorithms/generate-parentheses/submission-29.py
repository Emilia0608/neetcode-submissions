# # 간단 구상1
# # 모든 조합 다 표시 -> 가능한 것만 거르기

# # 간단 구상
# # 간략한 필터링 조건 설정
# # close로 시작하면 안됨
# # open로 끝나면 안됨

# # 간략한 필터링 조건 모든 케이스 만든 다음에 짝꿍인 경우만 answer return
# ## open list 만들어서 append 한 다음에 close 오면 pop
# ## open list 가 비어 있고 close pop 에러 안나야 anser

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        par_list = ["("]

        if n == 1:
            return ["()"]
        elif n > 1:
            for i in range(1, n*2):
                new_list = []
                for par in par_list:
                    if i < n*2-1:
                        new_list.append(par+"(")
                    new_list.append(par+")")

                par_list = new_list

            answer = []
            for par in par_list:
                open_list = []
                check = True
                for p in par:
                    if p == "(":
                        open_list.append(p)
                    else:
                        if len(open_list)>0:
                            open_list.pop()
                        else:
                            check = False
                    
                if len(open_list)==0 and check:
                    answer.append(par)

        return answer

                        
    









