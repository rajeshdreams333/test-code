str1=input()
str2=input()
list=list(str1)
count=0
n=str2[len(str2)-1]
for i in list:
    if n in i:
        count+=1
print(count)