class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_list = []

        check_duplicate = False
        for num in nums:
            if num not in n_list: # 한 번도 없으면 append
                n_list.append(num)
            elif num in n_list: # 이미 있으면 중복 체크
                check_duplicate = True
                break

        if check_duplicate:
            return True
        else:
            return False
        
        