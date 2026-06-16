
pattern=input("enter pattern:")
text=input("enter text:")
d=int(input("enter d:"))

count1=0
for i in range(len(text)-len(pattern)+1):
    st=text[i:i+len(pattern)]
    count=0
    for j in range(len(pattern)):
        if st[j]!=pattern[j]:
            count+=1
    if count<=d:
      print(i," ",end="")




