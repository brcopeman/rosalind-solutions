"""
Rosalind: FIB - Rabbits and Recurrence Relations
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path

def rabbit_pair_count(n: int, k: int, memo: dict) -> int:
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    result = rabbit_pair_count(n-1, k, memo) + k*rabbit_pair_count(n-2, k, memo)
    memo[n] = result
    return result

if __name__ == "__main__":
    print(rabbit_pair_count(5,3,{}))

    path = Path(__file__).parent /"data"/"rosalind_fib.txt"
    if path.exists():
        n, k = map(int, path.read_text().split())
        print(rabbit_pair_count(n,k,{}))