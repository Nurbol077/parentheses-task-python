import time
from main import countWellFormedParenthesis

start = time.perf_counter()
countWellFormedParenthesis(15)
end = time.perf_counter()

print(f"Execution time: {(end - start) * 1000:.6f} ms")