print("Enter your Byte: ")

a = input()
b = []
c = []
i= 0
while(len(a) > i):
	
		if( (a[i] == "D" or a[i] == "d")  and (a[i+1] == "L" or a[i+1] == "l") and (a[i+2] == "E"  or a[i+2] == "e")):
			b.append(a[i])
			b.append(a[i+1])
			b.append(a[i+2])
			
			if(a[i] == "D"):
				b.append("D")
			elif(a[i] == "d"):
				b.append("d")
				
			i = i+1
				
			if(a[i] == "L"):
				b.append("L")
			elif(a[i] == "l"):
				b.append("l")
				
			i = i+1
				
			if(a[i] == "E"):	
				b.append("E")
			elif(a[i] == "e"):
				b.append("e")
				
			i = i+1
					
		else:
		
			b.append(a[i])
			i = i+1
s =""
x = s.join(b)
print(f"After Byte Stuffing: {x}")

i = 0

while(len(x) > i):
	
		if(((x[i] == "D" or x[i] == "d")  and (x[i+1] == "L" or x[i+1] == "l") and (x[i+2] == "E"  or x[i+2] == "e"))):
			c.append(x[i])
			c.append(x[i+1])
			c.append(x[i+2])
			i = i+6
		else:
		
			c.append(x[i])
			i = i+1

t =""
y = t.join(c)
print(f"After Byte Unstuffing: {y}")

