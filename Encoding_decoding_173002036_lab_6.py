#Sender
print("Enter your Data: ")
data = input()

print("Enter your cipher data position: range (1 to 26) ")

c = int(input())

ciphertext = []


data2 = []
data_in_ascii = []

for i in data:
    data2.append(i)


for i in data2:
    data_in_ascii.append(ord(i))


i = 0
while(i < len(data_in_ascii)):

    x = int(data_in_ascii[i])
    p = x+c

    if((x >= 65 and x<= 90)):
        if(p >= 65 and p<= 90):
            ciphertext.append(chr(p))
        elif(p > 65):
            ciphertext.append(chr(abs(p-26)))
            
    if((x >= 97 and x<= 122)):
        if(p >= 97 and p<= 122):
            ciphertext.append(chr(p))
        elif(p > 97):
            ciphertext.append(chr(abs(p-26)))

    i = i+1

listToStr = ''.join(map(str,ciphertext ))
print(f"Encryption data: {listToStr}")

#Reciver


ciphertext2 = []


data3 = []
data_in_ascii2 = []

for i in listToStr:
    data3.append(i)


for i in data3:
    data_in_ascii2.append(ord(i))


i = 0
while(i < len(data_in_ascii2)):

    x = int(data_in_ascii2[i])
    p2 = x-c
    if((x >= 65 and x<= 90)):
        if(p2 >= 65 and p2<= 90):
            ciphertext2.append(chr(p2))
        elif(p2 < 65):
            ciphertext2.append(chr(abs(p2+26)))
            
    if((x >= 97 and x<= 122)):
        if(p2 >= 97 and p2<= 122):
            ciphertext2.append(chr(p2))
        elif(p2 < 97):
            ciphertext2.append(chr(abs(p2+26)))
    
    

    i = i+1

listToStr2 = ''.join(map(str,ciphertext2 ))
print(f"Decryption data: {listToStr2}")
