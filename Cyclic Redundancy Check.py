#AR Abhi

#Sender:

print("Enter your data in binary: ")
n = input()

a = []
b = []
p = []

crc = [1,0,1,1]

for i in n:
	a.append(int(i))
	b.append(int(i))
		
for i in range(len(crc)-1):
	a.append(0)
	
for i in range(4):
	p.append(a[i])
	

	
	
x = len(n) + len(crc) -1
i = 3
k = 3

while(i < x):
	if(k == x):
		break
	z = []
	j= 0
	while(j < 4):
		s = int((p[j] + crc[j])%2)
		z.append(s)
		j = j+1
	
	j=0
	g = 0
	while(j < 4):
		if(z[j] == 1):
			break
		elif(z[j]== 0):
			k = k+1
			if(k == x):
				break
			z.append(a[k])
			
			g = g+1
			j = j+1
			i = i+1
						
	p = z[g:]			
	
		
print(f"Sender Remainder's: {p[1:]}")



for i in range(len(p)-1):
	b.append(int(p[i+1]))
	
	
#Reciver:

i = 0

f = []

for i in range(4):
	f.append(b[i])
	
	
x = len(n) + len(crc) -1
i = 3
k = 3

while(i < x):
	if(k == x):
		break
	h = []
	j= 0
	while(j < 4):
		s = int((f[j] + crc[j])%2)
		h.append(s)
		j = j+1
		
		
	j=0
	g = 0
	while(j < 4):
		if(h[j] == 1):
			break
		elif(h[j]== 0):
			k = k+1
			if(k == x):
				break
			h.append(b[k])
			
			g = g+1
			j = j+1
			i = i+1
			
			
						
	f = h[g:]			
	

print(f"Reciver Remainder's: {f[1:]}")
