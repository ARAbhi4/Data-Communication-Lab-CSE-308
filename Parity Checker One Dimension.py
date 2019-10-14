#AR Abhi

#Sender

print("Enter your data by binary: ")
n = input()

print(f"Sender: {n}")

a = []
z = 0
p = 0

for i in n:
	a.append(int(i))
	if(int(i)%2 == 1):
		z = z+1
	
if(z%2 == 1):
	x = 1
	a.append(1)
elif(z%2 == 0):
	x = 0
	a.append(0)
	
print(f"Parity bit: {x}")
			
#Reciver

s = ""

for j in a:
	s = s + str(j)
	

print(f"Reciver: {s}")

i = 0
while(i<len(a)):
	if(a[i]%2 == 1):
		p = p+1
	i = i + 1
	
if(p%2 == 0):
	print("Parity is Even data accepted.")	
else:
	print("Parity is Odd data Error!")
	
