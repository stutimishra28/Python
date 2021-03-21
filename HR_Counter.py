from collections import Counter
n=int(input())
shoes=list(map(int,input().strip().split()))[:n] #list of shoe_sizes input
ssc=Counter(shoes) #convert list to dict of counter
customers=int(input())
money=0
for _ in range(customers):
    size, price=map(int,input().split())
    if ssc[size]:
        money=money+price
        ssc[size]-=1
print(money)       
