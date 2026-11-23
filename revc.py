"""
Rosalind: REVC: Complementing a Strand of DNA
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path 

def reverse_complement_dna(data: str) -> str:
    result = ''
    for base in data:
        if base == 'A':
            result += 'T'
        elif base == 'C':
            result += 'G'
        elif base == 'G':
            result += 'C'
        elif base == 'T':
            result += 'A'
    return result[::-1]

if __name__ == "__main__":
    sample = "AAAACCCGGT"
    print(reverse_complement_dna(sample))

    path = Path(__file__).parent/"data"/"rosalind_revc.txt"
    if path.exists():
        print(reverse_complement_dna(path.read_text().strip()))

