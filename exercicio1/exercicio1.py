class Solution:
    def maxProfit(self, prices: [int]) -> int:
            
            n = len(prices)
            max_transactions = 2

            # inicializa a matriz
            matriz = [[[0] * 2 for _ in range(max_transactions + 1)] for _ in range(n)]

            for k in range(max_transactions + 1):
                matriz[0][k][1] = -prices[0] # compra a primeira ação

            # itera sobre a matriz e compara as opções para fazer a melhor escolha 
            for i in range(1, n):
                for k in range(1, max_transactions + 1):

                    matriz[i][k][0] = max(matriz[i - 1][k][0], matriz[i - 1][k][1] + prices[i])
                    matriz[i][k][1] = max(matriz[i - 1][k][1], matriz[i - 1][k - 1][0] - prices[i])

            return matriz[n - 1][max_transactions][0]

solution = Solution()
prices = [3,3,5,0,0,3,1,4]
output = solution.maxProfit(prices)
print(output)  # Output: 6
