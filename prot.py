"""
Rosalind: PROT - Translating RNA into Protein
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path

RNA_CODON_TABLE_TEXT = """UUU F CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

def build_codon_table(text: str) -> dict:
    rna_codon_table = {}
    items = text.split()
    for item in items:
        if len(item) == 3:
            current_codon = item
        else:
            rna_codon_table[current_codon] = item
    return rna_codon_table

RNA_CODON_TABLE = build_codon_table(RNA_CODON_TABLE_TEXT)

def translate_rna_to_protein(data: str) -> str:
    result = ''
    for i in range(0, len(data), 3):
        codon = RNA_CODON_TABLE[data[i:i+3]]
        if codon == 'Stop':
            break
        result = result + codon
    return result

if __name__ == "__main__":
    sample = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    print(translate_rna_to_protein(sample))

    path = Path(__file__).parent/"data"/"rosalind_prot.txt"
    if path.exists():
        print(translate_rna_to_protein(path.read_text().strip()))
