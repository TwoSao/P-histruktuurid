from operator import index

p=[]
i=[]

def LisaAndmed(p: list, i: list):
    """
    :param p:
    :param i:
    :return:
    """
    while True:
        try:
            nimi=input("Sissesta nimi:")
            if nimi.isalpha():
                try:
                    palk=input("Palk: ")
                except:
                    print("Palk on arv!")
                break
        except:
            print("Kirjuta ainult tähtede ksautades")
    p.append(palk)
    i.append(nimi)

def KasutaAndmed(p:list, i: list):
    """
    :param p:
    :param i:
    :return:
    """
    try:
        nimi=input("Введите имя пользователя которого хотите удалить: ")
        if nimi.isalpha():
            c=i.count(nimi)
            if c>0:
                for j in range(c):
                    ind=i.index(nimi)
                    i.pop(ind)
                    p.pop(ind)
                print("Andmed on kustutatud")
            else:
                print("Andmed puuduvad")
    except:
        print("Error")

def SuurPalk(p: list, i:list):
    """
    :param p:
    :param i:
    :return:
    """
    suur=max(p)
    k=p.count(suur)
    ind=p.index(suur)
    for j in range(k):
        ind=p.index(suur, ind)
        print(f"Saab kätte {i[ind]}, {p[ind]}")
        ind +=1

def MaadalimPalk(p: list, i:list):
    """
    :param p:
    :param i:
    :return:
    """
    madal=min(p)
    k=p.count(madal)
    ind=p.index(madal)
    for j in range(k):
        ind=p.index(madal, ind)
        print(f"Saab kätte {i[ind]}, {p[ind]}")
        ind +=1
def JarjestaPalgad(p: list, i: list):
    """
    Järjestab palgad kasvavas ja kahanevas järjekorras koos nimedega.
    :param p: Palgad
    :param i: Nimed
    """
    kasvav = sorted(p)
    kahanev = sorted(p, reverse=True)
    print("Kasvav järjestus:")
    for palk in kasvav:
        ind = p.index(palk)
        print(f"{i[ind]}: {palk}")
    print("Kahanev järjestus:")
    for palk in kahanev:
        ind = p.index(palk)
        print(f"{i[ind]}: {palk}")  
#1
def SamaPalk(p: list, i: list):
    """
    parem: p
    parem: i
    return
    """
    sama=[]
    for j in range(len(p)):
        if p.count(p[j])>1:
            sama.append(i[j])
    sama=list(set(sama))
    sama.sort()
    print(sama)

#2

def foundsalary(p: list, i:list):
    """

    :param p:
    :param i:
    :return:
    """
    try:
        nimi=input("Siseta nimi: ")
        if nimi.isalpha():
            ind=i.index(nimi)
            print(f"Palk on: {p[ind]}")
        else:
            print("Error")
    except:
        print("Error")
#3
def inpsalarythan(p: list, i:list):
    """

    :param p:
    :param i:
    :return:
    """
    newlistm={}
    try:
        salary=int((input("Sisesta palk: ")))
        ans=int(input("Choose:"))
        if ans == 1:
            for j in range(len(p)):
                if p[j]< salary:
                    newlistm[i[j]] = p[j]

    except:
        print("Error2")

    print(newlistm.items())
#4
