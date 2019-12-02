a1 = input("Enter your data: ")

bob = []

i = 0
j = 0

count = 0 

while(i < len(a1)):
	if(int(a1[i]) == 1):
		count = count + 1
		if(count == 5):
			bob.append(int(a1[i]))
			bob.append(0)
			i = i+1
			j = j+2
			count = 0
		else:
			
			bob.append(int(a1[i]))
			i = i+1
			j = j+1
			
	else:
		count = 0
		bob.append(int(a1[i]))
		i = i + 1
		j = j + 1
		
listToStr3 = ' '.join([str(elem) for elem in bob]) 
  
print(listToStr3)  
		


u = 0
r = 0
count = 0

cob = []

while(u<len(bob)):
	if(bob[u] == 1):
		count = count + 1
		if(count == 5):
			cob.append(bob[u])
			r = r+1
			u = u+2
			count = 0
		else:
			cob.append(bob[u])
			r = r+1
			u = u+1
			
	else:
		count = 0
		cob.append(bob[u])
		r = r+1
		u = u+1
		
listToStr4 = ' '.join([str(elem) for elem in cob]) 
  
print(listToStr4)  
		
			
