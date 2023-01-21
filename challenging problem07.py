gens = input("염기 서열을 입력해주세요:")
counter = {}
for i in range(0,len(gens),3):
    codon = gens[i:i+3]
    if len(codon) ==3 :
        if codon not in counter:
            counter[codon] = 0
        counter[codon] = 1
print(counter)