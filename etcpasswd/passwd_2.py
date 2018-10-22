def getfile(f1):
    mylist1=list()
    data=list()

    with open(f1, "r") as fp:
        for line in fp:
            if line.strip():
                mylist1.append(line.split(':'))

    tmpserver_name = mylist1[0]
    server=tmpserver_name[0].split("|")[0]

    for i in mylist1[1:]:
        data.append((i[0]))

    return data,server


c1, a1 =getfile("passwd2.txt")[0],getfile("passwd2.txt")[1]
c2, a2 =getfile("passwd1.txt")[0],getfile("passwd2.txt")[1]

print("Compare server {} with {} found missing user" .format(a1, a2))
#iterate start from 1
compare =  enumerate(set(c1)-(set(c2)),1)

#gen = (i for i in compare if "m" not in compare)
#for x in gen:
#    print(x)

#for i in enumerate(set(c1)-(set(c2)),1):
#    print(i)

for i in compare:
    print(i)