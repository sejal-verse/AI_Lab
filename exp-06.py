#alpha beta pruning
import math
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, height, alpha, beta):
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
    values = list(map(int, input("Enter the 8 leaf node values: ").split()))
    height = int(math.log2(len(values)))
    alpha = -math.inf
    beta = math.inf
    result = alpha_beta(0, 0, True, values, height, alpha, beta)
    
    print("The optimal value is:", result)
    