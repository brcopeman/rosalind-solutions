"""
Rosalind: HAMM - Counting Point Mutations
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path

def count_point_mutations(data: str) -> int:
    hamm_d = 0
    s, t = data.splitlines()
    for i in range(len(s)):
        if s[i] != t[i]:
            hamm_d += 1
    return hamm_d

if __name__ == "__main__":
    sample = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"
    print(count_point_mutations(sample))

    path = Path(__file__).parent/"data"/"rosalind_hamm.txt"
    if path.exists():
        print(count_point_mutations(path.read_text().strip()))
    
        

