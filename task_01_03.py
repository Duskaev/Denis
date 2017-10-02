a=int(input())
b=int(input())
c=int(input())
if a<=b and a<=c:
	if b<=c:
	    print(a,b,c)
	elif c<=b:
	    print(a,c,b)
elif b<=a and b<=c:
	if c<=a:
	    print(b,c,a)
	elif a<=c:
	    print(b,a,c)