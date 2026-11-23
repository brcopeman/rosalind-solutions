"""
Rosalind: RNA - Transcribing DNA into RNA
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path

def transcribe_dna_to_rna(data: str) -> str:
    result = ''
    for base in data:
        if base == 'T':
            result += 'U'
        else:
            result+= base
    return result

if __name__ == "__main__":
    sample = "GATGGAACTTGACTACGTAAATT"
    print(transcribe_dna_to_rna(sample))

    path = Path(__file__).parent/"data"/"rosalind_rna.txt"
    if path.exists():
        print(transcribe_dna_to_rna(path.read_text().strip()))