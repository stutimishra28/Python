from collections import Counter
n=int(input())
shoes=list(map(int,input().strip().split()))[:n]
ssc=Counter(shoes)
customers=int(input())
m=0
for _ in range(customers):
    size, price=map(int,input().split())
    if ssc[size]:
        m=m+price
        ssc[size]-=1
print(m)       
