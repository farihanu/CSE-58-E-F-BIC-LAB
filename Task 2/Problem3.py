
pattern=input()
complement={
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
}

reverse_complement =""
for nucleotide in pattern:
    reverse_complement += complement[nucleotide]
    
reverse_complement=reverse_complement[::-1]
print(reverse_complement)
