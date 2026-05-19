# 탐색 인덱스를 돌면서 탐색 인덱스보다 큰 인덱스 값을 가진 데이터 중 수익을 낼 수 있는지 체크
# 탐색 인덱스, 비교할 인덱스, 수익
# 시간 복잡도 O(n^2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for idx, price in enumerate(prices):
            for i in range(idx+1, len(prices)):
                if prices[i] - price > max_profit:
                    max_profit = prices[i] - price
        return max_profit

        