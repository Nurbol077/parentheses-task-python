import math

def countWellFormedParenthesis(nCouples: int) -> int:
    return math.comb(2 * nCouples, nCouples) // (nCouples + 1)