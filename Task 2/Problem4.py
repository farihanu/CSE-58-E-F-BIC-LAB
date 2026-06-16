
pattern = input("Enter pattern: ")
text= input("Enter text:")
for i in range(len(text)-len(pattern)+1):
    str = text[i:i+len(pattern)]
    if str==pattern:
        print(i," ",end="")
    
