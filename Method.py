n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
max=a[0]
for i in range(n) :
    if a[i]>max:
        max=a[i]
print(max)