"""
Rosalind: DNA - Counting DNA Nucleotides
Time  Complexity: O(n)
Space Complexity: O(1)
"""
from pathlib import Path

def count_nucleotides(data: str) -> str:
    bases = {"A":0,"C":0,"G":0,"T":0}

    for base in data:
        bases[base] += 1
    return f"{bases['A']} {bases['C']} {bases['G']} {bases['T']}"

if __name__ == "__main__":
    sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print(count_nucleotides(sample))

    path = Path(__file__).parent/"data"/"rosalind_dna.txt"
    if path.exists():
        print(count_nucleotides(path.read_text().strip()))