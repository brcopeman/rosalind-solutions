"""
Rosalind: GC - Computing GC Content
Time  Complexity: O(n)
Space Complexity: O(n)
"""
from pathlib import Path

def gc_content(data: str) -> tuple[str, float]:
    percent = 0.0
    name = ''
    sequences = {}
    for line in data.splitlines():
        if line.startswith(">"):
            current_id = line[1:]
            sequences[current_id] = ''
        else:
            sequences[current_id] += line
    for seq_id, seq in sequences.items():
        gc_count = 0 
        for char in seq:
            if char in "GC":
                gc_count+=1
        result = (gc_count/len(seq))*100
        if result > percent:
            percent = result
            name = seq_id
    return name, percent

if __name__ == '__main__':
    sample = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
    name, percent = gc_content(sample)
    print(name)
    print(f"{percent:.6f}")

    path = Path(__file__).parent/"data"/"rosalind_gc.txt"
    if path.exists():
        name, percent = gc_content(path.read_text().strip())
        print(name)
        print(f"{percent:.6f}")