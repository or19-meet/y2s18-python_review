# Write your solution for 1.2 here
a=0
for i in range(101):
	if i % 2 == 0:
		a+=i
print(a)

#####

a=0
for i in range(1000):
	if i % 6 == 2 and (i*i*i)%5==3:
		print(i)

