num=int(input("Find factorial of:"))

def fact(num):
	if num==0:
		return 1
	elif num==1:
		return 1	
	else:	
		return num*fact(num-1)

print(f"Factorial of {num} is {fact(num)}")

trail=0
if 5**1 < num:
	trail=int(num/5)
if 5**2 < num:
	trail=trail + int(num/25) #how many times 25 comes in num is then added to trail
if 5**3 < num:
	trail=trail + int(num/125) #how many times 125 comes in num is then added to trail
if 5**4 < num:
	trail=trail	+ int(num/625) #how many times 625 comes in num is then added to trail

print(f"There are {trail} Trailing zeros")
#Because the no. of 5s are multiples of that number that many trailing zeros are there in that number 
# --> as multiples of 2 are always there in abundance for 2*5
#OR
'''
count=0
i=5
while((num//i) !=0):
	count=count+ int(num/i)
	i=i*5

print(f"Trailing zeros of {num} are {count}")	
'''
