"""
Rosalind: IPRB - Mendel's First Law
Time  Complexity: O(1)
Space Complexity: O(1)
"""
from pathlib import Path

def mendelian_inheritance(k:int,m:int,n:int) -> float:
    population = k+m+n

    P_Aa_Aa = ((m/population) * ((m-1)/(population-1)))*1/4
    P_Aa_aa = ((m/population) * (n/(population-1)))*1/2
    P_aa_Aa = ((n/population) * (m/(population-1)))*1/2
    P_aa_aa = ((n/population) * ((n-1)/(population-1)))*1

    p_recessive =  P_Aa_Aa + P_Aa_aa + P_aa_Aa + P_aa_aa
    p_dominant = 1 - p_recessive
    return p_dominant

if __name__ == '__main__':
    sample = 2, 2, 2
    print(f"{mendelian_inheritance(*sample):.5f}")

    path = Path(__file__).parent/"data"/"rosalind_iprb.txt"
    if path.exists():
        k, m, n = map(int,path.read_text().split())
        print(f"{mendelian_inheritance(k, m, n):.5f}")



    
