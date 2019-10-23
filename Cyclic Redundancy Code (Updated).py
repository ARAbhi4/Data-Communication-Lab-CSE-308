# Sender
print("Enter your dataword data by binary: ")
n = input()

print("Enter your key data by binary: ")
ke = input()

a = []
b = []
c = []
key = []

for i in ke:
    key.append(int(i))

print(f"Dataword is {n}.")

sr = ""
for i in key:
    sr = sr + str(i)


print(f"Key is {sr}.")

for i in n:
    a.append(int(i))
    b.append(int(i))

for rr in range(len(key) - 1):
    a.append(0)

sc = ""
for i in a:
    sc = sc + str(i)

print(f"Divident is {sc}.")

for i in range(len(key)):
    c.append(a[i])
i =  len(key) - 1
k =  len(key)



while(i < len(a)):
    if(k == len(a)):
        break

    z = []

    j = 0
    while(j < len(key)):
        s = int((c[j] + key[j]))%2
        z.append(s)
        j = j+1
    f = 0
    j = 0
    dd = len(key)
    while(j < dd):
        if(z[j] == 1):
            break

        if(z[j] == 0):
            if(k == len(a)):
                break
            z.append(a[k])
            k = k + 1
            dd = dd + 1

            f = f+1
            j = j+1
            i = i+1


        c = z[f:]


sa = ""
for i in c[1:]:
    sa = sa + str(i)
print(f"Redundancy is {sa}.")


for i in c[1:]:
    b.append(int(i))

ll = ""

for i in b:
    ll = ll + str(i)

print(f"Codeword is {ll}.")


# Receiver for change data

print("Do you want change your Codeword? [for yes 1 & for no 0]. ")

pk = int(input())

if(pk == 1):
    print("Enter your new data: ")
    az = input()

    aa = []
    bb = []
    cc = []


    print(f"Receiver Dataword is {az}.")

    print(f"Receiver Key is {sr}.")

    for i in az:
        aa.append(int(i))
        bb.append(int(i))


    for i in range(len(key)):
        cc.append(aa[i])


    ii =  len(key) - 1
    kk =  len(key)



    while(ii < len(aa)):
        if(kk == len(aa)):
            break

        zz = []

        jj = 0
        while(jj < len(key)):
            ss = int((cc[jj] + key[jj]))%2
            zz.append(ss)
            jj = jj+1
        ff = 0
        jj = 0
        dddd = len(key)
        while(jj < dddd):
            if(zz[jj] == 1):
                break

            if(zz[jj] == 0):
                if(kk == len(aa)):
                    break
                zz.append(aa[kk])
                kk = kk + 1
                dddd = dddd + 1

                ff = ff+1
                jj = jj+1
                ii = ii+1


            cc = zz[ff:]


    sasa = ""
    for i in cc[1:]:
        sasa = sasa + str(i)
    print(f"Receiver Redundancy is {sasa}.")


    count = 0

    for i in sasa:
        if (int(i) == 1):
            count = count + 1
    if(count >= 1):
        print("Receiver Data is error!")
    else:
        print("Receiver Data is correct.")

# Receiver for original data

else:

    aa = []
    bb = []
    cc = []


    print(f"Receiver Dataword is {ll}.")

    print(f"Receiver Key is {sr}.")

    for i in ll:
        aa.append(int(i))
        bb.append(int(i))


    for i in range(len(key)):
        cc.append(aa[i])


    ii =  len(key) - 1
    kk =  len(key)



    while(ii < len(aa)):
        if(kk == len(aa)):
            break

        zz = []

        jj = 0
        while(jj < len(key)):
            ss = int((cc[jj] + key[jj]))%2
            zz.append(ss)
            jj = jj+1
        ff = 0
        jj = 0
        dddd = len(key)
        while(jj < dddd):
            if(zz[jj] == 1):
                break

            if(zz[jj] == 0):
                if(kk == len(aa)):
                    break
                zz.append(aa[kk])
                kk = kk + 1
                dddd = dddd + 1

                ff = ff+1
                jj = jj+1
                ii = ii+1


            cc = zz[ff:]


    sasa = ""
    for i in cc[1:]:
        sasa = sasa + str(i)
    print(f"Receiver Redundancy is {sasa}.")


    count = 0

    for i in sasa:
        if (int(i) == 1):
            count = count + 1
    if(count >= 1):
        print("Receiver Data is error!")
    else:
        print("Receiver Data is correct.")
