print("Enter your IP number: ")
ip_num = input()

g = []

for i in ip_num:
    g.append(i)

g.append(".")


z = ""
i = 0
k = []

while(i < len(g)):

    z = z + g[i]
    i = i + 1

    if(g[i] == "."):
        k.append(z)
        z = ""
        i = i+1

r = []
for i in k:
    r.append(int(i))


x = []

i = 0

while(i < len(r)):
    x.append(bin(r[i]))
    i = i+1


a = []
b = []
c = []
d = []

a = x[0]
b = x[1]
c = x[2]
d = x[3]




a1 = a[2:]
b1 = b[2:]
c1 = c[2:]
d1 = d[2:]


z1 = []
z2 = []
z3 = []
z4 = []
i = 0
while(i < 7):
    if(i < 8- len(a1)):
        z1.append("0")

    if(i < 8-len(b1)):
        z2.append("0")

    if(i < 8-len(c1)):
        z3.append("0")

    if(i < 8-len(d1)):
        z4.append("0")

    i = i+1



r1 = ""
for i in z1:
    r1 = r1+ i

r2 = ""
for i in z2:
    r2 = r2+ i

r3 = ""
for i in z3:
    r3 = r3+ i

r4 = ""
for i in z4:
    r4 = r4+ i



r1 = r1 + a1
r2 = r2 + b1
r3 = r3 + c1
r4 = r4 + d1


print(f" Binary IP: {r1}.{r2}.{r3}.{r4}")




print(f" Decimal IP: {int(a,2)}.{int(b,2)}.{int(c,2)}.{int(d,2)}")

