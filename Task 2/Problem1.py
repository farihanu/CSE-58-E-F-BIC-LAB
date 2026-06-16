text=input("Enter text: ")
pattern=input("Enter pattern: ")
count=0
for i in range(len(text)-len(pattern)+1):
    str=text[i:i+len(pattern)]
    if str==pattern:
        count+=1
print(count)        
